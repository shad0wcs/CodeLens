# -*- coding: utf-8 -*-
import pytesseract
from pytesseract import Output
from PIL import Image
import pandas as pd

CONFIG = {
    'TESSERACT_EXE_PATH': 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe',
    'CONFIG KEYS': r'-c preserve_interword_spaces=1 --oem 1 --psm 1 -l eng+ita'
}

def _setup():
    pytesseract.pytesseract.tesseract_cmd = CONFIG.get('TESSERACT_EXE_PATH')

def get_idented_text(imgage_src: str) -> str:
    _setup()

    d = pytesseract.image_to_data(Image.open(imgage_src),
                                  config=CONFIG.get('CONFIG KEYS'), output_type=Output.DICT)
    df = pd.DataFrame(d)

    # clean up blanks
    df1 = df[(df.conf != '-1') & (df.text != ' ') & (df.text != '')]
    result = ""

    # sort blocks vertically
    ind = 1
    sorted_blocks = df1.groupby('block_num').first().sort_values('top').index.tolist()
    for block in sorted_blocks:
        curr = df1[df1['block_num'] == block]
        sel = curr[curr.text.str.len() > 3]
        char_w = (sel.width / sel.text.str.len()).mean()
        prev_par, prev_line, prev_left = 0, 0, 0
        text = ''
        for ix, ln in curr.iterrows():
            # add new line when necessary
            if prev_par != ln['par_num']:
                text = text.rstrip() + '\n'
                prev_par = ln['par_num']
                prev_line = ln['line_num']
                prev_left = 0
            elif prev_line != ln['line_num']:
                text = text.rstrip()+  '\n'
                prev_line = ln['line_num']
                prev_left = 0

            added = 0  # num of spaces that should be added
            if ln['left'] / char_w > prev_left + 1:
                added = int((ln['left']) / char_w) - prev_left
                text += ' ' * added
            text += ln['text'] + ' '
            prev_left += len(ln['text']) + added + 1
        text = text.rstrip() + '\n'

        #custom code
        result += text

    return result