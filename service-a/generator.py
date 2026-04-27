import pandas as pd
from faker import Faker
import random

fake = Faker()

def generate_csv(file_path="./data/students.csv", num_records=100):
    data = []

    for i in range(num_records):
        email = fake.email() if random.random() > 0.5 else "invalid_email"

        record = {
            "name": fake.name(),
            "email": email,
            "age": random.choice([random.randint(18, 25), None]),
            "cgpa": round(random.uniform(0.0, 10.0), 2) if random.random() > 0.1 else None,
            "rollNumber": f"CS{random.randint(1000000, 9999999)}"
        }

        data.append(record)

    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)
    print(f"CSV generated at {file_path}")