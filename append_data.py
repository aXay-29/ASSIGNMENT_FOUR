def write_to_file(filename):
    # Write user input
    data = input("Enter text to write to the file: ")
    with open(filename, 'w') as file:
        file.write(data + '\n')

def append_to_file(filename):
    # Append user input
    more_data = input("Enter text to append to the file: ")
    with open(filename, 'a') as file:
        file.write(more_data + '\n')

def read_file(filename):
    # Read and display file content
    print("\nFinal content of the file:")
    with open(filename, 'r') as file:
        for line in file:
            print(line.strip())

# Main Program
file_name = "output.txt"
write_to_file(file_name)
append_to_file(file_name)
read_file(file_name)
