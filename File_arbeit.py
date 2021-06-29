import os

def createfolder(folder_name, path):

    if not (os.path.exists(path+'/'+ folder_name)):
        os.chdir(path)
        os.mkdir(folder_name)


createfolder('qwerty','c:\work\FIL_arbeit')