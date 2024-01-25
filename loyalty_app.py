from fastapi import FastAPI, File, UploadFile
import csv
from helpers import *

app = FastAPI()

data_path = 'data.csv'
loaded_data = None

@app.get("/loyalty")
async def predict(customerid: str):
    global loaded_data

    # Check if data is already loaded
    if not loaded_data:
        with open(data_path) as f: 
            loaded_data = list(csv.reader(f))

    for row in loaded_data:
        if row[0] == customerid:
            return {"category": row[1]}
    return {"category": "N/A"}

