#!/usr/bin/env python3

# Author ID: upandey3@myseneca.ca

import subprocess

def free_space():
    # Run the 'df -h' command and filter for root disk space with awk
    p = subprocess.Popen(
        "df -h | grep '/$' | awk '{print $4}'", 
        shell=True, 
        stdout=subprocess.PIPE, 
        stderr=subprocess.PIPE
    )

    # Capture the output and error
    output, error = p.communicate()

    # If there was an error, return an error message
    if error:
        return f"Error: {error.decode('utf-8').strip()}"
    
    # Return the free space as a string, stripping newline characters
    return output.decode('utf-8').strip()

if __name__ == '__main__':
    print(free_space())
