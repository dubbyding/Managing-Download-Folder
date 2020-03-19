import os 
import platform
import shutil
import getpass
from time import sleep
'''
    Contains all the Necessary functions for Organising
'''
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
'''
    Class To Organise
'''
class org:
    def __init__(self):
        #Check Username of logged in user
        self.user =username()
        #checking os
        self.platformName = platform.system()
        if(self.platformName =='Windows'):
            self.initialPath = 'C:/Users/'
        elif(self.platformName =='Linux'):
            self.initialPath = '/home/'
        #Path of Download folder and Documents folder
        self.path_ = self.initialPath + self.user+'/Downloads/'
        if self.platformName == 'Linux':
            self.path2_ = self.initialPath + self.user+'/Documents/'
        else:
            self.path2_ = self.initialPath + self.user+'/OneDrive/Documents/'
    def runInfinite(self):
        '''Repeat organizing every 60 seconds'''
        while(1):
            self.runOnce()
            sleep(60)
    def runOnce(self):      
        '''Organize everything once'''
        for entry in os.scandir(path = self.path_):    #Scan dir of path of Downloads
            if entry.is_dir():  #check if it is dir
                continue
            self.ext = entry.name.split('.')[-1] #gets extension for a file
            if (self.ext == 'crdownload' or self.ext == 'part'):
                continue
            self.move_ =checkFileType(self.ext, self.user, self.path_, self.initialPath, self.platformName)
            if self.move_ == 'None': 
                moveByExt(self.path_ , self.ext, entry.name)
            else:
                moveToRespectiveFolder(self.move_, entry.name, self.path_)
        for entry in os.scandir(path = self.path2_):  #Scans dir of path of Documents
            if entry.is_dir():  #Checks if it is dir
                continue
            self.ext = entry.name.split('.')[-1] #gets extension for a file
            moveByExt(self.path2_ , self.ext, entry.name)  #move file by extension