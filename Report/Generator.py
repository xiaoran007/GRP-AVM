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
        Initialize the generator.
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
        """
        This method is used to render the HTML template with the given data.
        :param data: dict, the input data.
        :return: string, rendered HTML.
        """
        return self.Template.render(data)

    def RenderPDF(self, data, out_path):
        """
        This method is used to render the PDF file with the given data and save to given path.
        :param data: dict, the input data.
        :param out_path: string, the output path.
        """
        html_obj = HTML(string=self.renderHTML(data=data))
        html_obj.write_pdf(out_path, stylesheets=[self.StyleSheet], font_config=self.FontConfig)

    @staticmethod
    def DataPasser(enable_llm, enable_full, model_sel, enable_hidden, rID, price, description, features, cp_values):
        """
        This method is used to transform the input args to dict.
        :param enable_llm: bool, set True to enable LLM.
        :param enable_full: bool, set True to enable full model.
        :param model_sel: string, the selected model.
        :param enable_hidden: bool, set True to enable hidden prediction.
        :param rID: string, the ID of the report.
        :param price: string, the range price of the house.
        :param description: string, the description of why give such price.
        :param features: list of dicts, the input features.
        :param cp_values: float, the confidence level of the prediction.
        :return: dict
        """
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
        """
        This method is used to transform rID in batch mode.
        :param rID: string, the ID of the batch event.
        :param i: int, the prediction index inside one batch event.
        :return: string, the rID inside batch event.
        """
        rID = f'{rID}_{i}'
        return rID

