# Template for Neural Network Models

Change ``package_name`` to your own module name.

## Install

Install this package via:

```bash 
pip install .
```

## Experiment and Prediction Environments
Experiment environment is the situation where model runs on benchmark
datasets. In this situation, model obtains train, dev, and test datasets.
Usually, all the datasets are labeled (or at least dev and test set are
labeled). Furthermore, the intermediate results can be restored on the
disk, and the data will only be processed once. The runtime directories
are usually fixed.

On the other hand, Prediction environment is the situation where model
runs on unlabeled raw data. Usually the models are seen as well-trained
tools to process data. The intermediate training data may not be needed,
but the model need to process the raw data into the tensors in memory.
In addition, the model will be possible to be imported to any directory.

Here is the basic difference of the two:

|                      | Experiment Env | Prediction Env |
|----------------------|:--------------:|:--------------:|
| labeled data         |      Yes       |       No       |
| intermediate results |    On disk     |   In memory    |
| Train                |      Yes       |       No       |
| Runtime Directory    |     Fixed      |   Arbitrary    |
| Package              |       No       |      Yes       |

This template is mainly designed for experiment environment usage. However,
we still want to provide some additional features. For example, though we
haven't implemented the methods for prediction environment, we provide 
some basic interface; The directory can be assigned by config file rather
than totally fixed; The model is packaged and can be installed.

## Arguments
Argument override follows such priority:
```command line > config file > default config ```

Here, we restrict command line arguments to two: 
``--config [config]`` and ``--device [device]``

Default settings for all models are in ``config/default.yml``.
Any other config file will override it.

## Preprocessor
In experiment environment, preprocessor usually requires to handle training 
data, such as generating negative training samples. In addition, usually the
data only need to be processed once. Thus, a heavy preprocessor which 
produces many intermediate results is acceptable.

However, for a model in production environment, it should be able to
process raw data and output results immediately. Thus, a light preprocessor
should be implemented.

## Model
Model concentrates on the neural network architecture design. It is
recommended to inherit the basic model class ``BasicModel``. Developers
should define the ``__init__`` and ``forward`` methods for it. The 
implemention should be like:

```python
from package_name.model import AbstractModel


class MyModel(AbstractModel):
    """A specific model."""

    def __init__(self,
                 anything_specific_to_this_model,
                 **kwargs):
        super(MyModel, self).__init__(**kwargs)
        ...  # Parameters and network design

    def forward(self,
                any_input_data):
        """Forward method for model."""
        ...  # Inference
```

``predict`` method is used for predicting on raw data. However, it can be
ignored if developers just want to run model in experiment environment.

## Dataset
The dataset is used to make batched inputs for model. It converts list/dict
to aligned tensors. ``DatasetCollection`` is a special type of dataset, which
load slices one-by-one, since the whole dataset is not able to load once.
Basically it is similar with the torch Dataset class.

## Trainer
In experiment environment, the trainer controls the whole processing steps.
Basically it should contain following steps:
- Preprocess (sampling, indexing, etc.)
  - input: ``data_dir`` for raw data
  - output: ``preprocess_dir`` for processed data
- Train (usually with validate)
  - input: ``preprocess_dir`` for train and dev data
  - output: ``model_dir`` for checkpoints
- Continue training
  - input: ``preprocess_dir`` for train and dev data, ``model_dir`` for checkpoints
  - output: ``model_dir`` for checkpoints
- Test
  - input: ``preprocess_dir`` for test data
  - output: ``result_dir`` for results
