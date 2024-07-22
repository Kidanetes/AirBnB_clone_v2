#!/usr/bin/env bash
#set up a web browser for deployment
sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
echo "Web static" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
sudo sed -i '39i location /hbnb_static/ {\nalias /data/web_static/current/;\n}' /etc/nginx/sites-available/default
sudo service nginx restart
