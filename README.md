# python-modern-example

An opinionated example for modern Python projects using best-in-class tooling.

## Features

- 📦 [uv](https://github.com/astral-sh/uv) for blazingly fast package management
  and virtual environments and python version management
- ✨ [Ruff](https://github.com/astral-sh/ruff) for comprehensive linting and
  formatting, configured with:
  - Google-style docstring enforcement
  - Type annotation checking
  - Security checks via Bandit rules
  - Import sorting
  - And more!
- 🔍 [Pyright](https://github.com/microsoft/pyright) in strict mode for robust
  static type checking
- 🏃 Pre-configured VS Code development environment extension recommendations
  for the tools
- 🔧 Task runner with [Just](https://github.com/casey/just) for streamlined
  development

## Getting Started

1. Clone this repository:
   ```bash
   git clone https://github.com/zenion/python-modern-example.git
   cd python-modern-example
   ```
2. Install uv: `curl -LsSf https://astral.sh/uv/install.sh | sh`
3. Install [Just](https://github.com/casey/just): `uv tool install rust-just`

## Development

### Available Commands

Use the following commands via `just`:

- `just check` - Run all checks and test (lint-check, format-check, type-check,
  and tests)
- `just lint-check` - Run Ruff linting check
- `just lint-fix` - Fix linting issues with Ruff
- `just format-check` - Check code formatting with Ruff
- `just format` - Format code with Ruff
- `just type-check` - Run Pyright type checking
- `just test` - Run tests

### VS Code Integration

This template includes recommended VS Code extensions for the best development
experience:

- Python language support and debugging
- Ruff for linting and formatting
- Pyright/Pylance for type checking
- Additional helpful extensions for TOML, YAML, and more

### Project Structure
