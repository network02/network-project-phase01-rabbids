import socket


def host_is_online(host, p_list):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    is_online = False
    open_port_list = []
    for port in p_list:
        try:
            sock.connect((host, port))
            is_online = True
            open_port_list.append(port)

        except socket.error as e:
            pass

    if is_online:
        print(f"Host {host} is online.")
        return is_online, open_port_list
    else:
        print(f"Host {host} is offline.")
        return False, None


if __name__ == '__main__':
    inp = input()
    host_port_list = inp.split(" ")
    host_ip = host_port_list.pop(0)

    port_list = []
    for word in host_port_list:
        port_list.append(int(word))

    host_online, open_ports = host_is_online(host_ip, port_list)

    if host_online:
        for port in open_ports:
            service = socket.getservbyport(port)
            print(f"open port detected: {host_ip} \t -- Port: {port} \t -- Service: {service}")

