# File Explanations

## **Web App Files:**

### **`simple_app.py`** ✅ **WORKING VERSION**
- **Purpose**: Simple, working sentiment classifier web app
- **Features**: 
  - Enhanced word lists (100+ positive/negative words)
  - Beautiful web interface
  - Real-time sentiment analysis
  - No complex ML training required
- **Status**: ✅ **Use this one - it works!**

### **`app.py`** ❌ **COMPLEX VERSION**
- **Purpose**: Full Naive Bayes implementation with ML training
- **Features**:
  - Trains on actual movie review dataset
  - Uses Laplace smoothing
  - More accurate but complex
- **Status**: ❌ **Has dependency issues - use simple_app.py instead**

### **`run_web_app.py`** 🔧 **HELPER SCRIPT**
- **Purpose**: Automated setup and deployment script
- **Features**:
  - Installs dependencies automatically
  - Provides easy startup
  - Shows helpful messages
- **Status**: 🔧 **Helper tool - not the main app**

## **Core ML Files:**

### **`naive_bayes.py`** 🎯 **MAIN ASSIGNMENT FILE**
- **Purpose**: Your CS440/ECE448 MP1 assignment implementation
- **Features**:
  - Complete Naive Bayes algorithm
  - 89.32% accuracy on development set
  - Laplace smoothing
  - Log probability calculations
- **Status**: ✅ **Ready for submission to Gradescope**

### **`mp1.py`** 📊 **TESTING FRAMEWORK**
- **Purpose**: Command-line testing and evaluation
- **Features**:
  - Parameter tuning
  - Performance metrics
  - Batch testing
- **Status**: ✅ **Use for testing your ML model**

### **`reader.py`** 📁 **DATA LOADER**
- **Purpose**: Loads and preprocesses movie review data
- **Features**:
  - Tokenization
  - Stemming support
  - Lowercase conversion
- **Status**: ⚠️ **DO NOT MODIFY - used by autograder**

## **Documentation:**

### **`README.md`** 📖 **PROJECT DOCUMENTATION**
- **Purpose**: Complete project documentation
- **Features**:
  - Algorithm explanation
  - Usage instructions
  - Performance results
  - Submission guidelines

### **`requirements.txt`** 📦 **DEPENDENCIES**
- **Purpose**: Lists required Python packages
- **Features**:
  - Flask for web app
  - NLTK for text processing
  - Other ML libraries

## **Data:**

### **`data/movie_reviews/`** 🎬 **TRAINING DATA**
- **Purpose**: Movie review dataset for training
- **Contents**:
  - 8,000 training reviews
  - 5,000 development reviews
  - Positive/negative labels

### **`test_data/`** 🧪 **CUSTOM TEST DATA**
- **Purpose**: Your custom test reviews
- **Contents**:
  - 5 positive test reviews
  - 10 negative test reviews

## **Templates:**

### **`templates/simple_index.html`** 🌐 **WEB INTERFACE**
- **Purpose**: Beautiful web UI for sentiment analysis
- **Features**:
  - Modern design
  - Real-time analysis
  - Example reviews
  - Mobile responsive

## **Quick Start Guide:**

### **For Web App (Demo):**
```bash
python simple_app.py
# Then open http://localhost:5000
```

### **For ML Testing:**
```bash
python mp1.py
# Tests your Naive Bayes implementation
```

### **For Assignment Submission:**
- Submit only `naive_bayes.py` to Gradescope
- All other files are for development/testing
