from weasyprint import HTML

obj = HTML(filename='templates/template.html')
obj.write_pdf('./result.pdf')
