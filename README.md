# **This is Main repo for AVM Project.** <img src="https://raw.githubusercontent.com/aemmadi/aemmadi/master/wave.gif" width="30">



[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&pause=1000&color=F7B769&width=435&lines=We+are+GRP-Team13)](https://git.io/typing-svg)

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&pause=1000&color=F7B769&width=435&lines=Automated+Valuation+Model)](https://git.io/typing-svg)

<span > 
    <img src="https://img.shields.io/badge/Python-_3.9-blue"  alt="py39"/> 
    <img src="https://img.shields.io/badge/Tensorflow-_2.10-g"  alt="torch"/> 
    <img src="https://img.shields.io/badge/Flask-_2.2.2-g"  alt="flask"/> 
</span>

<img src="./markdown/img/teamlogo.png" width="23%" height="23%" alt="team13"/>

***

## **TODO**
- **Document**
- **Test**

## **working branch**
- **MaterialUIKit**
- **pytest-ut**

## Dev tips
- transformers model is saved in local mode, but do not track with git.
- transformers package version 4.37.1

## **OS and Platform Support**
This application is website based, since web server usually uses Unix system, this application only macOS and Linux is officially supported. The following is detailed OS and Platform support matrix. 

| OS      | Version           | Architecture  | Support |
|---------|-------------------|---------------|---------|
| macOS   | Big Sur and later | x86_64, arm64 | ✅       |
| Linux   | Ubuntu 20.04      | x86_64        | ✅       |
| Windows | 10                | x86_64        | ⚠️      |

This application is developed on macOS platform, and tested on MS Windows 10 and Ubuntu 22.04.

The webUI is developed on Chrome browser, and tested on MS Edge (chromium core) and Apple safari.

Some functionalities of this application rely on a general purpose computing framework, and we tested CPU and Nvidia CUDA framework, but AMD ROCm and other framework may also work well.

For the architecture, only amd64 (x86_64) and Apple Silicon (arm64) is tested, other architectures may also work well.


## **The support for Windows is added**
In current version, we added support for windows. Now you can use Windows to run this application. But still need to install some extra packages. Please follow the steps below to complete the configuration.

### 1. Setup wkhtmltopdf
You should download and install this tool before setup python related dependencies.
Simply download exe file from [website](https://wkhtmltopdf.org/downloads.html), and install.

### 2. Setup system path
Add wkhtmltopdf installed path to your system path. If it was installed with default settings, the path should be:
```shell
C:\Program Files\wkhtmltopdf\bin
```

### 3. Setup python-pdfkit
Download python-pdfkit from pip or conda (conda-forge channel). Inside conda env!!

via pip:
```shell
python -m pip install pdfkit
```
or via conda:
```shell
conda install python-pdfkit=1.0.0 -c conda-forge
```

Then you can start this application on Windows.



## **Compatibility problem on Windows platform**
This is a website project. Usually the website server uses Unix (Linux or BSD) system, so you will not encounter the compatibility issues described below. If you plan to use Windows as the server deployment platform, please read the following content carefully.

Please note, Windows platform is not officially supported by this project, but we still provide some limited supports.

The pdf generator depends on weasyprint package, it can be very easily installed by conda on Unix (macOS and Linux) platform, but needs much more work on Windows platform. In fact, some dependencies of weasyprint, for example gtk-3, fontconfig, pango, trying to install them on Windows platform is a very complicated process.

You should first follow conda env setup guide and finish all other dependencies installation process.

Following steps, If you're lucky, it will work.

### 1. Setup gtk-3 runtime on your machine
You need to install gtk-3 runtime, but the gtk project website only provide very simple guide for installing the gtk development environment on Windows. In fact, you only need to install gtk runtime, and there is an unofficial exe package available on [GitHub](https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases)

Download, and run it, do not change any settings.

### 2. Setup fontconfig
Use conda to install fontconfig, make sure use conda-forge channel rather than conda official channel.
```shell
conda search fontconfig -c conda-forge
conda install fontconfig=2.14.2 -c conda-forge
```

### 3. Setup weasyprint
Use pip to install weasyprint and other dependencies. You MUST inside conda env, but DO NOT use conda to install this package!!!
```shell
python -m pip install weasyprint
```
Then you can check:
```shell
python -m weasyprint --info
```
If no errors are reported, the installation process is successfully completed.

### 4. Issues
Although no errors when directly check the weasyprint, various compatibility issues will still be encountered in actual use. These issues are not the concern of this project and therefore will not be resolved in the future.


## **Compatibility on low-resolution devices**
This application is designed for the devices that the resolution is higher than 1080p (width is higher than 1920px). If you are planed to use this application on low-resolution devices, you may found some compatibility issues. You can use browser's resize (scale) method to resize the webUI, main-stream web browsers (chrome, safari, edge, firefox) both support this feature. 

For Windows and UNIX users:
```shell
Ctrl and + to zoom in, Ctrl and - to zoom out
```
For macOS users:
```shell
Command and + to zoom in, Command and - to zoom out
```


## **Fix Import Error**
If you try to start this application in command line by this command:
```shell
python app.py
```
you may found some import errors (package not found), to fix it, you need add package path to import search path
in app.py before all other import lines:
```python
import sys
sys.path.append('../')
sys.path.append('./')
```
then you can start application.

Current main and MaterialUIKit branch already fixed this issue.


## **Environment**
### Packages
This project uses Python and the following packages are needed:
* torch=1.13.1
* transformers (conda-forge)
* numpy=1.26.9
* pandas=2.1.1
* scikit-learn=1.3.0 (conda-forge)
* xgboost=2.0.3 (conda-forge)
* lightgbm=4.1.0
* flask=2.2.2
* mapie=0.8.2 (conda-forge)
* joblib=1.2.0
* weasyprint=61.2 (conda-forge) (macOS and Linux only!)
* pdfkit=1.0.0 (pip) (Windows only!)

For other dependent packages, see requirements.txt and environment.yml (macOS x86_64 only).

### Packages for Unit test
* pytest=8.1.1 (conda-forge)

### Virtual Environment
It is recommended to use a virtual environment and use conda as the manager.

If you decide to use conda, make sure only use conda to install packages.

Create a virtual environment:
```shell
conda create --name AVM python=3.9
```
You can use other python version, but python 3.9 is recommended and pre-tested.

Then install the packages, if you have Nvidia GPU, you need to install Nvidia CUDA toolkits first and then install torch-cuda version.

Transformers can run on CPU mode or GPU mode (pytorch backend or tensorflow backend), if you have Nvidia GPU, GPU mode with pytorch backend is recommended. Install Pytorch and then install transformers with conda:
```shell
conda install pytorch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2 pytorch-cuda=11.7 -c pytorch -c nvidia
conda install transformers -c conda-forge
```
Please note, you need first install the Nvidia CUDA toolkits, and then install compatible Pytorch, you can find more information from the [Pytorch website](https://pytorch.org/get-started/previous-versions/).

Some packages need install from conda-forge channel, use following command:
```shell
conda install "package-name" -c conda-forge
```

To install bootstrap-flask (optional)
```shell
conda install pip -c conda-forge
python -m pip install bootstrap-flask
```

## **Object Files**
We packaged our model as object file, which can be load or dump by joblib library.

Please note that pre-trained object files are not stored in this repository.

Object files should locate in:
```shell
./model/object # model object files (RF_Full.mdo) 
./NLGen/class # class object files (class_avg_Full.mdo and kmeans_model_full.mdo)
```

If you are interested in create your own model object file, follow this:

Create:

```python
import joblib

joblib.dump(object, "path")
```

Load and use:
```python
import joblib

my_object = joblib.load("path")
```

## **LLM Model Files**
For more details, see huggingface website.