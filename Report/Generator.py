import os
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration
from datetime import datetime


class Generator(object):
    """
    This class is used to generate the PDF files for the reports that user can download.
    """
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
        self.font_config = FontConfiguration()
        self.STYLESHEET = CSS(filename='./templates/template.css', font_config=self.font_config)
        os.chdir(self.CWD)
        print(f"set dir back: {self.CWD}")

    def renderHTML(self):
        # with open('./templates/rendered_template.html', 'w') as f:
        #     f.write(self.TEMPLATE.render(self.DATA))
        return self.TEMPLATE.render(self.DATA)

    def RenderPDF(self, out_path):
        os.chdir(os.path.dirname(__file__))
        print(f"set dir: {os.getcwd()}")
        # self.renderHTML()
        # html_obj = HTML(filename='./templates/rendered_template.html')
        html_obj = HTML(string=self.renderHTML())
        os.chdir(self.CWD)
        print(f"set dir back: {self.CWD}")
        html_obj.write_pdf(out_path, stylesheets=[self.STYLESHEET], font_config=self.font_config)

    @staticmethod
    def DataPasser(enable_llm, enable_full, model_sel, enable_hidden, rID, price, description, features):
        res = dict()
        res['enable_llm'] = enable_llm
        res['enable_full'] = enable_full
        if model_sel == "RF":
            res['model_sel'] = "Random Forest"
        elif model_sel == "XGB":
            res['model_sel'] = "XGBoost"
        elif model_sel == "LGBM":
            res['model_sel'] = "LightGBM"
        else:
            res['model_sel'] = "Random Forest"
        res['enable_hidden'] = enable_hidden
        res['rID'] = rID
        res['date'] = f'{datetime.today().date()}'
        res['price'] = price
        res['description'] = description
        res['features'] = features
        print(res)
        return res

    @staticmethod
    def rIDPasserBatch(rID, i):
        rID = f'{rID}_{i}'
        return rID


