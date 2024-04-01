"""
Copyright (c) 2024 Tangtangfang Fang

All rights reserved.

This file is part of AVM-GRP.

AVM-GRP is distributed under the GPLv3 License.
See the LICENSE file at the top level of the distribution for details.
"""

import platform

# Get the operating system name
os_name = platform.system()

# Check the operating system and execute different code accordingly
if os_name == "Windows":
    print("Running on Windows, load pdfkit")
elif os_name == "Linux":
    print("Running on Linux, load weasyprint")
elif os_name == "Darwin":
    print("Running on macOS, load weasyprint")
else:
    print("Running on an unsupported operating system, try to load weasyprint")



# from weasyprint import HTML
#
# obj = HTML(filename='templates/template.html')
# obj.write_pdf('./result.pdf')

import pdfkit


html_content = "./templates/template.html"


css_content = "./templates/templateForWin.css"


output_pdf = "output.pdf"


pdfkit.from_file(input=html_content, css=css_content, output_path=output_pdf, options={"enable-local-file-access": ""}, verbose=True)


