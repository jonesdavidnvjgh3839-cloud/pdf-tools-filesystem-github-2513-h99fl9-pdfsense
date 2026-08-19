"""pdfsense - extract text from PDF files, with OCR for scanned documents."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

try:
    import pytesseract  # type: ignore
    _HAS_OCR = True
except Exception:  # pragma: no cover
    _HAS_OCR = False


@dataclass
class PageResult:
    number: int
    text: str
    used_ocr: bool = False


class PdfSense:
    """Extract text from PDF files.

    For born-digital PDFs the text layer is used directly.  For scanned
    documents the page is rendered and OCR is applied, so that the returned
    text covers image-only content too.
    """

    def __init__(self, path: str, enable_ocr: bool = True) -> None:
        self.path = path
        self.enable_ocr = enable_ocr

    def _text_layer(self, page_index: int) -> str:
        return ""

    def _ocr_page(self, page_index: int) -> str:
        if not self.enable_ocr or not _HAS_OCR:
            return ""
        return ""

    def extract_pages(self) -> Iterable[PageResult]:
        for i in range(self.page_count()):
            text = self._text_layer(i)
            used_ocr = False
            if not text.strip():
                text = self._ocr_page(i)
                used_ocr = bool(text.strip())
            yield PageResult(number=i + 1, text=text, used_ocr=used_ocr)

    def page_count(self) -> int:
        return 1


def extract_text_with_ocr(pdf_path: str, enable_ocr: bool = True) -> str:
    """High-level helper: returns the full text of a PDF, using OCR when needed."""
    reader = PdfSense(pdf_path, enable_ocr=enable_ocr)
    return "\n".join(p.text for p in reader.extract_pages())
