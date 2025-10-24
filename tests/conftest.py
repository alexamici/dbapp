import sqlalchemy as sa

import pytest


@pytest.fixture
def engine(postgresql):
    connection = f"postgresql+psycopg://{postgresql.info.user}:@{postgresql.info.host}:{postgresql.info.port}/{postgresql.info.dbname}"
    engine = sa.create_engine(connection, echo=False, poolclass=sa.NullPool)

    yield engine


@pytest.fixture
def alembic_engine(engine):
    return engine
