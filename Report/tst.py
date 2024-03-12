from weasyprint import HTML

HTML(filename='templates/template.html').write_pdf('./result.pdf')

