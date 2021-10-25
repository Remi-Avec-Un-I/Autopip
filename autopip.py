import json, os
from os import system, path, remove
from shutil import copyfile

lib = []

speLib = {
    "tkinter" : "tk",
    "pillow" : "pil"
}


system("py -m ensurepip --upgrade") # Install pip

def main(path: str):
    
    for root, directories, file in os.walk(path):
        for file in file:
            if file.endswith('.py'):
                if file == os.path.basename(__file__):
                    pass
                else:
                    libInstaller(foundLib=False, anontherOne=False, toCopy=file)
    remove("tmp.txt")

def installer(word, lib: list, speLib: dict):
    for key in speLib:
        if key == word:
            word = speLib[key] 
    lib = lib.append(word)
    system(f"pip3 install {word}")
    
    
def libInstaller(foundLib, anontherOne, toCopy):
    
    
    copyfile(toCopy, "tmp.txt")
    
    with open("tmp.txt", "r") as f:
        words = f.read().split()
        
    for word in words:
        if foundLib:
            
            if "," in word:
                word = word.replace(",", "")
                anotherOne = True
                installer(word, lib, speLib)
            else:
                installer(word, lib, speLib)
                foundLib = False
        
                            
        elif word == "import" or word == "from":
            foundLib = True
        
        elif anontherOne:
            if "," in word:
                word = word.replace(",", "")
                anotherOne = True
                installer(word, lib, speLib)
            else:
                anontherOne = False
                installer(word, lib, speLib)
            

main(path=r'./')
print("All the libraries that it tried to downlaod :",*lib, sep = ", ")
input("Finish !")