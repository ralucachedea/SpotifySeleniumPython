
# Spotify automation framework

This is a repository containing a sample readme file

# Description

This repository contains a robust automation framework built using Python and Selenium. The framework is designed to automate Spotify web application efficiently and follows best practices in automation testing.


 
## Table of contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Project Structure](#projectstructure)
- [Running Tests](#runningtests)
- [Contributing](#contributing)


## **Features**


- Page Object Model (POM) implementation
- Data-driven testing with CSV/JSON/Excel support
- Cross-browser testing support
- Logging and reporting with pytest-html
- CI/CD integration support



## **Prerequisites**
Before you can start performing **Python** automation testing with **Selenium**, you would need to:

* Install the latest Python build from the [official website](https://www.python.org/downloads/). We recommend using the latest version.
* Make sure **pip** is installed in your system. You can install **pip** from [here](https://pip.pypa.io/en/stable/installation/).
* Download the latest **Selenium Client** and its **WebDriver bindings** from the [official website](https://www.selenium.dev/downloads/). Latest versions of **Selenium Client** and **WebDriver** are ideal for running your automation script on LambdaTest Selenium cloud grid.

  
## **Installation**

1. Clone the repository:
```
git clone https://github.com/ralucachedea/SpotifySeleniumPython.git
cd SpotifySeleniumPython
```
2. Create a virtual environment (optional but recommended):
```
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```
3. Install dependencies:
```
pip install -r requirements.txt
```


## **Project Structure**
```
SpotifySeleniumPythonPytest/
    │── configuration/   # Configuration files (URLs, credentials, etc.)
    │── ExcelFiles/      # Data-driven testing
    │── pages/           # Page Object Model (POM) classes
    │── Reports/         # Test reports
    │── tests/           # Test cases
    │── utilities/       # Utility functions (e.g., data handling, logging)
    │── requirements.txt # Required dependencies
```

## **Running Tests**

To execute test cases, use:
```
pytest --html=reports/report.html --self-contained-html
```
To run tests in parallel:
```
pytest -n 4 --html=reports/report.html
```


## **Reporting**
After execution, test reports will be available in the reports/ directory as an .json files.


## **Contributing**

1. Fork the repository.
2. Create a feature branch (git checkout -b feature-branch).
3. Commit your changes (git commit -m 'Add new feature').
4. Push to the branch (git push origin feature-branch).
5. Open a Pull Request.


