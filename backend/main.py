from fastapi import FastAPI, Depends, HTTPException
from authx import AuthX, AuthXConfig

app = FastAPI()

config = AuthXConfig(
    JWT_SECRET_KEY="your-secret-key",  # Change this!
    JWT_TOKEN_LOCATION=["headers"],
)

auth = AuthX(config=config)
auth.handle_errors(app)

@app.post("/login")
def login(username: str, password: str):
    if username == "test" and password == "test":
        token = auth.create_access_token(uid=username)
        return {"access_token": token}
    raise HTTPException(401, detail="Invalid credentials")

@app.get("/protected", dependencies=[Depends(auth.access_token_required)])
def protected():
    return {"message": "Hello World"}