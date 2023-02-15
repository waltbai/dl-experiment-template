# 神经网络模型的模版

将 ``package_name`` 改为你的项目名

## 安装

通过以下指令安装：

```bash 
pip install .
```

## 实验环境与预测环境
实验环境此处指：模型在基准数据集上运行。此时模型仅处理训练、验证、测试数据集。
通常来说，这些数据集都包含标注（或者至少验证和测试数据集是有标注的）。此外，中
间处理结果可以保存为文件，仅需要处理一次。运行时的目录也相对固定。

预测环境指：模型在无标注数据上运行。此时模型往往已经训练好，对训练集的中间处理
结果就不需要了，但是模型需要具备在内存中将未处理的数据处理为模型输入的能力。此
外，模型应当在任意目录下都能够导入。

以下为两者的基本区别：

|       | 实验环境 | 测试环境 |
|-------|:----:|:----:|
| 数据标注  |  有   |  无   |
| 中间结果  |  文件  |  内存  |
| 训练    |  有   |  无   |
| 运行时目录 |  固定  |  任意  |
| 打包    |  无   |  有   |

本模板主要针对实验环境使用而设计。然而本模板仍然提供了一些额外的特性。例如，尽管
本模板并未实现测试环境所用的方法，但是预留了相应的一些接口；特定目录可以通过配置
文件指定，而非完全固定；模型可以打包并安装。

## 参数设置
参数传入优先级为：
```命令行 > 配置文件 > 默认配置 ```

由于使用``yacs``包，命令行参数传入的风格应当遵循该包的要求。

默认配置由``config/default.yml``设置。每个模型各自独有的默认配置由各自代码中定
义。其他配置文件将会重写默认配置。

## 处理模块Processor
在实验环境中，处理模块往往也需要处理训练数据，例如进行负采样等。这些数据往往只需
要处理一次。因此需要一个可以处理出各种中间结果的处理模块，即使它较重，也是可以接
受的。

然而，在预测环境中，处理模块仅需要将未处理的数据处理为模型可接收的数据格式，因此
需要额外实现一个相对轻量级的处理模块。

## 模型Model
模型聚焦于神经网络结构设计。这里推荐继承基础模型类``BasicModel``。开发者应当重写
``__init__``和``forward``方法。其风格如下：

```python
from package_name.model import AbstractModel


class MyModel(AbstractModel):
    """特定模型."""

    def __init__(self,
                 anything_specific_to_this_model,
                 **kwargs):
        super(MyModel, self).__init__(**kwargs)
        ...  # 参数和网络定义

    def forward(self,
                any_input_data):
        """模型推断方法."""
        ...  # 推断流程
```

``predict`` 是在测试环境下用于从未处理数据预测结果的方法。在实验环境下，该方法可
被忽略，无需重写。

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
