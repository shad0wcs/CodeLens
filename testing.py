from tesseract_code import api_usage

if __name__ == '__main__':
    img = r'test_data/bad_image.jpg'
    api_usage.detect_words(img)
    result = api_usage.get_idented_text(img)

    print(result)
