from sqlalchemy.ext.asyncio import AsyncSession


class BaseService:
    """Base class for services that operate over a DB session."""

    def __init__(self, session: AsyncSession):
        self.session = session
