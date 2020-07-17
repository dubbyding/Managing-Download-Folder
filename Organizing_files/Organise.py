import os 
import platform
import shutil
import getpass
import datetime
import csv
from time import sleep
if __name__ == "__main__":
    from Fileextensions import *
else:
    from .Fileextensions import *

class org:
    #Class To Organise
    def __init__(self):
        print("Ready")
    def usernameFind(self): 
        """
        usernameFind()
        Check Username of logged in user
        """
        return self.username()
        
    def platformUsing(self):
        '''
        platfromUsing()
        checking os
        '''
        pltfrm = platform.system()
        return pltfrm
    def setPath(self, platformName):
        """
        setPath(platfromName)
            platformName: Platform name ie. Linux or Windows or Darwin(MacOS)
        Path of Download folder and Documents folder
        """
        if(platformName =='Windows'):
            return 'C:/Users/' + self.user
        elif(platformName =='Linux'):
            return '/home/' + self.user
        elif(platformName =='Darwin'):
            return '/Users/' + self.user
        
    def searchingPath(self, path, platformName):
        """
        searchingPath(path, platfromName)
            path: path till username in linux or windows or macOS
            platfromName: Platfrom name either linux or windows or macOS
        Set searching path of downloads and documents
        """
        self.path_ = path +'/Downloads/'
        self.path2_ = path +'/Documents/'
        if platformName == 'Windows':
            if(not(self.checkPath(self.path2_))):
                self.onedrive = True
                self.path2_ = path + '/OneDrive/Documents/'
    def checkPath(self, pathNeeded):
        """
        checkPath(self, pathNeeded)
            pathNeeded : Path of the directory
        Checks if the directory exists or not
        """
        return(os.path.isdir(pathNeeded))
    def username(self):
        '''
        username()
        Get username of logged in user
        '''
        return getpass.getuser()
    def checkFileType(self, ext, path, platformName):
        """
        checkFileType(ext, user, initialPath, platformName)
            ext: Gives the extension of a file
            path: Give the path of either C:/Users/Username or /home/username/ or pass setPath(pathformName)
            platformName: Linux or Windows 
        Check if the file is System, Video, audio, raster-image or none of them
        and returns the location of Music, Video, Picture and Document folder
        """
        types_ = ['audio' for i in audio[:] if i == self.ext]
        if types_ and types_[0] == 'audio':
                return(path + '/Music')
        types_ = ['video' for i in video[:] if i == self.ext]
        if types_ and types_[0] == 'video':
            return (path + '/Videos')
        types_ = ['raster-image' for i in image[:] if i == self.ext]
        if types_ and types_[0] == 'raster-image':
            if platformName == 'Linux':
                return(path +'/Pictures')
            else:
                if(self.onedrive):
                    return(path +'/OneDrive/Pictures')
                else:
                    return(path +'/Pictures')
        types_ = ['document' for i in document[:] if i == self.ext]
        if types_ and types_[0] == 'document':
            if platformName == 'Linux':
                return(path+'/Documents')
            else:
                if(self.onedrive):
                    return(path +'/OneDrive/Documents')
                else:
                    return(path +'/Documents')
        if not types_:
            return('None')
    def moveByExt(self, path_, ext, entry):
        '''
        moveByExt(path_, ext, entry)
            path_: path where the file exists and is the same location folder of extension name will be made
            ext: name of extension of the file
            entry: name of the file
        Arrange Files through Extension
        '''
        source = path_+'/'+entry
        destination = path_+'/'+ext+'/'+entry
        self.log(source, destination)
        if os.path.exists(path_+'/'+ext):
            shutil.move(source, destination)
        else:
            os.makedirs(path_+'/'+ext)
            shutil.move(source, destination)
    def moveToRespectiveFolder(self, move, name, path_):
        '''
        moveToRespectiveFolder(move, name, path_)
            move: Has the path of Music or Picture or Documents or Video folder respective to OS
            name: name of the file
            path_: Current location of the file
        Moves file to respective folder
        '''
        source = path_+'/'+name
        destination = move+'/'+name
        self.log(source, destination)
        shutil.move(source, destination)
    def log(self, source, destination):
        """
        log(source, destination)
            source: Source location of the file
            destination: Destination Location of the file
        Logs all the file that has been
        """
        logpath = self.path2_ + "/Managing-Download-Folder-Logs/"
        fieldnames = ['Year/Month/Day','HH/MM/SS', 'Source', 'Destination']
        year = datetime.datetime.now().strftime("%Y/%m/%d")
        time = datetime.datetime.now().strftime("%I:%M:%S %p")
        file_data_dict = {'Year/Month/Day': year,'HH/MM/SS': time, 'Source': source.encode('utf8'), 'Destination': destination.encode('utf8')}
        print(type(time))
        if not self.checkPath(logpath):
            os.makedirs(self.path2_ + "/Managing-Download-Folder-Logs/")
            with open(logpath + 'log.csv', 'w', newline="") as log_file:
                writer = csv.DictWriter(log_file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow(file_data_dict)
                print(file_data_dict)
                log_file.close
        else:
            with open(logpath + 'log.csv', 'a', newline="") as log_file:
                writer = csv.DictWriter(log_file, fieldnames=fieldnames)
                writer.writerow(file_data_dict)
                print(file_data_dict)
                log_file.close
        
    def runInfinite(self, tLoop):
        '''
        runInfinite(tLoop)
            tLoop: Time for program to loop in seconds
        Repeat organizing every tLoop seconds
        '''
        while(1):
            self.runOnce()
            print(".")
            sleep(tLoop)
    def runOnce(self):  
        """
        runOnce()
        Runs the program exactly one time
        """    
        self.user = self.usernameFind()
        platformName = self.platformUsing()
        path = self.setPath(platformName)
        if platformName == 'Darwin':
            platformName = 'Linux'
        self.searchingPath(path, platformName)
        '''Organize everything once'''
        for entry in os.scandir(path = self.path_):    #Scan dir of path of Downloads
            if entry.is_dir():  #check if it is dir
                continue
            self.ext = entry.name.split('.')[-1] #gets extension for a file
            if (self.ext == 'crdownload' or self.ext == 'part' or self.ext == 'ini'):
                continue
            self.move_ = self.checkFileType(self.ext, path, platformName)
            try:
                if self.move_ == 'None': 
                    self.moveByExt(self.path_ , self.ext, entry.name)
                else:
                    self.moveToRespectiveFolder(self.move_, entry.name, self.path_)
            except FileExistsError:
                continue
        for entry in os.scandir(path = self.path2_):  #Scans dir of path of Documents
            if entry.is_dir():  #Checks if it is dir
                continue
            self.ext = entry.name.split('.')[-1] #gets extension for a file
            try:
                self.moveByExt(self.path2_ , self.ext, entry.name)  #move file by extension
            except FileExistsError:
                continue
    def __del__(self):
        print("Done")
