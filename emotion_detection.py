
### URL: 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
### Headers: {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
### Input json: { "raw_document": { "text": text_to_analyze } }

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

    formatted_response = json.loads(response.text)

    return formatted_response

