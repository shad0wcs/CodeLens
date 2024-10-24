# import pytesseract
# from PIL import Image

from tesseract import api_usage

if __name__ == '__main__':
    result = api_usage.get_idented_text('test_data/code2.png')
    print(result)

    #with open(f'result.txt', 'w') as text_file:
        #text_file.write(result)
