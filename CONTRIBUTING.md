# Contributing to Simple PMM

Thank you for your interest in contributing to Simple PMM! This document provides guidelines for contributing to the project.

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/waffleflayer/simple-pmm.git
   cd simple-pmm
   ```
3. **Install dependencies**:
   ```bash
   python setup.py
   ```

## Development Setup

1. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   ```

2. **Install development dependencies**:
   ```bash
   pip install -r requirements.txt
   pip install pytest flake8 black
   ```

3. **Run tests**:
   ```bash
   python health_check.py
   ```

## Making Changes

1. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following these guidelines:
   - Follow PEP 8 style guidelines
   - Add type hints where appropriate
   - Include docstrings for new functions
   - Update configuration examples if needed

3. **Test your changes**:
   - Run the health check: `python health_check.py`
   - Test with Docker: `docker-compose up --build`
   - Verify Windows compatibility

4. **Commit your changes**:
   ```bash
   git add .
   git commit -m "feat: add your feature description"
   ```

## Pull Request Process

1. **Update documentation** if needed
2. **Ensure all tests pass**
3. **Update the README** if you've added features
4. **Submit a pull request** with:
   - Clear description of changes
   - Any breaking changes noted
   - Testing steps performed

## Code Style

- Use **PEP 8** formatting
- Maximum line length: 88 characters
- Use type hints for function parameters and returns
- Include comprehensive docstrings

## Reporting Issues

When reporting issues, please include:
- Operating system and version
- Python version
- Docker version (if applicable)
- Steps to reproduce
- Expected vs actual behavior
- Relevant log output

## Feature Requests

We welcome feature requests! Please:
- Check existing issues first
- Provide clear use case description
- Consider Windows Surface compatibility
- Suggest implementation approach if possible

## Questions?

Feel free to open an issue for any questions about contributing!
