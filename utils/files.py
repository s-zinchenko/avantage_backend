import os
import uuid
from typing import Any


def calculate_hex_uuid() -> str:
    return uuid.uuid4().hex


def get_file_ext(filename: str) -> str:
    filename, ext = os.path.splitext(filename)
    return filename, ext.strip(".")


def generate_filename(filename: str) -> str:
    file_uuid = calculate_hex_uuid()
    file_name, ext = get_file_ext(filename)
    return f"{file_name}_{file_uuid[:6]}.{ext}"


def upload_path(instance, filename: str) -> str:  # type: ignore
    filename = generate_filename(filename)
    return "/".join(
        [instance.__class__.__name__, filename[:2], filename[2:4], filename]
    )


def content_file_name(_: Any, filename: str) -> str:
    return f"media/{filename}"
