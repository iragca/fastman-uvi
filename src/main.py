from pathlib import Path

import pandas as pd
from fastapi import FastAPI
from DataModel import DataUpload

DATA_DIR = Path(__file__).parent / "data"


app = FastAPI()


@app.get("/data")
def all_data():
    """Fetch all data from the CSV file.

    Returns:
        dict: A dictionary representation of the CSV data.
    """
    # Load the data
    data = pd.read_csv(DATA_DIR / "data.csv")
    return data.to_dict()


@app.post("/data")
async def add_data(body: DataUpload):
    """Add a random number to the CSV file.

    Args:
        body (DataUpload): The data model containing the random number.

    Returns:
        dict: A message indicating the random number was added.
    """
    # Load the data
    data = pd.read_csv(DATA_DIR / "data.csv")

    # Add the new random number
    data = pd.concat(
        [data, pd.DataFrame({"RandomNumbers": [body.random_number]})], ignore_index=True
    )

    # Save the data
    data.to_csv(DATA_DIR / "data.csv", index=False)

    return {"message": f"Random number {body.random_number} added to the data!"}
