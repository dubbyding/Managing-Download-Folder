import os
import fleep  
import moving
user=moving.username()
path_ = 'C:\\Users\\'+user+'\\Downloads\\'
path2_ = 'C:\\Users\\'+user+'\\Documents\\'
for entry in os.scandir(path = path2_):
    if entry.is_dir():
        continue
    ext = entry.name.split('.')[-1]
    moving.moveByExt(path2_ , ext, entry.name)
for entry in os.scandir(path=path_):
    if entry.is_dir():
        continue
    ext = entry.name.split('.')[-1]
    with open(path_+'/'+entry.name,"rb") as file:
        DataType = fleep.get(file.read(128)).type
    if not DataType:
        moving.moveByExt(path_ , ext, entry.name)
    move_ = moving.checkFileType(DataType,user,path_)
    if move_ == 'None':
        moving.moveByExt(path_ , ext, entry.name)
    else:
        moving.moveToRespectiveFolder(move_,entry.name,path_)
    