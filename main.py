import sys
import openai


class ChatGPT():
    def __init__(self, key):
        self.messages = [[{"role": "system", "content": "as talking to a friend and talk freely and comfortably. \
                           You can ask me for my opinion\
                            answer length maximum is 4000\
                           Speak language only korean. Do not speak english"}],
                          [{"role": "system", "content": "as talking to a friend and talk freely and comfortably. \
                            You can ask me for my opinion\
                            answer length maximum is 4000\
                            Speak language only korean. Do not speak english"}]]
        
        openai.api_key = key

    def get_conversation(self, message, idx):
        self.messages[idx].append({"role": "user", "content": message})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.messages[idx]
        )

        return response.choices[0].message.content


    def start_conversation(self):

        print("Please Input topic.")
        user_input = input(">> ")

        print()
        print()
        user_input = user_input.lower()
        last_messages = ["", user_input]

        while True:
            print()

            last_messages[0] = self.get_conversation(last_messages[1], 0)
            self.messages[0].append({"role": "assistant", "content": last_messages[0]})
            print("[CHAT-1]", last_messages[0])
            print()

            last_messages[1] = self.get_conversation(last_messages[0], 1)
            self.messages[0].append({"role": "assistant", "content": last_messages[1]})
            print("[CHAT-2]", last_messages[1])
            




def main(key):
    gpt = ChatGPT(key)
    gpt.start_conversation()


if __name__ == '__main__':
    main(sys.argv[1])
