@echo on

pip install virtualenv

virtualenv Venv

python Venv\Scripts\activate

pip install -r requirements.txt

start main.py

exit