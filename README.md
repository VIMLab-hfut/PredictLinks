# SEAL for link prediction

SEAL, a link prediction framework based on [GNN](https://github.com/XuSShuai/GNN_tensorflow).

## 1 - About

This repository is a reference implementation of SEAL proposed in the paper: 

## 2 - Version

 - python 3.5.5</br>
 - **networkx 2.0**</br>
 - tensorflow 1.7.0</br>
 - numpy 1.14.2</br>

## 3 - Basic Usage

#### 3.1 - Example

Type the following command to run `seal` on data 'USAir'.

```python
python main.py
```

#### 3.2 - Option

 - `python main.py --data Celegans` to run `SEAL` on data `Celegans`
 - `python main.py --epoch 200` will assign the number of epochs to 200, default value is 100
 - `python main.py -r 0.00001` will set the learning rate which determine the speed of update parameters to 0.00001.

you can check out the other options available to use `python main.py --help`
