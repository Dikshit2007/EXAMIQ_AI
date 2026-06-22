import fitz
import pytesseract
from PIL import Image
import io

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

def extract_text_from_pdf(pdf_file):

    text = ""

    pdf_bytes = pdf_file.read()

    doc = fitz.open(stream=pdf_bytes, filetype="pdf")

    for page in doc:

        page_text = page.get_text()

        if page_text.strip():
            text += page_text + "\n"

        else:

            pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))

            img_bytes = pix.tobytes("png")

            image = Image.open(io.BytesIO(img_bytes))

            ocr_text = pytesseract.image_to_string(image)

            text += ocr_text + "\n"

    return text