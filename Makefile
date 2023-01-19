.PHONY: help install resume clean

BOOK_PATH=resume
JB=poetry run jupyter-book
INDEX_FILE=$(BOOK_PATH)/_build/html/index.html

help:
	@echo "Please use 'make <target>' where <target> is one of:"
	@echo "  install     to install the necessary dependencies for jupyter-book to build"
	@echo "  resume      to build the html and pdf output"
	@echo "  runall      to run all notebooks in-place, capturing outputs with the notebook"

install:
	poetry install

clean:
	$(JB) clean --all $(BOOK_PATH)

resume:
	$(JB) build $(BOOK_PATH) --builder html

open:
	open $(INDEX_FILE)

