@echo off
:loop
REM Prompt the user to input SUBJECT_NUM
set /p SUBJECT_NUM=Enter Subject Number:

REM update_config.py with the provided SUBJECT_NUM
python update_config.py %SUBJECT_NUM%

REM Run mk_dir.py
python mk_dir.py

REM Loop back to prompt again
goto loop
