import hashlib
import os

import arrow
from settings import HASH_NAME, ITERATIONS, SECRET_KEY
from werkzeug.datastructures import FileStorage


def save_file_field(file_field: FileStorage, dir: str) -> str:
    if not os.path.exists(dir):
        os.mkdir(dir)

    # Avoid duplicates, in case the same filename is a different imatge
    # Split filename and fileformat
    fileformat = file_field.filename.rsplit('.', maxsplit=1)[-1]

    ts = arrow.utcnow().int_timestamp
    new_filename = f'{file_field.filename}##{ts}'

    new_filename = hashlib.pbkdf2_hmac(
        HASH_NAME,
        new_filename.encode('utf-8'),
        SECRET_KEY.encode('utf-8'),
        ITERATIONS
    ).hex()

    # Append format at the end
    new_filename = f'{new_filename}.{fileformat}'
    file_field.save(
        os.path.join(dir, new_filename)
    )

    return new_filename
