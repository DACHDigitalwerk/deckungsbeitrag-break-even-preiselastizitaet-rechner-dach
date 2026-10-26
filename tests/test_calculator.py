# -*- coding: utf-8 -*-
import pytest
from deckungsbeitrag_dach import BreakEvenInput, calculate_break_even


def test_default_break_even_and_multistage_db():
    res = calculate_break_even(BreakEvenInput())
    assert res.unit_db == 140.0
    assert res.db_quote_pct == pytest.approx(58.33, abs=0.05)
    assert res.total_revenue == 2_040_000.0
    assert res.db1 == 1_190_000.0
    assert res.db2 == 970_000.0
    assert res.db3 == 660_000.0
    assert res.db4_ebit == 380_000.0
    # Total fixed = 810,000 / 140 = 5785.71 -> ceil = 5786 units
    assert res.break_even_units == 5_786


def test_cash_point_excludes_depreciation():
    res = calculate_break_even(BreakEvenInput())
    # Cash fixed = 810,000 - 130,000 = 680,000 / 140 = 4857.14 -> ceil = 4858
    assert res.cash_effective_fixed_costs == 680_000.0
    assert res.cash_point_units == 4_858
    assert res.cash_point_units < res.break_even_units


def test_target_profit_units():
    res = calculate_break_even(BreakEvenInput(target_profit=250_000.0))
    # (810,000 + 250,000) / 140 = 1,060,000 / 140 = 7571.42 -> 7572
    assert res.target_profit_units == 7_572


def test_margin_of_safety_and_operating_leverage():
    res = calculate_break_even(BreakEvenInput())
    assert res.margin_of_safety_pct == pytest.approx(31.93, abs=0.05)
    # DOL = 1,190,000 / 380,000 = 3.1315
    assert res.operating_leverage_dol == pytest.approx(3.13, abs=0.02)


def test_discount_volume_increase_formula():
    # p=100, kv=70 -> db=30 (30% DB quote). 10% discount -> new db=20 -> +50% required volume!
    inp = BreakEvenInput(unit_price=100.0, var_cost_per_unit=70.0, current_volume=1_000, discount_pct=10.0)
    res = calculate_break_even(inp)
    assert res.discounted_unit_db == 20.0
    assert res.required_volume_increase_pct == 50.0
    assert res.required_extra_units == 500


def test_price_increase_max_volume_loss():
    # p=100, kv=70 -> db=30. +10% price -> new db=40 -> max volume loss = (1 - 30/40) = 25%!
    inp = BreakEvenInput(unit_price=100.0, var_cost_per_unit=70.0, current_volume=1_000, price_increase_pct=10.0)
    res = calculate_break_even(inp)
    assert res.increased_price_unit_db == 40.0
    assert res.max_volume_loss_pct == 25.0
    assert res.max_lost_units == 250


def test_ch_currency_support():
    res = calculate_break_even(BreakEvenInput(country="CH"))
    assert res.currency == "CHF"


def test_zero_depreciation_equals_break_even():
    res = calculate_break_even(BreakEvenInput(depreciation_in_fixed=0.0))
    assert res.cash_point_units == res.break_even_units


def test_negative_unit_db_raises():
    with pytest.raises(ValueError):
        calculate_break_even(BreakEvenInput(unit_price=50.0, var_cost_per_unit=60.0))


def test_invalid_country_or_price_raises():
    with pytest.raises(ValueError):
        calculate_break_even(BreakEvenInput(country="UK"))
    with pytest.raises(ValueError):
        calculate_break_even(BreakEvenInput(unit_price=0.0))
