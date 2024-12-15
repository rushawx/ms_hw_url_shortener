import datetime
from typing import List

from pydantic import BaseModel


class UrlFullRequest(BaseModel):
    url: str


class UrlFullResponse(BaseModel):
    url: str


class UrlShortResponse(BaseModel):
    url: str


class UrlResponse(BaseModel):
    id: int
    short_url: str
    full_url: str
    created_at: datetime.datetime

    class Config:
        from_attributes = True
