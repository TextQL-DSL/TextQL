import docx
import PyPDF2
from pathlib import Path

def ReadDocx(path: str) -> list[str]:
    '''
    Reads the docx file from the path and returns a list of the words in the document.
    '''
    currDocument = docx.Document(Path(path))
    words = []

    for paragraph in currDocument.paragraphs:
        words += paragraph.text.split()
    
    return words


def ReadPDF(path:str) -> list[str]:
    '''
    Reads the pdf file from the path and returns a list of the words in the document.
    '''
    words = []

    with open(Path(path), 'rb') as file:
        pdf = PyPDF2.PdfFileReader(file)

        for i in range(pdf.numPages):
            currPage = pdf.getPage(i)
            words += currPage.extractText().split()
        
    return words

