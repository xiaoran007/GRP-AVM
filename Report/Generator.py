import os
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration
from datetime import datetime


class Generator(object):
    """
    This class is used to generate the PDF files for the reports that user can download.
    """
    def __init__(self, cwd):
        """
        :param cwd: string
        """
        self.Cwd = cwd
        os.chdir(os.path.dirname(__file__))
        print(f"Generator set dir: {os.getcwd()}")
        self.Env = Environment(loader=FileSystemLoader('./templates'))
        self.Template = self.Env.get_template('template.html')
        self.FontConfig = FontConfiguration()
        self.StyleSheet = CSS(filename='./templates/template.css', font_config=self.FontConfig)
        os.chdir(self.Cwd)
        print(f"Generator set dir back: {self.Cwd}")

    def renderHTML(self, data):
        return self.Template.render(data)

    def RenderPDF(self, data, out_path):
        html_obj = HTML(string=self.renderHTML(data=data))
        html_obj.write_pdf(out_path, stylesheets=[self.StyleSheet], font_config=self.FontConfig)

    @staticmethod
    def DataPasser(enable_llm, enable_full, model_sel, enable_hidden, rID, price, description, features, cp_values):
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
        res['cp_values'] = cp_values
        print(res)
        return res

    @staticmethod
    def rIDPasserBatch(rID, i):
        rID = f'{rID}_{i}'
        return rID

