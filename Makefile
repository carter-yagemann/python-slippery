help:
	@echo "  env      install all production dependencies"
	@echo "  dev      install all dev and production dependencies"
	@echo "  docs     build documentation"
	@echo "  test     run tests"
	@echo "  tor      run tests including proxy test (socks5://localhost:9050)"
	@echo "  lint     check style of source code"
	@echo "  clean    remove the intermediate python files"

env:
	pip install -Ur requirements.txt

dev: env
	pip install -Ur requirements.testing.txt
	pip install -Ur requirements.docs.txt

info:
	@python --version
	@pip --version

docs:
	$(MAKE) -C doc html

lint:
	pylint slippery/*.py examples/*.py

test: lint
	py.test

tor: lint
	py.test --tor-test=1

clean:
	find . -name '*.pyc' -exec rm -f {} \;
	find . -name '*.pyo' -exec rm -f {} \;	
