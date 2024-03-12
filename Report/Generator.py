import os
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML


class Generator(object):
    def __init__(self, data, rID, cwd):
        """
        :param data: dict, key: enable_llm, enable_full,
        model_sel, enable_hidden, rID, date, price, description, features
        :param rID: string
        :param cwd: string
        """
        self.DATA = data
        self.RID = rID
        self.CWD = cwd
        os.chdir(os.path.dirname(__file__))
        print(f"set dir: {os.getcwd()}")
        self.ENV = Environment(loader=FileSystemLoader('./templates'))
        self.TEMPLATE = self.ENV.get_template('template.html')
        os.chdir(self.CWD)
        print(f"set dir back: {self.CWD}")

    def renderHTML(self):
        with open('rendered_template.html', 'w') as f:
            f.write(self.TEMPLATE.render(data=self.DATA))

    def RenderPDF(self, out_path):
        os.chdir(os.path.dirname(__file__))
        print(f"set dir: {os.getcwd()}")
        self.renderHTML()
        html_obj = HTML(filename='rendered_template.html')
        os.chdir(self.CWD)
        print(f"set dir back: {self.CWD}")
        html_obj.write_pdf(out_path)


