import uvicorn
from fastapi import FastAPI, HTTPException, Depends
from controllers.person_controller import PersonController
from controllers.auth_controller import AuthController
from schemas.person import PersonLoginSchema

app = FastAPI()


app.include_router(PersonController().router)
app.include_router(AuthController().router)



# @app.get("/protected", dependencies=[Depends(security.access_token_required)])
# def protected():
#     return {"data": "TOP SECRET"}




if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)