import os

from werkzeug.datastructures import FileStorage


def save_file_field(file_field: FileStorage, dir: str):
    if not os.path.exists(dir):
        os.mkdir(dir)

    # TODO: Create md5 hash from filename and timestamp for example, to avoid duplicates
    # Rename the file and return the new filename
    file_field.save(
        os.path.join(dir, file_field.filename)
    )
