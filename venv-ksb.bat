echo off

pushd %~dp0
if not exist venv c:\python36\python.exe -m venv venv
if errorlevel 1 goto ending
call venv\Scripts\activate
if errorlevel 1 goto ending

SET NO_PROXY=%NO_PROXY%,*.keysystems.local
SET PIP_INDEX_URL=http://ksb-dev.keysystems.local:8808/simple/
SET PIP_TRUSTED_HOST=ksb-dev.keysystems.local
SET PIP_TIMEOUT=120

python -m pip install --upgrade -r requirements.txt --retries 2 --timeout 5
if errorlevel 1 goto ending

python mysite\manage.py migrate
if errorlevel 1 goto ending

:ending
popd
