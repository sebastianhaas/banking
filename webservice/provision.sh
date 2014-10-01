#!/usr/bin/env bash

#
# Provisioning shel script for the banking Django webservice
# Creates a simple build/test development machine
#

# Update package list etc.
apt-get update

# Install python3, setuptools3 and pip3
apt-get install -y python3
apt-get install -y python3-setuptools
apt-get install -y python3-pip

# Install MySQL database
sudo debconf-set-selections <<< 'mysql-server mysql-server/root_password password banking'
sudo debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password banking'
sudo apt-get -y install mysql-server

# Install Python MySql driver
wget http://dev.mysql.com/get/Downloads/Connector-Python/mysql-connector-python-2.0.1.tar.gz
gunzip mysql-connector-python-2.0.1.tar.gz
tar xf mysql-connector-python-2.0.1.tar
cd mysql-connector-python-2.0.1
python3 setup.py install
cd ..
rm -rf mysql-connector-python-2.0.1
rm -rf mysql-connector-python-2.0.1.tar

# Install other Python modules
pip3 install Django                 # Django itself
pip3 install djangorestframework    # Django REST framework
pip3 install django-oauth-toolkit   # Django OAuth2 authentication toolkit
pip3 install Pillow                 # Pillow image library required by ImageField

# Create database and user
mysql -uroot -pbanking -e "DROP DATABASE IF EXISTS banking";
mysql -uroot -pbanking -e "CREATE DATABASE banking DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;";