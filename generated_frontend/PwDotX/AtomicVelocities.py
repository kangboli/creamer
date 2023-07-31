from typing import Optional, List
from .Card import Card
from .FlagAtomvelTypeOptions import FlagAtomvelTypeOptions
from .AtomicVelocitiesEntry import AtomicVelocitiesEntry


class AtomicVelocities(Card):
    """
    Label:
    ================
    
     Optional card, reads velocities from standard input 


    """

    def __init__(self,
                 flag_atomvel_type: Optional[FlagAtomvelTypeOptions] = None,
                 table: Optional[List[AtomicVelocitiesEntry]] = List[AtomicVelocitiesEntry](),
                 ):
        """
        Parameters
        ----------
        **flag_atomvel_type**: FlagAtomvelTypeOptions

        **table**: List[AtomicVelocitiesEntry]

            Quantum Espresso Version
            ------------------------
            Not yet implemented.
        """
        self._flag_atomvel_type: Optional[FlagAtomvelTypeOptions] = flag_atomvel_type
        self._table: Optional[List[AtomicVelocitiesEntry]] = table

    @property
    def flag_atomvel_type(self) -> FlagAtomvelTypeOptions:
        """
        """
        return self._flag_atomvel_type

    @flag_atomvel_type.setter
    def flag_atomvel_type(self, value: FlagAtomvelTypeOptions):
        self._flag_atomvel_type = value

    @property
    def table(self) -> List[AtomicVelocitiesEntry]:
        """
        """
        return self._table

    @table.setter
    def table(self, value: List[AtomicVelocitiesEntry]):
        self._table = value

