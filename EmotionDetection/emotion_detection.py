import requests
import json

def emotion_detector(text_to_analyze):
    if not text_to_analyze:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, headers=headers, json=input_json)
    
    if response.status_code == 200:
        response_dict = json.loads(response.text)

        anger_score = response_dict.get('emotion', {}).get('anger', 0)
        disgust_score = response_dict.get('emotion', {}).get('disgust', 0)
        fear_score = response_dict.get('emotion', {}).get('fear', 0)
        joy_score = response_dict.get('emotion', {}).get('joy', 0)
        sadness_score = response_dict.get('emotion', {}).get('sadness', 0)

        emotions = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score
        }
        
        dominant_emotion = max(emotions, key=emotions.get)
        
        return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }
    else:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
print(emotion_detector("I am glad this happened"))