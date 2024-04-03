from fastapi import FastAPI
from src.routers.routes import router

#################################################
app = FastAPI()
app.title = "Product API"
app.summary = "Product REST API with FastAPI and Python"
app.description = "This is a demostration of API REST using Python"
app.version = "0.0.2"
app.contact = {
 "name": "Jorge I. Meza",
 "url": "https://co.linkedin.com/in/jimezam",
 "email": "jimezam@autonoma.edu.co",
}
#################################################
app.openapi_tags = [
 {
 "name": "web",
 "description": "Endpoints of example",
 },
 {
 "name": "products",
 "description": "Product handling endpoints",
 },
]
#################################################

app = FastAPI()


## Router's definition (endpoints sets)
app.include_router(router)
#################################################


