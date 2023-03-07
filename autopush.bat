echo off
git add -A
git commit -m "Autopush %time%"
git push origin main
timeout 10
goto start


