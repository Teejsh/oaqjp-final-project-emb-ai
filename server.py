''' Executing this function initiates the application of emotion detector
    to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package : TODO
# Import the emotion_detector function from the package created:
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detect():
    '''This function checks for emotions using text argument sent to the route'''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)
    #Check if there is a dominant emotion from the response is None indicating an error
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    #Extract the emotion object values from the respose
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    #Return a formatted string with the emotion object showing the dominant emootion
    return f"""For the given statement, the system response is
    'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy}, 'sadness': {sadness}. 
    The dominant emotion is {dominant_emotion}."""

@app.route("/")
def render_index_page():
    '''Displays the home page'''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
