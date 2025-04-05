import random
import string
import re
from transformers import pipeline

class PasswordGenerator:
    def __init__(self):
        self.special_chars = '!@#$%^&*'
        self.text_generator = pipeline("text-generation", model="gpt2")
        
    def generate_suggestions(self, original_password):
        """Generate improved password suggestions based on the original password"""
        suggestions = []
        
        # Generate multiple variations
        for _ in range(3):
            suggestion = self._improve_password(original_password)
            if suggestion and suggestion != original_password:
                suggestions.append(suggestion)
        
        return suggestions
    
    def _improve_password(self, password):
        """Generate an improved version of the password"""
        # Convert to list for manipulation
        chars = list(password)
        
        # Randomly decide which improvements to apply
        improvements = [
            self._add_special_chars,
            self._add_numbers,
            self._capitalize_random,
            self._leetspeak_substitution,
            self._add_length
        ]
        
        # Apply 2-3 random improvements
        num_improvements = random.randint(2, 3)
        random.shuffle(improvements)
        
        for improvement in improvements[:num_improvements]:
            chars = improvement(chars)
        
        return ''.join(chars)
    
    def _add_special_chars(self, chars):
        """Add special characters to the password"""
        # Add 1-2 special characters at random positions
        num_chars = random.randint(1, 2)
        for _ in range(num_chars):
            pos = random.randint(0, len(chars))
            chars.insert(pos, random.choice(self.special_chars))
        return chars
    
    def _add_numbers(self, chars):
        """Add numbers to the password"""
        # Add 1-2 numbers at random positions
        num_chars = random.randint(1, 2)
        for _ in range(num_chars):
            pos = random.randint(0, len(chars))
            chars.insert(pos, str(random.randint(0, 9)))
        return chars
    
    def _capitalize_random(self, chars):
        """Randomly capitalize some letters"""
        for i in range(len(chars)):
            if chars[i].islower() and random.random() < 0.3:
                chars[i] = chars[i].upper()
        return chars
    
    def _leetspeak_substitution(self, chars):
        """Apply leetspeak substitutions"""
        leet_map = {
            'a': '4', 'e': '3', 'i': '1', 'o': '0',
            's': '5', 't': '7', 'l': '1', 'g': '9'
        }
        
        for i in range(len(chars)):
            if chars[i].lower() in leet_map and random.random() < 0.5:
                chars[i] = leet_map[chars[i].lower()]
        return chars
    
    def _add_length(self, chars):
        """Add random characters to increase length"""
        # Add 2-4 random characters
        num_chars = random.randint(2, 4)
        for _ in range(num_chars):
            pos = random.randint(0, len(chars))
            chars.insert(pos, random.choice(string.ascii_letters + string.digits))
        return chars 