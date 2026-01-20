#!/bin/bash

COPPELIA_URL_22="https://downloads.coppeliarobotics.com/V4_10_0_rev0/CoppeliaSim_Edu_V4_10_0_rev0_Ubuntu22_04.tar.xz"
COPPELIA_URL_24="https://downloads.coppeliarobotics.com/V4_10_0_rev0/CoppeliaSim_Edu_V4_10_0_rev0_Ubuntu24_04.tar.xz"

# Detect OS Version
if [ -f /etc/os-release ]; then
    . /etc/os-release
    OS_VERSION_ID=$VERSION_ID
else
    print_error "Cannot detect OS version. Defaulting to Ubuntu 22.04 link."
    OS_VERSION_ID="22.04"
fi

if [[ "$OS_VERSION_ID" == "24.04" ]]; then
    COPPELIA_URL=$COPPELIA_URL_24
    COPPELIA_FILE="CoppeliaSim_Edu_V4_10_0_rev0_Ubuntu24_04.tar.xz"
    print_msg "Detected Ubuntu 24.04. Using corresponding CoppeliaSim version."
else
    COPPELIA_URL=$COPPELIA_URL_22
    COPPELIA_FILE="CoppeliaSim_Edu_V4_10_0_rev0_Ubuntu22_04.tar.xz"
    print_msg "Detected Ubuntu $OS_VERSION_ID (or other). Using Ubuntu 22.04 CoppeliaSim version."
fi

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
echo "   Project MANAS RL Workshop - Final Task "
echo "=========================================="

check_dependency xz-utils


if [ -d "CoppeliaSim" ]; then
    print_msg "CoppeliaSim directory exists. Skipping download."
else
    print_msg "Downloading CoppeliaSim (approx 200MB+)..."
    if wget -O "$COPPELIA_FILE" "$COPPELIA_URL"; then
        print_msg "Extracting CoppeliaSim..."
        tar -xf "$COPPELIA_FILE"
        
        # Renaissance the extracted folder to a simpler name
        EXTRACTED_DIR=$(tar -tf "$COPPELIA_FILE" | head -1 | cut -f1 -d"/")
        mv "$EXTRACTED_DIR" "CoppeliaSim"
        mv "CoppeliaSim" "../../"
        
        rm "$COPPELIA_FILE"
        print_msg "CoppeliaSim installed in /CoppeliaSim"
    else
        print_error "Failed to download CoppeliaSim. Check your internet connection or URL."
        exit 1
    fi
fi

print_msg "=========================================="
print_msg "           Final Task Setup Complete!     "
print_msg "=========================================="
echo "To Run CoppeliaSim:"
echo "   cd /CoppeliaSim"
echo "   ./coppeliaSim.sh"
print_msg "=========================================="
