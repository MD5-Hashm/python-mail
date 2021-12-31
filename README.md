# python-mail
A python mailserver meant for friends who value privacy and a hard to use interface....

# Basic info
This mailserver was just a random project of mine that I thought I would share.
It isnt great but in my opinon it's still pretty cool.

# Commands
"ping" : Sends a responds

"help" : Shows a list of commands

"send" : Sends mail

"read" : Reads your mail

"purgemail" : Purges your mail

"exit" : "Disconnects you from the server"

# Admin commands
"addusr" : Generates a key that someone can use as a username to create a new account (1 time use)

"purgekeys" : Deletes all the stored key


# Server setup
Start by finding your local ip and edit "config.py" to include your local ip and desired port.

Edit "path.py" and include the full path of the mailbox, keys and, server

Edit "db.py" and add the base account you want to include (You can add more later without access to the server)

Insure you have at least one account with admin/root permissions by editing the "ADMINS" list

# Client setup
Edit config.py to include the ip (If lan then local ip if public ip include that) and the port

# Starting
Start the server with:

```python3 server.py```

Or whatever python3 is aliased to

You may need to accept a prompt for firewall changes.

This program does not need to be run as root

This program has been tested on Windows 10 and Ubuntu 20.04.3 LTS (WSL) but should work on Mac os/OSX and other linux distros

This program does not require any python requirments not already pre-installed with the base installation of python3

The program has been completely written by myself and I would appreciate that if you like the program to leave a star!

If you have any issues with the program please do not hesitate to submit an issue
