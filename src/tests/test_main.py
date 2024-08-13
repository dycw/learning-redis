from __future__ import annotations

from learning_redis import __version__


def test_main() -> None:
    assert isinstance(__version__, str)
