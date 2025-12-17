import os
from joblib import Memory

# Paths
CACHE_DIR = os.path.join(os.path.expanduser('~'), '.cache-xircuits')
OUTPUT_DIR = os.path.join(os.path.expanduser('~'), 'output')

os.makedirs(CACHE_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Cache
def _get_vbi_version():
    try:
        import vbi
        return getattr(vbi, "__version__", "unknown")
    except Exception:
        return "unknown"

def create_memory():
    vbi_version = _get_vbi_version()
    cache_dir = os.path.join(CACHE_DIR, f"vbi-{vbi_version}")
    os.makedirs(cache_dir, exist_ok=True)
    return Memory(cache_dir, verbose=2)

memory = create_memory()