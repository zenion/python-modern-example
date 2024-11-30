"""Example tool template demonstrating best practices for Python tooling."""

import logging
from dataclasses import dataclass

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


@dataclass
class Config:
    max_length: int = 100
    prefix: str | None = None
    filter_empty: bool = True


def process_items(items: list[str], config: Config | None = None) -> list[str]:
    """Process a list of strings according to the provided configuration.

    Args:
        items: List of strings to process
        config: Configuration settings for processing

    Returns:
        Processed list of strings
    """
    if config is None:
        config = Config()

    processed: list[str] = []

    for item in items:
        if config.filter_empty and not item.strip():
            continue

        # Convert to uppercase and strip whitespace
        item = item.strip().upper()

        if config.prefix:
            item = f"{config.prefix}{item}"

        if len(item) > config.max_length:
            item = item[: config.max_length]

        processed.append(item)

    return processed


def main() -> None:
    """Main entry point for the tool."""
    try:
        config = Config(max_length=100, prefix="prefix_", filter_empty=True)
        items = ["example", "  test  ", "template", "        "]
        result = process_items(items, config)
        logger.info("Processed results: %s", result)
    except Exception as e:
        logger.error("Error running tool: %s", str(e))
        raise


if __name__ == "__main__":
    main()
