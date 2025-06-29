import os

def test_model_exists():
    assert os.path.exists("model.pkl"), "model.pkl not found"

def test_metrics_exists():
    assert os.path.exists("metrics.json"), "metrics.json not found"