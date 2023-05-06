Description

    This Python script is a basic SSH password cracker

Dependencies

    pip install -r requirements.txt

Usage

   1 - Run the script using the command "python3 brute_force_ssh.py <target> <username> <password_file>".

   2 - Replace <target> with the IP address of the target.
   
   3 - Replace <username> with the username to bruteforce.

   4 - Replace <password_file> with the location of the password file.

Exemples

   python3 brute_force_ssh.py 192.168.1.10 john /usr/share/wordlists/rockyou.txt

Limitations

   This script is a very basic implementation of an SSH password cracker and may not be effective against complex passwords or secure SSH configurations. 
   It is recommended to use a more advanced tool or technique for more complex SSH attacks.

Note

   This script is intended for educational and ethical purposes only. Do not use it to scan networks without proper authorization.
