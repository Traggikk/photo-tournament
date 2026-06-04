@echo off
echo Creating tournament.exe...
pyinstaller --noconsole --onefile tournament.py
echo.
echo Done! Check the 'dist' folder for tournament.exe
pause