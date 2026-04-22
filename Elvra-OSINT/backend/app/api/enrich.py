from fastapi import APIRouter
import asyncio

from app.modules.email_tool import analyze_email
from app.modules.phone_tool import analyze_phone
from app.modules.global_score import compute_global_score
from app.modules.radar import build_radar
from app.modules.ai_analyst import explain
from app.modules.ai_profile import build_profile
from app.modules.multi_search import multi_search
from app.modules.ai_psycho import psycho_profile
from app.modules.graph import build_graph
from app.modules.osint_scraper import scrape_osint
from app.modules.fake_identity import detect_fake_identity

from app.modules.username_search import search_username
from app.modules.email_search import analyze_email_identity
from app.modules.identity_fusion import build_identity_fusion
from app.modules.username_matcher import find_similar

router = APIRouter()

CACHE = {}

def make_key(email, phone, username):
    return f"{email}|{phone}|{username}"


@router.get("/enrich")
async def enrich(email: str = None, phone: str = None, username: str = None):

    email = email or None
    phone = phone or None
    username = username or None

    if not (email or phone or username):
        return {
            "error": "No input provided",
            "osint_score": 0,
            "radar": {"labels": [], "values": []},
            "profile": {},
            "identity_fusion": {"identity": {"confidence": 0}}
        }

    key = make_key(email, phone, username)

    if key in CACHE:
        return CACHE[key]

    email_task = asyncio.create_task(analyze_email(email)) if email else None
    phone_task = asyncio.create_task(analyze_phone(phone)) if phone else None
    email_osint_task = asyncio.create_task(analyze_email_identity(email)) if email else None

    email_data = await email_task if email_task else None
    phone_data = await phone_task if phone_task else None
    email_osint = await email_osint_task if email_osint_task else None

    username_results = search_username(username) if username else []

    similar_accounts = find_similar(username, username_results) if username else []

    ip = {"active": bool(email or phone or username)}
    risk = {"risk_score": 70}
    socials = []

    osint_score = compute_global_score(ip, risk, socials)
    radar = build_radar(osint_score, risk, socials, ip)
    ai = explain(osint_score, risk)

    profile = build_profile(
        username=username,
        email=email,
        phone=phone,
        osint_score=osint_score,
        radar=radar,
        ai=ai
    )

    multi = multi_search(email=email, phone=phone, username=username)
    psycho = psycho_profile(osint_score, multi)

    graph = build_graph({
        "target": "user",
        "email": email,
        "phone": phone,
        "username": username
    })

    scraper = scrape_osint(username)
    fake = detect_fake_identity(multi, osint_score)

    fusion = build_identity_fusion(
        username=username,
        email=email,
        phone=phone,
        osint_results=username_results
    )

    result = {
        "email": email_data,
        "phone": phone_data,
        "email_osint": email_osint,
        "username_results": username_results,
        "similar_accounts": similar_accounts,
        "osint_score": osint_score,
        "radar": radar,
        "ai": ai,
        "profile": profile,
        "multi_search": multi,
        "psycho_profile": psycho,
        "graph": graph,
        "scraper": scraper,
        "fake_identity": fake,
        "identity_fusion": fusion
    }

    CACHE[key] = result

    return result