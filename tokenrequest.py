from flask import Flask, jsonify
import requests
import base64

CLIENT_ID = 'ae596fd96e6c460a9613c41c6e1fccce'
CLIENT_SECRET = '8ee9b071fb1c457d91ba8e326348abf4'
REFRESH_TOKEN = 'AQDa-IZZW8HcFyNK3gD5gGidMZ0PbiZipKHYedthxgKisDd1k8E0ynZ748ZC6D4Er_EVEuFw_bbs07VgvDy0ngI2Pus5N8tavc_3N-tcDuLeIn7GHV0WkAQNjzVh_pjv0Eg'

app = Flask(__name__)

def refresh_access_token():
    url = 'https://accounts.spotify.com/api/token'
    headers = {
        'Authorization': f'Basic {base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode()}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'grant_type': 'refresh_token',
        'refresh_token': REFRESH_TOKEN
    }
    response = requests.post(url, headers=headers, data=data)
    return response.json()['access_token']

@app.route('/token', methods=['GET'])
def get_token():
    access_token = refresh_access_token()
    return jsonify({"access_token": access_token})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
