from openai import OpenAI
import json
from app.core.config import settings
from openai import AsyncOpenAI

client = OpenAI(api_key=settings.OPENAI_API_KEY)


def fallback_response(drug_data):
    return {
        "biological_mechanism": drug_data.get("mechanism"),
        "clinical_risk_summary": drug_data.get("whyRisk"),
        "dosing_guideline": drug_data.get("dosage"),
        "evidence_level": drug_data.get("cpic")
    }


def generate_clinical_explanation(drug_data, matched_variants):

    if not settings.OPENAI_API_KEY:
        return fallback_response(drug_data)

    prompt = f"""
Generate STRICT JSON.

Fields:
- biological_mechanism
- clinical_risk_summary
- dosing_guideline
- evidence_level

Drug: {drug_data.get("name")}
Gene: {drug_data.get("gene")}
Diplotype: {drug_data.get("diplotype")}
Phenotype: {drug_data.get("phenotype")}
CPIC Level: {drug_data.get("cpic")}
Detected Variants: {matched_variants}

Return JSON only.
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a pharmacogenomics clinical expert."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )

        raw_text = response.choices[0].message.content.strip()
        return json.loads(raw_text)

    except Exception as e:
        print("🔥 OPENAI ERROR:", e)
        return fallback_response(drug_data)