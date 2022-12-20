import re
def readFromFile():
    #open file
    file = open("Day7/example.txt")
    #get contents
    con = file.readlines()
    #close fle
    file.close()
    return con


def p1():
    #variables
    totalSum = 0
    currDirectorySum = 0
    i = 0
    directorySizes = []
    dirPath = []
    currLine = ""
    currDirectory = ""
    content = readFromFile()

    #loop to end of file
    while i < len(content):
        #if command is cd /
        if "/" in content[i]:
            print("cd /")
            #set current directory to root
            currDirectory = "root"
            #add currernt directory to end of directory root list
            dirPath.append(currDirectory)
            print(dirPath)
            print("Current Directory is: " + currDirectory)
        #if command is cd..
        elif "cd .." in content[i]:
            print("cd ..")
            #remove last element of dir path list
            dirPath.pop()
            #update current directory
            currDirectory = dirPath[-1]
            print(dirPath)
            print("Current Directory is: " + currDirectory)
        elif "$ cd" in content[i]:
            #get name of current directory
            currDirectory = content[i].replace("cd","").replace("$","")
            print("cd " + currDirectory)
            #update directory path lists
            dirPath.append(currDirectory)
            print(dirPath)
            print("Current Directory is: " + currDirectory)
        elif "$ ls" in content[i]:
            x = 1
            print("ls " + currDirectory)
            
             
             
             

            
                

            

           

        i+=1 







        

        



p1()