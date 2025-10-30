# Contributing to Hypothesis Testing

Thank you for your interest in contributing to this project! This document provides guidelines for contributing.

## How to Contribute

### Reporting Issues

If you find a bug or have a suggestion:
1. Check if the issue already exists in the issue tracker
2. Create a new issue with a clear title and description
3. Include relevant code examples or error messages
4. Specify which notebook or module is affected

### Submitting Changes

1. **Fork the Repository**
   ```bash
   git clone https://github.com/your-username/hypothesis-testing.git
   cd hypothesis-testing
   ```

2. **Create a Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Set Up Development Environment**
   ```bash
   make setup
   source .venv/bin/activate  # or your venv name
   ```

4. **Make Your Changes**
   - Follow existing code style and conventions
   - Add comments where necessary
   - Update documentation as needed

5. **Test Your Changes**
   - Run all notebooks to ensure they execute without errors
   - Verify visualizations render correctly
   - Check for any broken links in markdown

6. **Commit Your Changes**
   ```bash
   git add .
   git commit -m "Brief description of changes"
   ```

7. **Push and Create Pull Request**
   ```bash
   git push origin feature/your-feature-name
   ```

## Style Guidelines

### Notebook Style

- Use clear, descriptive headings
- Include explanatory text before code cells
- Add comments in complex code sections
- Ensure all formulas render correctly in markdown
- Test visualizations with sample data

### Code Style

- Follow PEP 8 style guidelines for Python code
- Use meaningful variable names
- Keep functions focused and modular
- Add docstrings to functions and classes

### Documentation

- Use proper grammar and punctuation
- Be concise but thorough
- Include examples where helpful
- Update README.md if adding new notebooks or features

## Adding New Notebooks

When adding a new notebook:

1. Follow the naming convention: `##-descriptive-name.ipynb`
2. Include these sections:
   - Title and objective
   - Theoretical background
   - Formulas with LaTeX
   - Practical examples with visualizations
   - Interpretation of results
3. Update README.md with notebook description
4. Ensure all dependencies are in requirements.txt

## Testing

Before submitting:
- Run `make clean` to remove artifacts
- Restart kernel and run all cells in order
- Verify all outputs display correctly
- Check that no sensitive data is included

## Questions?

Feel free to open an issue for any questions about contributing!

## Code of Conduct

- Be respectful and constructive
- Focus on what is best for the project
- Show empathy towards other contributors
- Accept constructive criticism gracefully

Thank you for contributing! 🎉
