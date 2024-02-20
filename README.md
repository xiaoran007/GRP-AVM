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
- **Transformers**
- **Model optimize**
    * classifier + regressor

## **Environment**
### Packages
This project uses Python and the following packages are needed:
* torch
* transformers
* numpy
* pandas
* scikit-learn
* flask

For other dependent packages, see Requirements.txt.

### Virtual Environment
It is recommended to use a virtual environment and use conda as the manager.

Create a virtual environment:
```shell
conda create --name AVM python=3.9
```
Then install the packages, if you have Nvidia GPU, you need to install Nvidia CUDA toolkits first and then install torch-cuda version.

transformers can run on CPU mode or GPU mode (pytorch backend or tensorflow backend), if you have Nvidia GPU, GPU mode with pytorch backend is recommended. Install Pytorch and then install transformers with conda:
```shell
conda install pytorch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2 pytorch-cuda=11.7 -c pytorch -c nvidia
conda install transformers -c conda-forge
```
Please note, you need first install the Nvidia CUDA toolkits, and then install compatible Pytorch, you can find more information from the [Pytorch website](https://pytorch.org/get-started/previous-versions/).
## **Object Files**
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

Please note that pre-trained object files are not stored in this repository.

Object files should locate in:
```shell
./model/object # model object files (RF_Full.mdo) 
./NLGen/class # class object files (class_avg_Full.mdo and kmeans_model_full.mdo)
```