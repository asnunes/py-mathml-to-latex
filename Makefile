.PHONY: test build clean publish docker-test

# Run tests using pytest
test:
	python -m unittest discover tests

# Build the package (wheel and source distribution)
build:
	python -m build

# Clean build artifacts
clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/

# Publish the package to PyPI
publish: build
	twine upload dist/*

# Run tests inside Docker
docker-test:
	docker build -t mathml-to-latex-test .
	docker run --rm mathml-to-latex-test
