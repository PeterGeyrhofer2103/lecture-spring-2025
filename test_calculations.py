from predict_q import predict_q
from calculate_lcoe import calculate_lcoe
import pytest


# tests predict_q_wind
def test_predict_q_valid_input():
    assert (
        predict_q(3.5, 0.35) == 10731.0
    )  # to test if the calculated value is the expected value


def test_predict_q_invalid_capacity_factor():
    with pytest.raises(ValueError):
        predict_q(3.5, 1.2)  # to test if the function declines unwanted value


# tests calculate_lcoe
def test_calculate_lcoe_valid_input():
    assert (
        calculate_lcoe(0.05, 25, 1500000, 30000, 3.5, 0.35) == 12.71
    )  # see test_predict_q_wind_valid_input


def test_calculate_lcoe_zero_production():
    with pytest.raises(ZeroDivisionError):
        calculate_lcoe(
            0.05, 25, 1500000, 30000, 0, 0
        )  # to test if the function reacts to a division by 0
