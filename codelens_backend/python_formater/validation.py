# -*- coding: utf-8 -*-
import ast
import astvalidate

def quick_validation(src: str) -> bool:
    try:
        tree = ast.parse(src, mode='exec')
        assert astvalidate.validate(tree)
    except Exception as e:
        return False
    return True

