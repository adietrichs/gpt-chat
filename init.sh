# run with "source init.sh"

# Initialize a flag for venv creation
venv_created=0

# create venv if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating venv"
    python -m venv venv
    echo "Venv created"
    # Set the flag to indicate that venv has just been created
    venv_created=1
fi

# activate venv
source venv/bin/activate
echo "Venv activated"

# if venv was just created, upgrade pip and install package
if [ $venv_created -eq 1 ]; then
    echo "Upgrading pip"
    pip install --upgrade pip
    echo "Pip upgraded"
    echo "Installing package in dev mode"
    pip install -e .[dev]
    echo "Package installed"
fi
