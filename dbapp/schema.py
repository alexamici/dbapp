import sqlalchemy as sa


metadata = sa.MetaData()

users = sa.Table(
    "users",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("created", sa.DateTime(), default=sa.func.now()),
    sa.Column("user_uuid", sa.String, nullable=False, unique=True, index=True),
)

requests = sa.Table(
    "requests",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column(
        "created", sa.DateTime(), default=sa.func.now(), nullable=False, index=True
    ),
    sa.Column("request_url", sa.String, nullable=False),
    sa.Column("user_id", sa.ForeignKey("users.id"), nullable=False, index=True),
)
