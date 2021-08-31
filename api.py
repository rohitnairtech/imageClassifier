
from fastapi import FastAPI, File, UploadFile

import psutil

app = FastAPI()


@app.get("/")
def read_root():
    return {"server_status": "Running"}

@app.get("/serverstatus")
def server_status():
    ram, cpu, available_ram = psutil.virtual_memory().percent, psutil.cpu_percent(), psutil.virtual_memory().available * 100 / psutil.virtual_memory().total
    return {"server_status": "Running", "ram" : ram, "cpu" : cpu, "avail_ram" : available_ram}


@app.post("/uploadimage/")
async def create_upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    return {"filename": file.filename}