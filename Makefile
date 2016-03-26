ENV = $(CURDIR)/env
PYTHON = $(ENV)/bin/python3
PIP = $(ENV)/bin/pip3
TMPDIR = $(CURDIR)/tmp

$(ENV):	clean
	@virtualenv $(ENV) --python=/usr/bin/python3
	@$(PIP) install -r requirements.txt

test: 
	${PYTHON} -m testtools.run discover indexgen.tests

clean:
	rm -rf $(ENV)
	rm -rf $(TMPDIR)
	find -name '*.pyc' -delete
	find -name '*.~*' -delete

.PHONY: test clean
