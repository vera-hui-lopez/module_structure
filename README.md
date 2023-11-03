# Tensor Calculator

Tensor calculator and other operations 

## Table of Contents

- [Introduction](#Introduction)
- [Features](#Features)
- [Usage](#usage)


## Introduction

Creation of tensors + operations made inside of a Class: "TensorCalculator". 

## Features

- Create a tensor of Zeros
- Create a tensor of Ones
- Create a tensor of random numbers
- Sum two tensors
- Multiply tensors
- Normalize (0,1) of a tensor
- Average of a tensor
- Max of a tensor
- Min of a tensor

### Prerequisites

- Python >=3.9
- Pytorch

### Installation

1. Clone the repository:

   git clone  https://github.com/vera-hui-lopez/module_structure.git

## Usage
from TensorCalculator import TensorCalculator

# Creation of tensors
tensor_a = TensorCalculator.tensor_zeros(3, 4, 2)
tensor_b = TensorCalculator.tensor_ones(3, 4, 2)

# Example of an operation
result_sum = TensorCalculator.tensor_sum(tensor_a, tensor_b)
result_mult = TensorCalculator.tensor_mult(tensor_a, tensor_b)
