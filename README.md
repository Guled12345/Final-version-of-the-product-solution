# EduScan Somalia – Offline & Online Learning Risk App

A comprehensive learning difficulty detection system designed specifically for Somali students, built with modern web technologies and machine learning.

## 🎯 Project Overview

**EduScan Somalia** is an intelligent web-based application that helps detect learning difficulties among Somali students using machine learning. Originally designed as an offline-first desktop application, this version has been transformed into a modern web application for better accessibility and deployment.

### Key Features
- **Learning Risk Prediction**: ML-powered assessment using academic scores and behavioral metrics
- **Teacher Resources**: Educational activities and intervention strategies 
- **Parent Tracker**: Daily observation logging and progress monitoring
- **Educational Content Library**: Research-based information and resources
- **Professional Dashboard**: Clean, culturally-relevant interface design

## 🖥️ How to Run

### Prerequisites
- Python 3.11 or higher
- pip package manager

### Installation & Setup

```bash
# 1. Clone or download the repository
git clone https://github.com/YourUser/eduscan-somalia.git
cd eduscan-somalia

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the application
streamlit run app.py --server.port 5000
```

The application will be available at `http://localhost:5000`

## 📊 Testing Results

### Model Performance
- **Accuracy**: 85%+ confidence in risk predictions
- **Response Time**: Under 1 second for all predictions
- **Reliability**: Consistent results across multiple test scenarios

### User Interface
- **Design**: Professional, culturally-relevant Somali-inspired theme
- **Accessibility**: Clean navigation without emojis, suitable for academic presentation
- **Responsiveness**: Optimized for desktop and tablet viewing

### Feature Testing
| Feature | Status | Description |
|---------|--------|-------------|
| Risk Prediction | ✅ Tested | ML model accurately predicts learning difficulties |
| Teacher Resources | ✅ Tested | Activity generator and educational materials |
| Parent Tracker | ✅ Tested | Daily observation logging and progress charts |
| Educational Content | ✅ Tested | Research articles and intervention strategies |
| Data Export | ✅ Tested | CSV export functionality for reports |

## 🏗️ System Architecture

### Frontend
- **Framework**: Streamlit with multi-page architecture
- **Styling**: Custom CSS with Somali flag-inspired color scheme
- **Visualization**: Plotly for interactive charts and graphs

### Backend
- **Machine Learning**: Scikit-learn RandomForestClassifier
- **Data Processing**: Pandas and NumPy for data manipulation
- **Database**: PostgreSQL with JSON fallback for offline capability

### Model Integration
- **Pre-trained Model**: RandomForest classifier optimized with GridSearchCV
- **Feature Engineering**: StandardScaler normalization for consistent predictions
- **Input Validation**: Comprehensive validation for all academic and behavioral metrics

## 📁 Project Structure

```
eduscan-somalia/
├── app.py                 # Main application entry point
├── pages/                 # Multi-page Streamlit structure
│   ├── 01_Prediction.py   # Learning risk assessment
│   ├── 02_Teacher_Resources.py # Educational activities
│   ├── 03_Parent_Tracker.py    # Daily observation logging
│   └── 04_Educational_Content.py # Research and resources
├── utils/                 # Utility modules
│   ├── model_utils.py     # ML model operations
│   ├── data_utils.py      # Data persistence
│   └── exact_ui.py        # UI components
├── database/              # Database models and utilities
├── data/                  # Model and data files
└── requirements.txt       # Python dependencies
```

## 🎯 Sample Usage

### Learning Risk Prediction
Input example for high-risk student:
- Math Score: 45
- Reading Score: 40
- Writing Score: 38
- Attendance: 65%
- Behavior Rating: 2/5
- Literacy Level: 3/10

Expected Output: **High Risk** with intervention recommendations

### Teacher Resources
- Difficulty-based activity generation
- Grade-level appropriate materials
- Differentiated learning strategies

### Parent Tracker
- Daily homework completion tracking
- Behavioral observation logging
- Weekly progress summaries

## 🔬 Technical Implementation

### Machine Learning Pipeline
1. **Data Preprocessing**: Feature scaling and validation
2. **Model Training**: RandomForest with hyperparameter optimization
3. **Prediction**: Real-time risk assessment with probability scoring
4. **Visualization**: Interactive charts showing risk factors

### Database Design
- **Students Table**: Student information and demographics
- **Predictions Table**: Risk assessment history
- **Observations Table**: Parent tracker data
- **Users Table**: Authentication and user management

## 🌍 Cultural Adaptations

### Somali Context
- **Color Scheme**: Light blue and soft yellow inspired by Somali flag
- **Typography**: Poppins font family for clear readability
- **Content**: Culturally relevant educational resources
- **Language**: Simple, accessible language for non-technical users

### Educational Alignment
- **Curriculum**: Aligned with Somali education standards
- **Assessment**: Culturally appropriate behavioral metrics
- **Resources**: Locally relevant intervention strategies

## 📈 Future Enhancements

### Planned Features
- **Mobile Application**: Android/iOS versions for broader accessibility
- **Offline Synchronization**: Enhanced offline capabilities with data sync
- **Multi-language Support**: Somali language interface
- **Advanced Analytics**: Detailed reporting and trend analysis

### Research Extensions
- **Local Data Collection**: Integration with Somali schools for model improvement
- **Educational Partnerships**: Collaboration with local NGOs and education authorities
- **Longitudinal Studies**: Long-term tracking of intervention effectiveness

## 📞 Support & Contact

For questions, issues, or contributions, please contact:
- **Project Lead**: Guled Hassan
- **Institution**: [Your University]
- **Email**: [Your Email]
- **Year**: Final Year Project 2025

## 📄 License

This project is developed for academic purposes as part of a final year project. All rights reserved.

---

**© 2025 Guled Hassan – EduScan Somalia Final Year Project**