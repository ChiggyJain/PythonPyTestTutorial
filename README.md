# 🧪 PythonPyTestTutorial
**Industry-Grade PyTest (Sync + Async) for FastAPI Backends**

## 📌 Overview
This repository demonstrates **production-ready testing practices using PyTest** for modern Python backends.
It focuses on **real-world FastAPI and async testing patterns**, not just basic unit tests.

The project is designed so that **HR, interviewers, and senior engineers** can clearly see hands-on expertise in:
- PyTest fundamentals
- Async testing
- FastAPI endpoint testing
- Dependency isolation
- Mocking external systems
- CI-friendly deterministic tests

---

## 🎯 What This Project Demonstrates

✔ PyTest fundamentals (assertions, exceptions, discovery rules)  
✔ Clean test organization & naming conventions  
✔ Fixtures, scopes, and shared fixtures (`conftest.py`)  
✔ Parametrized tests & markers for CI pipelines  
✔ Monkeypatch & mocking (APIs, env vars, time, UUID, randomness)  
✔ Sync + Async test patterns  
✔ FastAPI async endpoint testing (without running a real server)  
✔ Dependency overrides (Auth, DB, Redis patterns)  
✔ Async database isolation (transaction rollback pattern)  
✔ Background task & Celery-like job testing strategies  

---

## 🏗️ Project Structure

```text
PythonPyTestTutorial/
├── app/
│   ├── main.py                  # FastAPI app
│   ├── dependencies.py          # Auth / dependency examples
│   ├── async_math.py
│   ├── async_resource.py
│   ├── fake_async_db.py
│   ├── api_client.py
│   ├── user_service.py
│   ├── background_tasks.py
│   ├── time_service.py
│   ├── id_service.py
│   └── random_service.py
│
├── tests/
│   ├── unit/
│   │   ├── test_topic_1_*        # PyTest basics
│   │   ├── test_topic_2_*        # Fixtures, mocks, parametrization
│   │   ├── test_topic_3_*        # Async, FastAPI, DB, background tasks
│   ├── conftest.py               # Shared fixtures
│
├── pytest.ini                    # Central PyTest configuration
└── README.md
```

---

## 🧠 Key Concepts Covered

### 🔹 PyTest Core
- Test discovery rules
- Assertions & exception testing
- CLI usage & failure analysis
- Test organization & naming

### 🔹 Fixtures & Mocking
- Fixture scopes (function / module / session)
- Setup & teardown with `yield`
- Shared fixtures using `conftest.py`
- Parametrized tests
- Markers for selective test runs
- Monkeypatch for dependency isolation

### 🔹 Async & FastAPI Testing
- `pytest-asyncio`
- Async fixtures & lifecycle management
- FastAPI endpoint testing with `httpx.AsyncClient + ASGITransport`
- Dependency overrides for auth, DB, Redis
- Async DB transaction rollback pattern
- Background task & worker testing strategy

---

## ⚙️ How to Run Tests

Run all tests:
```bash
pytest
```

Run only unit tests:
```bash
pytest -m unit
```

Verbose mode (default via pytest.ini):
```bash
pytest -v
```


## 🧩 Tech Stack

- Python 3.12
- PyTest
- pytest-asyncio
- FastAPI
- httpx
- Async programming patterns

---

## 🏁 Final Note

This repository is built to reflect **real production testing scenarios**, not toy examples.
All patterns demonstrated here are directly applicable to **enterprise FastAPI and microservice backends**.