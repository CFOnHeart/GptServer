from flask import Flask, request
app = Flask(__name__)

@app.route('/postchat', methods=['POST'])
def postchat():
    print ("go into post chat")
    body = request.data.decode("utf-8")
    return f'Data recevied: {body}' 

@app.route('/getchat', methods=['GET'])
def getchat():
    print ("go into post chat")
    body = request.data.decode("utf-8")
    return f'Data recevied: {body}'

@app.route('/testget', methods=['GET'])
def testget():
    print ("go into post chat")
    body = request.data.decode("utf-8")
    return f'testget: {body}' 

@app.route('/')
def index():
    print ("go into index /")
    user_agent = request.headers.get('User-Agent')
    return f'Hello! Your user agent is: {user_agent}'

if __name__ == '__main__':
    app.run(host='0.0.0.0')