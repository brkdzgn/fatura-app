from sqlalchemy import Column, Integer, String, Float, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Sayac(Base):
    __tablename__ = "sayaclar"

    id = Column(Integer, primary_key=True)
    sayac_id = Column(String, unique=True, index=True)
    dagitim_bolgesi = Column(String)
    lokasyon = Column(String)
    sayac_turu = Column(String)
    belediye = Column(String)
    tarife = Column(String)
    sozlesme_tarihi = Column(String)
    kbk_orani = Column(Float, nullable=True)

    faturalar = relationship("Fatura", back_populates="sayac")


class Fatura(Base):
    __tablename__ = "faturalar"

    id = Column(Integer, primary_key=True)
    sayac_id = Column(String, ForeignKey("sayaclar.sayac_id"))
    sayac_adi = Column(String)
    ft_tarih = Column(String)
    vade_tarih = Column(String)
    seri = Column(String)
    no = Column(Integer)
    ao_ptf = Column(Float)
    yekdem = Column(Float)
    aktif_bf = Column(Float)
    aktif_tuketim = Column(Float)
    aktif_tutar = Column(Float)
    mahsup_tutar = Column(Float)
    mahsuplu_dagitim_bedeli = Column(Float)
    btv = Column(Float)
    ek_kalem_tutar = Column(Float)
    tutar_kdv_haric = Column(Float)
    kdv = Column(Float)
    genel_toplam = Column(Float)

    odendi = Column(Boolean, default=False)
    odeme_tarihi = Column(String, nullable=True)
    odeme_tutari = Column(Float, nullable=True)

    sayac = relationship("Sayac", back_populates="faturalar")


class Odeme(Base):
    __tablename__ = "odemeler"

    id = Column(Integer, primary_key=True)
    tarih = Column(String)
    tutar = Column(Float)
    aciklama = Column(String)
    fatura_id = Column(Integer, ForeignKey("faturalar.id"), nullable=True)
    eslestirildi = Column(Boolean, default=False)