"""A tiny greeting package with contribution guide."""


def greet(name: str) -> str:
    """Return a greeting, using "world" when the name is blank."""
    name = name.strip() or "world"
    return f"Hello, {name}!"
