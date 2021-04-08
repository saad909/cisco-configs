import paramiko
import time


def send_command(conn, command):
    conn.send(command + "\n")
    time.sleep(1)


def get_output(conn):
    return conn.recv(65535).decode("utf-8")


def main():
    hosts = ["10.10.10.10", "20.20.20.20", "30.30.30.30"]

    for host in hosts:
        conn_params = paramiko.SSHClient()
        conn_params.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        conn_params.connect(
            hostname=host,
            port=22,
            username="cisco",
            password="cisco",
            look_for_keys=False,
            allow_agent=False,
        )
        conn = conn_params.invoke_shell()
        time.sleep(1)
        print(f"Logged in to {get_output(conn).strip()} successfuly")
        commands = ["terminal length 0", "show version | include Software,"]
        for command in commands:
            send_command(conn, command)
            print(get_output(conn))
        conn.close()


if __name__ == "__main__":
    main()
