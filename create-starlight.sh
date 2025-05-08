#!/usr/bin/expect -f

spawn npm create astro@latest -- --template starlight

# Increase timeout and add debugging after expect
expect -timeout 20 "*Where should we create your new project?*" {
    send "./documentaition\r"
    puts "Sent project directory."
} timeout {
    puts "Timeout occurred while waiting for project directory prompt."
    exit 1
}

expect -timeout 20 "*Install dependencies?*" {
    send "y\r"
    puts "Sent 'yes' for dependencies."
} timeout {
    puts "Timeout occurred while waiting for install dependencies prompt."
    exit 1
}

expect -timeout 20 "*Initialize a new git repository?*" {
    send "n\r"
    puts "Sent 'no' for Git initialization."
} timeout {
    puts "Timeout occurred while waiting for Git init prompt."
    exit 1
}

expect eof