from fastapi import FastAPI
from app.routes.auth import router as auth_router 
from app.routes.chat import router as chat_router   
from app.routes.interview import router as interview_router  

app = FastAPI()
app.include_router(auth_router)
app.include_router(chat_router)
app.include_router(interview_router)

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
# @app.get("/health")
# def health_check():
#     return {"status": "healthy"}