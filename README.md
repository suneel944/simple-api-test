# Simple API Testing Repo
A simple api testing repo demonstrating the ease of api testing using python, uplink

## Features
- Easy to understand code
- Github CI integration
- Dockerised

## Running the test
- Install python version >=3.11
- Install dependencies
    ```
    pipenv shell # to create a new virtual environment for the project
    pipenv install -r ./requirements/requirements.txt # installing requirements from the requirements.txt file
    pipenv activate # to activate the shell
    ```
- When trying to run, the below tests using allure-service you might encounter permission denied error, to resolve that:
    ```
    sudo chmod 777 allure-reports
    sudo chmod 777 allure-results
    ```

- To run the test, use the below commands
    ```
    # parallel mode
    pytest -n <number_of_parallel_threads> <relative_.py_test_file_path>
    -or-
    # normal mode
    pytest <relative_.py_test_file_path>
    -or-
    pytest <relative_.py_test_file_path>::<specific_method_that_required to be run>
    # want to generate report along with it
    pytest <relative_.py_test_file_path>::<specific_method_that_required to be run> --alluredir=allure-results
    -or-
    pytest <relative_.py_test_file_path> --alluredir=allure-results
    -or-
    pytest -n <number_of_parallel_threads> <relative_.py_test_file_path> --alluredir=allure-results
    -or- pytest -n <number_of_parallel_threads> --alluredir=allure-results
    ```