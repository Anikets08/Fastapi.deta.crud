from fastapi import FastAPI
from pydantic import BaseModel
from deta import Deta
from localFile import key, base


app = FastAPI()
deta = Deta(key)
db = deta.Base(base)

class Structure(BaseModel):
    name: str
    email:str
    todo: str
    due_date: int

app = FastAPI()

@app.get("/")
def say_hello():
    return {"toh kaise hai aap log 😈"}


@app.get("/allData")
def all_data():
    return db.fetch()

@app.post("/add")
def add_todo(body: Structure):
    name = body.name
    email = body.email
    todo = body.todo
    date = body.due_date

    user = db.put({
        "name": name,
        "email": email,
        "todo": todo,
        "date":date
    })
    return {"data": user, "statusCode":200}

@app.delete("/delete/{key}")
def delete_todo(key):
    response = db.delete(key)
    return {"statusCode": 200}

@app.patch("/update/{key}")
def update_todo(key,body:Structure):
    todo = body.todo
    update = db.update({"todo": todo}, key)
    return {"data" : update, "statusCode":200}