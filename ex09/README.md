# ft_package

A sample Python package for data science training, demonstrating package building and distribution.

## Description

`ft_package` is a lightweight utility package created as part of the Python for Data Science curriculum. It provides basic sequence utility functions, such as counting item occurrences within a list.

## Installation

You can install the package using `pip` from the built wheel or source distribution in the `dist/` directory:

```bash
# Install from Wheel
pip install dist/ft_package-0.0.1-py3-none-any.whl

# Or install from Source Distribution
pip install dist/ft_package-0.0.1.tar.gz
```

## Usage

```python
from ft_package import count_in_list

# Count occurrences of an item in a list
print(count_in_list(["toto", "tata", "toto"], "toto"))  # Output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu"))  # Output: 0
```

## License
MIT License
