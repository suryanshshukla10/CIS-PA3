import numpy as np
from pathlib import Path


class Problem3BodyA:
    """Rigid Body Degign File."""

    def __init__(self, path: str):
        self.path = path
        with open(path, "r") as f:
            line = next(f)
            toks = line.replace(" ", "").split(",")
            self.N_marker = int(toks[0])

        arr = np.loadtxt(path, delimiter=" ", skiprows=1, dtype=np.float64)
        self.marker = arr[: self.N_marker]
        self.tip = arr[-1]
