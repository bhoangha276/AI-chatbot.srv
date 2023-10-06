from pathlib import Path

from prepared.chat import get_response
from prepared.training import train_artificial_intelligence, add_new_intents

def main():
    path = 'prepared/data.pth'
    exist_file = Path(path).exists()

    if not exist_file:
        error = train_artificial_intelligence()
        print('Bot initialized successfully!')
        if error != None:
            return error

    print("GO! Bot is running! (type 'quit' or 'CTRL + C' to exit)")

    try:
        while True:
            # chat with 1 question
            sentence = input("You: ")

            if sentence == "quit":
                break

            learn, resp = get_response(sentence)
            print(resp.capitalize())
            
            if learn == 1:
                new_answer = input("Viết thêm câu trả lời hoặc gõ 'skip' để bỏ qua: ")
                
                if new_answer == 'skip': continue
                
                error = add_new_intents(sentence, new_answer)
                if error != None:
                    return error

                error = train_artificial_intelligence()
                if error != None:
                    return error

                resp = "Cảm ơn bạn! Tôi đã học được :)"
                print(resp.capitalize())
        
    except KeyboardInterrupt:
        print("You typed CTRL + C => exit!")
    
    except Exception as error:
        return error

if __name__ == "__main__":
    error = main()
    if error != None:
        print("Error: ", error)