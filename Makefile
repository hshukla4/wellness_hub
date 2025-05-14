install:
	pip install -e .

run:
	python app/planner.py

test:
	pytest tests/

lint:
	black . && flake8 .

clean:
	rm -rf __pycache__ .pytest_cache *.pyc

check-pip-upgrade:
	@echo "🔍 Checking if pip is outdated..."
	@pip list --outdated | grep '^pip' || echo "✅ pip is up to date"
