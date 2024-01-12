from flask import Flask, request, jsonify
from flask_cors import CORS
import requests, dropbox

# -------------------------------- WebApp API -------------------------------- #
app = Flask(__name__)
CORS(app)


@app.route('/auth-step-one', methods=['GET'])
def main():
    '''
    Fulfills GET requests.
    Responds with authorization URL & a DropboxOAuth2FlowNoRedirect instance (JSON).
    '''
    APP_KEY = "bx9yg1jyu7zkj18"
    APP_SECRET = "qmqy549b9wab3dk"

    authorization_flow = dropbox.DropboxOAuth2FlowNoRedirect(
        consumer_key= APP_KEY, 
        consumer_secret= APP_SECRET, 
        token_access_type= 'legacy',
        timeout= 100.0
        )

    authorization_url = authorization_flow.start()
    headers = {'Content-Type': 'application/json'}

    return jsonify({'authorizationURL': authorization_url, 'authorizationFlow': authorization_flow}), 200, headers



@app.route('/auth-step-two', methods=['POST'])
def main():
    '''
    Fulfills POST requests transporting authorization code & its DropboxOAuth2FlowNoRedirect instance.
    Responds with long-lived no-expiration access token (JSON).
    '''
    try:
        response_data = request.get_json()
        authorization_flow = response_data['authorizationFlow']
        authorization_code = response_data['authorizationCode'].strip()
        oauth_result = authorization_flow.finish(authorization_code)
        long_lived_access_token = oauth_result.access_token
        headers = {'Content-Type': 'application/json'}

        return jsonify({'longLivedAccessToken': long_lived_access_token}), 200, headers
    
    except Exception as e:
        raise Exception(f'{e}')

if __name__ == '__main__':
    app.run(debug=True)



"""
NAMES FOR JS:

authorizationURL
authorizationFlow
authorizationCode
longLivedAccessToken

"""