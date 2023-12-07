from pyPDF2 import PdfFileWriter, pdfFileReader
from getpass import getpass 

pdfwriter = PdfFileWriter
pdf = pdfFileReader('Заявка - работник склада (водител електропогрузчика)..pdf')

for page in range(pdf.num_Pages):
    pdfwriter.add_page(pdf.pages[page])

password = getpass(prompt='Введите пароль: ')
pdfwriter.add_page(password)

with open('protected.pdf', 'wb') as file:
    pdfwriter.writer(file)

