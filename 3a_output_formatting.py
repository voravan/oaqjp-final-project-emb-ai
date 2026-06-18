"""
This module communicates with the Watson NLP Emotion Detection service to analyze text inputs.
"""
import json
import requests

def emotion_detector(text_to_analyse):
    """
    Sends input text to the Watson NLP Emotion Detection API and returns parsed emotion scores.
    Handles blank inputs or API errors by returning dictionary sets with None values.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    
    # Check for empty or whitespace-only inputs before sending request
    if not text_to_analyse or not text_to_analyse.strip():
        return {
            'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None
        }

    response = requests.post(url, json=myobj, headers=headers, timeout=10)
    
    # Check if the API request failed with status code 400
    if response.status_code == 400:
        return {
            'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None
        }

    formatted_response = json.loads(response.text)
    emotion_predictions = formatted_response['emotionPredictions'][0]['emotion']
    
    anger_score = emotion_predictions['anger']
    disgust_score = emotion_predictions['disgust']
    fear_score = emotion_predictions['fear']
    joy_score = emotion_predictions['joy']
    sadness_score = emotion_predictions['sadness']
    
    emotion_dict = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    dominant_emotion = max(emotion_dict, key=emotion_dict.get)

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
