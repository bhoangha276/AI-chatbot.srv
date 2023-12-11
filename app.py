from flask import Flask, render_template, request, jsonify

from prepared.chat import get_response

app = Flask(__name__)

@app.get("/")
def index_get():
    return render_template("base.html")

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    learn, response = get_response(text)
    message = {"answer": response}

    if(learn == 1) {
        # training
        #1 get - request
        #2 use training
        #3 respone
    }

    return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True, port=8008)

