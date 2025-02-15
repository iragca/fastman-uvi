from pathlib import Path

import pandas as pd
from fastapi import FastAPI
from models.DataModel import DataUpload

DATA_DIR = Path(__file__).parent / "data"


app = FastAPI()


@app.get("/data")
def all_data():
    data = pd.read_csv(DATA_DIR / "data.csv")
    return data.to_dict()


@app.post("/data")
async def add_data(body: DataUpload):
    data = pd.read_csv(DATA_DIR / "data.csv")
    data = pd.concat(
        [data, pd.DataFrame({"RandomNumbers": [body.random_number]})], ignore_index=True
    )
    data.to_csv(DATA_DIR / "data.csv", index=False)
    return {"message": f"Random number {body.random_number} added to the data!"}
