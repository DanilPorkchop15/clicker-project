@echo off

set launch_mode=release

IF EXIST venv\Scripts\activate.bat (
	echo "venv exist"
	call venv\Scripts\activate.bat
) ELSE (
	echo "Installing venv"
	python -m venv venv
	call venv\Scripts\activate.bat
	pip install -r requirements.txt
)

python src/main.py %launch_mode%