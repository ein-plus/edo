"""
Init database
"""

from yoyo import step

__depends__ = {}

steps = [
    step(
        "CREATE TABLE links ( "
        "  id INT, "
        "  hash INT, "
        "  rnd INT, "
        "  longUrl VARCHAR(255), "
        "  PRIMARY KEY (id) "
        ")",
        "DROP TABLE links",
    )
]
