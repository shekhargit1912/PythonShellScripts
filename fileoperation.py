import os 

with open("example.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a sample file.\n")

with open("example.txt", "r") as file:
    content = file.read()
    print("File Content:")
    print(content)

# This script demonstrates basic file operations in Python.
# It creates a file named 'example.txt', writes some text into it,
 
# and check the errors in logs file and counts the error 

with open("logs.log", "r") as log_file:
    error_count = {}
    for line in log_file:
        if "Error" in line:
            if line not in error_count:
                error_count[line] = 0
            error_count[line] += 1
    print("Error Counts:")
    for error, count in error_count.items():
        print(f"{error.strip()}: {count}")# then reads the content back and prints it to the console.

# Finally, it reads a log file named 'logs.log', counts occurrences of each error type,
# and prints the counts to the console.
