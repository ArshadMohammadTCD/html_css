echo off
:start
python .\commiter.py
git push origin main
timeout 10
goto start


