import requests  # Import the requests library to handle HTTP requests
import json

# Define a function named sentiment_analyzer that takes a string input (text_to_analyse)
def emotion_detector(text_to_analyse):  
    # URL of the sentiment analysis service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Custom header specifying the model ID for the sentiment analysis service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Sending a POST request to the sentiment analysis API
    response = requests.post(url, json=myobj, headers=header)

    if response.status_code == 500:
        return {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}
    elif response.status_code == 400:
        return {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}
    else:
        # Parsing the JSON response from the API
        formatted_response = json.loads(response.text)

        emotions = formatted_response['emotionPredictions'][0]['emotion']

        emotion_values = list(emotions.values())

        emotion_values.sort()
        
        max_score = emotion_values[len(emotion_values) - 1]

        for key in emotions.keys():
            if emotions[key] == max_score:
                emotions["dominant_emotion"] = key
                break
            else:
                continue

        return emotions

    

