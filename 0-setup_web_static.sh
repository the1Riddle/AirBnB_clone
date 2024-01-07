#!/usr/bin/env bash
# sets up the web servers for the deployment of web_static

sudo apt-get -y update > /dev/null
sudo apt-get -y upgrade > /dev/null
sudo apt-get -y install nginx > /dev/null

sudo mkdir -p /data/web_static/releases/test/ /data/web_static/shared
echo "Testing Nginx configuration" | sudo tee /data/web_static/releases/test/index.html

# this checks if the directory already exists
if [ -d "/data/web_static/current" ]
then
        sudo rm -rf /data/web_static/current
fi

# Create a symbolic link to test
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# changes ownership to user ubuntu
sudo chown -hR ubuntu:ubuntu /data/
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

#the server must be restarted to implement the changes
sudo service nginx start
