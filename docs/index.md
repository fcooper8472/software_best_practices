[![Build Status](https://travis-ci.org/fcooper8472/software_best_practices.svg?branch=master)](https://travis-ci.org/fcooper8472/software_best_practices)

# Outline
 - Version control
 - GitHub
 - Unit tests
 - Continuous integration

# Version control

 > Version control is a system that records changes to a file or set of files over time so that you can recall specific versions later.

There is no reason to keep any code, software, script, LaTeX file, or website anywhere other than in a version control repository.

There are several version control systems in common use:
 * Git
 * Subversion
 * Mercurial
 * ...

but, in reality, git has pretty much won the argument.

## What is Git

 * info here


# GitHub

GitHub is a site for hosting and allowing access to git repositories.  It's:
 * Free
 * Popular
 * Has great student perks
 * Has many popular integrations

# A little bit of Python

Let's write a little bit of Python to set the scene:

 * A simple module called `maths_custom_functions.py`

```python
def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n - 1)
```