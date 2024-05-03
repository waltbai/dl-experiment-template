# Neural Network-based Experiment Template
This is a template for neural network-based experiments.

## Requirements
- python==3.10
- torch==2.2
- transformers==4.40
- datasets>=2.19
- llama_factory>=0.7.0
- tqdm

## Usage
Create a virtual environment:
```shell
conda create -n experiment-template python=3.10
```

Install dependency:  
```shell
pip install -r requirements.txt
```

Run unit test:
```shell
chmod +x scripts/unittest.sh
scripts/unittest.sh
```

Run prepare:
```shell
chmod +x scripts/prepare.sh
scripts/prepare.sh
```

Run train:
```shell
chmod +x scripts/train.sh
scripts/train.sh
```

Run evaluate:
```shell
chmod +x scripts/evaluate.sh
scripts/evaluate.sh
```

Run test:
```shell
chmod +x scripts/test.sh
scripts/test.sh
```

## Extensions
### Project Structure
```
root
|-- src					      # Store source codes
  |-- exp_1			      # Codes for each experiment settings
    |-- workflow.py   # Overall workflow control
    |-- prepare.py    # Prepare data
    |-- train.py      # Train model on train and valid sets
    |-- inference.py  # Evaluate on valid and test sets
  |-- utils				    # Utility classes and functions
|-- scripts				    # Store command line scripts
  |-- unittest.sh     # Scripts to run unit tests
  |-- train.sh        # Scripts to run train on train and valid sets
  |-- evaluate.sh     # Scripts to run evaluation on valid set
  |-- test.sh         # Scripts to run evaluation on test set
|-- config				    # Store config files
|-- tests   			    # Store unit test cases
|-- requirements.txt		# List python requirements
```

### Guide
1. Add folders in `src/` if the experiment contains multiple model variants.
2. It's ***highly recommended*** to design unit test cases for important preparation classes and functions!
