from sqlalchemy import Column, ARRAY, Integer, String, DateTime, Text, Float, Boolean, ForeignKey, inspect, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Spec(Base):
    __tablename__ = 'specs'
    name = Column(String, primary_key=True)

    created = Column(DateTime(timezone=True), server_default=func.now())
    updated = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())
    headbuild = Column(Text) #type:ignore
    audio_config: str = Column(Text) #type:ignore
    colorspace: str = Column(String(50)) #type:ignore
    bitrate: int = Column(Integer) #type:ignore
    bitdepth: int = Column(Integer) #type:ignore

    def __init__(self, headbuild: str, **kwargs):
        self.headbuild = headbuild
        super().__init__(**kwargs)

