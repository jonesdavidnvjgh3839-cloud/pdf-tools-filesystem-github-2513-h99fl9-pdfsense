# pdfsense

A Python library to extract text from PDF files, with OCR support for scanned
documents so image-only pages are covered too.

## Features

- Extracts text from the embedded text layer
- Runs OCR on scanned / image-only pages
- Returns per-page results

## Usage

```python
from pdfsense import extract_text_with_ocr

text = extract_text_with_ocr("scan.pdf", enable_ocr=True)
```

## License

Apache-2.0
