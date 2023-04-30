# 0x07. Python - Test-driven development
<code>Python</code> <code>UnitTest</code> <code>PDD</code>

## Learning Objectives
At the end of this project, you are expected to be able to [explain to anyone](https://intranet.alxswe.com/rltoken/tYtzLvssHW_9zR6SZQlNrQ), **without the help of Google**:

### General
* Why Python programming is awesome
* What’s an interactive test
* Why tests are important
* How to write Docstrings to create tests
* How to write documentation for each module and function
* What are the basic option flags to create tests
* How to find edge cases

## Requirements

### Python Scripts
* Allowed editors: vi, vim, emacs
* All your files will be interpreted/compiled on Ubuntu 20.04  LTS using python3 (version 3.9)
* All your files should end with a new line
* The first line of all your files should be exactly #!/usr/bin/python3
* A README.md file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle (version 2.8.*)
* All your files must be executable
* The length of your files will be tested using wc

### Python Test Cases
* Allowed editors: vi, vim, emacs
* All your files should end with a new line
* All your test files should be inside a folder tests
* All your test files should be text files (extension: .txt)
* All your tests should be executed by using this command: python3 -m doctest ./tests/*
* All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
* All your functions should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)')
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
*We strongly encourage you to work together on test cases, so that you don’t miss any edge case – The Checker is checking for tests!

## Tasks :page_with_curl:

* **0. Integers addition**
  * [0-add_integer.py](./0-add_integer.py): Python function that returns the integer addition
  of two numbers.
  * If either of `a` or `b` is not an `int` or `float`, a `TypeError` is raised
  with the message `a must be an integer` or `b must be an integer`.
  * If either of `a` or `b` is a `float`, it is casted to an `int`
  before addition.

