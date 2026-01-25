import uvicorn
from fastapi import FastAPI, HTTPException, Response, Depends
from authx import AuthX, AuthXConfig
from models.User import UserLoginSchema
app = FastAPI()

config = AuthXConfig()
config.JWT_SECRET_KEY="SECRET_KEY"
config.JWT_ACCESS_COOKIE_NAME= "my_access_token"
config.JWT_TOKEN_LOCATION=["cookies"]


security =  AuthX(config=config)

@app.post("/login")
def login(creds: UserLoginSchema, response: Response):
    if creds.username == "test" and creds.password == "test":
        token = security.create_access_token(uid="12345")
        response.set_cookie(config.JWT_ACCESS_COOKIE_NAME, token)
        return {"acess_token": token}
    raise HTTPException(status_code=401, detail="idi nahuy")

@app.get("/protected", dependencies=[Depends(security.access_token_required)])
def protected():
    return {"data": "TOP SECRET"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)