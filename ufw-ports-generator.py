import random
import subprocess

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

# Save ports to a file
with open('minecraft_ports.txt', 'w') as file:
    for port in ports:
        file.write(str(port) + '\n')

print('Ports saved to minecraft_ports.txt')

# Add firewall rules using ufw
for port in ports:
    subprocess.run(['ufw', 'allow', str(port)])

print('Firewall rules added for Minecraft ports.')
