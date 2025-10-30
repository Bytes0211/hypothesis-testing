# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- LICENSE file (MIT License)
- CONTRIBUTING.md with contribution guidelines
- CHANGELOG.md to track project history
- setup.py for proper package installation
- Comprehensive .gitignore patterns
- Full dependency list in requirements.txt

### Changed
- Renamed `03_one_two_tail_test_diff_props.ipynb` to `03-one-two-tail-test-diff-props.ipynb` for consistency
- Updated README.md with corrected notebook references
- Enhanced Makefile clean target to handle notebook checkpoints
- Moved unrelated utility files (aws.py, backup.py, etc.) to utilities/ folder
- Improved project structure and organization

### Fixed
- requirements.txt now includes all necessary dependencies (numpy, pandas, bokeh, scipy, matplotlib, seaborn, statsmodels, jupyter, ipython)
- Grammar and factual corrections in notebook 02 (one-two-tail-test-diff-mean.ipynb)
- Makefile syntax for clean target

## [1.0.0] - 2025-10-29

### Added
- Initial release with 5 comprehensive notebooks:
  - 01-intro-to-pvalue.ipynb - P-value fundamentals
  - 02-one-two-tail-test-diff-mean.ipynb - Testing means
  - 03-one-two-tail-test-diff-props.ipynb - Testing proportions
  - 04-chi-squared.ipynb - Chi-squared tests
  - 05-regression-hypothesis.ipynb - Regression testing
- Resources module with datum.py, test.py, glyph.py, plot.py
- Sample datasets (cod_population.csv, salmon_population.csv)
- Comprehensive README.md with project documentation
- Makefile for environment setup and management
- Interactive Bokeh visualizations throughout notebooks

### Features
- Complete hypothesis testing framework
- Visual learning with distribution plots
- Practical examples with real-world datasets
- Step-by-step explanations of statistical concepts
- Custom test framework for programmatic hypothesis testing
