from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Hello, I am alive!"

def run():
    port = int(os.environ.get("PORT", 10000))  # Render는 포트 10000을 사용
    app.run(host='0.0.0.0', port=port)
    
def keep_alive():
    t = Thread(target=run)
    t.start()
