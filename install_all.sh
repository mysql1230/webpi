#!/bin/bash

apt-get install -y python-dev python-pip sshpass
pip install paramiko PyYAML Jinja2 httplib2 six ansible

ansible -i ansible/hosts local -m ping


###to do: move to ansible
#apt-get install -y apache2
#apt-get install -y libapache2-mod-wsgi
#pip install web.py

#chmod a+rw /dev/vchiq