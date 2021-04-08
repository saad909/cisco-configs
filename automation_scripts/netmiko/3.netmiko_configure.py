"""
This script is used to configure device in global configuration mode
"""
from netmiko import ConnectHandler


def send_command(conn, commands):
    # send_commands is used for sending command into enable mode
    return conn.send_config_set(commands)


def main():
    # inline inventory

    hosts = ["10.10.10.10", "20.20.20.20", "30.30.30.30"]

    i = 0
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
            "int l1",
            "no ip address",
            f"ip address {i+1}1.{i+1}1.{i+1}1.{i+1}1 255.255.255.255",
        ]
        output = send_command(conn, commands)
        conn.disconnect()
        i += 1

        # write output to the file
        with open("{host}_facts.txt", "w") as handler:
            handler.write(output)


if __name__ == "__main__":
    main()
