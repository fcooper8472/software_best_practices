---
title: Unit testing
layout: page
---

# Unit testing

> A software testing method by which individual units of source code ... are tested to determine whether they are fit for use.

## A little bit of Python

Let's write a little bit of Python to set the scene:

 * A simple module called `maths_custom_functions.py`
 * Module currently has two functions

```python
def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n - 1)
```

```python
def is_perfect_number(n):

    if n < 0:
        raise ValueError("The number %s is negative!" % n)

    if n in [6, 28, 496, 8128, 33550336, 8589869056, 137438691328, 2305843008139952128]:
        return True
    return False
```

These may be simple functions, but the code we write is not always completely straightforward.

Often uncaught sources of error can include:
* Copy'n'paste errors
* Edge cases not properly considered
* Human error
* Last minute changes!

We write code to support the science we are doing, whether that is:
* Occasional script to post-process data
* Scripts to plot graphs
* Small stochastic simulations
* Full-blown software development

We have a duty to ensure results obtained from the scripts we write are:
* Correct!

## Software often splits naturally into units

* Functions
* Classes
* Modules

As a general rule, functions should express a single simple concept.
Functions may be chained together to express more complicated control flows.

If every function is simple, and we can verify it is correct, and takes proper account of edge cases, then our scripts that chain multiple functions together stand a much better chance of being fit for use.

Unit testing is the practice of ensuring each function is correct.

* Almost all languages have well-used unit testing frameworks
* Python:
  * [unittest module](https://docs.python.org/2/library/unittest.html)
* C++:
  * [google test](https://github.com/google/googletest)
  * [catch](https://github.com/catchorg/Catch2)
* Matlab:
  * [I've not tried this...](http://uk.mathworks.com/help/matlab/matlab-unit-test-framework.html?requestedDomain=uk.mathworks.com)

#### >> Demo of how to unit-test the python example

___
[<< back](https://fcooper8472.github.io/software_best_practices/#outline)
