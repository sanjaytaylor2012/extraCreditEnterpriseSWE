# extraCreditEnterpriseSWE

# InMemory Database

This project implements an in-memory key-value database with transaction support. It allows you to perform operations like `begin_transaction`, `put`, `get`, `commit`, and `rollback` with proper transactions.

---

## Prerequisites

To run the code, ensure you have the following installed on your system:

- **Python 3.8+**

---

## Setup

1. Clone the repository or download the code files.

   ```bash
   git clone https://github.com/sanjaytaylor2012/extraCreditEnterpriseSWE
   cd extraCreditEnterpriseSWE
   ```

2. Import the code into a testing file in the directory of the repository with the import statement:

```
from inmemoryDB import inmemoryDB
```

3. Otherwise, run `python test.py` to simulate the usage of the database with the same commands in the assignment description using the provided test file.

---

## Assignment Improvements

One way this assigment could be improved is with more clear guidelines on the edge case of commit and rollback where there may not be a transaction in progress and these functions are called. In the example commands, it does say to throw an error if these are called without a transaction being in progress but it could be more clear if this was also
made clear in the descriptions of the functions above. Also, consistent error messages would be a good addition so that everybody's code has the same expected output. This may make grading easier as the same error messages would be thrown which could reduce ambiguity on what a certain error message means. Also, adding a delete functionality to the
database could be a good feature to have as well as many databases have that feature.
