# AI-Powered Password Strength Analyzer

An intelligent tool that analyzes password strength using GenAI and Machine Learning techniques to predict password vulnerability and provide improvement suggestions.

## Features

- Password strength analysis beyond basic metrics
- Time-to-crack estimation
- AI-powered password improvement suggestions
- Pattern recognition for common password weaknesses
- Real-time feedback with detailed reasoning
- Cross-referencing with public data sources

## Installation

1. Clone the repository
2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the Flask application:
```bash
python app.py
```
2. Open your browser and navigate to `http://localhost:5000`
3. Enter a password to analyze its strength and get improvement suggestions

## Project Structure

- `app.py`: Main Flask application
- `password_analyzer/`: Core password analysis modules
  - `analyzer.py`: Password strength analysis logic
  - `generator.py`: Password generation and improvement
  - `time_to_crack.py`: Time-to-crack estimation
  - `ml_model.py`: Machine learning model for pattern recognition
- `templates/`: HTML templates
- `static/`: Static files (CSS, JS)
- `data/`: Training data and models

## Security Considerations

- No passwords are stored or logged
- All analysis is performed locally
- Uses secure hashing algorithms for time-to-crack estimation

## License

MIT License 