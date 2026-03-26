@echo off
:: Request administrative privileges
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo Requesting administrative privileges...
    powershell -Command "Start-Process '%~f0' -Verb RunAs"
    exit /b
)

setlocal
color 1f
echo color set [1f]
cd C:\Server
echo Server Dir set.
for /f "tokens=2 delims=:" %%a in ('ipconfig ^| findstr /c:"IPv4 Address"') do (
    set "ipv4_address=%%a"
    goto :found_ip
)
mkdir C:\Server
:found_ip
color a
echo IPv4 address found.
echo Your IPv4 Address is: %ipv4_address%
set "serverdir=C:\Server"
color 1f
echo ---------------------------------------------------------------------------------
echo Welcome to the simple server Hosting interface! This is the software interface for hosting a simple http python-based server. Began on 24/11/2025. 
echo.
echo MODDED EDITION - DEISGNED FOR [PYTHON CHAT.PY] 
echo.
echo Place chat.py within the C:\server directory. Run this file to run it.
echo.
echo.
echo To access; As of 0.1.4.5, the form of access is: http://%ipv4_address%:3000 [auto set] within a browser.
echo.
echo.
echo All files and access is contained within the C:\Server directory.
echo.
echo.
echo.
echo Currently only operational on same-network access.
echo User Directory currently: %Username%
echo Server Directory currently: %serverdir%
echo ---------------------------------------------------------------------------------
python chat.py
pause