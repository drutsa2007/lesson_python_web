import docx
from docx.shared import Inches, Cm, Mm
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.enum.section import WD_SECTION_START, WD_ORIENTATION

# создаем объект документа
doc = docx.Document()

section = doc.sections[0]
# размеры листа
section.page_height = Cm(29.7)
section.page_width = Cm(21.0)
# отступы на странице
section.left_margin = Mm(25)
section.right_margin = Mm(10)
section.top_margin = Mm(15)
section.bottom_margin = Mm(10)
# отступ на колонтитулы
section.header_distance = Mm(10)
section.footer_distance = Mm(10)

# сохраняем файл Название файла
doc.save('filename.docx')
