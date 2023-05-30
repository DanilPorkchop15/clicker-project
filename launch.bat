@echo off


:start
cls

set python_ver=36

python ./get-pip.py

pip install requirements.txt

start main.py

pause
exit