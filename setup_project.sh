#!/usr/bin/env bash

set -e

echo "Updating system packages..."
sudo apt update

echo "Installing Java, Node.js, npm, and Chrome dependencies..."
sudo apt install -y \
  default-jre \
  nodejs \
  npm \
  wget \
  curl \
  unzip

echo "Installing Allure CLI globally..."
sudo npm install -g allure-commandline --save-dev

echo "Creating virtual environment if missing..."
if [ ! -d ".venv" ]; then
  python3 -m venv .venv
fi

echo "Activating virtual environment..."
source .venv/bin/activate

echo "Upgrading pip..."
python -m pip install --upgrade pip

echo "Installing Python test dependencies..."
python -m pip install selenium pytest faker allure-pytest

echo "Writing requirements.txt..."
cat > requirements.txt << EOF
selenium
pytest
faker
allure-pytest
EOF

echo "Verifying installations..."
python --version
python -m pytest --version
python -m pip show selenium
python -m pip show allure-pytest
allure --version

echo ""
echo "Setup complete."
echo ""
echo "Run tests with:"
echo "source .venv/bin/activate"
echo "python -m pytest --alluredir=allure-results"
echo ""
echo "Open Allure report with:"
echo "allure serve allure-results"