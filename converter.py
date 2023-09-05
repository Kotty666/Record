#!/usr/bin/python3
import os, pydub, shutil
from PLOG import logger
from pydub.playback import play

class Convert:
    def __init__(self,origin_file) -> None:
        self.file_info = os.path.split(origin_file)
        self.checkFolders()
        try:
            wav_file = pydub.AudioSegment.from_file(file = origin_file, format = 'wav')
        except Exception as err:
            logger('Could not load file {}. Got Error: {}'.format(origin_file,err),'ERROR')
            return
        self.file_info = os.path.split(origin_file)
        new_file = self.incVolume(wav_file)
        self.saveNewFile(new_file)
        self.moveOrigin()
        
    def incVolume(self,wav_file):
        logger('Increasing Volume on file: {}'.format(self.file_info[1]))
        louder = wav_file + 20
        return louder
    
    def saveNewFile(self,new_file):
        new_name = self.file_info[0] + "/comp/" + self.file_info[1].replace('.wav','.mp3')
        logger('Save MP3 to: {}'.format(new_name))
        new_file.export(new_name, format="mp3", bitrate="192k")

    def moveOrigin(self):
        new_origin = self.file_info[0] + "/orig/" + self.file_info[1]
        logger('Move {} to {}'.format(self.file_info[1], new_origin))
        shutil.move(self.file_info[0] + "/" + self.file_info[1], new_origin)
    
    def checkFolders(self):
        if not os.path.isdir('{}/comp'.format(self.file_info[0])):
            logger('Creating non existing Directory:{}'.format(self.file_info[0] + "/comp/"))
            os.makedirs(self.file_info[0] + "/comp/")
        if not os.path.isdir('{}/orig'.format(self.file_info[0])):
            logger('Creating non existing Directory:{}'.format(self.file_info[0] + "/orig/"))
            os.makedirs(self.file_info[0] + "/orig/")
