from dbapp import schema


def test_metadata_create_all(engine):
    schema.metadata.create_all(bind=engine)
