# AGENTS.md

## Project shape
Order management service for a logistics platform. Handles order lookup,
status tracking, and batch processing. Written in Python.

## Build and test
pytest tests/ -x --tb=short

## Task protocol
When given a new task, ask the user 3 questions before reading any file or writing any code.
Make them specific — the kind of questions where a different answer would lead to a different implementation.
Wait for answers before proceeding.

## Done definition
All tests pass. No new warnings. Diff touches the minimum number of files.
