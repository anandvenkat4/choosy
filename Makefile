# Makefile for utility work on Choosy

.PHONY: clean test

default:
	@echo "* No default action *"

clean:
	-rm -rf build dist htmlcov server/htmlcov
	-rm -f *.pyc */*.pyc */*/*.pyc */*/*/*.pyc */*/*/*/*.pyc */*/*/*/*/*.pyc
	-rm -f *.pyo */*.pyo */*/*.pyo */*/*/*.pyo */*/*/*/*.pyo */*/*/*/*/*.pyo
	-rm -f *.bak */*.bak */*/*.bak */*/*/*.bak */*/*/*/*.bak */*/*/*/*/*.bak
	-rm -f *$$py.class */*$$py.class */*/*$$py.class */*/*/*$$py.class */*/*/*/*$$py.class */*/*/*/*/*$$py.class
	-rm -rf __pycache__ */__pycache__ */*/__pycache__ */*/*/__pycache__ */*/*/*/__pycache__ */*/*/*/*/__pycache__
	-rm -f MANIFEST
	-rm -f .coverage .coverage.* coverage.xml server/.coverage
	-rm -f setuptools-*.egg distribute-*.egg distribute-*.tar.gz

test:
	@echo "use 'manage.py test' in the server directory."
