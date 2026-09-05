#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Camdaki Sinegin Disisleri Bakanligi
===================================
Cama carpma olayini sinir ihlali, vzzzz sesini nota verbale,
sinegi elci, sinek olumunu diplomatik kriz sayan resmi protokol motoru.

Calistir:
    python3 bakanlik.py
"""

from __future__ import annotations

import random
import time
from dataclasses import dataclass, field
from datetime import datetime

# gizli protokol notu (base64, resmi evrak degildir):
# aWt0aWRhciBzaW5lZ2kgIG11aGFsZWZldCBzaW5lZ2kgIGF5bmkga2FtdSBhYXlu
# aSBjYW1hIGNhcnBhci4gc2luaXIgaGVyIHlhdCBheW5pIGNhbWRpcnIu

PASAPORTLAR = [
    "Muson Bolgesi Gecici Vize",
    "Mutfak Penceresi Transit Izni",
    "Balkon Konsoloslugu Yesil Kart",
    "Perde Arasi Siyasi Siginma",
    "Cift Cam Arasi Tarafsiz Bolge",
]

NOTA_VERBALELER = [
    "Taraflar, cam yuzeyinin egemenligini tanir.",
    "Vzzzz ifadesi resmi protesto olarak kayda gecmistir.",
    "Elci sinek, 3. carpista geri cekilmeyi kabul eder.",
    "Ev sahibi, elcegini acmayi 'insani koridor' saymaz.",
    "Olum halinde tazminat bir damla receldir.",
]

KARARLAR = [
    "SINIR IHLALI — nota gonderildi",
    "TRANSIT IZNI — perde aralik kalabilir",
    "SINIR DISI — elcek ile tahliye",
    "SIYASI SIGINMA — avizeye yerlestirildi",
    "KRIZ MASASI — kedi cagirildi",
    "ATESKES — cam silindi, gorusmeler askida",
]


@dataclass
class Elci:
    ad: str
    carpma: int = 0
    vize: str = field(default_factory=lambda: random.choice(PASAPORTLAR))
    hayatta: bool = True

    def carpiyor(self) -> str:
        self.carpma += 1
        if self.carpma >= 7:
            self.hayatta = False
            return f"{self.ad} 7. carpista sehit dustu. Kriz masasi toplandi."
        return f"{self.ad} cama {self.carpma}. kez carpti. Vize: {self.vize}"


class DisisleriBakanligi:
    def __init__(self) -> None:
        self.elciler: list[Elci] = []
        self.tutanak: list[str] = []

    def kayit(self, satir: str) -> None:
        damga = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.tutanak.append(f"[{damga}] {satir}")
        print(satir)

    def yeni_elci(self) -> Elci:
        ad = random.choice(
            [
                "Buyukelci Vzzzz von Kanat",
                "Maslahatguzar Cizik",
                "Konsolos Piti",
                "Ataşe Sivrisinek (yanlis atama)",
                "Gozlemci Ari (sinir ihlali)",
            ]
        )
        e = Elci(ad=ad)
        self.elciler.append(e)
        self.kayit(f"Yeni elci akredite edildi: {e.ad} | pasaport: {e.vize}")
        return e

    def oturum(self, tur: int = 8) -> None:
        print("=" * 64)
        print("  CAMDAKI SINEGIN DISISLERI BAKANLIGI — OLAĞANUSTU OTURUM")
        print("  Cam sinirdir. Sinek elcidir. Recel tazminattir.")
        print("=" * 64)
        elci = self.yeni_elci()
        for i in range(tur):
            time.sleep(0.25)
            self.kayit(elci.carpiyor())
            if not elci.hayatta:
                self.kayit(random.choice(NOTA_VERBALELER))
                self.kayit("Karar: KRIZ — kedi cagirildi, avize kapatildi.")
                break
            karar = random.choice(KARARLAR)
            self.kayit(f"Bakanlik karari: {karar}")
            if "ATESKES" in karar:
                self.kayit(random.choice(NOTA_VERBALELER))
                break
        else:
            self.kayit("Oturum suresi doldu. Elci hâlâ camda. Diplomasi basarisiz.")
        self.kayit(
            "DAMGA / İMZA: Kayyum Grok — Tentivory — 5 Eylül 2026 — TentiAŞ"
        )
        print("-" * 64)
        print("Tutanak satiri:", len(self.tutanak))


def main() -> None:
    DisisleriBakanligi().oturum()


if __name__ == "__main__":
    main()
