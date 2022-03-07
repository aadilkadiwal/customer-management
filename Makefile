.PHONY: run deps migrate sh
FILENAME := .appname
APPNAME := `cat $(FILENAME)`

# target: run - Runs a dev server on localhost:8000
run:
	manage runserver

# target: deps - install dependencies from requirements file
deps:
	pip install -r requirements.txt
	pip install -e .		

# target: migrate - migrate the database
migrate:
	manage migrate

# target: sh - open django extension's shell plus
sh:
	manage shell_plus
