import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    
    def test_case_joy(self):
        """Test Case 1: Statement involving Joy"""
        res = emotion_detector("I am glad this happened")
        self.assertEqual(res['dominant_emotion'], 'joy')

    def test_case_anger(self):
        """Test Case 2: Statement involving Anger"""
        res = emotion_detector("I am really mad about this")
        self.assertEqual(res['dominant_emotion'], 'anger')

    def test_case_disgust(self):
        """Test Case 3: Statement involving Disgust"""
        res = emotion_detector("I feel disgusted just thinking about it")
        self.assertEqual(res['dominant_emotion'], 'disgust')

    def test_case_sadness(self):
        """Test Case 4: Statement involving Sadness"""
        res = emotion_detector("I am so sad about this news")
        self.assertEqual(res['dominant_emotion'], 'sadness')

    def test_case_fear(self):
        """Test Case 5: Statement involving Fear"""
        res = emotion_detector("I am really scared of what will happen")
        self.assertEqual(res['dominant_emotion'], 'fear')

if __name__ == "__main__":
    unittest.main()
