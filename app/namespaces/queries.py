from string import Template
from dataclasses import dataclass


@dataclass(frozen=True)
class Queries:
    UPDATE = Template('UPDATE $table SET $column = ? WHERE $filter_col = ?')
    SELECT_ALL = Template('SELECT * FROM $table')
    SELECT_TABLE = (
        "SELECT name FROM sqlite_master WHERE type='table' AND name = ?"
    )
