import pickle
import hashlib

def hash_pickle(obj, protocol=pickle.HIGHEST_PROTOCOL):
    byte_stream = pickle.dumps(obj, protocol=protocol)
    return hashlib.sha256(byte_stream).hexdigest(), byte_stream

def is_pickle_deterministic(obj, trials=10):
    """Check if pickling the same object multiple times yields the same hash."""
    hashes = {hash_pickle(obj)[0] for _ in range(trials)}
    return len(hashes) == 1

def hash_pickle(obj):
    return hashlib.sha256(pickle.dumps(obj)).hexdigest()
