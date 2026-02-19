import asyncio
import json
import os
from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "drug_seed.json")


async def seed():
    print("🔄 Connecting to MongoDB Atlas...")

    client = AsyncIOMotorClient(settings.MONGO_URI)
    db = client[settings.DATABASE_NAME]

    with open(DATA_PATH, "r", encoding="utf-8") as file:
        drugs = json.load(file)

    print(f"📦 Loaded {len(drugs)} drugs from JSON")

    # Clear existing drugs (optional but recommended)
    await db.drugs.delete_many({})
    print("🗑 Old drug records cleared")

    result = await db.drugs.insert_many(drugs)

    print(f"✅ Successfully inserted {len(result.inserted_ids)} drugs")

    client.close()
    print("🎉 Database seeding completed!")


if __name__ == "__main__":
    asyncio.run(seed())