import os
with open("text.txt","r") as file1:
    reading = file1.read()
    print("Reading content...\n",reading)

with open("test.txt","w") as file2:
   
   
    print(os.getcwd())
    os.chdir('G:\\Learn Python\\python')
    print(os.getcwd())
    os.chdir('G:\\Learn Python')
    print(os.getcwd())

    print("Listing Directories and Files",os.listdir())

    #os.mkdir('test')
    #print(os.listdir())

    #renaming directory
   #// os.rename('test','new')
    print(os.listdir())
    #os.remove("test.txt")
    os.rmdir('new')
    print(os.listdir())
