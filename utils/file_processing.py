import io
import PyPDF2
import docx
import pandas as pd

def process_pdf(file_path):
    text = ""
    with open(file_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text

def process_docx(file_path):
    text = ""
    doc = docx.Document(file_path)
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text

def process_excel(file_path):
    text = ""
    # Read all sheets into a dictionary of DataFrames
    dfs = pd.read_excel(file_path, sheet_name=None)
    for sheet_name, df in dfs.items():
        text += f"Sheet: {sheet_name}\n" + df.to_string() + "\n"
    return text
