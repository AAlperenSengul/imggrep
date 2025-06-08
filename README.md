# imggrep

`imggrep` is a simple command-line tool written in Python that scans `.png` images in a folder recursively, performs OCR using Tesseract, and prints the paths of images that contain the desired word.

This project is portable and includes its own copy of `tesseract.exe` for Windows. No system installation of Tesseract is required.

---

## Features

- Recursively scans folders for `.png` files
- Uses OCR to extract text from each image
- Searches for a user-specified word or phrase
- Outputs matched image paths to terminal or file
- Requires no system-wide Tesseract installation (Windows)

---

## Requirements

- Python 3.7 or higher
- Packages from `requirements.txt`

Install dependencies:

```bash
pip install -r requirements.txt
