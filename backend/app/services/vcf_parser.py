from typing import List


async def parse_vcf(file_bytes: bytes, filename: str):

    text = file_bytes.decode("utf-8", errors="ignore")

    rsids: List[str] = []
    sample_id = filename.replace(".vcf", "")

    for line in text.splitlines():

        # Capture sample ID from header
        if line.startswith("#CHROM"):
            parts = line.strip().split("\t")
            if len(parts) > 9:
                sample_id = parts[9]
            continue

        if line.startswith("#"):
            continue

        columns = line.strip().split("\t")
        if len(columns) < 10:
            continue

        rsid = columns[2]
        genotype_field = columns[9].split(":")[0]  # GT field

        # Only include variants that are NOT 0/0
        if rsid.startswith("rs") and genotype_field != "0/0":
            rsids.append(rsid)

    return {
        "sampleId": sample_id,
        "variants": rsids,           # 🔥 LIST (not number)
        "variantCount": len(rsids)
    }
