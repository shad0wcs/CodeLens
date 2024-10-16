# -*- coding: utf-8 -*-
from tesseract import api_usage
from python_formater import validation

from dotenv import load_dotenv
import os

def test_method(filename: str) -> str:
    load_dotenv()

    api_usage.CONFIG['TESSERACT_EXE_PATH'] = os.getenv('TESSERACT_EXE_PATH')

    result = api_usage.get_idented_text(filename)

    if validation.quick_validation(result):
        return result
    else:
        return ""
