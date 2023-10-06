from prepared.chat import get_response

if __name__ == "__main__":
    print("GO! Bot is running! (type 'quit' to exit)")
    while True:
        # sentence = "do you use credit cards?"
        sentence = input("You: ")
        if sentence == "quit":
            break

        resp = get_response(sentence).capitalize()
        print(resp)