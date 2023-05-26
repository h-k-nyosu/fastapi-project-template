.PHONY: install run test

# install dependencies
install:
	poetry install

# run the FastAPI application
run:
	poetry run uvicorn app.main:app --reload

# run the test suite
test:
	poetry run pytest app/tests
