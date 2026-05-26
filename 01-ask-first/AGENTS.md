# AGENTS.md

## Project shape
Order management service for a logistics platform. Handles order lookup,
status tracking, and batch processing. Written in Python.

## Build and test
pytest tests/ -x --tb=short

## Task protocol
When given a new task, before reading any source file or writing any code:
1. List exactly 3 clarifying questions whose answers would change your approach.
2. Stop and wait for the user to answer them.
3. Only after receiving answers may you read files and begin work.

## Done definition
All tests pass. No new warnings. Diff touches the minimum number of files.
