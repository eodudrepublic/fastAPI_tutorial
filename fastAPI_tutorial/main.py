from fastapi import FastAPI
app = FastAPI()

from fastapi.responses import FileResponse
# DB 입출력 기능 : DB 접속해주세요~

@app.get("/")       # main page에 접속 했을때
def test():
    # DB 입출력 기능 : DB에서 데이터 꺼내주세요~
    # return "hello"  # return할 데이터
    return FileResponse('index.html')   # main page에 접속시 index.html 파일 전송
# async def -> await
# await : 기다려라 -> 비동기 처리 가능

@app.get("/test1")
def test1():
    return FileResponse('test1.html')

@app.get("/test2")
def test1():
    return FileResponse('test2.html')

@app.get("/test3")
def test1():
    return FileResponse('test3.html')

@app.get("/test4")
def test1():
    return FileResponse('test4.html')

@app.get("/data")       # /data에 접속 했을때
def test():
    return {"hello" : 1234}  # return할 데이터

# API 문서 확인 : /docs, /redoc

# 유저에게 데이터를 받는 기능 테스트

# 유저에게 데이터를 받고 싶으면 모델부터 생성해야 함
from pydantic import BaseModel
# Model 클래스 안에 유저들이 어떤 데이터를 보낼 수 있는지 명시해줘야 함
class Model(BaseModel):
    name : str
    phone : int
@app.post("/send")      # /send에 접속 했을때 : post -> 유저가 데이터를 보낼 수 있는 기능
def test(data : Model): # data : 보낸 데이터 담김, 타입 기능 기본 제공
    print(data)
    return 'Send Successfully'  # return할 데이터