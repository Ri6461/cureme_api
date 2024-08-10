@echo off
title CureMeAPI

echo [!] Make sure, you've already installed all the required dependencies, along with environment setup and stuff.
echo [!] ALSO DO MAKE SURE YOU'VE CONFIGURED YOUR .env FILE.
uvicorn app.app:api --host 0.0.0.0 --port 8888
echo 
echo NOTE: even though you are no to upcoming prompt, its still gonna quit.
