from fpdf import FPDF, HTMLMixin

class MyFPDF(FPDF, HTMLMixin):
    pass

html = '''<h1 align="center">PyFPDF HTML Demo</h1>
    <p>This is regular text</p>
    <p>You can also <b>bold</b>, <i>italicize</i> or <u>underline</u>
    '''

pdf = MyFPDF()
pdf.add_page()
pdf.write_html(html)
pdf.output('html.pdf')

# Необходимо избавиться от ошибки
# text = h2p.unescape(text) # To deal with HTML entities
# просто закомментировать ее, если это делаете вы, то проблем не будет
# если код отправляет клиент, то думайте как обработать
# либо добавить свою функцию обработки (unescape - метод отсутствует)