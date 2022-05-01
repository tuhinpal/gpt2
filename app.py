from flask import Flask, request
from flask_cors import CORS
from transformers import pipeline, set_seed
import os

generator = pipeline('text-generation', model='gpt2')
set_seed(42)

app = Flask(__name__)
CORS(app)
# get the app url from the environment variable
port = int(os.environ.get('PORT', 8080))


@app.route('/gpt2', methods=['POST'])
def index():
    try:
        payload = request.json
        text = payload["text"]
        max_length = int(payload["max_length"])
        if (max_length > 1024):
            max_length = 1024

        generated = generator(text, max_length=max_length,
                              num_return_sequences=1)

        return {
            "status": True,
            "input": text,
            "result": generated
        }

    except:
        return {
            "status": False
        }


# if __name__ == '__main__':
#     app.debug = True
#     app.run(host='0.0.0.0', port=port, use_reloader=True, threaded=True)

# Production
if __name__ == '__main__':
    app.debug = False
    app.run(host='0.0.0.0', port=port)
