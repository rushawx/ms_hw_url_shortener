from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from app.db.engine import Url
from app.models.urls import UrlFullRequest, UrlResponse, UrlShortResponse
from app.utils.utils import get_db, shorten

router = APIRouter(prefix="/urls", tags=["urls"])


@router.post("/shorten")
async def shorten_url(
    request: Request, url: UrlFullRequest, db: Session = Depends(get_db)
) -> UrlShortResponse:
    full_url = url.url.split("://")[1]
    shortened_url = await shorten(full_url)
    item = Url(short_url=shortened_url, full_url=full_url)
    db.add(item)
    db.commit()
    db.refresh(item)
    return UrlShortResponse(url=shortened_url)


@router.get("/{short_id}")
async def redirect_by_url(
    request: Request, short_id: str, db: Session = Depends(get_db)
) -> RedirectResponse:
    db_url = db.query(Url).filter(Url.short_url == short_id).first()
    if not db_url:
        raise HTTPException(status_code=404, detail="Url not found")
    return RedirectResponse(url="https://" + db_url.full_url)


@router.get("/stats/{short_id}")
async def stats_by_url(
    request: Request, short_id: str, db: Session = Depends(get_db)
) -> UrlResponse:
    db_url = db.query(Url).filter(Url.short_url == short_id).first()
    if not db_url:
        raise HTTPException(status_code=404, detail="Url not found")
    response = UrlResponse(
        id=db_url.id,
        short_url=db_url.short_url,
        full_url=db_url.full_url,
        created_at=db_url.created_at,
    )
    return response
