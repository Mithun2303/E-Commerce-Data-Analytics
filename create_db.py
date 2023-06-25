from database import Base,engine

from schemas.market_fact import Market_Fact

Base.metadata.create_all(engine)