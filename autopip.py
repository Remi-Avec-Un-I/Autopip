import json, os
from os import system, path, remove
from shutil import copyfile

lib = []

def main(path: str):
    
    for root, directories, file in os.walk(path):
        for file in file:
            if file.endswith('.py'):
                libInstaller(foundLib=False, anontherOne=False, toCopy=file)
    remove("tmp.txt")

def installer(word, lib: list ):
    lib = lib.append(word)
    system(f"pip install {word}")
    
    
def libInstaller(foundLib, anontherOne, toCopy):
    
    
    copyfile(toCopy, "tmp.txt")
    
    with open("tmp.txt", "r") as f:
        words = f.read().split()
        
    for word in words:
        if foundLib:
            
            if "," in word:
                word = word.replace(",", "")
                anotherOne = True
                installer(word, lib)
            else:
                installer(word, lib)
                foundLib = False
        
                            
        elif word == "import" or word == "from":
            foundLib = True
        
        elif anontherOne:
            if "," in word:
                word = word.replace(",", "")
                anotherOne = True
                installer(word, lib)
            else:
                anontherOne = False
                installer(word, lib)
            

main(path=r'./')
print("All the libraries that it tried to downlaod :",*lib, sep = ", ")
input("Finish !")