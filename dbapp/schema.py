import sqlalchemy as sa


metadata = sa.Metadata()

users = sa.Table(
    "users",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("user_uuid", sa.String),
)

requests = sa.Table(
    "requests",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("request_url", sa.String),
    sa.Column("user_id", sa.ForeignKey("users.id"), nullable=False),
)
