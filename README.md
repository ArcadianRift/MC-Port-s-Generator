# Random Minecraft Ports Generator

This script generates random ports for Minecraft servers, saves them to a text file, and adds firewall rules using `ufw`.

## Prerequisites

- Python installed on your computer
- `ufw` firewall management tool installed and enabled

## Usage

1. Clone the repository or download the script file (`add_firewall_rules.py`).

2. Open a terminal or command prompt and navigate to the directory where the script file is located.

3. Run the following command to execute the script:

[ python add_ufw-ports-generator.py ]

4. The script will generate random ports for Minecraft servers, save them to a text file named `minecraft_ports.txt`, and add firewall rules using `ufw`.

5. If prompted, provide your password or administrative privileges to modify the firewall settings.

6. Once the script finishes running, the ports will be saved to `minecraft_ports.txt`, and the firewall rules will be added to allow incoming connections on the generated ports for Minecraft servers.

## License

This project is licensed under the [MIT License](LICENSE).

