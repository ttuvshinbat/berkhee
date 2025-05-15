# file read with Context

with open('output.text', "w") as file:
    file.write("Hello World")

with open("log.txt", "a") as file:
    file.write("New log Entry centextoos handaj bn \n")

# working with multiple files

with open('input.txt','r' ) as input_file, open('output.txt', 'w') as output_file:
    for line in input_file:
        output_file.write(line.upper().strip())
        