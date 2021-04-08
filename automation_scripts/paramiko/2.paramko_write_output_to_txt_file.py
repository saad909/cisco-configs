import paramiko
import time


# sending command to the connection
def send_command(conn, command):
    if command == "enable":
        conn.send("enable" + "\n")
        conn.send("cisco" + "\n")
        # conn.send_command(enablepass)
    conn.send(command + "\n")
    time.sleep(1)


# get the output from the conenction
def get_output(conn):
    return conn.recv(65535).decode("utf-8")


def main():
    # inline-inventory
    hosts = ["10.10.10.10", "20.20.20.20", "30.30.30.30"]

    # iterate over all hosts to send commands
    for host in hosts:
        # create connection parameter object
        conn_params = paramiko.SSHClient()

        """
        paramiko terminates the session if does not finds the ssh key of host.
        this command is used to prevent that from happening and says that ignore this
        """
        conn_params.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # set paramenters of device to connection parameter object
        conn_params.connect(
            hostname=host,
            port=22,
            username="cisco",
            password="cisco",
            look_for_keys=False,
            allow_agent=False,
        )
        # create connection handler from the connection paramter object
        conn = conn_params.invoke_shell()
        time.sleep(1)
        print(f"Logged in to {get_output(conn).strip()} successfuly")
        # commands to send to the hosts
        commands = [
            "enable",
            "terminal length 0",
            "show run",
            "show version | include Software,",
        ]
        # empty string to get the output of commands for a host
        output = ""
        for command in commands:
            send_command(conn, command)
            output += get_output(conn)
            breakpoint()
        # as soon as output is obtained, kill the connection
        conn.close()

        # write the output to a text file for each host
        print(f"Writing output of {host} to the {host}_output.txt file")
        with open(f"{host}_output.txt", "w") as handler:
            handler.write(output)


if __name__ == "__main__":
    main()
