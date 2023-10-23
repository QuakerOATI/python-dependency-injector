FastAPI-SQLAlchemy Demo
=======================

Useful Tidbits
--------------

- Pattern: use a singleton DB provider that exposes a "session" method
  - this can then be used as a factory for "repository" objects
