import asyncio
import json
import os
from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "drug_seed.json")


async def seed():
    client = AsyncIOMotorClient(settings.MONGO_URI)
    db = client[settings.DATABASE_NAME]

    with open(DATA_PATH, "r") as file:
        drugs = json.load(file)

    await db.drugs.delete_many({})
    result = await db.drugs.insert_many(drugs)

    print(f"✅ Inserted {len(result.inserted_ids)} drugs successfully.")

    client.close()


if __name__ == "__main__":
    asyncio.run(seed())