# -*- coding: utf-8 -*-
"""
CLI fuer den DACH Mehrstufigen Deckungsbeitrags-, Break-Even- & Preiselastizitaets-Rechner 2026
"""

import argparse
import json
from .calculator import BreakEvenInput, calculate_break_even


def main():
    parser = argparse.ArgumentParser(
        description="DACH Mehrstufiger Deckungsbeitrags-, Break-Even-Point-, Cash-Point- & Preiselastizitaets-Rechner 2026"
    )
    parser.add_argument("--country", default="DE", choices=["DE", "AT", "CH"], help="Land (DE, AT, CH)")
    parser.add_argument("--price", type=float, default=240.0, help="Netto-Verkaufspreis pro Einheit")
    parser.add_argument("--var-cost", type=float, default=100.0, help="Variable Stueckkosten")
    parser.add_argument("--volume", type=int, default=8_500, help="Geplante / Ist-Absatzmenge (Stueck)")
    parser.add_argument("--discount", type=float, default=10.0, help="Geplanter Rabatt in Prozent (%%)")
    parser.add_argument("--price-increase", type=float, default=8.0, help="Geplante Preiserhoehung in Prozent (%%)")
    parser.add_argument("--json", action="store_true", help="Ausgabe als JSON")

    args = parser.parse_args()
    inp = BreakEvenInput(
        country=args.country,
        unit_price=args.price,
        var_cost_per_unit=args.var_cost,
        current_volume=args.volume,
        discount_pct=args.discount,
        price_increase_pct=args.price_increase,
    )
    res = calculate_break_even(inp)

    if args.json:
        print(json.dumps(res.__dict__, indent=2, ensure_ascii=False))
    else:
        print("=" * 76)
        print(f"DACH DECKUNGSBEITRAGS- & BREAK-EVEN-ANALYSE 2026 ({res.country} / {res.currency})")
        print("=" * 76)
        print(f"Stueckdeckungsbeitrag (db) : {res.unit_db:,.2f} {res.currency} / Stk. (DB-Quote: {res.db_quote_pct:.1f} %)")
        print(f"Break-Even-Point (BEP)     : {res.break_even_units:,} Stk. ({res.break_even_revenue:,.2f} {res.currency})")
        print(f"Cash-Point (vor AfA)       : {res.cash_point_units:,} Stk.")
        print(f"DB I -> DB II -> DB III    : {res.db1:,.0f} -> {res.db2:,.0f} -> {res.db3:,.0f} {res.currency}")
        print(f"DB IV / EBIT               : {res.db4_ebit:,.2f} {res.currency} ({res.ebit_margin_pct:.1f} % Marge)")
        print(f"Sicherheitskoeffizient     : +{res.margin_of_safety_pct:.1f} % (DOL: {res.operating_leverage_dol:.2f}x)")
        print(f"Bei -{args.discount:.0f}% Rabatt noetig     : +{res.required_volume_increase_pct:.1f} % (+{res.required_extra_units:,} Stk.)")
        print(f"Bei +{args.price_increase:.0f}% Preis verkraftbar : -{res.max_volume_loss_pct:.1f} % (-{res.max_lost_units:,} Stk.)")
        print("=" * 76)


if __name__ == "__main__":
    main()
