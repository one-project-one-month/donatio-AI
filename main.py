from flask import Flask, render_template, request
import requests
import os
url = f"https://graph.facebook.com/v21.0/me"

params = {
    "fields": "name",
    "access_token": os.getenv("FB_ACCESS_TOKEN")  # Use environment variable for access token
}

app = Flask(__name__)

# @ is python decorater -> wrap one function inside of another
@app.route("/")
def index():
    try:
        response = requests.get(url, params=params, timeout=10)
        # response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"
   

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)