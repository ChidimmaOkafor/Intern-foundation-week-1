# Refactoring Notes

## Overview

This document explains the improvements made to the Week 2 programming exercises as part of the Week 3 refactoring task.

## Exercises Reviewed

* Simple Calculator
* Number Checker
* Student Grade Checker
* Shopping List
* User Profile Object
* File Reader and Writer
* Basic Error Handling
* Mini Feature

## Improvements Made

### 1. Improved Variable Names

Unclear variable names were replaced with more descriptive names to improve readability and maintainability.

Example:

* `x` → `studentScore`
* `n` → `userName`

### 2. Reduced Duplicate Code

Repeated logic was extracted into reusable functions where appropriate.

Benefits:

* Easier maintenance
* Reduced code duplication
* Improved readability

### 3. Replaced Hardcoded Values

Frequently used fixed values were stored in constants.

Example:

* Pass mark values
* Default configuration values

### 4. Improved Formatting

Code formatting was standardized by:

* Using consistent indentation
* Adding appropriate spacing
* Organizing code into logical sections

### 5. Removed Unnecessary Comments

Comments that simply repeated what the code already explained were removed.

Meaningful comments were retained where they helped explain important logic.

### 6. Improved Code Organization

Functions and related logic were grouped together to make files easier to navigate and maintain.

## Testing

All exercises were tested after refactoring to ensure functionality remained unchanged.

Result: All programs executed successfully and produced the expected output.

## Outcome

The codebase is now easier to read, maintain, review, and extend while preserving the original functionality.
