from paramiko import SSHClient
from paramiko import AutoAddPolicy
from argparse import ArgumentParser
#
#You can use this script as below:
#python run_fortigate_commands.py --fortigate <fortigate_ssh_ip> --username <fortigate_login_user> --password <fortigate_login_pass> --commands "get system status" "get system interface"
#python run_fortigate_commands.py -f <fortigate_ssh_ip> -u <fortigate_login_user> -p <fortigate_login_pass> -c "get system status" "get system interface"
#
# Command  Lines Argument
parser = ArgumentParser(description="Run Fortigate Commands over SSH")
parser.add_argument('--commands', '-c', nargs='*', type=str)
parser.add_argument('--fortigate', '-f', type=str)
parser.add_argument('--username', '-u', type=str)
parser.add_argument('--password', '-p', type=str)
args = parser.parse_args()
commands = []

def main():
    commands = args.commands
    ssh = SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(AutoAddPolicy())
    ssh.connect(args.fortigate, username=args.username, password=args.password)
    for command in commands:
        ssh.exec_command(command)
        #test print out on terminal
        #stdin, stdout, stderr = ssh.exec_command(command)
        #print stdout.read()
    ssh.close()

if __name__ == "__main__":
       main()

