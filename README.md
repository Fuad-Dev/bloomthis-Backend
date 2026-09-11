# Backend

## Overview


The Task covers:

* Basic coding and data aggregation
* SQL relational queries
* Git version control workflow

## 1. Basic Coding

The Python script `transaction_revenue.py` calculates the total revenue from completed transactions.

For the provided transaction data, the total completed revenue is **$125.25**.

## 2. SQL Query

The `query.sql` file contains a SQL query that retrieves the names and emails of users who have placed at least one order with an `order_total` strictly greater than $100.

## 3. Git Workflow

The following commands were used to initialize the repository, create the assessment branch, and commit the assessment files.

```bash
git init
git switch -c feature/assessment-answers
git branch --show-current
git add transaction_revenue.py
git commit -m "Add completed transaction revenue calculation"
git add query.sql
git commit -m "Add SQL query for qualifying users"
git remote add origin https://github.com/Fuad-Dev/bloomthis-software-developer-assessment.git
git push -u origin feature/assessment-answers
```

The repository is hosted in a public GitHub repository as part of the submission.

## Files

* `transaction_revenue.py` — Python solution for the data aggregation task
* `query.sql` — SQL solution for the relational query task
* `README.md` — Project overview and Git workflow
