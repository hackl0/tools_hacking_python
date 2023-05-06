Directory Enumerator

    This Python script checks for valid directories on a web server using a provided list of directories and a target URL.

Requirements

    using the command "pip install -r requirements.txt"

Usage

    1 - Run the script using the command "python3 enum_directory.py <target_URL>" where <target_URL> is the URL of the web server you want to check directories for.
    
    2 - The script will iterate through each directory in wordlist.txt, append it to <target_URL>, and send a GET request to the resulting URL.
    
    4 - If a valid directory is found, the script will print the full URL to the console.

Exemple 

    python3 enum_directory.py 54.239.28.85

Notes

    The script will ignore any directories that return a 404 status code.
    This script is intended for educational and ethical purposes only. Do not use it to scan networks without proper authorization.
