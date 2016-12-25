"""
Init database
"""

from yoyo import step

__depends__ = {}

steps = [
    step(
        "CREATE TABLE links ( "
        "  id INT UNSIGNED NOT NULL AUTO_INCREMENT, "
        "  long_url VARCHAR(255), "
        "  PRIMARY KEY (id) "
        ")",
        "DROP TABLE links",
    )
]
