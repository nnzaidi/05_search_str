import os

text = input("Enter specific text/word: ")
dir = input("Enter directory path: ")

def getfiles(dir):
    f = 0
    os.chdir(dir)
    files = os.listdir()
    for filename in files:
        abs_path = os.path.abspath(filename)
        if os.path.isdir(abs_path):
            getfiles(abs_path)
        if os.path.isfile(abs_path):
            f = open(filename,"r")
            if text in f.read():
                f = 1
                final_path = os.path.abspath(filename)
                print(text + " found in " + final_path)
                return True
            
    if f != 1:
        print(text + " not found in any files!")
        return False
    
getfiles(dir)