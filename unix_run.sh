#!/bin/bash
python3 -m venv python-env
source python-env/bin/activate
pip install -r requirements.txt
python3 main.py
