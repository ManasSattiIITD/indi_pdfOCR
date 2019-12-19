# indi_pdfOCR
An OCR software in python3 for pdfs of BHARAT languages.

Requirements:

  Python 3
  Windows/Ubuntu(Preffered)/macOS

  APIs:-
  1. Tesseract-ocr
      https://github.com/tesseract-ocr/tesseract/wiki
  2. Poppler.
      https://blog.alivate.com.au/poppler-windows/
  3. tesseract language data.
      https://github.com/tesseract-ocr/tessdata

  python modules:-
  1. threading
  2. pytesseract
  3. pdf2image
  4. Pillow
  5. os
  6. sys
  7. shutil

  *TIP* :  Use command "pip3 install <module_name>" in cmd with admin privileges.
  eg.:-   pip3 install threading

Note: 
The script uses 4 threads for computation. Decrease no. of threads by if your system is not compatible.
