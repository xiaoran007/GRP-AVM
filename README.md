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
* matplotlib
* flask
* joblib

### Virtual Environment
It is recommended to use a virtual environment and use conda as the manager.

Create a virtual environment:
```shell
conda create --name AVM python=3.9
```
Then install the packages, if you have Nvidia GPU, you need to install Nvidia CUDA toolkits first and then install torch-cuda version.

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