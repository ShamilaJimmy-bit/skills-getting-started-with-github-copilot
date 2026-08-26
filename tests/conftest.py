import copy

import pytest

from src.app import activities


@pytest.fixture(autouse=True)
def reset_activities():
    """Restore the in-memory activities store after each test to avoid cross-test leakage."""
    original = copy.deepcopy(activities)
    yield
    activities.clear()
    activities.update(copy.deepcopy(original))
