# Field State Classification

#### How to make use of the repository?

Step 1: Install the package by running ```pip install git+https://github.com/Davit98/fscpy.git```

Step 2: Create a folder named *data/* and populate it by running ```aws s3 cp --recursive s3://intelinair-internship/field_state_classification/  . --no-sign-request```

Step 3: Import and run *write_blocks_to_disk()* from the module *data_processing.py*

#### Training a model
Use the function *train()* from the module *train.py* to train a ResNet-18 model:
```
from fscpy.train import train
train(epochs=5,batch_size=32)
```

#### Testing
1. First, it is necessary to download the weights of my trained ResNet-18 model (trained for 2 epochs, reached 65.703% accuracy on the validation data) from the following [link](https://www.dropbox.com/sh/jqubx0rir3s4g61/AAA4PodOOvT4s2Qdh1-YvvyLa?dl=0).
2. Afterwards, use the function *test()* from the module *inference.py*. Example:
```
from fscpy import inference
inference.test('model.pt','1TJZT39WQ_0_test.npy')
```
