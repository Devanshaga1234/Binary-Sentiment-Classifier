from flask import Flask, render_template, request, jsonify
import math
from collections import Counter

app = Flask(__name__)

# Simple sentiment classifier using basic word lists
positive_words = {
    'good', 'great', 'excellent', 'amazing', 'fantastic', 'wonderful', 'awesome', 
    'brilliant', 'outstanding', 'perfect', 'love', 'loved', 'best', 'superb',
    'incredible', 'marvelous', 'terrific', 'fabulous', 'magnificent', 'stunning',
    'beautiful', 'gorgeous', 'delightful', 'charming', 'impressive', 'remarkable',
    'exceptional', 'phenomenal', 'spectacular', 'breathtaking', 'inspiring',
    'enjoyable', 'entertaining', 'fun', 'funny', 'hilarious', 'engaging',
    'compelling', 'captivating', 'thrilling', 'exciting', 'satisfying'
}

negative_words = {
    'bad', 'terrible', 'awful', 'horrible', 'disgusting', 'hate', 'hated', 
    'worst', 'disappointing', 'boring', 'stupid', 'dumb', 'annoying', 'irritating',
    'frustrating', 'confusing', 'messy', 'chaotic', 'disorganized', 'unclear',
    'poor', 'weak', 'pathetic', 'ridiculous', 'absurd', 'nonsense', 'garbage',
    'trash', 'waste', 'pointless', 'useless', 'meaningless', 'empty', 'shallow',
    'predictable', 'cliché', 'overrated', 'underwhelming', 'mediocre', 'average',
    'bland', 'dull', 'lifeless', 'dead', 'flat', 'uninspiring', 'uninteresting'
}

def classify_sentiment(text):
    """Improved sentiment classification with weighted scoring"""
    words = text.lower().split()
    
    # Weighted sentiment scoring
    pos_score = 0
    neg_score = 0
    
    # Strong sentiment words get higher weights
    strong_positive = {'fantastic', 'amazing', 'outstanding', 'brilliant', 'perfect', 'excellent', 'incredible', 'wonderful', 'superb', 'magnificent', 'spectacular', 'phenomenal', 'exceptional', 'marvelous', 'terrific', 'fabulous', 'stunning', 'breathtaking', 'inspiring', 'masterpiece', 'flawless', 'seamless'}
    strong_negative = {'terrible', 'awful', 'horrible', 'disgusting', 'worst', 'disaster', 'nightmare', 'torture', 'painful', 'unbearable', 'miserable', 'depressing', 'devastating', 'ruined', 'destroyed', 'pathetic', 'ridiculous', 'absurd', 'garbage', 'trash', 'waste', 'pointless', 'useless'}
    
    # Count sentiment words with weights
    for word in words:
        if word in strong_positive:
            pos_score += 3  # Strong positive words get 3 points
        elif word in strong_negative:
            neg_score += 3  # Strong negative words get 3 points
        elif word in positive_words:
            pos_score += 1  # Regular positive words get 1 point
        elif word in negative_words:
            neg_score += 1  # Regular negative words get 1 point
    
    # Calculate total sentiment score
    total_sentiment_score = pos_score + neg_score
    
    if total_sentiment_score == 0:
        return {
            'prediction': 'Neutral',
            'confidence': 0.0,
            'pos_score': pos_score,
            'neg_score': neg_score
        }
    
    # Calculate sentiment strength
    sentiment_difference = abs(pos_score - neg_score)
    sentiment_ratio = sentiment_difference / total_sentiment_score
    
    # SIMPLE HIGH CONFIDENCE CALCULATION
    # Start with high base confidence
    confidence = 0.8  # Start at 80%
    
    # Boost for strong sentiment words
    if any(word in strong_positive for word in words) or any(word in strong_negative for word in words):
        confidence += 0.1  # +10% for strong words
    
    # Boost for clear sentiment (not mixed)
    if (pos_score > 0 and neg_score == 0) or (neg_score > 0 and pos_score == 0):
        confidence += 0.05  # +5% for pure sentiment
    
    # Boost for multiple sentiment words
    if total_sentiment_score >= 3:
        confidence += 0.05  # +5% for multiple words
    
    # Cap at 95%
    confidence = min(confidence, 0.95)
    
    # Determine prediction
    if pos_score > neg_score:
        prediction = 'Positive'
    elif neg_score > pos_score:
        prediction = 'Negative'
    else:
        prediction = 'Neutral'
        confidence = 0.5
    
    return {
        'prediction': prediction,
        'confidence': confidence,
        'pos_score': pos_score,
        'neg_score': neg_score
    }

@app.route('/')
def index():
    """Main page"""
    return render_template('simple_index.html')

@app.route('/classify', methods=['POST'])
def classify():
    """API endpoint for sentiment classification"""
    try:
        data = request.get_json()
        text = data.get('text', '').strip()
        
        if not text:
            return jsonify({'error': 'No text provided'}), 400
        
        result = classify_sentiment(text)
        return jsonify(result)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'model': 'simple_word_based'})

@app.route('/debug', methods=['POST'])
def debug_classify():
    """Debug endpoint to see detailed classification info"""
    try:
        data = request.get_json()
        text = data.get('text', '').strip()
        
        if not text:
            return jsonify({'error': 'No text provided'}), 400
        
        words = text.lower().split()
        
        # Strong sentiment words
        strong_positive = {'fantastic', 'amazing', 'outstanding', 'brilliant', 'perfect', 'excellent', 'incredible', 'wonderful', 'superb', 'magnificent', 'spectacular', 'phenomenal', 'exceptional', 'marvelous', 'terrific', 'fabulous', 'stunning', 'breathtaking', 'inspiring', 'masterpiece', 'flawless', 'seamless'}
        strong_negative = {'terrible', 'awful', 'horrible', 'disgusting', 'worst', 'disaster', 'nightmare', 'torture', 'painful', 'unbearable', 'miserable', 'depressing', 'devastating', 'ruined', 'destroyed', 'pathetic', 'ridiculous', 'absurd', 'garbage', 'trash', 'waste', 'pointless', 'useless'}
        
        # Analyze words
        detected_strong_pos = [word for word in words if word in strong_positive]
        detected_strong_neg = [word for word in words if word in strong_negative]
        detected_regular_pos = [word for word in words if word in positive_words and word not in strong_positive]
        detected_regular_neg = [word for word in words if word in negative_words and word not in strong_negative]
        
        result = classify_sentiment(text)
        
        return jsonify({
            'text': text,
            'total_words': len(words),
            'strong_positive_words': detected_strong_pos,
            'strong_negative_words': detected_strong_neg,
            'regular_positive_words': detected_regular_pos,
            'regular_negative_words': detected_regular_neg,
            'pos_score': result['pos_score'],
            'neg_score': result['neg_score'],
            'sentiment_difference': abs(result['pos_score'] - result['neg_score']),
            'final_result': result
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("🎬 Simple Sentiment Classifier Web App")
    print("=" * 50)
    print("Starting Flask app...")
    print("🌐 The app will be available at: http://localhost:5000")
    print("⏹️  Press Ctrl+C to stop the server")
    print("-" * 50)
    app.run(debug=True, host='0.0.0.0', port=5000)
