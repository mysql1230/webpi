# -*- coding: utf-8 -*- 

import os
import sys
import web
PATH =os.path.dirname(os.path.realpath(__file__))
sys.path.append(PATH)
from audio import *


urls = (
  '/(.*)', 'index',
  '/webpi/?(.*)', 'index'
)

app = web.application(urls, globals())
render = web.template.render(os.path.join(PATH, 'templates'))

if __name__ == 'main':
#     local debug
    audio = Audio('d:/11')
else:
    # on deployment
    audio = Audio()
    

class index:
    def GET(self, id):
        musicList = audio.list()
        if id and int(id) >=0 :
            audio.set(id)
            audio.play()
            
        return render.index(musicList)


if __name__ == '__main__':
    app.run()
elif __name__.startswith('_mod_wsgi'):
    application = app.wsgifunc()
    