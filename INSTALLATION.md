# EduScan Somalia - Installation Guide

## Quick Start

### Option 1: Using Python Script (Recommended)
```bash
# 1. Navigate to the project folder
cd EduScan_Somalia_Submission

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the application
python run_app.py
```

### Option 2: Direct Streamlit Command
```bash
# 1. Navigate to the project folder
cd EduScan_Somalia_Submission

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run with Streamlit
streamlit run app.py --server.port 5000
```

## Access the Application
Once started, open your web browser and go to:
**http://localhost:5000**

## System Requirements
- Python 3.11 or higher
- 4GB RAM minimum
- 1GB free disk space
- Modern web browser (Chrome, Firefox, Safari, Edge)

## Troubleshooting

### Common Issues
1. **Port already in use**: Change port number in the command
2. **Permission errors**: Run with administrator privileges
3. **Package conflicts**: Use a virtual environment

### Virtual Environment Setup (Recommended)
```bash
# Create virtual environment
python -m venv eduscan_env

# Activate (Windows)
eduscan_env\Scripts\activate

# Activate (Mac/Linux)
source eduscan_env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run application
python run_app.py
```

## Support
For technical issues, refer to the main README.md or contact the project maintainer.