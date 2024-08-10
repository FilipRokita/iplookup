from flask import Flask, request, jsonify, send_from_directory
import subprocess
import json

app = Flask(__name__, static_folder='.')

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/lookup', methods=['GET'])
def lookup():
    ip_address = request.args.get('ip')
    if not ip_address:
        return jsonify({"error": "IP address is required"}), 400
    
    # Call the Python script to perform the IP lookup
    try:
        result = subprocess.run(
            ['python3', 'iplookup.py', ip_address],
            capture_output=True,
            text=True,
            check=True
        )
        result_json = json.loads(result.stdout)
        return jsonify(result_json)
    except subprocess.CalledProcessError as e:
        return jsonify({"error": f"Error running script: {e.stderr}"}), 500
    except json.JSONDecodeError:
        return jsonify({"error": "Error decoding JSON from Python script"}), 500

if __name__ == '__main__':
    app.run(debug=True)
