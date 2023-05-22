# CodeEurope 2023

## Python: Code Quality - Assignment

In this assignment you'll get to check out the tools shown during the talk. You can find some code in `src` directory. It's of questionable quality. Please make sure it passes CI build.

### Prerequisites

- Python [^3.10](https://www.python.org/downloads/).
- Poetry [link](https://python-poetry.org/docs/).

```sh
curl -sSL https://install.python-poetry.org | python3 -
```

### Cheat sheet

```sh
poetry init                                 # Creates a basic pyproject.toml file in the current directory.
poetry config virtualenvs.in-project true   # Create the virtualenv inside the project’s root directory.
poetry install                              # Installs the project dependencies.
poetry add                                  # Adds required packages to your pyproject.toml and installs them.
poetry remove                               # Removes a package from the current list of installed packages.
poetry env info                             # Displays information about the current environment.
poetry shell                                # Spawns a shell within the virtual environment.
poetry show --tree                          # Shows information about packages.
poetry lock                                 # Compiles the dependencies in the poetry.lock file.
```

Add libraries:

```sh
poetry add -G dev flake8 isort black mypy pre-commit pytest
```

Run `pre-commit`:

```sh
poetry run pre-commit install -c .pre-commit-config.yml
poetry run pre-commit run -a -c .github/hooks/.pre-commit-config.yml
```
