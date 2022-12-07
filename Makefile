check:
	black --check tp_db tests
	isort --check-only tp_db tests
	mypy tp_db tests
	flake8 --count
	pylint tp_db tests

.PHONY: check
