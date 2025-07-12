from dotenv import load_dotenv
import os

load_dotenv()

from flask import Flask, render_template, request
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

app = Flask(__name__)

# Azure OpenAI configuration
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1"
token = os.environ.get("AZURE_API_TOKEN")

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        old_code = request.form['code']
        output_language = request.form['language']
        
        prompt = f"convert this code {old_code} into {output_language} the output should be only the new code (no any extra text other than code), and give a statement at the end after giving some space below, Your Code is Converted into given language(specify that language name), Thank You for Using Code Translator."
        
        response = client.complete(
            messages=[
                SystemMessage(""),
                UserMessage(prompt),
            ],
            temperature=1,
            top_p=1,
            model=model
        )
        
        translated_code = response.choices[0].message.content
        return render_template('index.html', translated_code=translated_code)

    return render_template('index.html', translated_code=None)

if __name__ == '__main__':
    app.run(debug=True)