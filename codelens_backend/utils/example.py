# -*- coding: utf-8 -*-
from tesseract import api_usage
from python_formater import validation

from dotenv import load_dotenv
import os

from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

load_dotenv()

FORMATTER = HtmlFormatter(lineos=True, cssclass="code-block")
CSS_SHEET = FORMATTER.get_style_defs()


def test_method(filename: str) -> (str, str):

    api_usage.CONFIG['TESSERACT_EXE_PATH'] = os.getenv('TESSERACT_EXE_PATH')

    result = api_usage.get_idented_text(filename)

    # todo choose language or recognize it before validation and creating lexer
    if validation.quick_validation(result):
        lexer = get_lexer_by_name("python")
        html_result = highlight(result, lexer=lexer, formatter=FORMATTER)
        return html_result, CSS_SHEET
    else:
        return ""
