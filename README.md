# xayah
A lightweight testing tool with test report functionality

## Table of contents
* [General info](#general-info)
* [Installation](#installation)
* [Usage](#usage)

## General info
Xayah is used to test and generate report for 
python application. 
## Installation

Xayah is available on PyPI:
```commandline
python -m pip install xayah
```

## Usage
In order to generate report the test class should be
decorated with TestSuite.init
```python
@TestSuite.init
class CheckTestCase:
    def test_method(self):
        assert 1 == 1
```

then all test method (with test prefix) of the 
tested class can be executed by calling
run_test_cases method
```
CheckTestCase.run_test_cases()
```

in order to created test result