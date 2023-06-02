    @echo off

set launch_mode=release

IF EXIST venv\Scripts\activate.bat (
	echo "venv exist"
) ELSE (
	python -m venv venv
	pip install -r requirements.txt
)

python src/main.py %launch_mode%