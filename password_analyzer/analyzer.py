import re
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from transformers import pipeline
import os

class PasswordAnalyzer:
    def __init__(self):
        self.common_patterns = [
            r'\d{4}$',  # Year at the end
            r'^[A-Z][a-z]+$',  # Capitalized word
            r'^[a-z]+$',  # All lowercase
            r'^[A-Z]+$',  # All uppercase
            r'^\d+$',  # All numbers
            r'^[!@#$%^&*]+$',  # All special characters
        ]
        self.sentiment_analyzer = pipeline("sentiment-analysis")
        
    def analyze(self, password):
        """Analyze password strength and provide detailed feedback"""
        
        # Basic metrics
        length = len(password)
        has_upper = bool(re.search(r'[A-Z]', password))
        has_lower = bool(re.search(r'[a-z]', password))
        has_digit = bool(re.search(r'\d', password))
        has_special = bool(re.search(r'[!@#$%^&*]', password))
        
        # Pattern analysis
        patterns_found = []
        for pattern in self.common_patterns:
            if re.search(pattern, password):
                patterns_found.append(pattern)
        
        # Entropy calculation
        entropy = self._calculate_entropy(password)
        
        # Pattern recognition using ML
        pattern_score = self._analyze_patterns(password)
        
        # Generate feedback
        feedback = {
            'length': length,
            'has_upper': has_upper,
            'has_lower': has_lower,
            'has_digit': has_digit,
            'has_special': has_special,
            'entropy': entropy,
            'pattern_score': pattern_score,
            'patterns_found': patterns_found,
            'strength_score': self._calculate_strength_score(
                length, has_upper, has_lower, has_digit, 
                has_special, entropy, pattern_score
            )
        }
        
        return feedback
    
    def _calculate_entropy(self, password):
        """Calculate password entropy"""
        char_set = 0
        if re.search(r'[a-z]', password):
            char_set += 26
        if re.search(r'[A-Z]', password):
            char_set += 26
        if re.search(r'\d', password):
            char_set += 10
        if re.search(r'[!@#$%^&*]', password):
            char_set += 8
            
        return len(password) * np.log2(char_set) if char_set > 0 else 0
    
    def _analyze_patterns(self, password):
        """Analyze password patterns using ML"""
        # This is a simplified version. In production, you would use a trained model
        # on the RockYou dataset to identify common patterns
        score = 1.0
        
        # Deduct points for common patterns
        if re.search(r'\d{4}$', password):  # Year at the end
            score -= 0.2
        if re.search(r'^[A-Z][a-z]+$', password):  # Capitalized word
            score -= 0.1
        if len(password) < 8:
            score -= 0.3
            
        return max(0, score)
    
    def _calculate_strength_score(self, length, has_upper, has_lower, 
                                has_digit, has_special, entropy, pattern_score):
        """Calculate overall password strength score"""
        score = 0
        
        # Length contribution
        if length >= 12:
            score += 3
        elif length >= 8:
            score += 2
        elif length >= 6:
            score += 1
            
        # Character type contribution
        score += sum([1 for x in [has_upper, has_lower, has_digit, has_special] if x])
        
        # Entropy contribution
        if entropy >= 100:
            score += 3
        elif entropy >= 60:
            score += 2
        elif entropy >= 30:
            score += 1
            
        # Pattern score contribution
        score += pattern_score * 2
        
        return min(10, score)  # Normalize to 10-point scale 