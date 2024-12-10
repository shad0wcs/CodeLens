"""
Методы валидирования кода.

Методы проверяют синтаксис куска кода на корректность.
В данный момент реализован только python.
"""
# -*- coding: utf-8 -*-
import ast

import astvalidate


def python_validation_ast(src: str) -> bool:
    """
    Проверяет строку с кодом на python на наличие синтаксических ошибок.

    src: строка, код на python.
    retrun: True, если код валидный и False, если найдена ошибка.
    """
    try:
        tree = ast.parse(src, mode='exec')
        astvalidate.validate(tree)
    except SyntaxError:
        return False
    return True
