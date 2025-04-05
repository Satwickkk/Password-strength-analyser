from flask import Flask, render_template, request, jsonify
from password_analyzer.analyzer import PasswordAnalyzer
from password_analyzer.generator import PasswordGenerator
from password_analyzer.time_to_crack import TimeToCrackEstimator
import os

app = Flask(__name__)

# Initialize components
analyzer = PasswordAnalyzer()
generator = PasswordGenerator()
time_estimator = TimeToCrackEstimator()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze_password():
    data = request.get_json()
    password = data.get('password', '')
    
    if not password:
        return jsonify({'error': 'No password provided'}), 400
    
    # Analyze password
    analysis = analyzer.analyze(password)
    
    # Estimate time to crack
    time_to_crack = time_estimator.estimate(password)
    
    # Generate improvement suggestions
    suggestions = generator.generate_suggestions(password)
    
    return jsonify({
        'analysis': analysis,
        'time_to_crack': time_to_crack,
        'suggestions': suggestions
    })

if __name__ == '__main__':
    app.run(debug=True) 