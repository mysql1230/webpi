# -*- coding: utf-8 -*- 

import glob
import os


class Music(object):
    def __init__(self, filepath):
        self.filepath = filepath
        
    def isValid(self):
        for ext in ['.mp3', '.wma']:
            if self.filepath.lower().endswith(ext):
                return True


class Audio(object):
    def __init__(self, basedir='/data/music'):
        self.basedir = basedir
        self.boxes = []
        self.index = -1
        
    def __flush_list(self,dirname):
        self.boxes = []
        for dirpath,dirnames,filenames in os.walk(dirname):
            for filename in filenames:
                music = Music(os.path.join(dirpath,filename))
                if music.isValid():
                    self.boxes.append(music)
        
    def list(self):
        self.__flush_list(self.basedir)
        return self.boxes
    
    def next(self):
        pass
    
    def last(self):
        pass
    
    def set(self, index):
        self.index = int(index)
    
    def play(self):
        cmd = 'omxplayer \"' + str(self.boxes[self.index].filepath) + '\"'
        os.popen(cmd)
        
    def stop(self):
        pass
        