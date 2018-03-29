# thursdaymorning
Generative python

on local: 

cd setup

edit sanity.py .txt to be cleaned (and delete existing generated html and python files)

python3 sanity.py

then run ./upstart.sh



on remote:

apt-get update -y install python3-pip

pip3 install flask flask_bootstrap

change run/wsgi.py hostname

""
