# Project Dependencies

## Python Version
- Python 3.11 or higher

## Core Dependencies

### Web Framework
- `streamlit>=1.46.0` - Web application framework for interactive dashboards

### Data Processing
- `pandas>=2.3.0` - Data manipulation and analysis
- `numpy>=2.3.1` - Numerical computing library

### Machine Learning
- `scikit-learn>=1.7.0` - Machine learning algorithms and model training

### Visualization
- `plotly>=6.1.2` - Interactive plotting and charting library

### Database
- `psycopg2-binary>=2.9.10` - PostgreSQL database adapter
- `sqlalchemy>=2.0.41` - Database ORM and toolkit
- `alembic>=1.16.2` - Database migration tool

## Installation Commands

### Using pip (recommended)
```bash
pip install streamlit>=1.46.0 pandas>=2.3.0 numpy>=2.3.1 scikit-learn>=1.7.0 plotly>=6.1.2 psycopg2-binary>=2.9.10 sqlalchemy>=2.0.41 alembic>=1.16.2
```

### Using conda
```bash
conda install streamlit pandas numpy scikit-learn plotly psycopg2-binary sqlalchemy alembic
```

## Development Dependencies (Optional)
- `jupyter` - For notebook development and testing
- `pytest` - For unit testing
- `black` - Code formatting
- `flake8` - Code linting

## System Requirements
- **Operating System**: Windows 10+, macOS 10.14+, or Linux
- **Memory**: 4GB RAM minimum, 8GB recommended
- **Storage**: 1GB free space
- **Network**: Optional (for database connectivity)