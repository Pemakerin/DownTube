#!/bin/bash

apt update && echo "S" | apt upgrade
echo "S" | apt install python3 python3-pip
echo "S" | apt-get install python3-wxgtk4.0
echo "S" | apt-get install build-essential python3-dev libwebkit2gtk-4.0-dev libtiff-dev libnotify-dev freeglut3-dev libsdl1.2-dev libgstreamer-plugins-base1.0-dev
echo "S" | pip3 install wheel pytube
echo "S" | pip3 install wxPython 
mkdir /opt/downtube
cp -r * /opt/downtube
touch /usr/share/applications/ytube.desktop
echo "[Desktop Entry]" >> /usr/share/applications/ytube.desktop
echo "Type=Application" >> /usr/share/applications/ytube.desktop
echo "Icon=/opt/downtube/icon/img_1.png" >> /usr/share/applications/ytube.desktop
echo "Name=DownTube" >> /usr/share/applications/ytube.desktop
echo "Exec=python3 /opt/downtube/ytube.py" >> /usr/share/applications/ytube.desktop
echo "NoDisplay=false" >> /usr/share/applications/ytube.desktop
echo 
echo "Pronto ..."
