#!/usr/bin/env bash

python3 -m virtualenv django_env
source django_env/bin/activate
pip install -r requirements.txt
