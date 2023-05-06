Description

    This Python script is a basic hash cracker for MD5 hashes. The script takes in a wordlist file location and a hash to be cracked as inputs. 
    The script then reads each line of the wordlist file, hashes the line using MD5 algorithm and compares it with the provided hash. 
    If a match is found, the cleartext password is printed to the console.

Dependencies

    pip install -r requirements.txt

Usage

    1 - Run the script using the command "python3 crack_hash.py <password_file> <hash>".
    
    2 - Enter the file location of the wordlist when prompted.
   
    3 - Enter the MD5 hash to be cracked when prompted.
    
    4 - Wait for the script to finish running. If a cleartext password is found, it will be printed to the console.

Exemple 

    python3 crack_hash.py /usr/share/wordlists/rockyou.txt 5d41402abc4b2a76b9719d911017c592

Limitations

    This script is a very basic implementation of a hash cracker and may not be effective against complex hashes or strong passwords. 
    It is recommended to use a more advanced tool or technique for more complex hashes. Additionally, the script is currently limited to only cracking MD5 hashes. 

Note

    This script is intended for educational and ethical purposes only. Do not use it to scan networks without proper authorization.
