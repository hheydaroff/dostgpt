#!/bin/bash

# Change the working directory to the script's directory
cd "$(dirname "$0")"

# Check if the virtual environment exists, and create it if not
if [ ! -d "dostgpt_env" ]; then
    python3 -m venv dostgpt_env
fi

# Activate the virtual environment
source dostgpt_env/bin/activate

# Check if all required packages are installed and install them if not
if ! python -c "import openai" &> /dev/null; then
    echo "Installing required packages..."
    pip install -r requirements.txt
fi

# Run the Python script
python3 -m main

# Deactivate the virtual environment
deactivate
