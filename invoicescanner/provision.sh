#!/usr/bin/env bash

apt-get update
apt-get install -y build-essential
apt-get install -y tesseract-ocr
apt-get install -y libtesseract-dev
apt-get install -y libleptonica-dev

# Set tessdata environment variable which is currently not working
export TESSDATA_PREFIX=/vagrant/invoicescanner/

# Install Java 8
wget --no-check-certificate https://github.com/aglover/ubuntu-equip/raw/master/equip_java8.sh && bash equip_java8.sh

# Install Android
#wget --no-check-certificate https://github.com/aglover/ubuntu-equip/raw/master/equip_android.sh && bash equip_android.sh