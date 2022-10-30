from fastapi import FastAPI
from sql.database import engine
from router import apiuser

import sql.models.models as models

models.Base.metadata.create_all(bind=engine)



app = FastAPI()
app.include_router(router=apiuser.router)
@app.get("")
def read_users():

    return {"Hello":"TriMai"}





