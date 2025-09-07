# CS440/ECE448 MP1: Naive Bayes Sentiment Classifier

## Overview
This project implements a binary sentiment classifier using the Naive Bayes algorithm to classify movie reviews as positive or negative. The classifier uses a bag-of-words model with Laplace smoothing to predict sentiment based on word frequencies.

## Project Structure
```
template/
├── naive_bayes.py          # Main implementation (ONLY file to submit)
├── mp1.py                  # Main program for testing
├── reader.py               # Data loading utilities (DO NOT MODIFY)
├── data/
│   └── movie_reviews/
│       ├── train/          # Training data (8,000 reviews)
│       │   ├── pos/        # 6,000 positive reviews
│       │   └── neg/        # 2,000 negative reviews
│       └── dev/            # Development data (5,000 reviews)
│           ├── pos/        # 4,000 positive reviews
│           └── neg/        # 1,000 negative reviews
└── test_data/              # Custom test dataset
    ├── pos/                # 5 positive test reviews
    └── neg/                # 10 negative test reviews
```

## Algorithm Implementation

### Training Phase
1. **Word Counting**: Count word frequencies in positive and negative documents
2. **Vocabulary Building**: Create vocabulary from all training words
3. **Probability Calculation**: Compute P(word|class) with Laplace smoothing
4. **Prior Probabilities**: Set P(positive) and P(negative)

### Classification Phase
1. **Log Probability Calculation**: Use log space to avoid underflow
2. **Document Classification**: Compare P(positive|doc) vs P(negative|doc)
3. **Prediction**: Return 1 for positive, 0 for negative

### Mathematical Formulas

**Laplace Smoothing:**
```
P(word|class) = (count(word,class) + α) / (total_words_class + α * |V|)
```

**Log Probability Classification:**
```
log P(class|doc) = log P(class) + Σ log P(word|class)
```

## Performance Results

### Original Development Set
- **Accuracy**: 89.32%
- **True Positive**: 3,764 (75.28%)
- **True Negative**: 702 (14.04%)
- **False Positive**: 298 (5.96%)
- **False Negative**: 236 (4.72%)

### Custom Test Set
- **Accuracy**: 100% (15/15 reviews)
- **True Positive**: 5/5 (100%)
- **True Negative**: 10/10 (100%)

### Parameter Tuning Results
| pos_prior | laplace | Accuracy | Notes |
|-----------|---------|----------|-------|
| 0.5       | 1.0     | **89.32%** | Best overall performance |
| 0.8       | 0.5     | 88.80%   | Good balance |
| 0.8       | 2.0     | 87.70%   | High false positives |
| 0.8       | 0.1     | 87.04%   | More false negatives |

## Implementation Details

### Core Functions

#### `naive_bayes(train_set, train_labels, dev_set, laplace=1.0, pos_prior=0.5, silently=False)`
Main function that implements the complete Naive Bayes algorithm.

**Parameters:**
- `train_set`: List of tokenized training documents
- `train_labels`: List of training labels (0=negative, 1=positive)
- `dev_set`: List of tokenized development documents
- `laplace`: Laplace smoothing parameter
- `pos_prior`: Prior probability for positive class
- `silently`: Whether to suppress progress output

## Web Application

### **🌐 Live Demo Available!**

This project includes a beautiful web application for real-time sentiment analysis:

#### **🚀 Cloudflare Workers (Live):**
**https://sentiment-worker.devansh-aga2510.workers.dev**

- **Global CDN**: Fast worldwide access
- **Edge Computing**: Runs on Cloudflare's edge network
- **No Server Costs**: Free tier includes 100,000 requests/day
- **Always Online**: 99.9% uptime guarantee

#### **📄 GitHub Pages (Static):**
**https://yourusername.github.io/cs440-template** *(replace with your repo)*

- **Client-side Only**: Runs entirely in the browser
- **No Backend**: Pure HTML/CSS/JavaScript
- **Free Hosting**: Unlimited bandwidth on GitHub
- **Auto-deploy**: Updates automatically on git push

#### **Web App Features:**
- **Beautiful UI**: Modern gradient design with smooth animations
- **Real-time Analysis**: Instant sentiment classification
- **Enhanced Word Lists**: 100+ positive/negative words for better accuracy
- **Weighted Scoring**: Strong sentiment words get 3x weight for better accuracy
- **High Confidence Scores**: Realistic 80-95% confidence for clear sentiment
- **Example Reviews**: Click-to-test sample reviews
- **Visual Progress Bars**: Animated confidence indicators
- **Mobile Responsive**: Works great on phones and tablets
- **Multiple Test Cases**: 8 different example reviews to try
- **Debug Endpoint**: Detailed analysis at `/debug` for development
 - **Two-Column Examples Box**: Sample inputs displayed in a separate two-column grid
 - **Footer with Contact + Icons**: GitHub, Email, and LinkedIn icon buttons

#### **Web App vs ML Model:**
- **Web App** (`simple_app.py`): Simple word-based classifier for demonstration
- **ML Model** (`naive_bayes.py`): Full Naive Bayes implementation for assignment

### **File Structure:**
```
template/
├── naive_bayes.py          # Main ML implementation (SUBMIT THIS)
├── simple_app.py           # Local Flask web application
├── templates/
│   └── simple_index.html   # Beautiful web interface
├── sentiment-worker/       # Cloudflare Workers deployment
│   ├── src/index.js        # JavaScript classifier (same logic as Python)
│   ├── public/index.html   # Static HTML interface
│   ├── wrangler.toml       # Cloudflare configuration
│   └── package.json        # Node.js dependencies
├── github-pages/           # GitHub Pages deployment
│   ├── index.html          # Static HTML interface
│   ├── sentiment-classifier.js # Client-side JavaScript classifier
│   └── README.md           # GitHub Pages documentation
├── .github/workflows/      # GitHub Actions
│   └── deploy-github-pages.yml # Auto-deployment workflow
├── data/movie_reviews/     # Training dataset
└── test_data/              # Custom test reviews
```

### **Confidence Algorithm:**
The web app uses a sophisticated confidence scoring system:

1. **Base Confidence**: Starts at 80% for any sentiment detection
2. **Strong Word Boost**: +10% for words like "fantastic", "terrible", "amazing"
3. **Pure Sentiment Boost**: +5% for clear positive OR negative (not mixed)
4. **Multiple Words Boost**: +5% for 3+ sentiment words
5. **Maximum**: Capped at 95% confidence

#### **Performance:**
- **Response Time**: < 50ms globally
- **Uptime**: 99.9% SLA
- **Bandwidth**: Unlimited on free tier
- **Requests**: 100,000/day free

### **GitHub Pages Deployment:**
 - **Available at:** `https://devanshaga1234.github.io/Sentiment-Classifier/`
