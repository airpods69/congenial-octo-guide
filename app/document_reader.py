from typing import List
from PIL.Image import Image
from pdf2image.pdf2image import convert_from_bytes
import pytesseract
from utils import MissingEnvironmentVariable

import os

if "TESSERACT_PATH" in os.environ:
    pytesseract.pytesseract.tesseract_cmd = os.environ["TESSERACT_PATH"]
else:
    raise MissingEnvironmentVariable(
        "Tesseract path not set. Set environment variable TESSERACT_PATH"
    )


def get_pages(pdf_bytes) -> List[Image]:
    """
    Returns the images of each page from the pdf file

    Input: Path to PDF
    Output: List of PIL Images

    Feel free to edit this if you have a different way of retrieving files.
    But make sure to return List[Images]
    """
    pages = convert_from_bytes(pdf_bytes)
    return pages


def read_page(page: Image) -> str:
    """
    Reads the content of the page image and returns it.

    Input: PIL Image
    Output: string
    """
    contents_string = pytesseract.image_to_string(page)
    return contents_string


def read_pages(pages: List[Image]) -> List[str]:
    """
    Reads all of the pages and returns list of strings

    Input: List[Images]
    Output: List[String]
    """

    total_content = []

    for page in pages:
        content_of_page = read_page(page)
        total_content.append(content_of_page)

    return total_content


def get_content(pdf_bytes) -> str:
    """
    Gets PDF and returns the content of that pdf
    Input: None
    Output: str
    """
    pages = get_pages(pdf_bytes)
    content = read_pages(pages=pages)
    content = "".join(content)

    return content
