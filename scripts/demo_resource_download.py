"""Run the recording fixture on localhost without loading AI or audio services."""

import sys
from pathlib import Path

import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "src"))

from open_llm_vtuber.resource_download import create_resource_router  # noqa: E402

app = FastAPI(title="Learning resources demonstration")
app.include_router(create_resource_router(str(REPO_ROOT / "demo_resources/public")))


@app.get("/", response_class=HTMLResponse)
async def index() -> str:
    """Offer the public course guide for the recording."""
    return """<!doctype html><title>Learning resources</title>
    <main style="font:20px system-ui;max-width:720px;margin:80px auto">
    <h1>Learning resources</h1><p>Negotiation basics</p>
    <a href="/resources/download?filename=course-guide.txt">Open course guide</a>
    <p style="font-size:14px;color:#666">Demonstration. All records are fictional.</p>
    </main>"""


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8766)
