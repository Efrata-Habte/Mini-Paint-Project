from __future__ import annotations

from typing import Iterable

import numpy as np
from OpenGL.GL import (
    GL_ARRAY_BUFFER,
    GL_COLOR_BUFFER_BIT,
    GL_FLOAT,
    GL_FRAGMENT_SHADER,
    GL_LINE_LOOP,
    GL_LINE_STRIP,
    GL_LINES,
    GL_STATIC_DRAW,
    GL_TRIANGLES,
    GL_TRIANGLE_FAN,
    GL_VERTEX_SHADER,
    glBindBuffer,
    glBindVertexArray,
    glBufferData,
    glClear,
    glClearColor,
    glCreateProgram,
    glCreateShader,
    glDeleteBuffers,
    glDeleteProgram,
    glDeleteShader,
    glDeleteVertexArrays,
    glDrawArrays,
    glEnableVertexAttribArray,
    glGenBuffers,
    glGenVertexArrays,
    glGetUniformLocation,
    glLineWidth,
    glShaderSource,
    glCompileShader,
    glAttachShader,
    glLinkProgram,
    glUseProgram,
    glVertexAttribPointer,
    glViewport,
    glUniformMatrix3fv,
    glUniformMatrix4fv,
    glUniform3f,
)

from .math_utils import Vec2, identity3, to_gl_mat3, to_gl_mat4, vec2
from .shapes import Shape, ShapeKind
from .viewport import Viewport

class Renderer:
    def __init__(self) -> None:
            self.program = _create_program(VERTEX_SHADER, FRAGMENT_SHADER)
            self.u_projection = glGetUniformLocation(self.program, "uProjection")
            self.u_model = glGetUniformLocation(self.program, "uModel")
            self.u_color = glGetUniformLocation(self.program, "uColor")
            self._vao = glGenVertexArrays(1)
            self._vbo = glGenBuffers(1)
            glBindVertexArray(self._vao)
            glBindBuffer(GL_ARRAY_BUFFER, self._vbo)
            glEnableVertexAttribArray(0)
            glVertexAttribPointer(0, 2, GL_FLOAT, False, 8, None)
            glBindVertexArray(0)

    def dispose(self) -> None:
        glDeleteBuffers(1, [self._vbo])
        glDeleteVertexArrays(1, [self._vao])
        glDeleteProgram(self.program)

def _create_program(vertex_source: str, fragment_source: str) -> int:
    vertex_shader = glCreateShader(GL_VERTEX_SHADER)
    fragment_shader = glCreateShader(GL_FRAGMENT_SHADER)
    glShaderSource(vertex_shader, vertex_source)
    glShaderSource(fragment_shader, fragment_source)
    glCompileShader(vertex_shader)
    glCompileShader(fragment_shader)
    program = glCreateProgram()
    glAttachShader(program, vertex_shader)
    glAttachShader(program, fragment_shader)
    glLinkProgram(program)
    glDeleteShader(vertex_shader)
    glDeleteShader(fragment_shader)
    return program