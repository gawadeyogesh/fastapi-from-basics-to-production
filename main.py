from fastapi import FastAPI, Request
from mockdata import products


app=FastAPI()


@app.get("/")

def home():

    return { "message": "Hellow World!!"}


@app.get("/about")

def about():

    return { "message":"This is the about the page of the FastAPI application."}



@app.get("/product")

def get_product():
    return products


@app.get("/product/{product_id}")
def get_product_by_id(product_id: int):
    
    for oneproduct in products:
        if oneproduct.get("id")== product_id:
            return oneproduct
    return{
         "message": "Product not found"
    }
    
        

@app.get("/greet")

def greet(name: str):

    return {
        "message": f"helllo everyone My name is {name} !!!!!!! how are you doing"
    }



@app.get("/some")

def some(request: Request):

    print(request.query_params)


    return {
        "some":"this is the my age"
    }