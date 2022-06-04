import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")               # GET /를 호출할 수 있는 엔드포인트
def hello():                # 함수명 - hello
    return "Hello, World!"  # 값 반환


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
