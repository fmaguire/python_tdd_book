Provisioning a new site
=======================

## Required packages:

* nginx
* Python 3
* Git
* pip
* virtualenv

eg, on Ubuntu:
    
    sudo apt-get install nginx git python3 python3-pip
    sudo pip3 install virtualenv

## Nginx Virtual Host config

* see nginx.template.conf
* replace SITENAME with e.g. staging.finlaymagui.re

## Upstart Job

* see gunicorn-upstart.template.conf
* replace SITENAME with e.g. staging.finlaymagui.re

## Folder structure: 
Assume we have a user account at /home/username

/home/username
|__sites
    |__SITENAME
        |__database
        |__source
        |__static
        |__virtualenv

