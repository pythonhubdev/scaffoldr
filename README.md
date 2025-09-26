# Scaffoldr

> Previously this package was known as `faag-cli` now renamed to `scaffoldr`.

**Modern Python web framework project generator with production-ready architecture.**

Scaffoldr is a CLI tool designed to help developers quickly set up and manage project structures, configurations, and boilerplate code for modern Python web frameworks. It automates the initial setup process, allowing developers to focus on writing code rather than spending time on repetitive tasks.

[![Python 3.13+](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

## ✨ Features

- 🚀 **Multiple Framework Support**: FastAPI, Flask, Litestar, BlackSheep, Robyn (coming soon)
- 🏗️ **Production-Ready Architecture**: Feature-driven design with clear separation of concerns
- 📦 **Modern Tooling**: Built with `uv` package manager, `ruff` for linting, and `typer` for CLI
- 🔧 **Automated Setup**: Pre-configured development environment with testing, linting, and pre-commit hooks
- 📝 **Best Practices**: Follows industry standards and patterns for maintainable code
- 🎯 **Extensible**: Easy to add new frameworks and customize generated projects

## 📋 Requirements

- **Python 3.13+**
- **uv** package manager (will be installed automatically if not present)

## 🚀 Quick Start

### Installation

```bash
# Install from PyPI (coming soon)
pip install scaffoldr

# Or install with uv
uv add scaffoldr

# Or install from source
git clone https://github.com/pythonhubdev/scaffoldr.git
cd scaffoldr
uv sync
```

### Usage

```bash
# Generate a new FastAPI project (default)
scaffoldr generate my-api

# Generate with specific framework
scaffoldr generate my-api --framework fastapi
scaffoldr generate my-flask-app --framework flask

# Generate with additional options
scaffoldr generate my-project --framework fastapi --database postgres --auth jwt

# Get help
scaffoldr --help
scaffoldr generate --help
```

## 🏗️ Supported Frameworks

| Framework | Status | Description |
|-----------|--------|-------------|
| **FastAPI** | ✅ Available | Modern, high-performance web framework |
| **Flask** | 🚧 Coming Soon | Lightweight and flexible web framework |
| **Litestar** | 🚧 Planned | High-performance ASGI web framework |
| **BlackSheep** | 🚧 Planned | Fast ASGI web framework |
| **Robyn** | 🚧 Planned | Rust-powered Python web framework |

## 📁 Generated Project Structure

Scaffoldr generates projects with a clean, scalable architecture:

```
my-project/
├── src/
│   └── backend/
│       ├── api/                # API layer configuration
│       ├── core/               # Core components (config, utils, etc.)
│       ├── features/           # Feature modules (business logic)
│       ├── services/           # External service integrations
│       └── database/           # Data access layer
├── tests/                      # Comprehensive test suite
├── scripts/                    # Development scripts
├── .github/                    # GitHub workflows and templates
├── pyproject.toml              # Project configuration
├── Taskfile.yaml              # Task automation
└── README.md                   # Project documentation
```

## 🛠️ Development

### Prerequisites

- Python 3.13+
- [Task](https://taskfile.dev/) (optional, for automated commands)

### Setup

```bash
# Clone the repository
git clone https://github.com/pythonhubdev/scaffoldr.git
cd scaffoldr

# One-shot setup (installs uv, syncs deps, sets up pre-commit)
task setup

# Or manually:
# Install uv if not present
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies
uv sync --all-extras

# Install pre-commit hooks
uv run pre-commit install
```

### Available Commands

```bash
# Development
task setup          # Complete project bootstrap
task deps           # Sync dependencies
task pre-commit     # Run pre-commit hooks

# Code Quality
task lint           # Run linters and formatters
task test           # Run tests with coverage
task test-u         # Run unit tests only

# Cleanup
task pycache        # Remove Python cache files
task ds-store       # Remove .DS_Store files
```

### Project Philosophy

Scaffoldr follows these principles:

1. **Developer Experience First**: Minimize setup time, maximize productivity
2. **Modern Tooling**: Use the best tools available in the Python ecosystem
3. **Production Ready**: Generated projects should be deployment-ready
4. **Extensible**: Easy to add new frameworks and customize templates
5. **Community Driven**: Built for and by the Python community

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### Quick Contribution Steps

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes
4. Run tests: `task test`
5. Run linting: `task lint`
6. Commit your changes: `git commit -m 'Add amazing feature'`
7. Push to the branch: `git push origin feature/amazing-feature`
8. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [Typer](https://typer.tiangolo.com/) for the CLI interface
- Uses [uv](https://github.com/astral-sh/uv) for fast Python package management
- Code quality maintained with [Ruff](https://github.com/astral-sh/ruff)

## 📞 Support

- 🐛 [Report Issues](https://github.com/pythonhubdev/scaffoldr/issues)
- 💡 [Request Features](https://github.com/pythonhubdev/scaffoldr/issues/new?template=feature_request.md)
- 📖 [Documentation](https://github.com/pythonhubdev/scaffoldr/wiki)

---

**Scaffoldr** - *Building better Python projects, faster.*
