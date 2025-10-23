import pytest_alembic

from dbapp import schema

history_1 = pytest_alembic.create_alembic_fixture({"file": "alembic.ini"})


def test_metadata_create_all(engine):
    schema.metadata.create_all(bind=engine)


def test_alembic_upgrade(history_1):
    pytest_alembic.tests.test_upgrade(history_1)
