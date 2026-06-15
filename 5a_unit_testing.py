import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        # Test Case 1: Statement involving Joy
        res_1 = emotion_detector("I am glad this happened")
        self.assertEqual(res_1['dominant_emotion'], 'joy')
        
        # Test Case 2: Statement involving Anger
        res_2 = emotion_detector("I am really mad about this")
        self.assertEqual(res_2['dominant_emotion'], 'anger')
        
        # Test Case 3: Statement involving Disgust
        res_3 = emotion_detector("I am feel disgusted with this jokes")
        self.assertEqual(res_3['dominant_emotion'], 'disgust')
        
        # Test Case 4: Statement involving Sadness
        res_4 = emotion_detector("I am so sad about this")
        self.assertEqual(res_4['dominant_emotion'], 'sadness')
        
        # Test Case 5: Statement involving Fear
        res_5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(res_5['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()
