import random
import json

import torch

from prepared.model import NeuralNet
from prepared.nltk_utils import bag_of_words, tokenize

bot_name = "HaJun"
request_name = "name"
response_exception = "Tôi không biết điều này. Bạn có thể dạy không?"

def get_response(msg):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    FILE = "prepared/data.pth"
    data = torch.load(FILE)

    input_size = data["input_size"]
    hidden_size = data["hidden_size"]
    output_size = data["output_size"]
    all_words = data['all_words']
    tags = data['tags']
    model_state = data["model_state"]

    model = NeuralNet(input_size, hidden_size, output_size).to(device)
    model.load_state_dict(model_state)
    model.eval()

    sentence = tokenize(msg)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    learn = 1
    with open('prepared/intents.json', 'r', encoding="utf8") as json_data:
        intents = json.load(json_data)

    if prob.item() > 0.75:
        for intent in intents['intents']:
            # get name bot
            if tag == intent["tag"] and tag == request_name:
                response_random = random.choice(intent['responses']).capitalize()
                response_name = " ".join([response_random, bot_name])
                learn = 0

                return learn, response_name

            if tag == intent["tag"]:
                response_random = random.choice(intent['responses']).capitalize()
                learn = 0

                return learn, response_random

    return learn, response_exception
