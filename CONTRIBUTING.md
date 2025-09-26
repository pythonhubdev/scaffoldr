# Contributing to Scaffoldr

Hello Developers! 👋🏻

Thank you for spending your valuable time to contribute to **Scaffoldr**. All PRs, contributions, reviews, and
suggestions are welcome. Please follow the guidelines below to contribute to this project.

## 🐛 Creating an Issue

Please follow the issue template while creating an issue. If you are creating an issue, follow the below templates:

1. **For Bugs
   ** - [Bug Template](https://github.com/pythonhubdev/scaffoldr/blob/main/.github/ISSUE_TEMPLATE/bug_report.md)
2. **For Feature Requests
   ** - [Feature Template](https://github.com/pythonhubdev/scaffoldr/blob/main/.github/ISSUE_TEMPLATE/feature_request.md)

You can also use the custom template to create an issue if the above templates don't match your needs.

## 🛠️ Development Setup

### Prerequisites

- Python 3.13+
- [Task](https://taskfile.dev/) (optional but recommended for automated commands)
- Git

### Quick Setup

1. **Fork and Clone**
   ```bash
   # Fork the repository on GitHub, then clone your fork
   git clone git@github.com:<your-username>/scaffoldr.git
   cd scaffoldr
   ```

2. **One-shot Setup** (Recommended)
   ```bash
   # This will install uv, sync dependencies, set up venv, and install pre-commit hooks
   task setup
   ```

3. **Manual Setup** (Alternative)
   ```bash
   # Install uv if not present (macOS/Linux)
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # For Windows
   # powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

   # Sync dependencies
   uv sync --all-extras

   # Install pre-commit hooks
   uv run pre-commit install
   ```

### 🏃‍♂️ Development Workflow

1. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
	- Follow the existing code style and patterns
	- Add tests for new functionality
	- Update documentation if needed

3. **Run quality checks**
   ```bash
   # Run all linters and formatters
   task lint

   # Run tests
   task test

   # Run pre-commit hooks
   task pre-commit
   ```

4. **Commit your changes**
   ```bash
   git add .
   git commit -m "feat: add amazing new feature"
   ```

5. **Push and create PR**
   ```bash
   git push origin feature/your-feature-name
   ```

## 🧪 Testing

- **Run all tests**: `task test`
- **Run unit tests only**: `task test-u`
- **Run with coverage**: Tests automatically generate coverage reports in `htmlcov/`

## 📏 Code Style

We use modern Python tooling for code quality:

- **Formatting**: `ruff format`
- **Linting**: `ruff check`
- **Type Checking**: `mypy` and `pyright`
- **Pre-commit hooks**: Automatic formatting and validation

### Style Guidelines

1. **Follow PEP 8** and use type hints
2. **Write docstrings** for public functions and classes
3. **Keep functions small** and focused
4. **Use meaningful variable names**
5. **Add tests** for new functionality

## 🚀 Adding New Framework Support

When adding support for a new framework (e.g., Litestar, BlackSheep):

1. Create a new template directory: `templates/{framework_name}/`
2. Add framework-specific templates and configurations
3. Update the CLI to include the new framework option
4. Add comprehensive tests
5. Update documentation

## 📋 Available Tasks

```bash
task setup          # Complete project bootstrap
task deps           # Sync dependencies
task lint           # Run linters and formatters
task test           # Run tests with coverage
task test-u         # Run unit tests only
task pre-commit     # Run pre-commit hooks
task pycache        # Remove Python cache files
task ds-store       # Remove .DS_Store files
```

## 🔄 Creating a Pull Request

1. **Ensure all checks pass**
	- All tests pass (`task test`)
	- Linting passes (`task lint`)
	- Pre-commit hooks pass (`task pre-commit`)

2. **Write a clear PR description**
	- Describe what your PR does
	- Reference any related issues
	- Include screenshots if UI changes are involved

3. **Use conventional commit messages**
   ```
   feat: add support for Litestar framework
   fix: resolve template generation issue
   docs: update installation instructions
   test: add unit tests for CLI commands
   ```

## 🎯 What We're Looking For

- **New Framework Support**: Help us add more Python web frameworks
- **Template Improvements**: Better project structures and configurations
- **Documentation**: Improve guides, examples, and API docs
- **Bug Fixes**: Fix issues reported by the community
- **Performance**: Make the CLI faster and more efficient
- **Testing**: Increase test coverage and add integration tests

## ❓ Questions?

- **General Questions**: Open a [Discussion](https://github.com/pythonhubdev/scaffoldr/discussions)
- **Bug Reports**: Create an [Issue](https://github.com/pythonhubdev/scaffoldr/issues)
- **Feature Requests**: Create
  a [Feature Request](https://github.com/pythonhubdev/scaffoldr/issues/new?template=feature_request.md)

## 📜 Code of Conduct

Please note that this project is released with a [Contributor Code of Conduct](CODE_OF_CONDUCT.md). By participating in
this project, you agree to abide by its terms.

---

Thank you for contributing to Scaffoldr! 🎉

1. Fork the repository
2. Create a branch from the `main`
3. Please have a proper name for the branch like **feature or a bug** related to what you are working on
4. Once completed raise a PR and add a reviewer
5. Once reviewed the PR will be merged

Please provide necessary changes or update if mentioned by a reviewer also stick to
the [CODE_OF_CONDUCT.md](https://github.com/pythonhubdev/PyNotion/blob/main/CODE_OF_CONDUCT.md) while adding review
comments or while answering review comments.
