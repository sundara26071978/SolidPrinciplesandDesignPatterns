# SolidPrinciplesandDesignPatterns

## SOLID principles

The SOLID principles are five design guidelines for writing clean, maintainable, and scalable object-oriented code. Here’s a brief explanation of each principle in Python context:

### Single Responsibility Principle (SRP):

A class should have only one reason to change, meaning it should only have one job.
Example: A class that handles user authentication should not also handle logging.

### Open/Closed Principle (OCP):

Software entities (classes, functions, etc.) should be open for extension but closed for modification.
Example: Use inheritance or composition to add new behavior without changing existing code.

### Liskov Substitution Principle (LSP):

Subclasses should be substitutable for their base classes without altering the correctness of the program.
Example: If a function uses a base class, it should work with any subclass.

### Interface Segregation Principle (ISP):

Clients should not be forced to depend on interfaces they do not use.
Example: Split large interfaces into smaller, more specific ones.

### Dependency Inversion Principle (DIP):

High-level modules should not depend on low-level modules; both should depend on abstractions.
Example: Use abstract classes or interfaces so that details depend on abstractions, not the other way around.

Applying SOLID principles in Python leads to code that is easier to test, maintain, and extend
