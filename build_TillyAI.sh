#!/bin/bash

# Script to build and set up TillyAI

echo "Setting up TillyAI environment..."

# Update system packages (for Termux/Linux)
if command -v pkg > /dev/null; then
    echo "Updating Termux packages..."
    pkg update -y && pkg upgrade -y
    pkg install python git -y
elif command -v apt-get > /dev/null; then
    echo "Updating system packages..."
    sudo apt-get update && sudo apt-get upgrade -y
    sudo apt-get install python3 python3-pip git -y
fi

# Install Python dependencies
echo "Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Download spaCy language model (optional)
echo "Downloading spaCy language model (optional)..."
python -m spacy download en_core_web_sm || echo "spaCy model download failed - continuing without it"

# Create necessary directories
echo "Creating project directories..."
mkdir -p logs data

# Create a run script
echo "Creating run script..."
cat > run_tilly.py << 'EOF'
#!/usr/bin/env python3
import sys
import os

# Add current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.main import app

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
EOF

chmod +x run_tilly.py

echo "TillyAI setup completed successfully!"
echo "To run the application: python3 run_tilly.py"
echo "Or with PYTHONPATH: PYTHONPATH=. python3 src/main.py"