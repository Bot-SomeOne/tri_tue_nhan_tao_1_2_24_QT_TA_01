.PHONY: run clear_cache clear_venv create_venv

help: 
	@echo "make run - run dfs"
	@echo "make clear_cache - clear cache when running"
	@echo "make clear_venv - clear pkg and ... venv python"
	@echo "make create_venv - create venv python"

run:
	python -m src.main

clear_cache:
	rm -rf **/__pycache__/

clear_venv:
	rm -rf bin/
	rm -rf include/
	rm -rf lib/
	rm -rf pyvenv.cfg

create_venv:
	python3 -m venv .
	bin/pip install -r requirements.txt