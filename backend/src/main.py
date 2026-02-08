import uvicorn
from fastapi import FastAPI, HTTPException, Depends
from middlewares.auth_middleware import AuthExceptionMiddleware
from controllers.person_controller import PersonController
from controllers.auth_controller import AuthController
from schemas.person import PersonLoginSchema

app = FastAPI()

app.add_middleware(AuthExceptionMiddleware)
app.include_router(PersonController().router)
app.include_router(AuthController().router)



# @app.get("/protected", dependencies=[Depends(security.access_token_required)])
# def protected():
#     return {"data": "TOP SECRET"}




if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)