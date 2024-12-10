# -*- coding: utf-8 -*-
"""Метод для извлечения программного кода из изображения."""
import os

import requests
from dotenv import load_dotenv
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name, guess_lexer

from python_formater import validation
from tesseract import api_usage

load_dotenv()

FORMATTER = HtmlFormatter(lineos=True, cssclass="code-block")
CSS_SHEET = FORMATTER.get_style_defs()


def process_code_snippet_image(filename: str) -> (str, str):
    """
    Метод для извлечения программного кода из изображения.

    filename: строка, путь к изображению
    return: tuple(str, str) - текст с изображения, таблица стилей для синтаксиса,
    предполагаемый язык, надежность распознавания
    """
    api_usage.CONFIG['TESSERACT_EXE_PATH'] = os.getenv('TESSERACT_EXE_PATH')

    result = api_usage.get_idented_text(filename)

    if result.strip() == "":
        return "", CSS_SHEET, None, True

    response = requests.get("https://guesslang.waterwater.moe/guess",
                            params={"text": result}, timeout=5)

    expected_lang = None
    reliable = False

    if response.ok:
        lang_js = response.json()
        if float(lang_js['reliable']):
            expected_lang = lang_js['languageName'].lower()
            reliable = True
    else:
        expected_lang = guess_lexer(result).name

    try:
        lexer = get_lexer_by_name(expected_lang)
    except Exception:
        lexer = get_lexer_by_name("text")

    print(f"Lang: {expected_lang}, reliable: {reliable}")

    if expected_lang == "python":
        html_result = highlight(result, lexer=lexer, formatter=FORMATTER)
        valid = validation.python_validation_ast(result)
        print(f"Valid: {valid}")
        return html_result, CSS_SHEET, (expected_lang if reliable else None), valid
    else:
        html_result = highlight(result, lexer=lexer, formatter=FORMATTER)
        return html_result, CSS_SHEET, expected_lang, True
