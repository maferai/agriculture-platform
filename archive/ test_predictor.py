import pandas as pd
from backend.predictor import get_crop_status, get_ndvi_trend, detect_sudden_drop

def test_crop_status_healthy():
    # Create a small series of NDVI values
    ndvi = pd.Series([0.6, 0.61, 0.62])
    # Assert that the function returns "healthy"
    assert get_crop_status(ndvi) == "healthy"

def test_ndvi_trend_declining():
    ndvi = pd.Series([0.7, 0.6, 0.5])
    # Assert that the trend detection works
    assert get_ndvi_trend(ndvi) == "declining"

def test_sudden_drop_detected():
    ndvi = pd.Series([0.6, 0.55])
    # Assert that the sudden drop alert works
    assert detect_sudden_drop(ndvi) is True

def test_sudden_drop_not_detected():
    ndvi = pd.Series([0.6, 0.58])
    # Assert no false alarm when drop < 0.05
    assert detect_sudden_drop(ndvi) is False
