"""
This script is used to send command in privilege mode
"""
from netmiko import ConnectHandler


def send_command(conn, command):
    # send_commands is used for sending command into enable mode
    return conn.send_command(command)


def main():
    # inline inventory

    hosts = ["10.10.10.10", "20.20.20.20", "30.30.30.30"]

    for host in hosts:
        device = {
            "device_type": "cisco_ios",
            "host": host,
            "username": "cisco",
            "password": "cisco",
            "secret": "cisco",
        }
        conn = ConnectHandler(**device)
        conn.enable()
        # send show command
        print(f"Connection to {host} successfully")

        commands = [
            "show version",
            "show running-config",
        ]
        output = ""
        for command in commands:
            result = send_command(conn, command)
            output += result
        conn.disconnect()
        print(output)


if __name__ == "__main__":
    main()
