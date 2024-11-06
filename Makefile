# Makefile

# Command to install dependencies (if any are listed in requirements.txt)
install:
    pip install -r requirements.txt

# Command to run unit tests
test:
    python -m unittest test_app.py

# Command to build the application (placeholder command)
build:
    echo "Building the application..."

# Command to deploy the application (placeholder command)
deploy:
    echo "Deploying the application..."
