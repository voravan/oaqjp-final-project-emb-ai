"""
Unit testing script for validating the emotion_detector application logic.
"""
import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    """
    Test suite containing evaluation cases for individual emotional statements.
    """
    
    def test_joy(self):
        """Validates correct tracking for joy."""
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result['dominant_emotion'], 'joy')
        
    def test_anger(self):
        """Validates correct tracking for anger."""
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result['dominant_emotion'], 'anger')
        
    def test_disgust(self):
        """Validates correct tracking for disgust."""
        result = emotion_detector("I feel disgusted just thinking about this")
        self.assertEqual(result['dominant_emotion'], 'disgust')
        
    def test_sadness(self):
        """Validates correct tracking for sadness."""
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result['dominant_emotion'], 'sadness')
        
    def test_fear(self):
        """Validates correct tracking for fear."""
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()
