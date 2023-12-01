import toml
from pathlib import Path
from types import MappingProxyType

__version__ = '1.1.0'

# Load config
CONFIG = MappingProxyType(
    toml.load(
        Path(__file__).parent.parent / 'config.toml',
    )
)  # Using MappingProxyType to prevent change to config
