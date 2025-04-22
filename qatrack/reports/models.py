from datetime import time as dt_time

from django.contrib.auth.models import Group, User
from django.db import models
from django.utils.translation import gettext_lazy as _l
from recurrence.fields import RecurrenceField

from qatrack.qatrack_core.fields import JSONField
from qatrack.qatrack_core.scheduling import RecurrenceFieldMixin

# ensure Django-Q can pick up all report types on Windows
from qatrack.reports import (  # noqa: F401
    faults,
    qc,
    service_log,
)

from qatrack.reports.reports import report_class


class SavedReport(models.Model):

    FORMATS = [('pdf', _l('PDF')), ('xlsx', 'Excel'), ("csv", _l("CSV"))]

    title = models.CharField(
        max_length=255,
        verbose_name=_l("Título"),
    )

    report_type = models.CharField(
        max_length=128,
        verbose_name=_l("Tipo de informe"),
    )

    report_format = models.CharField(
        max_length=8,
        choices=FORMATS,
        default="pdf",
        verbose_name=_l("Formato"),
    )

    include_signature = models.BooleanField(
        verbose_name=_l("Firma"),
        help_text=_l("¿Quieres firma al final del PDF?"),
        default=True,
    )

    filters = JSONField(blank=True, editable=True)

    visible_to = models.ManyToManyField(
        Group,
        verbose_name=_l("Visible para"),
        help_text=_l("Selecciona los grupos que pueden ver este informe. Dejar en blanco para mantenerlo privado."),
        blank=True,
    )

    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        editable=False,
        related_name="report_creator",
    )
    modified = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        editable=False,
        related_name="report_modifier",
    )

    class Meta:
        permissions = (
            ("can_run_reports", _l("Can Run Reports")),
            ("can_create_reports", _l("Can create Reports")),
            ("can_run_sql_reports", _l("Can run SQL Data Reports")),
            ("can_create_sql_reports", _l("Can create SQL Data Reports")),
        )

        ordering = ("title", "created",)

    def get_filter_class(self):
        return report_class(self.report_type).filter_class

    @property
    def base_opts(self):
        return {
            'title': self.title,
            'include_signature': self.include_signature,
            'report_id': self.id,
        }

    def get_report(self, user=None):
        ReportClass = report_class(self.report_type)
        user = user or self.created_by
        return ReportClass(base_opts=self.base_opts, report_opts=self.filters, user=user)

    def get_report_type_display(self):
        return report_class(self.report_type).name

    def render(self, user=None):
        """create in memory file containing rendering of report"""
        report = self.get_report(user)
        return report.render(self.report_format)

    def __str__(self):
        return "#%d. %s - %s - %s" % (
            self.pk,
            self.title,
            self.get_report_type_display(),
            self.get_report_format_display(),
        )


class ReportNote(models.Model):

    report = models.ForeignKey(SavedReport, on_delete=models.CASCADE)

    heading = models.TextField(
        help_text=_l("Añade un título para esta nota"),
    )
    content = models.TextField(
        help_text=_l("Escribe el contenido de la nota"),
        blank=True,
    )


class ReportSchedule(RecurrenceFieldMixin, models.Model):

    recurrence_field_name = "schedule"

    TIME_CHOICES = [(dt_time(x // 60, x % 60), "%02d:%02d" % (x // 60, x % 60)) for x in range(0, 24 * 60, 15)]

    report = models.OneToOneField(
        SavedReport,
        on_delete=models.CASCADE,
        help_text=_l("Select the report this schedule pertains to"),
        related_name="schedule",
    )

    schedule = RecurrenceField(
        verbose_name=_l("Schedule"),
        help_text=_l("Define the schedule this report should be sent with."),
    )

    time = models.TimeField(
        verbose_name=_l("Time of day"),
        help_text=_l("Set the time of day this report should be sent (00:00-23:59)"),
        choices=TIME_CHOICES
    )

    groups = models.ManyToManyField(
        Group,
        help_text=_l("Select which groups this report should be sent to."),
        blank=True,
        related_name="scheduledreports",
    )

    users = models.ManyToManyField(
        User,
        help_text=_l("Select individual users this report should be sent to."),
        blank=True,
        related_name="scheduledreports",
    )

    emails = models.TextField(
        verbose_name=_l("Extra recipient emails"),
        help_text=_l("Enter a comma separated list of extra emails this report should be sent to"),
        blank=True
    )

    last_sent = models.DateTimeField(null=True, editable=False)

    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        editable=False,
        related_name="reportschedule_creator",
    )
    modified = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        editable=False,
        related_name="reportschedule_modifier",
    )

    def recipients(self):
        """Gather recipients that are supposed to recieve this report"""

        users = list(self.users.values_list("first_name", "last_name", "email"))
        users += list(self.groups.values_list("user__first_name", "user__last_name", "user__email"))
        users += [("", "", e) for e in self.emails.split(",")]

        recipients = []
        for fn, ln, e in users:

            e = e.strip()

            if fn and ln and e:
                recipients.append('"%s %s"<%s>' % (fn, ln, e))
            elif e:
                recipients.append(e)

        return recipients
