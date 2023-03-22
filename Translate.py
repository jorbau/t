import requests
import json

class Translate():
    def __init__(self, url="http://localhost:5000/translate"):
        self.url = url
    def translate(self, text, source="auto", target="en", format="text", only_text=False):

        url = "http://localhost:5000/translate"
        data = {
            "q": text,
            "source": source,
            "target": target,
            "format": format,
            "api_key": ""
        }
        headers = {
            "Content-Type": "application/json"
        }

        response = requests.post(url, headers=headers, data=json.dumps(data))
        if only_text:
            return response.json()["translatedText"]
        return response.json()
