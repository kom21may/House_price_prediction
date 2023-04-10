## END to END ML Project 
### created a environment

```
conda create -p house_ppp python==3.8
```
### activate conda

```
conda activate (copy path of created env)
```

### Install all necessary libraries

```
pip install -r requirements.txt

```

### setup.py

```
setup.py to craete this project as package use setup.py
```
### -e . is used to share all the libraries from requirements.txt tosetup.py but for install we have to ignore -e .

### run setup.py 

```
python setup.py install

```