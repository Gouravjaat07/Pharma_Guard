from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.core.database import client
from app.core.config import settings

from app.routes import analysis_routes, vcf_routes, image_routes, history_routes


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        await client.admin.command("ping")
        print("✅ MongoDB Connected")
    except Exception as e:
        print("❌ MongoDB Error:", e)

    yield
    print("🛑 Server Shutdown")


app = FastAPI(title="PharmaGuard API", version="1.0.0", lifespan=lifespan)


# Proper CORS (Local + Production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def health():
    return {"status": "Backend Running 🚀"}


app.include_router(vcf_routes.router, prefix="/api/vcf", tags=["VCF"])
app.include_router(analysis_routes.router, prefix="/api/analysis", tags=["Analysis"])
app.include_router(image_routes.router, prefix="/api/image", tags=["Image"])
app.include_router(history_routes.router, prefix="/api/history", tags=["History"])