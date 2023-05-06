Port Scanner

    This Python script performs a TCP port scan on a target IP address to discover open ports. 
    It uses socket library to create a TCP socket and attempts to connect to each port in a range of 1-65535. 
    If a connection is successful, it is assumed that the port is open.
    
Requirements

    pip install -r requirements.txt

Usage

    1 - Run the script using the command "python3 scan_port.py 192.168.1.0".

    2 - The script will iterate through each port in the range of 1-65535 and attempt to connect to it.
    
    3 - If a connection is successful, the script will add the port number to a list of open ports.
    
    4 - If any open ports are found, the script will print the list of open ports to the console.
    
    5 - If no open ports are found, the script will print a message indicating that no ports are open.

Exemple
    
    python3 scan_port 192.168.1.0

Notes

    The default range of ports to scan is 1-65535, which may take a long time to complete. You can modify the ports variable to specify a smaller range of ports to scan.
    The probe_port() function attempts to connect to a given IP address and port using a TCP socket. 
    If the connection is successful, the function returns 0 to indicate that the port is open.
    This script is intended for educational and ethical purposes only. Do not use it to scan networks without proper authorization.
