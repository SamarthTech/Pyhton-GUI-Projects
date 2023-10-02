PACKAGE_NAME = GUIWttrTextualApp

.PHONY: all help lint format run

all: help

help: ## Show this help
	@echo 'Usage: make COMMAND'
	@echo
	@echo "Commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'

lint: ## Run black, pylint and flake8
	black --check main.py
	pylint main.py
	flake8 main.py

format: ## Format the Python code using black
	black main.py

run:
	python3 main.py	