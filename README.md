# **This is Main repo for AVM Project.** <img src="https://raw.githubusercontent.com/aemmadi/aemmadi/master/wave.gif" width="30">



[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&pause=1000&color=F7B769&width=435&lines=We+are+GRP-Team13)](https://git.io/typing-svg)

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&pause=1000&color=F7B769&width=435&lines=Automated+Valuation+Model)](https://git.io/typing-svg)

<span > 
    <img src="https://img.shields.io/badge/Python-_3.9-blue"  alt="py39"/> 
    <img src="https://img.shields.io/badge/PyTorch-_1.13.1-g"  alt="torch"/> 
    <img src="https://img.shields.io/badge/Flask-_2.2.2-g"  alt="flask"/> 
    <img src="https://img.shields.io/badge/sklearn-_1.3.0-g"  alt="sklearn"/>
    <img src="https://img.shields.io/badge/mapie-_0.8.2-g"  alt="mapie"/>
</span>

<p></p>
<img src="./markdown/img/teamlogo.png" width="23%" height="23%" alt="team13"/>

***

## Table of Contents
1. [Note](#note)
2. [Change Log](#change-log)
3. [OS and Platform Support](#os-and-platform-support)
4. [Deployment Guide](#deployment-guide)
5. [Troubleshooting](#troubleshooting)

## **Note**
This project **AVM-GRP** is part of **GRP** project.\
Some links (About us and code repo link) in this software is only designed for in-school access, which means you need access these links under __Eduroam__ network connection.\
The website [avm.asia](http://www.avm.asia) is the demo of this software.

## **Change Log**
[Change Log](changelog.md)

## **OS and Platform Support**
This application is website based, since web server usually uses Unix system, this application only macOS and Linux is officially supported. The following is detailed OS and Platform support matrix. 

OS support matrix:

| OS      | Version                 | Architecture  | Support |
|---------|-------------------------|---------------|---------|
| macOS   | Big Sur and later       | x86_64, arm64 | ✅       |
| Linux   | Ubuntu 22.04, Debian 12 | x86_64, arm64 | ✅       |
| Windows | 10                      | x86_64        | ✅       |

Platform support matrix:

| Platform | Version       | Support |
|----------|---------------|---------|
| Chrome   | current       | ✅       |
| Edge     | chromium core | ✅       |
| Safari   | current       | ✅       |
| FireFox  | current       | ⚠️      |



Notes:
- This application is developed on macOS platform, and tested on MS Windows 10 and Ubuntu 22.04. macOS and linux platforms have higher support priority, and deploying this project using the Windows platform may encounter some unpredictable problems. These problems come from compatibility issues with dependent packages and systems, so although this project has tried its best to avoid compatibility issues, it cannot completely fix such problems.

- The webUI is developed on Chrome browser, and tested on MS Edge (chromium core) and Apple safari.

- Some functionalities of this application rely on a general purpose computing framework, and we tested CPU and Nvidia CUDA framework, but AMD ROCm and other framework may also work well.

- For the architecture, only amd64 (x86_64) and Apple Silicon (arm64) is tested, other architectures may also work well.

### **Compatibility on low-resolution devices**
This application is designed for the devices that the resolution is higher than 1080p (width is higher than 1920px). If you are planed to use this application on low-resolution devices, you may found some compatibility issues. You can use browser's resize (scale) method to resize the webUI, main-stream web browsers (chrome, safari, edge, firefox) both support this feature. 

For Windows and UNIX users:
```shell
Ctrl and + to zoom in, Ctrl and - to zoom out
```
For macOS users:
```shell
Command and + to zoom in, Command and - to zoom out
```


# **Deployment Guide**
Please follow this deployment guide to configure the environment and start the application.
## **Environment Information**
### 1.Virtual Environment Manager
It is recommended to use a virtual environment and use conda as the manager. This guide will use conda as the environment management tool.

If you decide to use conda, make sure only use conda to install packages. DO NOT use conda and pip at the same time, this will cause inaccessible dependency conflicts.

### 2.Packages
This project uses Python and the following packages are needed (if you do not need LLM feature, then you only need to install the basic dependencies):
- Basic dependencies
    * flask=2.2.2
    * numpy=1.26.9
    * pandas=2.1.1
    * scikit-learn=1.3.0 (conda-forge)
    * xgboost=2.0.3 (conda-forge)
    * lightgbm=4.1.0
    * mapie=0.8.2 (conda-forge)
    * joblib=1.2.0
    * weasyprint=61.2 (conda-forge) (macOS and Linux only!)
    * pdfkit=1.0.0 (pip) (Windows only!)
- Advanced dependencies
    * torch=1.13.1
    * transformers=4.37.1 (conda-forge)
- Unit-Test dependencies
    * pytest=8.1.1 (conda-forge)

Please note that the requirements.txt and environment.yml is only for development purpose and macOS x86_64 only.


# Create and setup virtual environment:
First create a new env.
```shell
conda create --name AVM python=3.9
```
You can use other python version, but python 3.9 is recommended and pre-tested.

And activate conda env by:
```shell
conda activate AVM
```

# Install packages
Same version and source channel is recommended and pre-tested. The following commands only for basic user (exclude torch and transformers).

## For UNIX (macOS and Linux) users
Use the following commands to complete the installation of all dependencies:
```shell
conda install flask=2.2.2 pandas=2.1.1
conda install scikit-learn=1.3.0 xgboost=2.0.3 lightgbm=4.1.0 mapie=0.8.2 joblib=1.2.0 weasyprint=61.2 -c conda-forge
```

## For Windows users
### 1. Install wkhtmltopdf
#### 1.1. Setup wkhtmltopdf
You should download and install this tool before setup python related dependencies.
Simply download exe file from [website](https://wkhtmltopdf.org/downloads.html), and install.

#### 1.2. Setup system path
Add wkhtmltopdf installed path to your system path. If it was installed with default settings, the path should be:
```shell
C:\Program Files\wkhtmltopdf\bin  # Replace with your path
```
### 2. Install other packages
Use the following commands to complete the installation of python related dependencies:
```shell
conda install flask=2.2.2 pandas=2.1.1
conda install scikit-learn=1.3.0 xgboost=2.0.3 lightgbm=4.1.0 mapie=0.8.2 joblib=1.2.0 -c conda-forge
python -m pip install pdfkit==1.0.0
```


# **Before Start App**
### 1. Check object files
In versions 4.0 and newer, object files have been added to mainline tracking, so **no** additional configuration is required.\
You can check object files in following directory:
```shell
model/object/rev311
NLGen/class
```

### 2. Config working folders
In versions 4.0 and newer, the working folder will be automatically configured and checked by the program, so you **do not need to configure it manually**.

### 3. Check Import
In versions 4.0 and newer, the program will **automatically** check the import of all dependent packages. If there are missing dependencies, an exception prompt will be provided in the terminal, and the program will exit automatically. If you encounter such problems, please follow the prompts to check the dependency installation.

### 4. Set host and port
The host and port is set as local (127.0.0.1:5000) as default. If you want to deploy this software to real server, you must change the host and port settings in the last line of __app.py__.

For general purpose, set host to "0.0.0.0" and port to "80" (http) or port "443" (https).\
Here is the example:
```python
app.run(debug=False) # default setting
app.run(host="0.0.0.0", port=80, debug=False) # http setting
```

## **Start app**
The start point of this application is _app.py_. 
Make sure conda env is activated:
```shell
conda activate AVM # replace AVM to your env name.
```
Assuming you are in the root directory, use this command to start the app:
```shell
cd Interface
python app.py
```
**DO NOT** directly start app in root directory:
```shell
python Interface/app.py # DO NOT directly start app in root directory
```

If the dependencies and project configuration are normal, it has been successfully started.



## Troubleshooting

[Troubleshooting](Troubleshooting.md)



