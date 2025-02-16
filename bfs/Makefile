
# help command:
# make help
help:
	@echo "make help - Show this help"
	@echo "make run - Run the main program"
	@echo "make test [name_file_test] - Run the test with the given name"
	@echo "make getEnvironmentPythons - Get all pkg pip and write to `requirements.txt`"
	@echo "make install - Install all pkg pip from `requirements.txt`"
	@echo "make clear_cache - Clear the cache python files"
# test command:
# make test [file_name]
test:
	@echo "Running test: $(file_name)"
	python -m src.test.$(file_name)

# run command:
# make run
run:
	@echo "Running main program"
	python -m src.main

# getEnvironmentPythons command:
# make getEnvironmentPythons
getEnvironmentPythons:
	@echo "Getting all pkg pip and write to requirements.txt"
	pip freeze > requirements.txt

# install command:
# make install
install:
	@echo "Installing all pkg pip from requirements.txt"
	pip install -r requirements.txt

# clear_cache command:
# make clear_cache
clear_cache:
	@echo "Clearing the cache python files"
	find . -name "*.pyc" -exec rm -f {} \;
	find . -name "__pycache__" -exec rm -rf {} \;
	find . -name ".DS_Store" -exec rm -f {} \;