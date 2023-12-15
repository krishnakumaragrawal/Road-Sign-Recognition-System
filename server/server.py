from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/classify_images', methods=['GET', 'POST'])
def classify_images():
    # image_data = './test_images/00003.png'
    image_data = request.form['image_data']
    response = jsonify(util.classify_images(image_data))
    response.headers.add('Access-Control-Allow-Origin', '*')
    print(response)
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server for Road Sign Recognition")
    util.load_saved_artifacts()
    app.run(port=5000, debug=True)