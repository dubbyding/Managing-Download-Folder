#!/usr/bin/env python3
#!"C:\Python33\python.exe"
import Organizing_files
from createDesktopShortcutLinux import createDesktopShortcut
arrange = Organizing_files.org()
filename = 'Managing Downloads'
executing_filename = 'exec.py'
icon_name = 'logo.png'

if arrange.platformUsing() == 'Linux':
    newShortcut = createDesktopShortcut(filename, executing_filename, icon_name)
    newShortcut.create_desktop_shortcut()
arrange.runOnce()      #To Run Only once
#arrange.runInfinite(60)       #To Run Infinite times
