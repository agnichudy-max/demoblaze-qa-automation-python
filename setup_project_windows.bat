@echo off

echo ===========================================
echo  Demoblaze QA Automation Setup (Windows)
echo ===========================================

echo.
echo Checking Python installation...
python --version

echo.
echo Creating virtual environment...

if not exist .venv (
    python -m venv .venv
)

echo.
echo Activating virtual environment...

call .venv\Scripts\activate.bat

echo.
echo Upgrading pip...

python -m pip install --upgrade pip

echo.
echo Installing Python dependencies...

python -m pip install selenium pytest faker allure-pytest

echo.
echo Writing requirements.txt...

(
echo selenium
echo pytest
echo faker
echo allure-pytest
) > requirements.txt

echo.
echo Checking Chocolatey installation...

where choco >nul 2>nul

if %errorlevel% neq 0 (
    echo.
    echo Chocolatey is not installed.
    echo Please install Chocolatey manually:
    echo https://community.chocolatey.org/install
    pause
    exit /b
)

echo.
echo Installing Java...

choco install openjdk -y

echo.
echo Installing Node.js...

choco install nodejs -y

echo.
echo Installing Allure CLI...

call npm install -g allure-commandline --save-dev

echo.
echo ===========================================
echo  Verification
echo ===========================================

python --version

python -m pytest --version

allure --version

echo.
echo ===========================================
echo  Setup Complete
echo ===========================================

echo.
echo Run tests with:
echo python -m pytest --alluredir=allure-results

echo.
echo Open Allure report with:
echo allure serve allure-results

pause