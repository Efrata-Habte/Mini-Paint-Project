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

    def visible_bounds(self) -> tuple[float, float, float, float]:
        """Return world bounds adjusted so shapes keep uniform scale on any window aspect."""
        world_aspect = self.world_width / self.world_height
        window_aspect = self.window_width / self.window_height
        center_x = (self.world_left + self.world_right) / 2
        center_y = (self.world_bottom + self.world_top) / 2

        if window_aspect > world_aspect:
            half_height = self.world_height / 2
            half_width = half_height * window_aspect
        else:
            half_width = self.world_width / 2
            half_height = half_width / window_aspect

        return (
            center_x - half_width,
            center_x + half_width,
            center_y - half_height,
            center_y + half_height,
        )

    def screen_to_world(self, screen_x: float, screen_y: float) -> Vec2:
        """Convert GLFW screen coordinates (origin top-left) to world coordinates."""
        left, right, bottom, top = self.visible_bounds()
        visible_width = right - left
        visible_height = top - bottom
        nx = screen_x / self.window_width
        ny = 1.0 - (screen_y / self.window_height)
        world_x = left + nx * visible_width
        world_y = bottom + ny * visible_height
        return vec2(world_x, world_y)

    def world_to_ndc(self, point: Vec2) -> Vec2:
        """Convert world coordinates to normalized device coordinates."""
        left, right, bottom, top = self.visible_bounds()
        visible_width = right - left
        visible_height = top - bottom
        x = 2.0 * (point[0] - left) / visible_width - 1.0
        y = 2.0 * (point[1] - bottom) / visible_height - 1.0
        return vec2(x, y)

    def projection_matrix(self) -> np.ndarray:
        """Orthographic projection matching the visible world bounds."""
        left, right, bottom, top = self.visible_bounds()
        return np.array(
            [
                [2.0 / (right - left), 0.0, 0.0, -(right + left) / (right - left)],
                [0.0, 2.0 / (top - bottom), 0.0, -(top + bottom) / (top - bottom)],
                [0.0, 0.0, 1.0, 0.0],
                [0.0, 0.0, 0.0, 1.0],
            ],
            dtype=np.float32,
        )

    def projection_matrix_gl(self) -> np.ndarray:
        from .math_utils import to_gl_mat4

        return to_gl_mat4(self.projection_matrix())