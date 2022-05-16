# Bugs4Q Version-1.0.0

A benchmark for Quantum Programs

## Contents of B.M.4Q

### Qiskit Programs


| Bug Type  | Number of Bugs | Bug Ids |
| --- | --- | --- |
| Output Wrong | 16 | 5,7,8,10,11,12,14,16,17,21,25,26,27,29,31,39 |
| Throw Exception | 17 | 1,2,3,6,13,15,18,19,20,24,28,35,36,37,38,40,42 |
| Simulation Failed | 2 | 4,41  |
| Complex Output | 5 | 22,23,30,32,34 |
| Command Wrong | 1 | 9 |
| SyntaxError | 1 | 33 |
| Total | 42 | --- |

### Bugs
Each bug has the following properties:
* Issue filed in the corresponding issue tracker, and issue tracker identifier mentioned in the fixing commit message.
* Fixed in a single commit.
* Fixed by modifying the source code (as opposed to configuration files, documentation, or test files).
* A triggering test exists that failed before the fix and passes after the fix -- the test failure is not random or dependent on test execution order.

## Setting up Bugs4Q

### Requirements

* python 3.7
* git >= 1.9
* qiskit (The latest version is recommended)

### Steps to set up Bugs4Q
- Clone Bugs4Q
  ```
  git clone https://github.com/Z-726/Bugs4Q-Framework.git
  ```

- Get Start
  ```
  cd Bugs4Q-Framework
  python3 main.py
  ```

## Using Bugs4Q

### Example commands
- Get informaition for Program Language (Qiskit only now)
  ```
  python3 main.py info -r qiskit
  ```
- Get informaition for a bug (qiskit program, bug id1)
  ```
  python3 main.py info -r qiskit -b 1
  ```
- Checkout a buggy source code version (qiskit program, bug id1, buggy version)
  ```
  python3 main.py checkout -r qiskit -b 1 -v buggy -o output/
  ```
- Run a buggy file (qiskit program, bug 1, buggy version)
  ```
  python3 main.py run -r qiskit -b 1 -v buggy
  ```
  
- Run unit tests 

  ```
  python3 main.py test -r qiskit -b 1 -v fixed
  ```

### Command-line interface: Bugs4Q commands

| Command | Description |
|--- | --- |
|info | Prints out information about a given bug |
|checkout | Checks-out the source code and test case for a given bug |
|run |Run sources of buggy or fixed version|
|run test |Run tests for a given bug|



### Publications


