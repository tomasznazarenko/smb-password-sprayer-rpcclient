# SMB Password Sprayer Using rpcclient

A Python script that uses the `rpcclient` command to perform password spraying attacks against SMB server.
This script allows you to test multiple usernames and passwords from files or provide them individually.
It is used in place of Hydra or netexec (crackmapexec) which due to implementation were not able to discover credentials, though they existed, whereas rpcclient or metasploit (scanner/smb_login) worked as expected.

## Features

* Test single username/password combinations
* Test multiple usernames and passwords from files (newline-separated)
* Continue testing even if a successful logon is found (optional)

## Usage

To use this script, simply run it and provide the following arguments:

* `-u` or `--single-user`: The username to test (required for single-user mode)
* `-U` or `--user-list`: File containing list of usernames separated by newline characters (optional)
* `-p` or `--single-password`: The password to test (required for single-password mode)
* `-P` or `--password-list`: File containing list of passwords separated by newline characters (optional)
* `-i` or `--ip-address`: IP address to target
* `-c` or `--continue-on-success`: Continue testing even if a successful logon is found

Example:
```bash
python rpccclient_spray_smb.py -u <user> -p <pass> -i <IP>
```
## Requirements

* Python 3.x
* `rpcclient` command-line tool
## Disclaimer

This script is for educational purposes only. Do not use it to perform unauthorized or malicious activities.

## Contributing

Feel free to contribute to this project by submitting pull requests or reporting issues.
