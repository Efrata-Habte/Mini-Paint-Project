"""Vector shape definitions stored as mathematical objects."""

from __future__ import annotations

import math
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Iterable

import numpy as np

from .math_utils import Vec2, apply2, distance, identity3, translate2, vec2


class ShapeKind(Enum):
    LINE = auto()
    POLYLINE = auto()
    POLYGON = auto()