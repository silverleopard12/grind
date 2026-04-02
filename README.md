# grind

A personal repository for competitive programming practice and algorithm study.

## Overview

This repo tracks my solutions to problems from **Baekjoon Online Judge** and **Programmers**, written in C++ and Python. It also serves as a hands-on workspace for learning Git and GitHub workflows.

## Platforms

| Platform | URL | Focus |
|---|---|---|
| Baekjoon | https://www.acmicpc.net | Wide range of algorithm topics, Korean competitive programming standard |
| Programmers | https://school.programmers.co.kr | Coding test prep, Korean tech interview style |

## Repository Structure

```
grind/
├── baekjoon/
│   ├── bronze/
│   ├── silver/
│   ├── gold/
│   └── platinum/
├── programmers/
│   ├── level1/
│   ├── level2/
│   ├── level3/
│   └── level4/
└── README.md
```

> The folder structure above is a suggested layout. Organize however feels natural as you go.

## Languages

- **C++** — for performance-critical solutions and low-level algorithm practice
- **Python** — for rapid prototyping and problems where conciseness matters

## Topics Covered

- Data structures (stack, queue, heap, tree, graph)
- Sorting and searching
- Dynamic programming (DP)
- Greedy algorithms
- BFS / DFS / backtracking
- String manipulation
- Math and number theory
- Two pointers / sliding window

## Git & GitHub Learning Goals

This repo is also a practice ground for Git and GitHub fundamentals:

- Writing clear, meaningful commit messages
- Branching and merging
- Using `.gitignore` properly
- Pushing to and pulling from a remote repository
- Understanding `git log`, `git diff`, `git status`
- Resolving merge conflicts
- Using GitHub Issues and pull requests

### Useful Git Commands

```bash
# Stage and commit a new solution
git add baekjoon/silver/1234.cpp
git commit -m "Add BOJ 1234: problem name"
git push origin main

# Check what's changed
git status
git diff

# View commit history
git log --oneline
```

## Commit Message Convention

```
Add BOJ 1234: <problem name>          # new Baekjoon solution
Add PGS lv2: <problem name>           # new Programmers solution
Fix BOJ 1234: fix wrong answer        # bug fix
Refactor BOJ 1234: simplify DP        # refactor
```

## Goal

Solve at least one problem per day. Build consistency, not speed.
