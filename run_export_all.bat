@echo off
REM Prompt the user to input the total number of subjects
set /p TOTAL_SUBJECTS=Enter the number of subjects:

REM Initialize the subject number counter
set SUBJECT_NUM=0

:loop
REM Activate the motive environment
call mamba activate motive

REM Update update_config.py with the current SUBJECT_NUM
python update_config.py %SUBJECT_NUM%

REM Run move_tak.py
python move_tak.py

REM Run export_tak.py
python export_tak.py

REM Run move_raw.py
python move_raw.py

REM Increment the subject number counter
set /a SUBJECT_NUM+=1

REM Check if SUBJECT_NUM is greater than TOTAL_SUBJECTS, if yes, exit the loop
if %SUBJECT_NUM% leq %TOTAL_SUBJECTS% (
    goto loop
)

echo All subjects processed successfully!
