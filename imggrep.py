import os
import argparse
from PIL import Image
import pytesseract

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TESSERACT_PATH = os.path.join(BASE_DIR, "tesseract", "tesseract.exe")

if not os.path.exists(TESSERACT_PATH):
    print("Error: tesseract.exe not found in 'tesseract/' directory.")
    exit(1)

pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

def search_images_for_word(folder_path, search_word):
    matched_files = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith('.png'):
                file_path = os.path.join(root, file)
                try:
                    text = pytesseract.image_to_string(Image.open(file_path))
                    if search_word.lower() in text.lower():
                        matched_files.append(file_path)
                        print(f"[MATCH] {file_path}")
                except Exception as e:
                    print(f"[ERROR] {file_path}: {e}")
    return matched_files

def main():
    parser = argparse.ArgumentParser(description="Search .png images for a word using OCR")
    parser.add_argument("folder", help="Folder path to search recursively")
    parser.add_argument("word", help="Word to search for")
    parser.add_argument("-o", "--output", help="Optional output file to save matched image paths")

    args = parser.parse_args()

    if not os.path.isdir(args.folder):
        print("Error: Provided path is not a valid directory.")
        return

    print(f"Searching for '{args.word}' in PNG images under: {args.folder}")
    matches = search_images_for_word(args.folder, args.word)

    if args.output and matches:
        try:
            with open(args.output, 'w', encoding='utf-8') as f:
                for path in matches:
                    f.write(path + "\n")
            print(f"Results are written to: {args.output}")
        except Exception as e:
            print(f"Error writing to output file: {e}")

    if not matches:
        print("No matches found.")

if __name__ == "__main__":
    main()
