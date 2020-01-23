import os
import fleep  
import move
user=move.username() #Check Username of logged in user
#Path of Download folder and Documents folder
path_ = 'C:/Users/' +user+'/Downloads/'
path2_ = 'C:/Users/'+user+'/Documents/'
for entry in os.scandir(path = path2_):  #Scans dir of path of Documents
    if entry.is_dir():  #Checks if it is dir
        continue
    ext = entry.name.split('.')[-1] #gets extension for a file
    move.moveByExt(path2_ , ext, entry.name)  #move file by extension
for entry in os.scandir(path=path_):    #Scan dir of path of Downloads
    if entry.is_dir():  #check if it is dir
        continue
    ext = entry.name.split('.')[-1] #gets extension for a file
    with open(path_+'/'+entry.name,"rb") as file: #Opens that file as a binary file
        DataType = fleep.get(file.read(128)).type   #fleep gets the file type
    if not DataType:    #Somefile's data type is not returned hence those are sorted in download folder by extension
        move.moveByExt(path_ , ext, entry.name)
        continue
    move_ = move.checkFileType(DataType,user,path_) #check file type
    if move_ == 'None': 
        move.moveByExt(path_ , ext, entry.name)
    else:
        move.moveToRespectiveFolder(move_,entry.name,path_)
