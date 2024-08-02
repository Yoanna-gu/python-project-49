install:
	poetry install
brain-games:
	poetry run brain-games
brain-even:
	poetry run first_game
brain-calc:
	poetry run calc_game
brain-gcd:
	poetry run brain_gcd
brain-prog:
	poetry run brain_progression
brain-prime:
	poetry run brain_prime
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --user --force-reinstall dist/*.whl
make lint:
	poetry run flake8 brain_games
patch:
	poetry install
	poetry version patch
	poetry build
	poetry publish --dry-run
	python3 -m pip install --user dist/*.whl