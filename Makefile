# Makefile

install:
	poetry install

brain-calc:
	poetry run python brain_games/scripts/brain_games_script.py brain-calc

brain-even:
	poetry run python brain_games/scripts/brain_games_script.py brain-even

brain-gcd:
	poetry run python brain_games/scripts/brain_games_script.py brain-gcd

brain-prime:
	poetry run python brain_games/scripts/brain_games_script.py brain-prime

brain-progression:
	poetry run python brain_games/scripts/brain_games_script.py brain-progression

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install dist/*.whl

lint:
	poetry run flake8 brain_games