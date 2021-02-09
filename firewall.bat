echo off

set PORT=%1
set PORT=5000
set RULE_NAME="Stream Audio Over Network"
@REM set REMOTE_IP=%2
@REM set REMOTE_IP="192.168.1.XXX"



netsh advfirewall firewall show rule name=%RULE_NAME% >nul
if not ERRORLEVEL 1 (
    echo Deleting Rule
    if not "%1"=="am_admin" (powershell start -verb runas '%0' am_admin & exit /b)
    @REM add to the end remoteip=%REMOTE_IP%
    netsh advfirewall firewall delete rule name=%RULE_NAME% dir=in protocol=TCP localport=%PORT%
    netsh advfirewall firewall delete rule name=%RULE_NAME% dir=in protocol=UDP localport=%PORT%
) else (
    echo Rule %RULE_NAME% does not exist. Creating...
    if not "%1"=="am_admin" (powershell start -verb runas '%0' am_admin & exit /b)
    @REM add to the end remoteip=%REMOTE_IP%
    netsh advfirewall firewall add rule name=%RULE_NAME% dir=in action=allow protocol=TCP localport=%PORT%
    netsh advfirewall firewall add rule name=%RULE_NAME% dir=in action=allow protocol=UDP localport=%PORT%
)
