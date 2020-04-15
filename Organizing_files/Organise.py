import os 
import platform
import shutil
import getpass
from time import sleep
from Organizing_files import Fileextensions
'''
    Contains all the Necessary functions for Organising
'''
'''
    Class To Organise
'''
class org:
    def __init__(self):
        #Check Username of logged in user
        self.user = self.username()
        #checking os
        self.platformName = platform.system()
        if(self.platformName =='Windows'):
            self.initialPath = 'C:/Users/'
        elif(self.platformName =='Linux'):
            self.initialPath = '/home/'
        #Path of Download folder and Documents folder
        self.path_ = self.initialPath + self.user+'/Downloads/'
        if self.platformName == 'Linux':
            self.path2_ = self.initialPath + self.user + '/Documents/'
        else:
            self.path2_ = self.initialPath + self.user + '/OneDrive/Documents/'
    def username(self):
        '''Get username of logged in user'''
        return getpass.getuser()
    def checkFileType(self):
        '''Check if the file is System, Video, audio, raster-image or none of them'''
        types_ = ['audio' for i in audio[:] if i == self.ext]
        if types_ and types_[0] == 'audio':
                return(self.initialPath + self.user+ '/Music')
        types_ = ['video' for i in video[:] if i == self.ext]
        if types_ and types_[0] == 'video':
            return (self.initialPath + self.user + '/Videos')
        types_ = ['raster-image' for i in image[:] if i == self.ext]
        if types_ and types_[0] == 'raster-image':
            if self.platformName == 'Linux':
                return(self.initialPath + self.user +'/Pictures')
            else:
                return(self.initialPath + self.user +'/OneDrive/Pictures')
        types_ = ['document' for i in document[:] if i == self.ext]
        if types_ and types_[0] == 'document':
            if self.platformName == 'Linux':
                return(self.initialPath + self.user+'/Documents')
            else:
                return(self.initialPath + self.user +'/OneDrive/Documents')
        if not types_:
            return('None')
    def moveByExt(self):
        '''Arrange Files through Extension'''
        if os.path.exists(self.path_+ '/' +self.ext):
            shutil.move(self.path_+'/'+self.entry.name,self.path_+'/'+self.ext+'/'+self.entry.name)
        else:
            os.makedirs(self.path_+'/'+ self.ext)
            shutil.move(self.path_+'/'+self.entry.name,self.path_+'/'+self.ext+'/'+self.entry.name)
    def moveToRespectiveFolder(self):
        '''Moves file to respectie folder'''
        shutil.move(self.path_ + '/' + self.entry.name,self.move_+'/' + self.entry.name)
    def runInfinite(self):
        '''Repeat organizing every 60 seconds'''
        while(1):
            self.runOnce()
            sleep(60)
    def runOnce(self):      
        '''Organize everything once'''
        for self.entry in os.scandir(path = self.path_):    #Scan dir of path of Downloads
            if self.entry.is_dir():  #check if it is dir
                continue
            self.ext = self.entry.name.split('.')[-1] #gets extension for a file
            if (self.ext == 'crdownload' or self.ext == 'part'):
                continue
            self.move_ = self.checkFileType()
            if self.move_ == 'None': 
                self.moveByExt()
            else:
                self.moveToRespectiveFolder()
        self.path_ = self.path2_
        for entry in os.scandir(path = self.path_):  #Scans dir of path of Documents
            if entry.is_dir():  #Checks if it is dir
                continue
            self.ext = entry.name.split('.')[-1] #gets extension for a file
            self.moveByExt()  #move file by extension