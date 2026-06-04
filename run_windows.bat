rmdir /s /q allure-results
rmdir /s /q allure-report
rmdir /s /q screenshots

python3 -m venv .venv
call .venv\Scripts\activate.bat
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

python3 -m pytest --alluredir=allure-results
allure serve allure-results