# 📈 DACH Mehrstufiger Deckungsbeitrags-, Break-Even-Point-, Cash-Point- & Preiselastizitäts-Rechner 2026 (`deckungsbeitrag_dach`)

[![CI & Pytest](https://github.com/DACHDigitalwerk/deckungsbeitrag-break-even-preiselastizitaet-rechner-dach/actions/workflows/ci.yml/badge.svg)](https://github.com/DACHDigitalwerk/deckungsbeitrag-break-even-preiselastizitaet-rechner-dach/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-emerald.svg)](LICENSE)
[![Live Web-App](https://img.shields.io/badge/Live_Web_App-100%25_Client_Side-10b981)](https://dachdigitalwerk.github.io/deckungsbeitrag-break-even-rechner/)

Finanzmathematische Python-Bibliothek und CLI (`dach-breakeven`) zur Berechnung von **Stückdeckungsbeitrag ($db$), Deckungsbeitragsquote, mehrstufiger Fixkostendeckungsrechnung (DB I bis DB IV / EBIT), Break-Even-Point (Gewinnschwelle), Cash-Point (Liquiditätsschwelle ohne AfA), Sicherheitskoeffizient (Margin of Safety), Operating Leverage (DOL)** sowie **Preiselastizität (Rabatt-Mehrabsatz vs. Preiserhöhungs-Hebel)** für KMU in **Deutschland, Österreich und der Schweiz**.

---

## 🌐 Interaktive Web-Applikation & Controlling-Fachratgeber (100 % Client-Side)

Nutzen Sie den kostenlosen Online-Rechner mit **druckfertigem DIN-A4 Deckungsbeitrags-, Break-Even- & Preiselastizitäts-Dossier** direkt im Browser:

- 🚀 **[DACH Mehrstufiger Deckungsbeitrags-, Break-Even-Point-, Cash-Point- & Preiselastizitäts-Rechner 2026](https://dachdigitalwerk.github.io/deckungsbeitrag-break-even-rechner/)**
- 📘 **[Deckungsbeitrag berechnen 2026: Formel für Stückdeckungsbeitrag, DB I–IV & DB-Quote](https://dachdigitalwerk.github.io/deckungsbeitrag-berechnen-formel-db1-db2-stueckdeckungsbeitrag-2026.html)**
- 🎯 **[Break-Even-Point (Gewinnschwelle) & Cash-Point berechnen: Formel, Beispiel & Margin of Safety](https://dachdigitalwerk.github.io/break-even-point-gewinnschwelle-berechnen-formel-cash-point-beispiel.html)**
- 📊 **[Rabatt-Mehrabsatz-Rechner & Preiserhöhungs-Tabelle 2026 (B2B Pricing)](https://dachdigitalwerk.github.io/rabatt-mehrabsatz-rechner-preiserhoehung-deckungsbeitrag-tabelle-b2b.html)**
- 🏠 **[DACH Digitalwerk – Alle 37 Self-Serve Web-Tools im Überblick](https://dachdigitalwerk.github.io/)**

---

## ✨ Kernfunktionen

1. **Stück- & Mehrstufige Perioden-Deckungsbeitragsrechnung (DB I bis DB IV):**
   - `db = p - kv`, `DB I = x * db`, `DB II = DB I - Produktfixkosten`, `DB III = DB II - Bereichsfixkosten`, `DB IV (EBIT) = DB III - Unternehmensfixkosten`.
2. **Break-Even-Point, Cash-Point & Zielgewinn-Menge:**
   - Aufgerundete Mindeststückzahl für Gewinnschwelle (`EBIT = 0`), Liquiditätsschwelle (`EBITDA = 0`, ohne zahlungsunwirksame AfA) und Ziel-EBIT.
3. **Rabatt-Falle vs. Preiserhöhungs-Hebel:**
   - Berechnet exakt den notwendigen Mehrabsatz bei Preisnachlass bzw. den maximal verkraftbaren Mengenrückgang bei Preiserhöhung.

---

## 📦 Installation & CLI-Nutzung

```bash
pip install -e .
dach-breakeven --country DE --price 240 --var-cost 100 --volume 8500 --discount 10 --price-increase 8
```

---

## ⚠️ Rechtlicher Hinweis (§ 2 RDG / § 5 StBerG)

Dieses Paket dient ausschließlich der unverbindlichen betriebswirtschaftlichen Kalkulation und Controlling-Simulation. Es stellt keine Steuer-, Rechts- oder Unternehmensberatung dar.
