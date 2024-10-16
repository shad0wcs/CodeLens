# -*- coding: utf-8 -*-
from codelens_backend.tesseract import api_usage
from codelens_backend.python_formater import validation

from dotenv import load_dotenv
import os

load_dotenv()

api_usage.CONFIG['TESSERACT_EXE_PATH'] = os.getenv('TESSERACT_EXE_PATH')

result = api_usage.get_idented_text('test_data/img.png')

if validation.quick_validation(result):
    splited = result.split('\n')
    for ind, line in enumerate(splited):
        print(ind, line)
else:
    print("Text on image does not math python syntax")
    print(result)
