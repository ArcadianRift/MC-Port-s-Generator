import random

def generate_minecraft_ports(num_ports):
    # List to store the generated ports
    ports = []

    # Generate random ports
    for _ in range(num_ports):
        # Generate a random port between 1024 and 65535
        port = random.randint(1024, 65535)
        ports.append(port)

    return ports

# Generate 100+ random ports
ports = generate_minecraft_ports(100)

# Print the generated ports
for port in ports:
    print(port)
