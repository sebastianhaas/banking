#!/usr/bin/env bash

apt-get update
apt-get install -y build-essential
apt-get install -y tesseract-ocr
apt-get install -y libtesseract-dev
apt-get install -y libleptonica-dev

export TESSDATA_PREFIX=/vagrant/invoicescanner