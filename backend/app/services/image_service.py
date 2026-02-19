from openai import OpenAI
from app.core.config import settings
from app.core.database import db

client = OpenAI(api_key=settings.OPENAI_API_KEY)


async def scan_medicine(base64_data, media_type):

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:{media_type};base64,{base64_data}"
                            }
                        },
                        {"type": "text", "text": "Identify medication name only."}
                    ],
                }
            ],
        )

        detected_name = response.choices[0].message.content.strip().upper()

        db_match = await db.drugs.find_one({"name": detected_name})

        return {
            "detected": True,
            "drugName": detected_name,
            "confidence": 0.92,
            "description": "Detected via AI image scan",
            "warnings": "Check pharmacogenomic compatibility before use.",
            "matchesDatabase": True if db_match else False
        }

    except Exception as e:
        print("🔥 IMAGE AI ERROR:", e)
        return {
            "detected": False,
            "drugName": None,
            "confidence": 0.0,
            "description": "Image scan failed",
            "warnings": None,
            "matchesDatabase": False
        }
