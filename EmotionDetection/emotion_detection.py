
import requests, json

def emotion_detector(text_to_analyze):
    #API Url
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    #Object dictionary with text to be analized
    myobject = {"raw_document":{"text":text_to_analyze}}
    #Headers required by the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    #sent post
    response = requests.post(url,json = myobject, headers=header) 

    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    formatted_response = json.loads(response.text)
    result = formatted_response['emotionPredictions'][0]

    maxemotion = max(result['emotion'], key=result['emotion'].get)

    return {
        'anger': result['emotion']['anger'],
        'disgust': result['emotion']['disgust'],
        'fear': result['emotion']['fear'],
        'joy': result['emotion']['joy'],
        'sadness': result['emotion']['sadness'],
        'dominant_emotion': maxemotion
    }


