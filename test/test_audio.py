import os
import shutil
import sys
import unittest

TSTDIR =os.path.dirname(os.path.realpath(__file__))
ROOTDIR = os.path.dirname(TSTDIR)
SRCDIR = os.path.join(ROOTDIR,'webpi')
sys.path.append(TSTDIR)
sys.path.append(SRCDIR)

from audio import *

class Test_Audio(unittest.TestCase):

    def setUp(self):
        os.makedirs('music/subdir')
        with open('music/foo.mp3', 'w'): pass
        with open('music/subdir/bar.mp3', 'w'): pass
        with open('music/subdir/xxx.txt', 'w'): pass

    def tearDown(self):
        shutil.rmtree('music')

    def test_audio_List_is_empty(self):
        audio = Audio('not_exist')
        self.assertEqual(0,audio.list().__len__())
        
    def test_audio_List_is_got(self):
        audio = Audio('music')
        self.assertEqual(2,audio.list().__len__())


if __name__ == "__main__":
    unittest.main()