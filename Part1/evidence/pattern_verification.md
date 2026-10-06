# Part 1 Pattern Verification

## Scope
Python/Flask application in the repository root. The PHP subtree was excluded because the case study is Flask-based.

## Confirmed
- MVC — Event Creation MVC Flow
- Decorator — Authenticated Event Route Registration
- Active Record-like ORM — Event and Ticket Persistence Model
- Form Object — Event Creation Validation

## Rejected
- Singleton: no explicit controlled singleton construction/access.
- Strategy: baseline filtering uses direct conditional query construction.
- Observer: baseline registration has no subject/observer subscription collaboration.
- Facade: utility functions did not establish one sufficiently clear unified subsystem facade.

## Evidence basis
Pattern claims were checked against participant roles, source locations, calls/delegation, and behavior. No class name, decorator annotation, or LLM statement was accepted by itself.
