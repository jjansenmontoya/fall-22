import random
import math


class Node():
    def __init__(self, name):
        # They start by all sending at the same time
        self.time_to_send = 0

        # To keep track of which nodes have successfully transmitted
        self.successful = False

        # In case naming nodes is helpful for debugging
        self.name = name

        # Recalling number of times that a message has failed to be transmitted
        self.attempts = 0

    def retransmit(self, curr_time):
        # Update the number of attempts and utilize exponential backoff
        self.attempts += 1
        self.time_to_send += random.randrange(1, 2**self.attempts)


def simulate_collision(N):
    node_list = []
    for i in range(N):
        node_list.append(Node(f'Node {i}'))

    nodes_sending_at_slot = []
    curr_time = 0
    collisions = 0
    # Iterate through time slots and check which nodes are scheduled to send
    while not all([node.successful for node in node_list]):
        for node in node_list:
            if node.time_to_send == curr_time:
                # Implementation of optimal p-persistent (p = N)
                if random.randint(0, N) % N != 0:
                    node.time_to_send += 1
                else:
                    nodes_sending_at_slot.append(node)

        # Node sends successfully if it is the only one sending in a slot
        if len(nodes_sending_at_slot) == 1:
            nodes_sending_at_slot[0].successful = True
        elif len(nodes_sending_at_slot) > 1:
            for node in nodes_sending_at_slot:
                # Attempt to retransmit each message
                node.retransmit(curr_time)
            collisions += 1
        nodes_sending_at_slot = []
        curr_time += 1
    return collisions


def main():
    N = 5  # Number of nodes
    numCollisions = 0
    for i in range(0, 10):
        numCollisions += simulate_collision(N)


if __name__ == '__main__':
    main()
