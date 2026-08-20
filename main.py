from fastapi import FastAPI

app=FastAPI()


@app.get("/")

def home():

    return { "message": "Hellow World!!"}


@app.get("/about")

def about():

    return { "message":"This is the about the page of the FastAPI application."}


