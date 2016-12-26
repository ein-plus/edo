"""
Add clicks info
"""

from yoyo import step

__depends__ = {'20161225_01_I67HG-init-database'}

steps = [
    step(
        "ALTER TABLE links ADD COLUMN create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP",
        "ALTER TABLE links DROP COLUMN create_at",
    ),
    step(
        "CREATE TABLE clicks ( "
        "  id INT NOT NULL AUTO_INCREMENT, "
        "  link_id INT UNSIGNED NOT NULL, "
        "  channel_id INT UNSIGNED DEFAULT 0, "
        "  count INT UNSIGNED DEFAULT 0, "
        "  modify_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, "
        "  PRIMARY KEY (id), "
        "  UNIQUE KEY (link_id, channel_id) "
        ")",
        "DROP TABLE clicks",
    ),
]
