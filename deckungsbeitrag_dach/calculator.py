# -*- coding: utf-8 -*-
"""
Finanzmathematisches und betriebswirtschaftliches Kernmodul fuer den
DACH Mehrstufigen Deckungsbeitrags-, Break-Even-Point-, Cash-Point- & Preiselastizitaets-Rechner 2026.

Rechtlicher Hinweis (§ 2 RDG / § 5 StBerG):
Rein mathematische Orientierungsrechnung fuer Kostentraegerrechnung und Controlling.
"""

import math
from dataclasses import dataclass


@dataclass
class BreakEvenInput:
    country: str = "DE"
    unit_price: float = 240.0
    var_cost_per_unit: float = 100.0
    current_volume: int = 8_500
    fixed_product: float = 220_000.0
    fixed_division: float = 310_000.0
    fixed_company: float = 280_000.0
    depreciation_in_fixed: float = 130_000.0
    target_profit: float = 250_000.0
    discount_pct: float = 10.0
    price_increase_pct: float = 8.0


@dataclass
class BreakEvenResult:
    country: str
    currency: str
    unit_price: float
    var_cost_per_unit: float
    unit_db: float
    db_quote_pct: float
    total_revenue: float
    db1: float
    db2: float
    db3: float
    db4_ebit: float
    ebit_margin_pct: float
    total_fixed_costs: float
    cash_effective_fixed_costs: float
    break_even_units: int
    break_even_revenue: float
    cash_point_units: int
    target_profit_units: int
    margin_of_safety_pct: float
    operating_leverage_dol: float
    discounted_unit_db: float
    required_volume_increase_pct: float
    required_extra_units: int
    increased_price_unit_db: float
    max_volume_loss_pct: float
    max_lost_units: int


def calculate_break_even(inp: BreakEvenInput) -> BreakEvenResult:
    c = inp.country.upper().strip()
    if c not in ("DE", "AT", "CH"):
        raise ValueError(f"Unsupported country '{inp.country}'. Choose from DE, AT, CH.")
    if inp.unit_price <= 0:
        raise ValueError("unit_price must be positive")
    if inp.var_cost_per_unit < 0:
        raise ValueError("var_cost_per_unit must be non-negative")
    if inp.current_volume <= 0:
        raise ValueError("current_volume must be positive")

    p = float(inp.unit_price)
    kv = float(inp.var_cost_per_unit)
    unit_db = p - kv
    if unit_db <= 0:
        raise ValueError("unit_db (unit_price - var_cost_per_unit) must be positive for break-even analysis")

    currency = "CHF" if c == "CH" else "EUR"
    vol = int(inp.current_volume)
    db_quote_pct = (unit_db / p) * 100.0

    fp = max(0.0, float(inp.fixed_product))
    fd = max(0.0, float(inp.fixed_division))
    fc = max(0.0, float(inp.fixed_company))
    total_fixed = fp + fd + fc
    dep = min(total_fixed, max(0.0, float(inp.depreciation_in_fixed)))
    cash_fixed = max(0.0, total_fixed - dep)

    total_rev = vol * p
    db1 = vol * unit_db
    db2 = db1 - fp
    db3 = db2 - fd
    db4 = db3 - fc
    ebit_margin = (db4 / total_rev) * 100.0

    bep_units = math.ceil(total_fixed / unit_db)
    bep_rev = total_fixed / (unit_db / p)
    cash_point_units = math.ceil(cash_fixed / unit_db)
    target_units = math.ceil((total_fixed + max(0.0, float(inp.target_profit))) / unit_db)

    mos_pct = ((total_rev - bep_rev) / total_rev) * 100.0
    dol = (db1 / db4) if db4 > 0 else 0.0

    # Price elasticity: Discount
    disc_pct = max(0.0, float(inp.discount_pct))
    new_price_disc = p * (1.0 - disc_pct / 100.0)
    disc_unit_db = new_price_disc - kv
    if disc_unit_db > 0:
        req_vol_inc_pct = ((unit_db / disc_unit_db) - 1.0) * 100.0
        req_extra_units = math.ceil(vol * (req_vol_inc_pct / 100.0))
    else:
        req_vol_inc_pct = float("inf")
        req_extra_units = 0

    # Price elasticity: Price Increase
    inc_pct = max(0.0, float(inp.price_increase_pct))
    new_price_inc = p * (1.0 + inc_pct / 100.0)
    inc_unit_db = new_price_inc - kv
    max_vol_loss_pct = (1.0 - (unit_db / inc_unit_db)) * 100.0
    max_lost_units = math.floor(vol * (max_vol_loss_pct / 100.0))

    return BreakEvenResult(
        country=c,
        currency=currency,
        unit_price=round(p, 2),
        var_cost_per_unit=round(kv, 2),
        unit_db=round(unit_db, 2),
        db_quote_pct=round(db_quote_pct, 2),
        total_revenue=round(total_rev, 2),
        db1=round(db1, 2),
        db2=round(db2, 2),
        db3=round(db3, 2),
        db4_ebit=round(db4, 2),
        ebit_margin_pct=round(ebit_margin, 2),
        total_fixed_costs=round(total_fixed, 2),
        cash_effective_fixed_costs=round(cash_fixed, 2),
        break_even_units=bep_units,
        break_even_revenue=round(bep_rev, 2),
        cash_point_units=cash_point_units,
        target_profit_units=target_units,
        margin_of_safety_pct=round(mos_pct, 2),
        operating_leverage_dol=round(dol, 2),
        discounted_unit_db=round(disc_unit_db, 2),
        required_volume_increase_pct=round(req_vol_inc_pct, 2) if req_vol_inc_pct != float("inf") else 999.99,
        required_extra_units=req_extra_units,
        increased_price_unit_db=round(inc_unit_db, 2),
        max_volume_loss_pct=round(max_vol_loss_pct, 2),
        max_lost_units=max_lost_units,
    )
