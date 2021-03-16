from fastapi import FastAPI, Query
from starlette.responses import JSONResponse
from fastapi.responses import HTMLResponse
import torch
import src
from src.models.pytorch import get_device
import pandas as pd

app = FastAPI()

models = torch.load('../models/pytorch_beer_best_model.pt')

@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <html>
        <head>
            <title>ADSI Project 2</title>
        </head>
        <body>
            <h1>Objective</h1><br>
            <p>OBJECTIVE: deploy a machine learning model into  Heroku webapp as a production environment that could predict the type of beer accurately based on inputs.</p>
            
            <h1>Endpoints</h1>
            <p>root = / <br>
            healthcheck = /health <br>
            prediction = /beer/type <br>
            architecture = /model/architecture</p>
            
            <h1>Expected Inputs</h1>
            <p>
            Brewery Name: String <br>
            Review Aroma: Float, from 0.0 to 5.0 <br>
            Review Appearance: Float, from 0.0 to 5.0 <br>
            Review Palate: Float, from 0.0 to 5.0 <br>
            Review Taste: Float, from 0.0 to 5.0 <br>
            </p>
            
            <h1>Link to Github Repo</h1>
            
        </body>
    </html>
    """


@app.get('/health', status_code=200)
async def healthcheck():
    return 'The Beer app is ready to run'

def format_features(Brewery_Name: str, Review_Aroma: float, Review_Appearance: float, Review_Palate: float, Review_Taste: float):
  return {
        'Brewery Name': [Brewery_Name],
        'Review Aroma': [Review_Aroma],
        'Review Appearance': [Review_Appearance],
        'Review Palate': [Review_Palate],
        'Review Taste': [Review_Taste]
    }

@app.get("/beer/type/")
def predict(Brewery_Name: str, Review_Aroma: float, Review_Appearance: float, Review_Palate: float, Review_Taste: float):
    features = format_features(Brewery_Name, Review_Aroma, Review_Appearance, Review_Palate, Review_Taste)
    obs = pd.DataFrame(features)
    pred = models.predict(obs)
    return JSONResponse(pred.tolist())


@app.get("/model/architecture/", response_class=HTMLResponse)
def arch():
    return """
        <html>
            <head>
                <title>Model Architecture</title>
            </head>
            <body>
                PytorchMultiClass( <br>
                (layer_1): Linear(in_features=8, out_features=32, bias=True) <br>
                (layer_out): Linear(in_features=32, out_features=104, bias=True) <br>
                (softmax): Softmax(dim=1)
                )
            </body>
        </html>
        """

