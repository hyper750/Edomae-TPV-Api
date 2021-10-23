import os

from werkzeug.datastructures import FileStorage


def save_file_field(file_field: FileStorage, dir: str):
    file_field.save(
        os.path.join(dir, file_field.filename)
    )
