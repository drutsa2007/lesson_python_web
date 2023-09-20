from openpyxl.styles import PatternFill, Border, Side, Alignment, Font, GradientFill, Protection


# Шрифт
font = Font(
    name='Calibri',
    size=11,
    bold=False,
    italic=False,
    vertAlign=None,
    underline='none',
    strike=False,
    color='FF000000'
)

# Заливка
fill = PatternFill(fill_type=None, fgColor='FFFFFFFF')

# Границы
border = Border(
    left=Side(border_style=None, color='FF000000'),
    right=Side(border_style=None, color='FF000000'),
    top=Side(border_style=None, color='FF000000'),
    bottom=Side(border_style=None, color='FF000000'),
    diagonal=Side(border_style=None, color='FF000000'),
    diagonal_direction=0,
    outline=Side(border_style=None, color='FF000000'),
    vertical=Side(border_style=None, color='FF000000'),
    horizontal=Side(border_style=None, color='FF000000')
)

# Выравнивание
alignment = Alignment(
    horizontal='general',
    vertical='bottom',
    text_rotation=0,
    wrap_text=False,
    shrink_to_fit=False,
    indent=0
)

# Защита
protection = Protection(locked=True, hidden=False)