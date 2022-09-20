# xayah
A lightweight testing tool with test report functionality

## Table of contents
* [General info](#general-info)
* [Installation](#installation)
* [Features](#Features)
* [Documentation](#Documentation)
* [Usage](#usage)
* [Telegram bot example](#Telegram bot example)
* [Future work](#Future work)

## General info
Xayah is used to test and generate report for 
python applications.  It is built to combine
a testing tool with test report functionality. 
It allows testing modules and generate a test 
report in JSON format  

test suite example:
```
from xayah import TestSuite, TestResult

def add(a, b):
  return a + b

@TestSuite.init
class TestAdd:
  def test_add(self):
     assert add(2, 3) == 5

# generating a test report
TestAdd.run_test_cases()
report = TestResult().create_test_result()
```

## Installation
Xayah is available on PyPI:
```commandline
python -m pip install xayah
```

## Documentation
Xayah's documentation can be found in readthedocs: 
https://xayah.readthedocs.io/en/latest/

## Features
* adding title, description, severity levels, etc.
* test parametrization
* steps
* skipping tests
* generating test report

## Usage
In order to generate report, the test class should be
decorated with TestSuite.init method:
```
@TestSuite.init
class CheckTestCase:
    def test_method(self):
        assert 1 == 1
```

then all test method (with test prefix) of the 
tested class can be executed by calling
run_test_cases method:
```
CheckTestCase.run_test_cases()
```

in order to created test result
TestResult().create_test_result() method should
be called:
```
result = TestResult().create_test_result()
```
then test result can be parsed in any format

## Telegram bot example
Originally, xayah was built as a test report 
tool for telegram bots.

Here you can see the simple usage 
in telegram bot with selenium:
```
from aiogram import Bot, Dispatcher, executor, types
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from xayah import TestResult, TestSuite, TestCase

API_TOKEN = 'BOT TOKEN HERE'

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@TestSuite.init
@TestSuite.title('Google main page')
class TestGoogle:
    @TestCase.title('page title is Google')
    def test_google(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get('https://www.google.com/')
        assert driver.title == 'Google', 'title is not google'


@dp.message_handler(commands=['test'])
async def test(message: types.Message):
    webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    TestGoogle.run_test_cases()
    result = TestResult().create_test_result()
    test_suite = result.get(TestGoogle.__name__)
    test_suite_title = test_suite.get('title')
    test_case = test_suite.get('test_cases')[0]
    test_case_title = test_case.get('title')
    test_case_status = test_case.get('status')
    text = f'<pre><b>{test_suite_title}:</b></pre>\n  <pre>{test_case_title} - {test_case_status}</pre>'
    await message.reply(text, parse_mode=types.ParseMode.HTML)
    
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
```

telegram bot's response:
```
Google main page:
  
page title is Google - passed
```

## Future Work
Planned features:
- Console application
- Running xayah tests through console application
- JSON generation
- HTML page generation from the test report
- PDF page generation from the test report
- Integration with pytest
- Making telegram bot integration easier

