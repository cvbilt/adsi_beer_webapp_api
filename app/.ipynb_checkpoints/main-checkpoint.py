from fastapi import FastAPI, Query
from typing import List
from starlette.responses import JSONResponse
from joblib import load
import pandas as pd

app = FastAPI()

models = load('../models/pytorch_beer_best_model.pt')

@app.get("/")
def read_root():
    return 'Displaying a brief description of the project objectives, list of endpoints, expected input parameters and output format of the model, link to the Github repo related to this project'


@app.get('/health', status_code=200)
def healthcheck():
    return 'The Beer app is ready to run'

def format_features(Brewery_Name: str, Review_Aroma: int, Review_Appearance: int, Review_Palate: int, Review_Taste: int):
  return {
        'Brewery Name': [Brewery_Name],
        'Review Aroma': [Review_Aroma],
        'Review Appearance': [Review_Appearance],
        'Review Palate': [Review_Palate],
        'Review Taste': [Review_Taste]
    }

@app.post("/beer/type/")
def predict(Brewery_Name: str, Review_Aroma: int, Review_Appearance: int, Review_Palate: int, Review_Taste: int):
    features = format_features(Brewery_Name, Review_Aroma, Review_Appearance, Review_Palate, Review_Taste)
    obs = pd.DataFrame(features)
    pred = models.predict(obs)
    return JSONResponse(pred.tolist())


@app.get("/model/architecture/")
def arch():
    return 'Displaying the architecture of your Neural Networks (listing of all layers with their types)'


