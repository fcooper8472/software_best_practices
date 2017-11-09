---
title: Continuous integration
layout: page
---

# Continuous integration

# Hyrum's Law

>With a sufficient number of users of an API, it does not matter what you promise in the contract, all observable behaviors of your system will be depended on by somebody.

How can we make sure that the code we write carries on working over time?

Who here has written a script, only to come back next time you need it and find it no longer works?

Unit testing is great, but relies on you occasionally running the unit tests!

## Why would we need to keep running unit tests?

* You subtly change the behaviour of part of your script
* You forget that you relied on the length of your vector being a power of 2

Changes you make to your function might affect behaviour in a way that:
* You had forgotten would cause problems
* You didn't anticipate

## Do I have to remember to keep running my tests?

No.

> Continuous Integration (CI) is the process of automating the build and testing of code every time a team member commits changes to version control.

* [Travis CI](travis-ci.org)
* Jenkins
* Circle CI
* [Buildbot](https://chaste.cs.ox.ac.uk/buildbot/)

## Travis

* Integrates directly with GitHub
* Hosted elsewhere - no setup required on your machine
* Minutes to set up
* Free for open source projects

#### >> Demo of Travis integration for this repo

#### >> Demo of Buildbot integration for Chaste

___
[<< back](https://fcooper8472.github.io/software_best_practices/#outline)
