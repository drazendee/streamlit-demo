from fastapi import FastAPI, File, UploadFile
import csv

app = FastAPI()

@app.middleware("http")
async def process_valohai_prefix(request: Request, call_next):
    path = request.scope["path"]
    for prefix in (
        request.headers.get("X-VH-Prefix"),
        os.environ.get("VH_DEFAULT_PREFIX"),
    ):
        if not prefix:  # Could have no header or no envvar, so skip
            continue
        if path.startswith(prefix):  # If the path starts with this prefix,
            # ... tell FastAPI (0.56.0+) that that is the prefix we're mounted under...
            request.scope["root_path"] = prefix
            # ... then strip the prefix out as far as FastAPI is concerned.
            request.scope["path"] = "/" + path[len(prefix) :].lstrip("/")
            break
    return await call_next(request)

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

