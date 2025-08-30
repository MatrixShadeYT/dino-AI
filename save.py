import numpy as np
import json

def save(network,file="data.json"):
    serializable = {key: network[key].tolist() for key in network}
    with open(file, "w") as f:
        json.dump(serializable, f)

def get(file="data.json"):
    with open(file, "r") as f:
        data = json.load(f)
    network = {key: np.array(value) for key, value in data.items()}
    return network