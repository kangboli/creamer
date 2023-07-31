from typing import Optional, List
from .Card import Card
from .AtomicSpeciesEntry import AtomicSpeciesEntry


class AtomicSpecies(Card):
    """
    """

    def __init__(self,
                 table: Optional[List[AtomicSpeciesEntry]] = List[AtomicSpeciesEntry](),
                 ):
        """
        Parameters
        ----------
        **table**: List[AtomicSpeciesEntry]

            Quantum Espresso Version
            ------------------------
            Not yet implemented.
        """
        self._table: Optional[List[AtomicSpeciesEntry]] = table

    @property
    def table(self) -> List[AtomicSpeciesEntry]:
        """
        """
        return self._table

    @table.setter
    def table(self, value: List[AtomicSpeciesEntry]):
        self._table = value

