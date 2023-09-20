import fpdf

# ориентация Portrait LandScape
# измерения mm pt cm in
# форматы А3 A4 A5 letter legal
pdf = fpdf.FPDF(orientation='P', unit='mm', format='A4')
# создаем страницу
pdf.add_page()

# устанавливаем шрифт
pdf.set_font("Arial", size=12)
# устанавливаем точку, рамку, выравнивание, текст, ссылку
pdf.cell(190, 1, border=True, fill=True, ln=1, align="C")
pdf.cell(10, 5, link='http://yandex.ru', txt="Welcome to Python!", ln=3, align="L")
pdf.cell(190, 1, border=True, fill=True, ln=1, align="C")

# добавляем свой шрифт
pdf.add_font('calibri', '', 'C:\\Windows\\Fonts\\calibri.ttf', uni=True)
pdf.set_font('calibri', size=18)
pdf.set_text_color(220, 50, 50)
pdf.cell(190, 15, txt="Welcome to Python!", ln=1, align="C")

# вставляем картинку
pdf.image("logo.png", x=10, y=80, w=100)

# рисуем
pdf.line(10, 10, 10, 100)
pdf.set_line_width(1)
pdf.set_draw_color(255, 128, 0)
pdf.line(20, 20, 100, 20)

pdf.ellipse(10, 40, 10, 100, 'F')
pdf.set_fill_color(230, 230, 0)
pdf.rect(30, 30, 100, 50)

pdf.output("simple_demo.pdf")
