import os
from fastapi import FastAPI, Query
from generator import generate_csv
import threading
from watcher import watch_directory
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


dir="/app/data"

@app.on_event("startup")
def startup_event():
    os.makedirs(dir, exist_ok=True)
    thread = threading.Thread(target=watch_directory, daemon=True)
    thread.start()

@app.post("/generate")
def generate_data(records: int = Query(100, ge=1, le=100000)):
    file_path = f"{dir}/students_{records}.csv"
    generate_csv(file_path=file_path, num_records=records)
    return {
        "message": f"{records} records generated successfully",
        "file": file_path
    }


@app.get("/")
def read_root():
    return {"message": "Service A running"}

#app.mount("/static", StaticFiles(directory="build/static"), name="static")

#@app.get("/{full_path:path}")
#async def serve_react(full_path: str):
   # return FileResponse("build/index.html")