from sqlalchemy import Column, ARRAY, Integer, String, DateTime, Text, Float, Boolean, ForeignKey, inspect, func
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Client(Base):
    __tablename__ = 'clients'

    name = Column(String(100), primary_key=True)
    specs = relationship('Spec', back_populates='client')

class Spec(Base):
    __tablename__ = 'specs'
    
    name = Column(String, primary_key=True)
    description: str | None = Column(Text) #type:ignore

    created = Column(DateTime(timezone=True), server_default=func.now())
    updated = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    tags: list[str] | None = Column(ARRAY(Text)) #type:ignore

    dropframe: bool = Column(Boolean, default=False) #type:ignore
    lkfs: bool = Column(Boolean, default=False) #type:ignore
    vchip: bool = Column(Boolean, default=False) #type:ignore
    afd: bool = Column(Boolean, default=False) #type:ignore

    audio_flags: bool = Column(Boolean, default=True) #type:ignore
    audio_config: list[list[str]] | None = Column(ARRAY(Text)) #type:ignore
    audio_description: str | None = Column(Text) #type:ignore
    hdr_metadata_required: bool = Column(Boolean, default=False) #type:ignore
    hdr_metadata_description: str | None = Column(Text) #type:ignore
    streaming_flags_required: bool = Column(Boolean, default=False) #type:ignore
    streaming_flags_description: str | None = Column(Text) #type:ignore
    subcap_required: bool = Column(Boolean, default=False) #type:ignore
    subcap_format: list[str] | None = Column(ARRAY(Text)) #type:ignore
    act_breaks_required: bool = Column(Boolean, default=False) #type:ignore
    act_breaks_description: str | None = Column(Text) #type:ignore
    reports_required: bool = Column(Boolean, default=False) #type:ignore
    reports_description: str | None = Column(Text) #type:ignore
    artwork_required: bool = Column(Boolean, default=False) #type:ignore
    artwork_description: str | None = Column(Text) #type:ignore

    headbuild: str | None = Column(Text) #type:ignore
    colorspace: str | None = Column(Text) #type:ignore
    bitrate: int | None = Column(Integer) #type:ignore
    bitdepth: int | None = Column(Integer) #type:ignore
    burnins: str | None = Column(Text) #type:ignore
    resolution: list[int] | None = Column(ARRAY(Integer)) #type:ignore
    aspect_ratio: list[float] | None = Column(ARRAY(Float)) #type:ignore
    framerate: list[float] | None = Column(ARRAY(Float)) #type:ignore
    video_codec: str | None = Column(Text) #type:ignore
    audio_codec: str | None = Column(Text) #type:ignore
    audo_codec_profile: str | None = Column(Text) #type:ignore
    video_codec_profile: str | None = Column(Text) #type:ignore
    start_timecode: str | None = Column(String(11)) #type:ignore
    naming_convention: str | None = Column(Text) #type:ignore

    client_name = Column(String, ForeignKey('clients.name'))
    client = relationship('Client', back_populates='specs')

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.update_requirements()

    def update_requirements(self) -> None:
        if self.subcap_format:
            self.subcap_required = True
        if self.streaming_flags_description:
            self.streaming_flags_required = True
        if self.hdr_metadata_description:
            self.hdr_metadata_required = True
        if self.act_breaks_description:
            self.act_breaks_required = True
        if self.reports_description:
            self.reports_required = True
        if self.artwork_description:
            self.artwork_required = True