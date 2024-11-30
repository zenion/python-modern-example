"""Tests for the tooling template."""

import pytest

from main import Config, process_items


@pytest.fixture
def config() -> Config:
    """Fixture providing test configuration."""
    return Config(max_length=100, filter_empty=True)


def test_process_items_with_valid_input(config: Config) -> None:
    """Test processing with valid input."""
    items = ["test", "  example  ", "template"]
    result = process_items(items, config)
    assert result == ["TEST", "EXAMPLE", "TEMPLATE"]
    assert all(isinstance(item, str) for item in result)


def test_process_items_with_empty_list(config: Config) -> None:
    """Test processing with empty input."""
    result = process_items([], config)
    assert result == []


def test_process_items_with_prefix(config: Config) -> None:
    """Test processing with prefix."""
    config.prefix = "prefix_"
    result = process_items(["test"], config)
    assert result == ["prefix_TEST"]


def test_process_items_with_default_config() -> None:
    """Test processing with default config."""
    default_config = Config(max_length=50, filter_empty=False)  # Match default values from main.py
    result = process_items(["test"], default_config)
    assert result == ["TEST"]


@pytest.mark.parametrize(
    "input_items,expected",
    [
        (["test"], ["TEST"]),
        (["test", "example"], ["TEST", "EXAMPLE"]),
        (["  spaces  "], ["SPACES"]),
    ],
)
def test_process_items_parametrized(input_items: list[str], expected: list[str], config: Config) -> None:
    """Test processing with different input combinations."""
    assert process_items(input_items, config) == expected
