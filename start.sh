#!/bin/bash

# Railway deployment start script for CairoSVG testing

echo "Starting CairoSVG test deployment..."

# Check if Python and pip are available
echo "Checking Python environment..."
which python
which pip
python --version

# Run the CairoSVG test
echo "Running CairoSVG test..."
python test_cairosvg.py

echo "CairoSVG test completed successfully!"

# Start a simple HTTP server to keep the service running
echo "Starting HTTP server on port ${PORT:-8080}..."
python -m http.server ${PORT:-8080}
