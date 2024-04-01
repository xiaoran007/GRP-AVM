## Issues

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

via pip: (recommended)
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


## If you do not need advanced features, you can skip step 3.1.
##### 3.1 Setup transformers and pytorch with CUDA
if you have Nvidia GPU, you need to install Nvidia CUDA toolkits first and then install torch-cuda version.

Transformers can run on CPU mode or GPU mode (pytorch backend or tensorflow backend), if you have Nvidia GPU, GPU mode with pytorch backend is recommended. Install Pytorch and then install transformers with conda:
```shell
conda install pytorch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2 pytorch-cuda=11.7 -c pytorch -c nvidia
conda install transformers -c conda-forge
```
Above commands will install cuda-runtime inside conda env, it is enough for torch usage, but if you want to compile or build your own cuda program, you need install the Nvidia CUDA toolkits and cudnn.\
You can find more information from the [Pytorch website](https://pytorch.org/get-started/previous-versions/) and [Nvidia website](https://www.nvidia.com/en-us/)