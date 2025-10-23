from dbapp import schema


def test_metadata_create_all(postgresql):
    schema.metadata.create_all()
