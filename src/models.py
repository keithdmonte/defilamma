from sqlalchemy import Column, Integer, String, Boolean, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()


class Pool(Base):
    __tablename__ = "pools"

    id = Column(Integer, primary_key=True)
    pool_id = Column(String, unique=True, nullable=False)
    chain = Column(String)
    symbol = Column(String)
    project = Column(String)
    stablecoin = Column(Boolean)
    count = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)

    historical_data = relationship("PoolHistorical", back_populates="pool")


class PoolHistorical(Base):
    __tablename__ = "pools_historical"

    id = Column(Integer, primary_key=True)
    pool_id = Column(String, ForeignKey("pools.pool_id"))
    tvl = Column(Float)
    apy = Column(Float)
    timestamp = Column(DateTime)

    pool = relationship("Pool", back_populates="historical_data")
