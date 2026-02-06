import uvicorn
from fastapi import FastAPI, HTTPException, Response, Depends
from services.auth import AuthService
from schemas.person import PersonLoginSchema

app = FastAPI()


security = AuthService.make_config

@app.post("/login")
def login(creds: PersonLoginSchema, response: Response):
    if creds.username == "test" and creds.password == "test":
        token = security.create_access_token(uid="12345")
        response.set_cookie(config.JWT_ACCESS_COOKIE_NAME, token)
        return {"acess_token": token}
    raise HTTPException(status_code=401, detail="Incorrect username or password")

@app.get("/protected", dependencies=[Depends(security.access_token_required)])
def protected():
    return {"data": "TOP SECRET"}




if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)