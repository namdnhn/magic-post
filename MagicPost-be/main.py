from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import Base, engine
from routers import authRouters, manageRouters

from fastapi import Depends
from controllers.AuthController import reusable_oauth2, isTokenInvalidated

Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(authRouters.router)
app.include_router(manageRouters.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*", "sentry-trace", "baggage"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/api/ping")
def ping(data: str = Depends(reusable_oauth2)):
    if isTokenInvalidated(data):
        return "pong"