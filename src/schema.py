from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class PoolBase(BaseModel):
    pool_id: str
    chain: str
    symbol: str
    project: str
    stablecoin: bool
    count: int


class PoolCreate(PoolBase):
    pass


class Pool(PoolBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class PoolHistoricalBase(BaseModel):
    pool_id: str
    tvl: float
    apy: float
    timestamp: datetime


class PoolHistoricalCreate(PoolHistoricalBase):
    pass


class PoolHistorical(PoolHistoricalBase):
    id: int

    class Config:
        from_attributes = True
