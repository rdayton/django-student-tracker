Provisioning a new site
=======================

## Required packages:

* nginx
* Python 3
* Git
* pip
* virtualenv

e.g.,, on Ubuntu:

    sudo apt-get install nginx git python3 python3-venv

## Nginx Virtual Host config

* see nginx.template.conf
* replace SITENAME with, e.g., staging.my-domain.com

## Systemd service

* see gunicorn-systemd.template.service
* replace SITENAME with, e.g., staging.my-domain.com
