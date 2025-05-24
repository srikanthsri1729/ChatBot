from flask import Flask, render_template, request
from google import genai
from google.genai import types

app = Flask(__name__)

client = genai.Client(
    vertexai=True,
    project="qwiklabs-gcp-03-5897c8d86d7f",
    location="global",
)

model = "gemini-2.5-flash-preview-05-20"

@app.route("/", methods=["GET", "POST"])
def chat():
    response = ""
    if request.method == "POST":
        user_input = request.form["message"]
        contents = [
            types.Content(
                role="user",
                parts=[types.Part(text=user_input)]
            )
        ]
        config = types.GenerateContentConfig(
            temperature=1,
            top_p=1,
            seed=0,
            max_output_tokens=2048,
            safety_settings=[
                types.SafetySetting(category="HARM_CATEGORY_HATE_SPEECH", threshold="BLOCK_NONE"),
                types.SafetySetting(category="HARM_CATEGORY_DANGEROUS_CONTENT", threshold="BLOCK_NONE"),
                types.SafetySetting(category="HARM_CATEGORY_SEXUALLY_EXPLICIT", threshold="BLOCK_NONE"),
                types.SafetySetting(category="HARM_CATEGORY_HARASSMENT", threshold="BLOCK_NONE"),
            ],
        )
        for chunk in client.models.generate_content_stream(
            model=model,
            contents=contents,
            config=config
        ):
            response += chunk.text

    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)
