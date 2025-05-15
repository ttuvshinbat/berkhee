# with context

with open('log.txt', 'r') as file:
    pisda= []
    position = file.tell()
    file.seek(10)
    
    content = file.read()
    print(content)

# read file line by line 
with open("log.txt", 'r') as file:
    for line in file:
        print(line.rstrip())
        
    
    

    
        