# Fetch Coding Exercise

## Overview

This is a software engineering internship coding exercise for Fetch. The goal is to write a program that reads from a CSV file called `transactions.csv`, processes an argument, and returns a response based on specific conditions outlined below.

- Preliminary steps

  > Please install/ensure Python 3.7 is available before moving to next steps. [To install Python 3.7](https://www.python.org/downloads/)

  1. Clone the repository

  ```bash
  gh repo clone Preet538-neitzen/Fetch-Points
  ```

  1. Change directory to the newly created folder

  ```bash
  cd Fetch-Points
  ```

## Problem Statement

Our users have points in their accounts. Users only see a single balance in their accounts, but for reporting purposes, we actually track their points per payer. Each transaction record contains payer (string), points (integer), and timestamp (date).

For earning points, it is easy to assign a payer. We know which actions earned the points, and thus, which partner should be paying for the points.

When a user spends points, they don't know or care which payer the points come from. But our accounting team does care how the points are spent. There are two rules for determining what points to spend first:

1. The oldest points should be spent first (oldest based on transaction timestamp, not the order they’re received).
2. No payer's points should go negative.

## Solution

App.py does the following:

1. Read the transactions from the `transactions.csv` file.
2. Spend points based on the argument using the rules above.
3. Return all payer point balances.

Following are some examples of input and output.

## Input

The program will take in a single argument, which is the amount of points to spend. For example, using a Python program to spend 5000 points would look like this:

```
python3 app.py 5000
```

The `transactions.csv` file will contain records with the following format:

```
pythonCopy code"payer","points","timestamp"
"DANNON",1000,"2020-11-02T14:00:00Z"
"UNILEVER",200,"2020-10-31T11:00:00Z"
"DANNON",-200,"2020-10-31T15:00:00Z"
"MILLER COORS",10000,"2020-11-01T14:00:00Z"
"DANNON",300,"2020-10-31T10:00:00Z"
```

## Output

After the points are spent, the output should return the following results:

```
Accounts are: { 
"DANNON": 1000, 
"UNILEVER": 0, 
"MILLER COORS": 5300 
}
```
