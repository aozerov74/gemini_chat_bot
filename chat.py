import os
from flask import Flask, request, json
import google.generativeai as genai

app = Flask(__name__)

# Set the API key
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

@app.route('/v2/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        if 'userInput' not in data or 'systemInput' not in data:
            return json.jsonify({'error': 'Missing required fields'}), 400

        user_input = data['userInput']
        system_input = data['systemInput']
        limit = data.get('limit', 100)

        if 'limit' in data and not isinstance(data['limit'], int):
            return json.jsonify({'error': 'Limit must be an integer'}), 400

        model = genai.GenerativeModel(model_name='gemini-1.5-pro')
        chat = model.start_chat()
        chat.send_message(system_input, is_system=True)
        response = chat.send_message(user_input, generation_config={'maxOutputTokens': limit})
        bot_response = response.text
        return json.jsonify({'botResponse': bot_response})
    except Exception as e:
        return json.jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Changed to port 5000
