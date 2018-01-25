## Synopsis

The **Paint Calculator** is a hypothetical project that calculates how many gallons of paint would be required to paint a number of rooms.

## Requirements

* Python 3 (not 2)
* Pip

## What we're looking for

* Install Python / Pip
* Run application
* Write tests against the application. They do not have to be in Python, and should be in whatever language you are most comfortable with.
* Write a test plan for the application.  You are free to determine the structure and length of the test plan.
* You are allowed to change any of the source code as you see fit to make things easier for yourself. You are encouraged to fix any bugs you discover.
* Explain any problems you had while writing the tests, and what you did to make it easier. Pointing to localhost for the application is OK.
* What would be the proper level of execution for tests of this application?  If this differs from the testing level you wrote tests for, please explain where they would be better suited.

## Instructions

Because each applicant's code should be secret from one another, we should not submit it to the same repo.

1. Clone the repo (do not fork)
2. Create a new public repo on Github
3. Add the new repo as as a new remote
* `git remote add uptake <url>`
4. Initialize the new repo with what is cloned
* `git push uptake master`
5. Create a new branch off of master to put your changes on
6. Run the application locally
* `pip3 install -r requirements.txt`
* `python3 app/run.py`
7. Perform testing and debugging activities

## Submitting 

To make it easier on everybody, it's best if we use a PR to diff what work was completed.

1. Make any and all commits to your new branch and push the changes
* `git push uptake <branch>`
2. Create a PR to your new repo
3. Make sure you include your test plan and any automated tests, as well as update this README to instruct someone on how to run the tests
4. Include any other text in a file - which tests would be suited for a different level of execution, or any problems encountered...etc
5. Send the link to the PR

## Running Tests

Tests can be run by: `python -m unittest`
Note that the app needs to be running in another process with the default server location `http://127.0.0.1:5000/`

### Test plan:
The application lacked tests on all levels of the stack, every layer of the stack is important to cover

I decided to implement the following types of tests:

#### Unit tests
A simple set of tests that verify functionality

#### Functional tests
A data driven test suite that can verify corner scenarios and different combination of inputs for all of the main pieces of code within the app

#### Integration tests
A simple test that verifies that a given workflow that uses various functions is working properly

#### E2E tests
Black box implementation of a workflow that exercises the UI of the application

I will add comments to each code change and addition below.

### The proper level of execution:

Unit tests should be executed after every local code change, also on PRs and Deployments

Functional tests should be executed before PRs and Deployments

Integration tests should be ran after Deployment into any internal environment (sandboxes, staging etc)

E2E tests should be executed after every Deployment (Possibly a subset) and on a programmed set of intervals i.e. Every night at 11pm.



