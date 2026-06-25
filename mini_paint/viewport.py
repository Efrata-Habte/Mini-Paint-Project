"""Window-to-world coordinate mapping."""

from __future__ import annotations

import numpy as np

from .math_utils import Vec2, vec2

class Viewport:
    """Maps screen pixels to a 2D world coordinate system."""

    def __init__(
        self,
        world_left: float = -10.0,
        world_right: float = 10.0,
        world_bottom: float = -7.5,
        world_top: float = 7.5,
    ) -> None:
        self.world_left = world_left
        self.world_right = world_right
        self.world_bottom = world_bottom
        self.world_top = world_top
        self.window_width = 1
        self.window_height = 1

    def resize(self, width: int, height: int) -> None:
        self.window_width = max(1, width)
        self.window_height = max(1, height)

@property
    def world_width(self) -> float:
        return self.world_right - self.world_left
@property
    def world_height(self) -> float:
        return self.world_top - self.world_bottom