# Persistence using File and DB

## Where I Struggled
Understanding different serialization formats and handling complex object relationships was tricky.  
Managing database transactions and ensuring consistency in SQLAlchemy took time.

## Breaking the Problem Down
I split the problem into two main sections:

- **File-based Persistence:** Pickle, JSON, YAML for object serialization.
- **Database Persistence:** SQLite and SQLAlchemy with Pydantic models.

## File-based Persistence
- **Pickle Serialization:** Saved and loaded a `Person` object.
- **JSON Serialization:** Converted a `Book` object to and from JSON.
- **YAML Serialization:** Serialized a `Car` object with PyYAML.
- **Handling Complex Objects:** Custom serialization for a `Graph` class.
- **Skipping Sensitive Data:** Ensured passwords were excluded in `User` serialization.
- **Versioning Objects:** Managed backward compatibility in deserialization.
- **Cyclic References:** Handled objects referencing each other.

## Database Persistence
- **SQLite with SQLAlchemy:** Defined models, created tables, and performed CRUD operations.
- **Using Pydantic:** Validated data before inserting into the database.
- **Transactional Operations:** Ensured atomicity with commit and rollback handling.

## What Went Surprisingly Well
JSON and YAML were straightforward, and using Pydantic with SQLAlchemy made validation seamless.  
Managing transactions with SQLAlchemy sessions turned out to be easier than expected.

## Key Learnings
- Pickle is useful but not human-readable or secure.
- JSON is the best balance of readability and flexibility.
- SQLAlchemy simplifies database operations but requires careful session management.

## What AI Helped Me
Debugging serialization issues, handling SQLAlchemy ORM errors, and optimizing database queries.

---

*Note: This document is based on my experience working with persistence in Python.*
