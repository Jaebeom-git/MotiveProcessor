@echo off
:loop
REM Prompt the user to input SUBJECT_NUM
set /p SUBJECT_NUM=Enter Subject Number:

REM update_config.py with the provided SUBJECT_NUM
python update_config.py %SUBJECT_NUM%

REM Run move_tak.py
python move_tak.py

REM Run export_tak.py
python export_tak.py

REM Loop back to prompt again
goto loop
