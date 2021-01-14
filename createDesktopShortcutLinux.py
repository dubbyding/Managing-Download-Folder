import os
class createDesktopShortcut:
    def __init__(self, givenFileName, executing_filename, logo_filename):
        '''
            givenFileName = Filename for the shortcut
            executing_filename = Filename with extension whose shortcut is being created
            logo_filename = Icon for the shortcut
        '''
        # Get Current Directory Location
        current_directory = os.path.abspath(os.getcwd())

        # Get Username
        username = current_directory.split('/')[2]

        # Desktop Location
        desktop_location = '/home/' + username + '/Desktop/'

        # FileName
        self.filename = givenFileName

        # Filename of desktop shortcut
        self.file = desktop_location + '/' + givenFileName + '.desktop'

        # Executing file
        self.executing_file = 'Exec=' + current_directory + '/' + executing_filename + '\n'

        #Logo
        self.executing_filename_logo = 'Icon=' + current_directory + '/' + logo_filename +'\n'

    def create_desktop_shortcut(self):
        if not os.path.isfile(self.file):
            with open(self.file, "w") as f:
                f.writelines(["[Desktop Entry]\n",
                            "Name=" + self.filename + "\n", 
                            "Name[en_US]=" + self.filename + "\n",
                            "StartupNotify=true\n", 
                            "Terminal=false\n",
                            self.executing_file,
                            self.executing_filename_logo,
                            "Type=Application\n"])
            os.chmod(self.file, 0o777)

            
