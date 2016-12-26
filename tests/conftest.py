import pytest

from edo.models import db


@pytest.fixture(autouse=True)
def clean_db():
    yield
    result = db.session.execute("SHOW TABLES")
    tables = [x[0] for x in result if not x[0].startswith('_')]
    for table in tables:
        db.session.execute("TRUNCATE TABLE " + table)
