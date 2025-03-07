import openai
from dotenv import load_dotenv
import os
from flask import Flask, render_template, request, redirect, url_for, session
import markdown

load_dotenv()
openai.api_key = os.getenv("SECRET_KEY")
client = openai.OpenAI(api_key=os.getenv("SECRET_KEY"))

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "default-secret-key")


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
        return response_content

    def get_car_image(self, message):
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[{
                "role": "system", "content": "You are a car image model " +
                "system. With the model that the user inquires about, " +
                "generate an image of the car."
                },
                {"role": "user", "content": message}]
        )
        image_description = response.choices[0].message.content

        response = client.images.generate(
            model="dall-e-3",
            prompt=image_description,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        
        return response.data[0].url


# Initialize chatbot
chatbot = Chatbot(client=client)


@app.route('/', methods=['GET', 'POST'])
def index():
    if 'chat_history' not in session:
        session['chat_history'] = []
    
    if request.method == 'POST':
        vin = request.form['vin']
        if vin:
            # Clear existing chat history when a new VIN is submitted
            session['chat_history'] = []
            
            # Reset chatbot context to only include the system message
            chatbot.context = [
                {
                    "role": "system",
                    "content": "You are a helpful assistant providing " +
                    "information on used cars. When a VIN is received, provide " +
                    "a detailed report on the model. Include the year, make, " +
                    "model, trim, and other relevant information. " +
                    "Format your response in Markdown with headings, lists, and emphasis. " +
                    "Use bullet points for listing features and recommendations."
                }
            ]
            
            response_content = chatbot.chat(vin)
            image_url = chatbot.get_car_image(response_content)
            
            # Convert Markdown to HTML
            html_content = markdown.markdown(response_content)
            
            # Add to chat history
            session['chat_history'].append({
                'user': vin,
                'assistant': html_content,
                'image_url': image_url
            })
            session.modified = True
            
            return redirect(url_for('index'))
    
    return render_template('index.html', chat_history=session['chat_history'])


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
