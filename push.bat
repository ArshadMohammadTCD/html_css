@echo off
git add -A
set /p Input= Enter Commit Message:
git commit -m "%Input%"
git push origin main
