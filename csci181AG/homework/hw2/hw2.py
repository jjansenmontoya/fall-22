# Message is simply an object with a source and destination
class Message():
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst

# LAN is a broadcast domain - if any node on it sends a message, everyone else receives it


class LAN():
    def __init__(self, name):
        self.name = name

        # Receiver is any bridge or node on the LAN (anyone who hears the broadcast message)
        self.receivers = []

    # When a LAN receives a message, everyone on the LAN (nodes and bridges) except the sender should also receive it
    def receive_broadcast(self, src, m):
        for receiver in self.receivers:
            if receiver is not src:
                receiver.receive_message(self, m)

# Store and forward device to extend LANs


class Bridge():
    def __init__(self, name, port_LAN_map):
        self.name = name

        # Sign up for all messages by adding itself as a receiver on the LANs it's connected to
        for l in port_LAN_map.values():
            l.receivers.append(self)

        self.ports = [p for p in port_LAN_map.keys()]

        # Keep track of which LANs are associated with which ports
        self.port_LAN_map = port_LAN_map

    # Takes a LAN that a message was received from and returns the corresponding port
    # that message came in on
    def in_port_from_LAN(self, in_LAN):
        in_port = None
        for port, LAN in self.port_LAN_map.items():
            if LAN == in_LAN:
                in_port = port

        assert in_port is not None, "in_port must be deduced based on which LAN sent this message"
        return in_port

    # TODO: Fix this function
    # in_LAN: LAN from which bridge received the message
    def receive_message(self, in_LAN, m):
        # Determine which port this message arrived on
        in_port = self.in_port_from_LAN(in_LAN)

        print('m.src.name', m.src.name)
        print('receiver', in_LAN.receivers)
        print('self.port_LAN_map', self.port_LAN_map)

        # Go through all the ports and send message to all ports except the one that message came in on
        for p in self.ports:
            if p is not in_port:
                self.port_LAN_map[p].receive_broadcast(self, m)

# The devices on LANs that send and receive messages


class Node():
    def __init__(self, name, LAN):
        self.name = name

        # Sign up for all messages by adding itself as a receiver on its LAN
        self.LAN = LAN
        self.LAN.receivers.append(self)

    # Send message on its LAN
    def send_message(self, dst):
        message = Message(self, dst)
        self.LAN.receive_broadcast(self, message)

    # Receive message and check whether it's intended for self
    def receive_message(self, in_LAN, m):
        if m.dst is self:
            print(f'{self.name}: received message from {m.src.name}. It is for me!')
        else:
            print(
                f'{self.name}: heard message from {m.src.name} but it is not for me')


def main():
    L1 = LAN("L1")
    A = Node("A", L1)
    B = Node("B", L1)

    L2 = LAN("L2")
    C = Node("C", L2)

    L3 = LAN("L3")
    D = Node("D", L3)

    L4 = LAN("L4")
    E = Node("E", L4)

    L5 = LAN("L5")
    F = Node("F", L5)
    G = Node("G", L5)

    # Initalize bridges with a mapping of port number: LAN
    B1 = Bridge("B1", {"P1": L1, "P2": L2, "P3": L4})
    B2 = Bridge("B2", {"P1": L1, "P2": L3, "P3": L5})

    # Add your messages below:
    A.send_message(B)


if __name__ == '__main__':
    main()
