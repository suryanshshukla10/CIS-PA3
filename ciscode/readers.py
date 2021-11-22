import numpy as np
from pathlib import Path
import logging


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


class Vertices:
    """Read vertices
    """

    def __init__(self, path: str):
        self.path = path
        with open(path, "r") as f:
            line = next(f)
            toks = line.replace(" ", "").split(",")

            self.N_vertices = int(toks[0])

        arrVer = np.loadtxt(path, delimiter=" ", skiprows=1,
                            max_rows=self.N_vertices)
        self.arrVer = arrVer


class Indices:
    """Read Indices
    """

    def __init__(self, path: str):
        self.path = path
        with open(path, "r") as f:
            line = next(f)
            toks = line.replace(" ", "").split(",")

            self.N_vertices = int(toks[0])

        arrInd = np.loadtxt(path, delimiter=" ", skiprows=self.N_vertices+2, usecols=(0, 1, 2)
                            )
        self.arrInd = arrInd
