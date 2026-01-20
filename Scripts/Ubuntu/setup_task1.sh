#!/bin/bash
print_msg() {
    echo -e "\033[1;32m$1\033[0m"
}

print_warn() {
    echo -e "\033[1;33m$1\033[0m"
}

print_error() {
    echo -e "\033[1;31m$1\033[0m"
}

check_dependency() {
    if ! command -v $1 &> /dev/null; then
        print_warn "$1 could not be found. Attempting to install..."
        sudo apt-get update
        sudo apt-get install -y $1
    else
        print_msg "$1 is already installed."
    fi
}

# --- Main Execution ---

echo "=========================================="
echo "   Project MANAS RL Workshop - Task 1     "
echo "=========================================="

check_dependency python3
check_dependency python3-pip

print_msg "Installing Python Dependencies..."

pip3 install --upgrade pip --user

DEPENDENCIES=("numpy", "pygame", "cbor2", "pyzmq", "coppeliasim-zmqremoteapi-client")
for dep in "${DEPENDENCIES[@]}"; do
    print_msg "Installing $dep..."
    pip3 install $dep --user
done

print_msg "=========================================="
print_msg "           Task 1 Setup Complete!         "
print_msg "=========================================="
