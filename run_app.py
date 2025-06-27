#!/usr/bin/env python3
"""
EduScan Somalia - Learning Risk Assessment Application
Quick start script for running the application
"""

import subprocess
import sys
import os

def check_dependencies():
    """Check if required packages are installed"""
    required_packages = [
        'streamlit', 'pandas', 'numpy', 'scikit-learn', 
        'plotly', 'psycopg2', 'sqlalchemy', 'alembic'
    ]
    
    missing_packages = []
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print("Missing required packages:")
        for package in missing_packages:
            print(f"  - {package}")
        print("\nPlease install missing packages using:")
        print("pip install -r requirements.txt")
        return False
    
    return True

def run_application():
    """Run the Streamlit application"""
    if not check_dependencies():
        sys.exit(1)
    
    print("Starting EduScan Somalia Application...")
    print("Application will be available at: http://localhost:5000")
    print("Press Ctrl+C to stop the application")
    
    try:
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", "app.py", 
            "--server.port", "5000", "--server.address", "0.0.0.0"
        ])
    except KeyboardInterrupt:
        print("\nApplication stopped.")
    except Exception as e:
        print(f"Error running application: {e}")

if __name__ == "__main__":
    # Change to script directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    run_application()