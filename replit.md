# Learning Risk Assessment App

## Overview

This is a Streamlit-based web application designed to predict learning difficulties in students using machine learning. The app provides a comprehensive platform for teachers and parents to assess student learning risks, access educational resources, and track student progress. Originally conceived as a PyQt5 desktop application, it has been implemented as a web-based solution for better accessibility and deployment.

## System Architecture

### Frontend Architecture
- **Framework**: Streamlit with multi-page architecture
- **UI Components**: Custom CSS styling with educational theme
- **Visualization**: Plotly for interactive charts and graphs
- **Layout**: Wide layout with expandable sidebar navigation

### Backend Architecture
- **Web Framework**: Streamlit server
- **Machine Learning**: Scikit-learn RandomForestClassifier for risk prediction
- **Data Processing**: Pandas and NumPy for data manipulation
- **File Storage**: JSON-based data persistence for predictions and user data

### Data Storage Solutions
- **Primary Storage**: PostgreSQL database for robust, scalable data persistence
- **Fallback Storage**: Local JSON files for offline capability and backup
- **Model Storage**: Pickle format for trained ML model (supports user's existing model)
- **User Data**: Database tables for authentication and user management
- **Prediction Data**: Structured database tables for student assessments and predictions

## Key Components

### 1. Main Application (app.py)
- Entry point with custom CSS styling
- Educational theme with gradient headers and feature cards
- Sets up Streamlit configuration and navigation

### 2. Prediction Engine (pages/01_🔍_Prediction.py)
- Student risk assessment interface
- Input validation for academic scores and behavioral metrics
- ML model integration for real-time predictions
- Visualization of risk levels using gauge charts
- Data persistence for prediction history

### 3. Teacher Resources (pages/02_👨‍🏫_Teacher_Resources.py)
- Educational activity generator based on difficulty type and grade level
- Differentiated learning strategies
- Interactive resource library for classroom support

### 4. Parent Tracker (pages/03_👨‍👩‍👧‍👦_Parent_Tracker.py)
- Daily observation logging for parents
- Progress tracking with time-series visualizations
- Weekly summary reports
- Home-based intervention tracking

### 5. Educational Content Library (pages/04_📚_Educational_Content.py)
- Research-based information about learning difficulties
- Statistical data visualization
- Content categorized by audience (teachers, parents, administrators)
- Evidence-based intervention strategies

### 6. Utility Modules
- **model_utils.py**: ML model management, synthetic data generation, prediction logic
- **data_utils.py**: JSON file operations, data persistence, directory management

## Data Flow

1. **User Input**: Academic scores, attendance, behavioral ratings entered via Streamlit forms
2. **Validation**: Input validation ensures data quality and range compliance
3. **Prediction**: Features processed through trained RandomForest model
4. **Visualization**: Risk probabilities displayed via interactive Plotly charts
5. **Storage**: Prediction results saved to JSON files for tracking and analysis
6. **Reporting**: Historical data aggregated for progress monitoring

## External Dependencies

### Core Libraries
- **streamlit**: Web framework and UI components
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computations
- **scikit-learn**: Machine learning algorithms and model training
- **plotly**: Interactive visualization components

### Development Dependencies
- **Python 3.11**: Runtime environment
- **uv**: Package management and dependency resolution
- **Nix**: Environment isolation and reproducible builds

## Deployment Strategy

### Replit Configuration
- **Runtime**: Python 3.11 with Nix package management
- **Deployment Target**: Autoscale for dynamic resource allocation
- **Port Configuration**: Streamlit server on port 5000
- **Workflow**: Parallel execution with automatic port detection

### Production Considerations
- Application designed for offline capability (original PyQt5 concept)
- Relative file paths for cross-platform compatibility
- JSON-based storage for simplicity and portability
- Modular architecture supports future database integration

### Future Enhancements
- Database migration (application structure supports Drizzle/Postgres integration)
- User authentication system implementation
- Google Forms integration for external data collection
- Enhanced reporting and analytics dashboard

## Changelog

```
Changelog:
- June 23, 2025. Initial setup
- June 23, 2025. Major UI enhancement with Somali cultural design
  - Implemented premium design with gradient backgrounds and glass morphism effects
  - Added authentic student imagery throughout all pages
  - Created culturally-adapted visual elements with Somali color schemes
  - Enhanced typography with Poppins font family
  - Improved user experience with hover effects and smooth transitions
  - Added testimonials and success stories sections
  - Integrated visual storytelling elements for better engagement
- June 23, 2025. PostgreSQL database integration
  - Added PostgreSQL database with comprehensive table structure
  - Implemented fallback to JSON files for offline capability
  - Created database utilities for seamless data operations
  - Added database status monitoring in application footer
  - Maintained compatibility with existing model file structure
  - Enhanced data persistence and scalability
- June 23, 2025. User's trained model integration
  - Successfully integrated user's RandomForest model from Jupyter notebook
  - Implemented StandardScaler normalization as per user's training specifications
  - Created model package structure supporting both scaler and model components
  - Added comprehensive model information display in prediction interface
  - Verified model performance with test predictions showing correct risk differentiation
  - Enhanced prediction accuracy using user's GridSearchCV-optimized parameters
- June 25, 2025. Complete UI redesign to match EduScan dashboard design
  - Transformed application to professional dashboard layout with sidebar navigation
  - Implemented clean white background with blue accent colors matching design mockup
  - Created statistical overview cards showing Total, On Track, At Risk, and Intervention students
  - Added class performance overview chart with subject-wise performance metrics
  - Built Recent Assessments and Students Needing Attention sections
  - Integrated Quick Actions panel and System Status monitoring
  - Replaced top navigation with professional sidebar navigation system
  - Enhanced typography using Inter font family for better readability
  - Applied consistent color scheme: #2563eb (primary blue), #16a34a (green), #dc2626 (red), #d97706 (yellow)
  - Removed all emojis and visual indicators that suggest AI generation
  - Replaced emojis with professional symbols and letter abbreviations
  - Updated color scheme to match exact design specifications
- June 25, 2025. Premium UI transformation for commercial-grade appearance
  - Implemented gradient backgrounds and glass morphism effects throughout
  - Added sophisticated hover animations and micro-interactions
  - Enhanced typography with gradient text effects and improved spacing
  - Upgraded button styling with premium shadows and transforms
  - Applied backdrop blur effects for modern depth perception
  - Created professional color gradients using purple-blue scheme
  - Enhanced chart styling with gradient colors and improved readability
  - Added premium branding with "EduScan Pro" and live status indicators
- June 25, 2025. Somali flag-inspired design implementation
  - Updated color scheme to light blue (#87CEEB) and soft yellow (#F8DC75) 
  - Changed typography to Poppins font family for better readability
  - Simplified UI elements with clean cards and subtle shadows
  - Rebranded as "EduScan Somalia" with cultural relevance
  - Applied professional, trustworthy design suitable for thesis presentation
  - Maintained modern layout with rounded corners and consistent spacing
- June 25, 2025. Complete emoji removal and native component conversion
  - Systematically removed all emoji symbols from navigation, buttons, headers, and content
  - Converted HTML dashboard components to native Streamlit elements (st.metric, dataframes)
  - Replaced emoji-based page navigation with clean text-only professional buttons
  - Applied consistent white/light gray background (#f8fafc) across all pages
  - Enhanced accessibility with native components and screen reader compatibility
  - Achieved 100% professional, business-ready interface suitable for academic presentation
```

## User Preferences

```
Preferred communication style: Simple, everyday language.
UI preferences: No emojis in buttons or navigation - prefer clean, professional text-only interface.
Button style: Professional buttons with text labels only, no emoji symbols.
Design approach: Clean, business-ready interface suitable for professional presentation.
```

## Architecture Decisions

### Technology Choices

**Problem**: Need for accessible learning difficulty assessment tool
**Solution**: Streamlit web application over desktop PyQt5 application
**Rationale**: Better accessibility, easier deployment, cross-platform compatibility
**Trade-offs**: Requires internet connection vs. pure offline capability

**Problem**: Data persistence without database complexity
**Solution**: JSON file-based storage system
**Rationale**: Simplicity, portability, no database setup required
**Trade-offs**: Limited scalability vs. ease of deployment and maintenance

**Problem**: Machine learning model for risk prediction
**Solution**: RandomForest classifier with synthetic training data
**Rationale**: Robust performance, interpretable results, handles mixed data types
**Trade-offs**: Requires representative training data vs. immediate deployment capability

### Design Patterns

**Modular Architecture**: Separate utility modules for model and data operations enable code reusability and testing
**Multi-page Structure**: Streamlit's page system provides clear separation of concerns and user workflows
**Progressive Enhancement**: Basic functionality works without advanced features, supporting incremental development