# Team A15 — Design Pattern Case Study

## Application
Design Pattern Analysis in a Flask-Based Event Management Application.

## Team
| Roll number | Student | Batch |
|---|---|---|
| AM.SC.U4CSE23222 | Harshitha D | CSE |
| AM.SC.U4CSE23265 | T Heshaja | CSE |
| AM.SC.U4CSE23222 | Harshitha D | CSE |
| AM.SC.U4CSE23265 | T Heshaja | CSE |

Individual task allocation was not preserved in the supplied case-study materials, so no individual contribution claims are invented here.

## Source
- Application: https://github.com/ARUNAGIRINATHAN-K/Event-Management-system
- Baseline source: supplied repository ZIP snapshot inspected on 2026-10-06. The ZIP did not preserve a Git commit hash; the report therefore does not invent one.
- Scope: Python/Flask application in the repository root. `Event_Management_system_using_PHP/` is excluded because the assigned case study is Flask-based.

## Environment
- Python: >=3.11 (project requirement); structural tests run with Python 3 in the verification container.
- Flask 3.1.0, Flask-Login 0.6.3, Flask-SQLAlchemy 3.1.1, Flask-WTF 1.2.2, SQLAlchemy 2.0.40 from the supplied lock file.
- Database: SQLAlchemy; `DATABASE_URL` with SQLite fallback in the application source.

## Part 1
Four baseline collaborations were confirmed: MVC, Decorator framework idiom, Active Record-like ORM, and Form Object. Singleton, Strategy, Observer and Facade were rejected/uncertain based on the baseline evidence.

## Part 2
- CH01: Repository Pattern
- CH02: Strategy Pattern
- CH03: Observer Pattern

The evolved project contains the implementations and structural tests. The structural test suite passed 4/4. Full Flask runtime execution was not claimed because the verification environment lacked the Flask dependency/runtime setup.

## Part 3
Repository, Strategy and Observer representative problems were implemented in Java, Python, JavaScript and C++. All 12 implementations passed their deterministic tests. Each was compiled/interpreted as appropriate, warmed up once, then measured for five process runs; `median_process_ms` records the median. Timing includes process startup and test input execution. Raw timing evidence is in `Part3/evidence/timings_raw.csv`.

## Metrics rules
- Source LOC: nonblank, non-comment production lines; tests excluded.
- Cyclomatic complexity: maximum function complexity for the production snippet using the counting rule recorded in `data/cross_language.csv`.
- Timing: one warmup + five measured process runs; median reported; never estimated.

## Submission structure
`A15/` contains one final report and one dataset directory. Part1/Part2/Part3 contain supporting evidence only; the five required CSVs are kept only in `data/`.
