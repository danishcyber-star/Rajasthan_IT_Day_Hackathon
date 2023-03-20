from PyPDF2 import PdfReader, PdfWriter

def cropper(start, end, file):
    inputPdf = PdfReader(file)
    outPdf = PdfWriter()
    with open(file.split(".")[0] + "cropped" + ".pdf", "wb") as ostream:
        for page in range(start, end + 1):
            outPdf.add_page(inputPdf.pages[start-1])
        outPdf.write(ostream)
