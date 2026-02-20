import os
import json
from openai import AsyncOpenAI

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def generate_clinical_explanation(drug_data, matched_variants):

    prompt = f"""
You are a pharmacogenomics clinical decision support system.

Return ONLY valid JSON.
Do not add text outside JSON.

Format:
{{
  "summary": "...",
  "why_this_risk": "...",
  "clinical_recommendation": "...",
  "references": ["CPIC", "FDA"]
}}

Drug: {drug_data['name']}
Gene: {drug_data.get('gene')}
Phenotype: {drug_data.get('phenotype')}
Risk Level: {drug_data.get('risk')}
Matched Variants: {matched_variants}
"""

    try:
        response = await client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2
        )

        content = response.choices[0].message.content.strip()

        # Force clean JSON extraction
        if content.startswith("```"):
            content = content.split("```")[1]

        parsed = json.loads(content)

        return {
            "summary": parsed.get("summary", ""),
            "why_this_risk": parsed.get("why_this_risk", ""),
            "clinical_recommendation": parsed.get("clinical_recommendation", ""),
            "references": parsed.get("references", [])
        }

    except Exception as e:
        print("LLM ERROR:", e)

        return {
            "summary": f"{drug_data['name']} pharmacogenomic interpretation based on {drug_data.get('gene')} profile.",
            "why_this_risk": "No additional AI explanation available.",
            "clinical_recommendation": drug_data.get("dosage", ""),
            "references": []
        }