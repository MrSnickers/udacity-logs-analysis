# Udacity Logs Analysis Project

This is a command line script that queries a database and prints reports.  It was written for the Udacity Full Stack Developer Nanodegree against an example database.  It's written in Python3 and interfaces with a PostgresSQL database.

The three reports it executes are:

- A ranking of the three most popular articles in the database
- A ranking of the three most popular authors in the database
- A listing of days when more than 1% of requests errored

## Quick start

This project makes use of a Linux-based virtual machine (VM) inside a vagrant image.

Clone the vagrant image from https://github.com/udacity/fullstack-nanodegree-vm.  Enter the vagrant subdirectory, and run the command `vagrant up` to download dependencies.  Then download and unzip the [PostgreSQL database](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) into the vagrant subdirectory.

If you need to bring the virtual machine back online (with `vagrant up`), do so now. Then log into it with `vagrant ssh`.

Run the log analysis with `python3 reports.py`

## Example output

This will print out to your console three formatted reports that will look a bit like:

```text
========================= Most Popular Articles =========================

Greysand Paranormal captures the Jersey Devil -- 345,002 views
Charlie Cupid wins title belt at the Prominade Arena -- 258,862 views
Dionne Gabraux to star in upcoming sequel, 'The 87' -- 100,120 views

========================= Most Popular Authors =========================

Jack de Quidt -- 441,002 views
Grand Magnificent -- 253,762 views
Tawney Buck -- 100,333 views
```
