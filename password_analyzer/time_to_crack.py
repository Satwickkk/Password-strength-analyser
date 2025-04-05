import bcrypt
import hashlib
import math
from datetime import datetime, timedelta

class TimeToCrackEstimator:
    def __init__(self):
        # Common hashing speeds (hashes per second)
        self.hashing_speeds = {
            'bcrypt': 100,  # Conservative estimate
            'sha256': 1_000_000,  # Conservative estimate
            'md5': 10_000_000  # Conservative estimate
        }
        
        # Common attack scenarios
        self.attack_scenarios = {
            'brute_force': {
                'speed': self.hashing_speeds['sha256'],
                'description': 'Brute force attack using SHA-256'
            },
            'dictionary': {
                'speed': self.hashing_speeds['sha256'] * 100,  # Faster due to dictionary
                'description': 'Dictionary attack using common passwords'
            },
            'rainbow_table': {
                'speed': self.hashing_speeds['sha256'] * 1000,  # Much faster
                'description': 'Rainbow table attack'
            }
        }
    
    def estimate(self, password):
        """Estimate time to crack for different attack scenarios"""
        # Calculate password entropy
        entropy = self._calculate_entropy(password)
        
        # Calculate possible combinations
        combinations = 2 ** entropy
        
        results = {}
        for scenario, params in self.attack_scenarios.items():
            # Calculate time in seconds
            seconds = combinations / params['speed']
            
            # Convert to human-readable time
            time_str = self._format_time(seconds)
            
            results[scenario] = {
                'time': time_str,
                'description': params['description'],
                'entropy': entropy
            }
        
        return results
    
    def _calculate_entropy(self, password):
        """Calculate password entropy in bits"""
        char_set = 0
        if any(c.islower() for c in password):
            char_set += 26
        if any(c.isupper() for c in password):
            char_set += 26
        if any(c.isdigit() for c in password):
            char_set += 10
        if any(c in '!@#$%^&*' for c in password):
            char_set += 8
            
        return len(password) * math.log2(char_set) if char_set > 0 else 0
    
    def _format_time(self, seconds):
        """Convert seconds to human-readable time"""
        if seconds < 60:
            return f"{seconds:.2f} seconds"
        elif seconds < 3600:
            minutes = seconds / 60
            return f"{minutes:.2f} minutes"
        elif seconds < 86400:
            hours = seconds / 3600
            return f"{hours:.2f} hours"
        elif seconds < 31536000:
            days = seconds / 86400
            return f"{days:.2f} days"
        else:
            years = seconds / 31536000
            return f"{years:.2f} years" 