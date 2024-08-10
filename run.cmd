@echo off
title CureMeAPI

echo [!] Make sure, you've already installed all the required dependencies, along with environment setup and stuff.
echo [!] ALSO DO MAKE SURE YOU'VE CONFIGURED YOUR .env FILE.
echo.
echo [+] Respond with n/N while it asks to weather to terminate batch job or not, since we need to perform a bit of cleanup.
echo.
uvicorn app.app:api --host 0.0.0.0 --port 8888
rmdir /s /q "__pycache__" "app/__pycache__" "app/crud/__pycache__" "app/models/__pycache__" "app/routers/__pycache__" "app/schemas/__pycache__"
