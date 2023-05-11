import base64

from sqlalchemy import Column, ARRAY, Integer, String, DateTime, Text, Float, Boolean, ForeignKey, LargeBinary, func
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Client(Base):
    __tablename__ = 'clients'

    name = Column(String(100), primary_key=True)
    specs = relationship('Spec', back_populates='client')

class Spec(Base):
    __tablename__ = 'specs'
    
    name = Column(String, primary_key=True) #type:ignore
    description: str | None = Column(Text) #type:ignore

    created = Column(DateTime(timezone=True), server_default=func.now())
    updated = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    source: bytes | None = Column(LargeBinary) #type:ignore

    dropframe: bool = Column(Boolean, default=False) #type:ignore
    lkfs: bool = Column(Boolean, default=False) #type:ignore
    vchip: bool = Column(Boolean, default=False) #type:ignore
    afd: bool = Column(Boolean, default=False) #type:ignore
    audio_flags: bool = Column(Boolean, default=True) #type:ignore

    audio_description_required: bool = Column(Boolean, default=False) #type:ignore
    audio_description_details: str | None = Column(Text) #type:ignore
    hdr_metadata_required: bool = Column(Boolean, default=False) #type:ignore
    hdr_metadata_details: str | None = Column(Text) #type:ignore
    streaming_flags_required: bool = Column(Boolean, default=False) #type:ignore
    streaming_flags_details: str | None = Column(Text) #type:ignore
    subcap_required: bool = Column(Boolean, default=False) #type:ignore
    subcap_details: bool = Column(Text) #type:ignore
    act_breaks_required: bool = Column(Boolean, default=False) #type:ignore
    act_breaks_details: str | None = Column(Text) #type:ignore
    reports_required: bool = Column(Boolean, default=False) #type:ignore
    reports_details: str | None = Column(Text) #type:ignore
    artwork_required: bool = Column(Boolean, default=False) #type:ignore
    artwork_details: str | None = Column(Text) #type:ignore
    watermark_required: bool = Column(Boolean, default=False) #type:ignore
    watermark_details: str | None = Column(Text) #type:ignore
    burnins_required: bool = Column(Boolean, default=False) #type:ignore
    burnins_details: str | None = Column(Text) #type:ignore
    slate_required: bool = Column(Boolean, default=False) #type:ignore
    slate_details: str | None = Column(Text) #type:ignore

    start_timecode: str | None = Column(String(11)) #type:ignore
    naming_convention: str | None = Column(Text) #type:ignore
    headtailbuild: str | None = Column(Text) #type:ignore
    audio_config: list[list[str]] | None = Column(ARRAY(Text)) #type:ignore
    audio_details: str | None = Column(Text) #type:ignore

    colorspace: str | None = Column(Text) #type:ignore
    resolution: str | None = Column(Text) #type:ignore
    aspect_ratio: str | None = Column(Text) #type:ignore
    framerate: str | None = Column(Text) #type:ignore
    video_codec: str | None = Column(Text) #type:ignore
    video_codec_profile: str | None = Column(Text) #type:ignore
    video_bitrate: str | None = Column(Text) #type:ignore
    video_bitdepth: str | None = Column(Text) #type:ignore
    audio_codec: str | None = Column(Text) #type:ignore
    audio_codec_profile: str | None = Column(Text) #type:ignore
    audio_bitrate: str | None = Column(Text) #type:ignore
    audio_bitdepth: str | None = Column(Text) #type:ignore

    notes: str | None = Column(Text) #type:ignore

    client_name = Column(String, ForeignKey('clients.name'))
    client = relationship('Client', back_populates='specs')

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def as_dict(self):
        result = {}
        for c in self.__table__.columns:
            value = getattr(self, c.name)
            if isinstance(value, bytes):
                value = base64.b64encode(value).decode('utf-8')
            result[c.name] = value
        return result