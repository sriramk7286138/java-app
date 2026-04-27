import pandas as pd
import requests
import os
import time
from datetime import datetime

from validator import is_valid_record 

service_b = "http://java-backend:8081/api/students"
dir = "/app/data"
valid_file= "/app/data/validated_students.csv"
logs = "/app/data/processing.log"

BATCH_SIZE = 20


def log_stats(file_name, total, valid):
    with open(logs, "a") as log:
        log.write(
            f"{datetime.now()} | File: {file_name} | Total: {total} | Valid: {valid}\n"
        )


def append_valid_data(df):
    if not os.path.exists(valid_file):
        df.to_csv(valid_file, index=False)
    else:
        df.to_csv(valid_file, mode='a', header=False, index=False)


def process_file(file_path):
    try:
        df = pd.read_csv(file_path)
        total_records = len(df)
        valid = df[df.apply(lambda row: is_valid_record(row.to_dict()), axis=1)]
        valid_records_total = len(valid)
        if valid_records_total > 0:
            append_valid_data(valid)
            valid_records = valid.to_dict(orient="records")
            for i in range(0, len(valid_records), BATCH_SIZE):
                batch = valid_records[i:i + BATCH_SIZE]
                try:
                    requests.post(service_b, json=batch, timeout=5)
                except Exception as e:
                    print("Error sending batch:", e)
        log_stats(os.path.basename(file_path), total_records, valid_records_total)
        print(f"Processed {file_path}: {valid_records_total}/{total_records} valid")

    except Exception as e:
        print(f"Error processing file {file_path}:", e)


def watch_directory():
    os.makedirs(dir, exist_ok=True)
    while True:
        files = os.listdir(dir)
        for file in files:
            if file.endswith(".csv") and not file.startswith("validated_students"):
                file_path = os.path.join(dir, file)
                process_file(file_path)
                os.remove(file_path)
        time.sleep(5)