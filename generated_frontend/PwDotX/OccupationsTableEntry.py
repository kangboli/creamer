from typing import Optional, List
from .Row import Row


class OccupationsTableEntry(Row):
    """
    Others:
    ================
    -start 1 -end nbnd 


    Quantum Espresso Version:
    =========================
    Not yet implemented.
    """

    def __init__(self,
                 f_inp1: Optional[float] = None,
                 f_inp2: Optional[float] = None,
                 ):
        """
        Parameters
        ----------
        **f_inp1**: float

        **f_inp2**: float

            Quantum Espresso Version
            ------------------------
            Not yet implemented.
        """
        self._f_inp1: Optional[float] = f_inp1
        self._f_inp2: Optional[float] = f_inp2

    @property
    def f_inp1(self) -> float:
        """
        """
        return self._f_inp1

    @f_inp1.setter
    def f_inp1(self, value: float):
        self._f_inp1 = value

    @property
    def f_inp2(self) -> float:
        """
        """
        return self._f_inp2

    @f_inp2.setter
    def f_inp2(self, value: float):
        self._f_inp2 = value

