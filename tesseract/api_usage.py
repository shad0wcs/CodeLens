# -*- coding: utf-8 -*-
import pytesseract
from matplotlib import pyplot as plt
from pytesseract import Output
from PIL import Image, ImageFilter
from PIL import ImageEnhance
import cv2
import pandas as pd
from six import binary_type

CONFIG = {
    'TESSERACT_EXE_PATH': 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe',
    'CONFIG KEYS': r'-c preserve_interword_spaces=1 --oem 1 --psm 6 -l eng+rus'
}

def ImproveImg(img, size):
    scale_percent = int(size)
    image = cv2.imread(img)
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    cv2.imshow("123", gray)
    cv2.waitKey(0)
    return gray

def _setup():
    pytesseract.pytesseract.tesseract_cmd = CONFIG.get('TESSERACT_EXE_PATH')

def get_idented_text(imgage_src: str) -> str:
    _setup()

    d = pytesseract.image_to_data(ImproveImg(imgage_src, 350),
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