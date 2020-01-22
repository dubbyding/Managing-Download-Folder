import os
import shutil
def moveByExt(path_, ext, entry):
    if os.path.exists(path_+'/'+ext):
        shutil.move(path_+'/'+entry,path_+'/'+ext+'/'+entry)
    else:
        os.makedirs(path_+'/'+ext)
        shutil.move(path_+'/'+entry,path_+'/'+ext+'/'+entry)
def checkFileType(DataType, path_):
    for types_ in DataType:
        if types_ == 'system':
            break
        elif types_ == 'video':
            move_ = 'C:\\Users\\rmaha\\Videos\\'
        elif types_ == 'audio':
            move_ = 'C:\\Users\\rmaha\\Music\\'
        elif types_ == 'raster-image':
            move_ = 'C:\\Users\\rmaha\\Pictures\\'
        elif types_ == 'document':
            move_ = 'C:\\Users\\rmaha\\Documents\\'
        else:
            move_ = 'None'
    return move_
def moveToRespectiveFolder(move,name,path_):
    shutil.move(path_+'/'+name,move+'/'+name)
