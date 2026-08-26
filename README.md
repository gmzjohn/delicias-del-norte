# Delicias del Norte

## Project description

Delicias del Norte is a centralized platform designed to digitize and automate the core business logic of a restaurant. It acts as the operational backbone of the establishment, bridging the gap between customer orders and kitchen execution.

## Project scope

The project encompasses a comprehensive kitchen simulation system where customers place orders that are managed via a processing queue.

## Project Stack

- **Language**: Python 3

## Project Setup

To set up and run the project locally:

**Clone the repository**:

```bash
git clone https://github.com/gmzjohn/delicias-del-norte.git
cd delicias-del-norte
```

## Formatter Rules

**Select explanation**

  E   =  pycodestyle errors: bare except E722, imports-not-at-top E402, line length E501, etc.
  W   =  pycodestyle warnings: trailing whitespace W291/W293, missing newline at EOF W292, etc.
  F   =  Pyflakes: undefined names, unused imports/vars, redefinitions, duplicate/wildcard imports
  I   =  isort: import sorting + stdlib/third-party/local grouping
  UP  =  pyupgrade: flags outdated language constructs
  B   =  flake8-bugbear: no-effect/useless expressions (B018), likely bugs
  A   =  flake8-builtins: shadowing builtin names
  ARG =  flake8-unused-arguments: unused function/method arguments
  N   =  pep8-naming: naming convention consistency
  BLE =  flake8-blind-except: catching bare/overly-broad exceptions
  SIM =  flake8-simplify: redundant/needlessly complex code
  RUF =  Ruff-specific rules, including RUF100 (flags stale/unnecessary noqa)

**Ignore explanation**
  E111 = indentation-with-invalid-multiple: conflicts with `ruff format`
  E114 = indentation-with-invalid-multiple-comment: conflicts with `ruff format`
  E117 = over-indented: conflicts with `ruff format`
  W191 = tab-indentation: moot since we don't use tabs, kept for documentation/safety
