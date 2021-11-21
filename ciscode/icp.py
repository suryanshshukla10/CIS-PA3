from __future__ import annotations
from typing import Union
from typing import Type

import numpy as np
import logging

log = logging.getLogger(__name__)


class Frame:
    def __init__(self, r: np.ndarray, p: np.ndarray) -> None:
        """[summary]

        Args:
            r (np.ndarray): [description]
            p (np.ndarray): [description]
        """

    def __array__(self):
        out = np.eye(4, dtype=np.float32)
        out[:3, :3] = self.r
        out[:3, 3] = self.p
        return out

    def __str__(self):
        return np.array_str(np.array(self), precision=4, suppress_small=True)

    def inv(self) -> Frame:
        return Frame(self.r.T, -(self.r.T @ self.p))
