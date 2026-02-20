# 🧬 PharmaGuard  
## AI-Powered Pharmacogenomic Clinical Decision Support System

PharmaGuard is an AI-powered pharmacogenomic platform that converts raw genomic VCF data into personalized drug risk predictions and clinically actionable recommendations aligned with CPIC guidelines.

---

## 🚨 Problem Statement

### Adverse Drug Reactions (ADRs)
- Cause **100,000+ deaths annually in the US**
- Major contributor to preventable hospitalizations
- Often linked to genetic variations in drug-metabolizing genes

### The Clinical Gap
- Every individual carries millions of genetic variants
- Variants in genes like **CYP2D6, CYP2C19, CYP2C9, SLCO1B1, TPMT, DPYD** significantly affect drug response
- Raw genomic VCF files are difficult for clinicians to interpret

### The Core Problem
A platform that converts:
> **Raw Genetic Data → Actionable Drug Safety & Dosing Recommendations**

---

## 💡 Our Solution – PharmaGuard

### What We Built
An AI-powered pharmacogenomic decision support system that transforms raw genetic data into actionable clinical insights.

### Core Capabilities
- Upload & parse authentic **VCF files (v4.2)**
- Detect pharmacogenomic variants across 6 key genes:
  - CYP2D6
  - CYP2C19
  - CYP2C9
  - SLCO1B1
  - TPMT
  - DPYD
- Analyze selected drugs for:
  - Safe
  - Adjust Dosage
  - Toxic
  - Ineffective
  - Unknown
- Generate AI-powered clinical explanations
- Book Lab technician at home 
- Family members support 

### Outcome
- Enables precision prescribing
- Converts genomic data into clear, evidence-based treatment guidance

---

## ⚙️ Tech Stack Used

### 🌐 Frontend
- React (Vite) – UI development
- Tailwind CSS – Responsive styling
- JavaScript (ES6+) – Client-side logic
- File Upload & FormData API – VCF handling

Frontend runs on:
http://localhost:5173



### 🧠 Backend
- FastAPI (Python) – REST API framework
- Uvicorn – ASGI server to run FastAPI
- Python-dotenv – Environment management
- MongoDB – NoSQL database
- cyvcf2 – High-performance VCF parsing

Backend runs on:

http://localhost:3000


### 🔑 APIs
- OpenAI API – LLM-powered clinical explanation generation

---

## 🔬 Feasibility

- Real VCF parsing & PGx variant detection (CYP2D6, CYP2C19, etc.)
- CPIC-based drug risk prediction (Safe / Adjust / Toxic / Ineffective)
- Uses standard VCF genomic format (v4.2)
- Improved phenotype accuracy & clinical validation approach
- Downloadable structured clinical report

---

## 🏆 USP (Unique Selling Proposition)

- Converts real genomic VCF data into personalized drug risk
- Family member genomic risk screening capability
- Integrated lab technician booking for genetic testing
- Complete precision medicine workflow in one platform
- Extendable support for additional drugs

---

## 🔐 Security & Validation

- Backend file size validation (≤ 5MB)
- File type validation (`.vcf` only)
- Environment-based API key storage
- CORS middleware protection
- Input schema validation
- No permanent storage of raw genomic data (configurable)

---

## ⚠️ Disclaimer

PharmaGuard is a clinical decision-support prototype and is not a substitute for professional medical judgment. Clinical deployment requires regulatory approval and validation.

---

## 👨‍💻 Developed As

An academic pharmacogenomics AI project demonstrating real-world precision medicine workflow integration using modern full-stack architecture.
