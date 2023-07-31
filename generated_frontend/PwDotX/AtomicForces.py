from typing import Optional, List
from .Card import Card
from .AtomicForcesEntry import AtomicForcesEntry


class AtomicForces(Card):
    """
    Label:
    ================
    Optional card used to specify external forces acting on atoms. 
     BEWARE: if the sum of external forces is not zero, the center of mass of 
     the system will move 


    Message:
    ================
    
     BEWARE: if the sum of external forces is not zero, the center of mass of 
     the system will move 


    """

    def __init__(self,
                 table: Optional[List[AtomicForcesEntry]] = List[AtomicForcesEntry](),
                 ):
        """
        Parameters
        ----------
        **table**: List[AtomicForcesEntry]

            Quantum Espresso Version
            ------------------------
            Not yet implemented.
        """
        self._table: Optional[List[AtomicForcesEntry]] = table

    @property
    def table(self) -> List[AtomicForcesEntry]:
        """
        """
        return self._table

    @table.setter
    def table(self, value: List[AtomicForcesEntry]):
        self._table = value

