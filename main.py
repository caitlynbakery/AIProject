import openai
from dotenv import load_dotenv
import os
import webbrowser

load_dotenv()
openai.api_key = os.getenv("SECRET_KEY")
client = openai.OpenAI(api_key=os.getenv("SECRET_KEY"))


class Chatbot:
    def __init__(self, client):
        self.client = client
        self.context = [
            {
                "role": "system",
                "content": "You are a helpful assistant providing " +
                "information on used cars. When a VIN is received, provide " +
                "a detailed report on the model. Include the year, make, " +
                "model, trim, and other relevant information. " +
                "Recommendations for purchase."
            }
        ]
    
    def chat(self, message):
        self.context.append(
            {"role": "user", "content": message}
        )
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=self.context
        )
        response_content = response.choices[0].message.content
        self.context.append({"role": "assistant", "content": response_content})
        self.print_chat()
        self.show_car(response_content)
    
    def print_chat(self):
        for message in self.context:
            if message['role'] == 'user':
                print("USER: ", message['content'])
            elif message['role'] == 'assistant':
                print('RESPONSE: ', message['content'])
    
    def show_car(self, message):
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "system", "content": """
                        You are a car image model system. With the model that the user inquires about, generate an image of the car. 
                    """}, 
                    {"role": "user", "content": message}]
        )
        print(response.choices[0].message.content)
        image_description = response.choices[0].message.content

        response = client.images.generate(
            model="dall-e-3",
            prompt=image_description,
            size="1024x1024",
            quality="standard",
            n=1,
        )

        # img = Image(url=response.data[0].url)
        # output = climage.convert(response.data[0].url)
        webbrowser.open(response.data[0].url)

        # prints output on console.
        # print(output)
        # display(Image(url=response.data[0].url))


if __name__ == "__main__":
    chatbot = Chatbot(client=client)
    print("Welcome Oppkey Used Car Advisor!")
    print("Input a VIN to get started.")
    user_input = input()

    while (user_input != 'stop'):
        chatbot.chat(user_input)
        print("Enter stop to exit, or input a new message")
        user_input = input()
