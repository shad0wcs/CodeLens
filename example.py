# -*- coding: utf-8 -*-
from tesseract import api_usage
from python_formater import validation

from dotenv import load_dotenv
import os

load_dotenv()

api_usage.CONFIG['TESSERACT_EXE_PATH'] = os.getenv('TESSERACT_EXE_PATH')

result = api_usage.get_idented_text('test_data/good_code.png')

if validation.quick_validation(result):
    splited = result.split('\n')
    for ind, line in enumerate(splited):
        print(ind, line)
else:
    print("Text on image does not math python syntax")
    print(result)
