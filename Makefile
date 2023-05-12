.PHONY: install test tox build install-package clean pre-commit-install pre-commit help

# Install pipenv
install-pipenv:
	pip install pipenv

# Activate shell
activate-shell:
	pipenv shell

# Install dependencies
install:
	pipenv install --dev

# Clean up
clean:
	pipenv --rm
	rm -rf .pytest_cache
	rm -rf .tox
	rm -rf dist
	rm -rf build
	rm -rf .mypy_cache
	rm -rf *.egg-info
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete

# Install pre-commit hooks
pre-commit-install:
	pipenv run pre-commit install

# Run pre-commit hooks
pre-commit:
	pipenv run pre-commit run --all-files

help:
	@echo "Available targets:"
	@echo "  install-pipenv         Install pipenv"
	@echo "  activate-shell         Activate pipenv shell"
	@echo "  install                Install dependencies"
	@echo "  clean                  Clean up"
	@echo "  pre-commit-install     Install pre-commit hooks"
	@echo "  pre-commit             Run pre-commit hooks"
	@echo "  help                   Show this help message"