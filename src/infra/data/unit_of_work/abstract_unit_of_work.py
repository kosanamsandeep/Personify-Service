import logging
from abc import ABC, abstractmethod
from typing import Any


class AbstractUnitOfWork(ABC):
    def __init__(
        self,
        logger: logging.Logger
    ) -> None:
        super().__init__()
        self._logger = logger
        self._session = None

    @property
    def session(self) -> Any:
        return self._session

    @abstractmethod
    def commit(self) -> Any:
        raise NotImplementedError

    @abstractmethod
    def rollback(self) -> Any:
        raise NotImplementedError

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any):
        if exc_type is None:
            self.commit()
        else:
            self._logger.exception(exc_val)
            self.rollback()
