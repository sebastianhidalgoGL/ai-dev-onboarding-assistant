.PHONY: install run test clean

install:
	pip install -e .

run:
	streamlit run src/index.py

test:
	pytest

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info 