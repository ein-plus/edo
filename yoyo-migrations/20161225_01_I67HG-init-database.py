"""
Init database
"""

from yoyo import step

__depends__ = {}

steps = [
    step(
        "CREATE TABLE links ( "
        "  id INT UNSIGNED NOT NULL AUTO_INCREMENT, "
        "  hash INT UNSIGNED, "
        "  long_url VARCHAR(255), "
        "  PRIMARY KEY (id), "
        "  UNIQUE KEY (hash) "
        ")",
        "DROP TABLE links",
    )
]
