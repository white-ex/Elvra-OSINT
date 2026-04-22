from fastapi import FastAPI

from app.api import domain, social, enrich
from app.web import router as web_router

app = FastAPI(
    title="Elvra OSINT",
    version="0.1.0",
    description="Identity Intelligence Platform"
)

app.include_router(domain.router)
app.include_router(social.router)
app.include_router(enrich.router)
app.include_router(web_router)


@app.get("/")
def home():
    return {"status": "TraceScope X running"}