import api_usage
from dotenv import load_dotenv
import os

load_dotenv()

if __name__ == '__main__':
    api_usage.CONFIG['TESSERACT_EXE_PATH'] = os.getenv('TESSERACT_EXE_PATH')
    img = r''
    api_usage.detect_words(img)
    result = api_usage.get_idented_text(img)

    print(result)
