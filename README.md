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

## Usage

### Basic Usage
```bash
python mp1.py
```

### With Custom Parameters
```bash
# Adjust Laplace smoothing
python mp1.py --laplace 0.5

# Adjust positive prior
python mp1.py --pos_prior 0.8

# Enable text preprocessing
python mp1.py --lowercase True --stemming True

# Test on custom dataset
python mp1.py --development test_data
```

### Command Line Options
- `--laplace`: Laplace smoothing parameter (default: 1.0)
- `--pos_prior`: Positive class prior probability (default: 0.5)
- `--lowercase`: Convert all words to lowercase (default: False)
- `--stemming`: Apply Porter stemming (default: False)
- `--training`: Training data directory (default: data/movie_reviews/train)
- `--development`: Development data directory (default: data/movie_reviews/dev)

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

## Key Features

### Data Structures
- **Counter**: Efficient word frequency counting
- **Dictionaries**: Fast probability lookups
- **Log Probabilities**: Prevents numerical underflow

### Error Handling
- **Unseen Words**: Handled by Laplace smoothing
- **Empty Documents**: Gracefully handled
- **Vocabulary Mismatch**: Only uses words seen in training

### Performance Optimizations
- **Efficient Counting**: Uses Counter for O(1) word lookups
- **Log Space**: Avoids multiplication of small probabilities
- **Batch Processing**: Processes all documents efficiently

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

**Returns:**
- List of predictions (0=negative, 1=positive) for development documents

### Training Process
1. Count words in positive and negative documents separately
2. Build vocabulary from all training words
3. Calculate likelihood probabilities with Laplace smoothing
4. Set prior probabilities

### Classification Process
1. For each document, calculate log probabilities for both classes
2. Sum log probabilities for all words in the document
3. Classify based on which class has higher log probability

## Dependencies
- Python 3.12
- nltk (for tokenization and stemming)
- numpy (for numerical operations)
- tqdm (for progress bars)
- collections (for Counter)

## Installation
```bash
pip install nltk numpy tqdm
```

## Testing
The implementation has been tested on:
1. **Original development set**: 89.32% accuracy
2. **Custom test set**: 100% accuracy
3. **Various parameter combinations**: Comprehensive parameter tuning
4. **Text preprocessing options**: Lowercase and stemming experiments

## Submission
- **Submit only**: `naive_bayes.py`
- **Do not modify**: `reader.py`, `mp1.py`, or any data files
- **Autograder**: Uses original staff versions of all other files

## Author
CS440/ECE448 Student - Fall 2025

## License
Educational use only - University of Illinois at Urbana-Champaign
