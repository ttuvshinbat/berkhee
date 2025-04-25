# File Meta Data 
import os 

try: 
    if  os.path.exists('advanced.txt'):
        size = os.path.getsize('advanced.txt')
        print(size)
    
    #get modification time
        mod_time = os.path.getmtime('advanced.txt')
        os.rename('advanced.txt', 'new_advanced.txt')
        print('renamed')
        os.remove('new_advanced.txt') 
        print("removed")
    else:
        print("new_advanced.txt file chamd baina")
    
except ValueError: 
    print("advanced.txt alga baina")   




    
