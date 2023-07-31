from typing import Optional, List
from .Card import Card
from .OccupationsTableEntry import OccupationsTableEntry


class Occupations(Card):
    """
    Label:
    ================
    Optional card, used only if ~occupations~ == 'from_input', ignored otherwise !


    """

    def __init__(self,
                 table: Optional[List[OccupationsTableEntry]] = List[OccupationsTableEntry](),
                 ):
        """
        Parameters
        ----------
        **table**: List[OccupationsTableEntry]

            Quantum Espresso Version
            ------------------------
            Not yet implemented.
        """
        self._table: Optional[List[OccupationsTableEntry]] = table

    @property
    def table(self) -> List[OccupationsTableEntry]:
        """
        """
        return self._table

    @table.setter
    def table(self, value: List[OccupationsTableEntry]):
        self._table = value

