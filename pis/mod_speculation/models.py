from .. import db
from ..models import Base

class MainForce(Base):
    # New instance instantiation procedure
    name = db.Column(db.String(20), nullable=False)
    amount = db.Column(db.Float(), nullable=False)

class FundTrend(Base):
    # New instance instantiation procedure
    topic = db.Column(db.String(20), nullable=False)
    count = db.Column(db.Integer(), nullable=False)