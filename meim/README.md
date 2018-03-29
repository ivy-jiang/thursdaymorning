On local:
cd setup
python3 sanity.py
cd ..
./upstart.sh

On remote:
change hostname in run/wsgi.py
apt-get update
apt-get -y install python3-pip
pip3 install flask
pip3 install flask_bootstrap
""
