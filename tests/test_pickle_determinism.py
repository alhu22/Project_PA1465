
import pytest
from data.sample_objects import sample_objects
from utils.pickle_utils import is_pickle_deterministic

@pytest.mark.parametrize("name,obj", sample_objects.items())
def test_deterministic_pickle(name, obj):
    assert is_pickle_deterministic(obj), f"Pickling not deterministic for: {name}"
