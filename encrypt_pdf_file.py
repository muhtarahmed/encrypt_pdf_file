from PyPDF2 import PdfWriter, PdfReader
from getpass import getpass

pdf_writer = PdfWriter()
pdf_reader = PdfReader('zp.pdf')

for i in range(len(pdf_reader.pages)):
    pdf_writer.add_page(pdf_reader.pages[i])

password = getpass(prompt='Введите пароль: ')
pdf_writer.encrypt(password)

with open('new.pdf', 'wb') as file:
    pdf_writer.write(file)