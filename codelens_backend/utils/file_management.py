"""Методы для сохранения и удаления временных файлов."""
import os


def save_file(file_dest: str, file) -> None:
    """Метод для сохранения файла."""
    with open(file_dest, "wb+") as destination:
        for chunk in file.chunks():
            destination.write(chunk)


def delete_file(filename: str) -> bool:
    """Метод для удаления файла."""
    if os.path.exists(filename):
        os.remove(filename)
        return True
    else:
        return False
