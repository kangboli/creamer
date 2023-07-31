from typing import Optional, List
from .Choice import Choice
from .Choice0 import Choice0
from .AtomicCoordinatesEntry import AtomicCoordinatesEntry


class OtherwiseWsChoice0(Choice, Choice0):
    """
    """

    def __init__(self,
                 table: Optional[List[AtomicCoordinatesEntry]] = List[AtomicCoordinatesEntry](),
                 ):
        """
        Parameters
        ----------
        **table**: List[AtomicCoordinatesEntry]

            Quantum Espresso Version
            ------------------------
            Not yet implemented.
        """
        self._table: Optional[List[AtomicCoordinatesEntry]] = table

    @property
    def table(self) -> List[AtomicCoordinatesEntry]:
        """
        """
        return self._table

    @table.setter
    def table(self, value: List[AtomicCoordinatesEntry]):
        self._table = value

