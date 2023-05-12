![Build](https://github.com/suneel944/simple-api-test/actions/workflows/tests.yml/badge.svg)

# Simple API Testing Repo
A simple api testing repo demonstrating the ease of api testing using python, uplink

## Features
- Easy to understand code
- Github CI integration
- Dockerised

## Prepping the project
- [Install python](https://www.python.org/downloads/)
- [Install pip](https://pip.pypa.io/en/stable/installation/)
- [Install Docker](https://docs.docker.com/engine/install/)
- [Install Docker Compose](https://docs.docker.com.zh.xy2401.com/v17.12/compose/install/)
- Install any IDE of your choice
    - [Vscode](https://code.visualstudio.com/)
    - [Pycharm](https://www.jetbrains.com/pycharm/)
- Install project dependencies
    ```
    # to create a new virtual environment for the project
    pipenv shell
    # installing requirements from the 
    pipenv install -r ./requirements/requirements.txt  requirements.txt file
    # to activate the shell
    pipenv activate
    ```
- To set up the auto formatting prior to code commit run the code once during set up
    ```
    pipenv run pre-commit install
    ```

## Setting up the docker suite
- Build the project image using below command
    ```
    docker build -t python_test/simple-api-test:latest -f Dockerfile .
    ```
- Invoke the allure-docker-service
    ```
    docker compose up -d
    -or-
    docker compose up -d --build
    ```
## Running the test
- When trying to run, the below tests using allure-service you might encounter permission denied error, to resolve that:
    ```
    sudo chmod 777 allure-reports
    sudo chmod 777 allure-results
    ```
- If you are thinking where the report would be getting stored, it will be stored in the **allure-reports** directory with in the project root
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
    -or- 
    pytest -n <number_of_parallel_threads> --alluredir=allure-results
    ```
