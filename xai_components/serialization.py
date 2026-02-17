import json
import numpy as np

DATATYPES_KEY = "__datatypes__"

def save_params_npz(params, path):
    """
    Save a heterogeneous parameter dict to a single npz file.
    """
    payload = {}
    datatypes = {}

    for key, val in params.items():
        if isinstance(val, np.ndarray):
            payload[key] = val
            datatypes[key] = "ndarray"
        elif isinstance(val, (bool, int, float)):
            payload[key] = np.array(val)
            datatypes[key] = "scalar"
        elif isinstance(val, str):
            payload[key] = np.array(val)
            datatypes[key] = "str"
        elif val is None:
            payload[key] = np.array(0)
            datatypes[key] = "none"
        else:
            raise TypeError(f"Unsupported param type for '{key}': {type(val)}")
    payload[DATATYPES_KEY] = np.array(json.dumps(datatypes), dtype=np.str_)
    np.savez(path, **payload)

def load_params_npz(path):
    """
    Load parameters saved by save_params_npz().
    """
    with np.load(path, allow_pickle=False) as npzfile:
        if DATATYPES_KEY in npzfile.files:
            datatype_arr = json.loads(str(npzfile[DATATYPES_KEY].item()))
        else:
            datatype_arr = {}

        output= {}
        for key in npzfile.files:
            if key == DATATYPES_KEY:
                continue

            arr = npzfile[key]
            datatype = datatype_arr.get(key)

            if datatype == "ndarray":
                output[key] = arr
            elif datatype in ("scalar", "str"):
                output[key] = arr.item()
            elif datatype == "none":
                output[key] = None
            else:
                output[key] = arr

        return output