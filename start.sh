#!/bin/bash

# Railway deployment start script for CairoSVG testing

echo "Starting CairoSVG test deployment..."

# Install system dependencies for CairoSVG on Ubuntu/Debian
# echo "Installing system dependencies..."
# apt-get update
# apt-get install -y libcairo2 libcairo2-dev libpango-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info

# Check if Python and pip are available
echo "Checking Python environment..."
which python || which python3
which pip || which pip3
python --version || python3 --version

# Run the CairoSVG test
echo "Running CairoSVG test..."
python test_cairosvg.py || python3 test_cairosvg.py

# Keep the container running for testing
echo "CairoSVG test completed. Keeping container alive..."
tail -f /dev/null
