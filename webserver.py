from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Hello, I am alive!"

def run():
    if __name__ == "__main__":
    # Render에서 자동으로 설정한 PORT 환경 변수를 사용하여 서버 실행
    port = int(os.environ.get("PORT", 8080))  # PORT 환경 변수가 없을 경우 8080 사용
    app.run(host='0.0.0.0', port=port)
    
def keep_alive():
    t = Thread(target=run)
    t.start()
