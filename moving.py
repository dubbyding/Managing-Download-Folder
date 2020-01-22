import os
import shutil
import getpass
def username():
    return getpass.getuser()
def moveByExt(path_, ext, entry):
    if os.path.exists(path_+'/'+ext):
        shutil.move(path_+'/'+entry,path_+'/'+ext+'/'+entry)
    else:
        os.makedirs(path_+'/'+ext)
        shutil.move(path_+'/'+entry,path_+'/'+ext+'/'+entry)
def checkFileType(DataType, user, path_):
    for types_ in DataType:
        if types_ == 'system':
            break
        elif types_ == 'video':
            move_ = 'C:\\Users\\'+user+'\\Videos\\'
        elif types_ == 'audio':
            move_ = 'C:\\Users\\'+user+'\\Music\\'
        elif types_ == 'raster-image':
            move_ = 'C:\\Users\\'+user+'\\Pictures\\'
        elif types_ == 'document':
            move_ = 'C:\\Users\\'+user+'\\Documents\\'
        else:
            move_ = 'None'
    return move_
def moveToRespectiveFolder(move,name,path_):
    shutil.move(path_+'/'+name,move+'/'+name)
