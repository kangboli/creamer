from typing import Optional, List
from .Choice import Choice
from .Choice1 import Choice1
from .KpointsEntry import KpointsEntry


class TpibaWsOrWsCrystalWsOrWsTpibaBWsOrWsCrystalBWsOrWsTpibaCWsOrWsCrystalCWsChoice1(Choice, Choice1):
    """
    """

    def __init__(self,
                 nks: Optional[int] = None,
                 table: Optional[List[KpointsEntry]] = List[KpointsEntry](),
                 ):
        """
        Parameters
        ----------
        **nks**: int
            *Info*:             Number of supplied special k-points.



        **table**: List[KpointsEntry]

            Quantum Espresso Version
            ------------------------
            Not yet implemented.
        """
        self._nks: Optional[int] = nks
        self._table: Optional[List[KpointsEntry]] = table

    @property
    def nks(self) -> int:
        """
        Info:
        ================
        Number of supplied special k-points.



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._nks

    @nks.setter
    def nks(self, value: int):
        self._nks = value

    @property
    def table(self) -> List[KpointsEntry]:
        """
        """
        return self._table

    @table.setter
    def table(self, value: List[KpointsEntry]):
        self._table = value

