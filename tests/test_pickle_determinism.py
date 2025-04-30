
import pytest
from data.sample_objects import sample_objects
from utils.pickle_utils import is_pickle_deterministic, hash_pickle


test_cases = [
    pytest.param("integer", sample_objects["integer"], id="Test 1: Integer (42)"),
    pytest.param("float", sample_objects["float"], id="Test 2: Float (3.1415)"),
    pytest.param("string", sample_objects["string"], id="Test 3: String ('Pickle test!')"),
    pytest.param("list", sample_objects["list"], id="Test 4: Mixed list"),
    pytest.param("dict", sample_objects["dict"], id="Test 5: Dictionary with list"),
    pytest.param("tuple", sample_objects["tuple"], id="Test 6: Tuple"),
    pytest.param("nested", sample_objects["nested"], id="Test 7: Nested structure"),
]

@pytest.mark.parametrize("name,obj", test_cases)
def test_deterministic_pickle(name, obj):
    assert is_pickle_deterministic(obj), f"Pickling not deterministic for: {name}"

obj_cases = [
    pytest.param("obj1", {"x": 5, "y": 3}, id="Test 8: Object two keys"),
]
@pytest.mark.parametrize("name,obj", obj_cases)
def test_equivalent_but_not_identical_structures(name, obj):
    obj1 = {'x': 5, 'y': 3}
    obj2 = {'y': 3, 'x': 5}
    assert obj1 == obj2, f"{name}: Objects should be equivalent regardless of order."
    assert hash_pickle(obj1) != hash_pickle(obj2), f"{name}: Hashes should differ due to order."
    
