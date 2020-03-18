import os
import shutil
import getpass
def username():
    '''Get username of logged in user'''
    return getpass.getuser()
def moveByExt(path_, ext, entry):
    '''Arrange Files through Extension'''
    if os.path.exists(path_+'/'+ext):
        shutil.move(path_+'/'+entry,path_+'/'+ext+'/'+entry)
    else:
        os.makedirs(path_+'/'+ext)
        shutil.move(path_+'/'+entry,path_+'/'+ext+'/'+entry)
def checkFileType(ext, user, path_, initialPath,platformName):
    '''Check if the file is System, Video, audio, raster-image or none of them'''
    audio = ['3gp', 'acc', 'flac', 'm4a', 'm4b', 'm4p', 'mp3','wav', 'wma']
    document = ['doc', 'docx', 'pdf', 'odt', 'svg', 'txt', 'ppt', 'pptx', 'xls', 'xlsx']
    video = ['webm', 'mkv', 'flv', 'gif', 'avi', 'ts', 'mov', 'wmv', 'mp4', 'm4p', 'm4v', 'mpeg', 'svi', '3gp', 'm4v']
    image = ['jpg', 'jpeg', 'png', 'bmp', 'webp']
    types_ = ['audio' for i in audio[:] if i == ext]
    if types_ and types_[0] == 'audio':
            return(initialPath + user+'/Music')
    types_ = ['video' for i in video[:] if i == ext]
    if types_ and types_[0] == 'video':
        return (initialPath +user+'/Videos')
    types_ = ['raster-image' for i in image[:] if i == ext]
    if types_ and types_[0] == 'raster-image':
        if platformName == 'Linux':
            return(initialPath + user +'/Pictures')
        else:
            return(initialPath + user +'/OneDrive/Pictures')
    types_ = ['document' for i in document[:] if i == ext]
    if types_ and types_[0] == 'document':
        if platformName == 'Linux':
            return(initialPath + user+'/Documents')
        else:
            return(initialPath + user +'/OneDrive/Documents')
    if not types_:
        return('None')
def moveToRespectiveFolder(move,name,path_):
    '''Moves file to respectie folder'''
    shutil.move(path_+'/'+name,move+'/'+name)
