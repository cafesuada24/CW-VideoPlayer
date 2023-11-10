import tomllib
from pathlib import Path
from types import MappingProxyType

__version__ = '1.1.0'

# Load config file
CONFIG = None
with open(Path(__file__).parent.parent / 'config.toml', 'rb') as f:
    CONFIG = MappingProxyType(tomllib.load(f))
