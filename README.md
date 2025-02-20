# Deep Learning Experiment Template

This is a template for deep learning experiments,
especially adapted to llama-factory.

## Requirements

- python==3.11
- llama-factory>=0.9.1

## Usage

Create a virtual environment:

```shell
conda create -n experiment-template python=3.11
```

Install dependency:  

```shell
pip install -r requirements.txt
```

## Implementations

### `config/`

Directory to store configuration files for each experimental settings and hyper-parameters.

### `scripts/`

Directory to store scripts for running experiments.

Suggest to use `python -m module` to run source code.

### `src/`

Directory to store source codes for experiments.

### `tests/`

Directory to store unit test codes.

### Suggestions

It's ***highly recommended*** to design unit test cases for important data processing classes and functions!

## Citations

Place the bib file of corresponding paper here.
