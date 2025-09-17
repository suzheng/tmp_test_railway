#!/usr/bin/env python3
"""
Test script to verify CairoSVG installation and functionality on Railway
"""

import sys
import os

def test_cairosvg():
    """Test CairoSVG import and basic functionality"""
    try:
        print("Testing CairoSVG import...")
        import cairosvg
        print(f"✓ CairoSVG imported successfully (version: {cairosvg.__version__})")
        
        # Test SVG to PNG conversion
        print("Testing SVG to PNG conversion...")
        svg_content = b'<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100"><rect width="100" height="100" fill="blue"/></svg>'
        
        cairosvg.svg2png(bytestring=svg_content, write_to='test.png')
        
        # Check if file was created
        if os.path.exists('test.png'):
            file_size = os.path.getsize('test.png')
            print(f"✓ CairoSVG OK: test.png written (size: {file_size} bytes)")
            return True
        else:
            print("✗ Error: test.png was not created")
            return False
            
    except ImportError as e:
        print(f"✗ Error importing CairoSVG: {e}")
        return False
    except Exception as e:
        print(f"✗ Error during CairoSVG test: {e}")
        return False

def test_system_dependencies():
    """Test if required system libraries are available"""
    print("\nTesting system dependencies...")
    
    libraries = [
        'libcairo.so.2',
        'libpango-1.0.so.0',
        'libgdk_pixbuf-2.0.so.0',
        'libffi.so'
    ]
    
    for lib in libraries:
        try:
            import ctypes
            ctypes.CDLL(lib)
            print(f"✓ {lib} found")
        except OSError:
            print(f"✗ {lib} not found")

if __name__ == "__main__":
    print("=" * 50)
    print("CairoSVG Installation Test for Railway")
    print("=" * 50)
    
    # Test system dependencies
    test_system_dependencies()
    
    # Test CairoSVG
    print("\n" + "=" * 50)
    success = test_cairosvg()
    
    print("\n" + "=" * 50)
    if success:
        print("🎉 All tests passed! CairoSVG is working correctly.")
        sys.exit(0)
    else:
        print("❌ Tests failed. CairoSVG installation incomplete.")
        sys.exit(1)
