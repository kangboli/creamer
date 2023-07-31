from typing import Optional
import string
from .Choice import Choice
from .Choice1 import Choice1
from .KpointsRow import KpointsRow


class DqTpibaWsOrWsCrystalWsOrWsTpibaBWsOrWsCrystalBWsOrWsTpibaCWsOrWsCrystalCDqWsChoice1(Choice, Choice1):
    """
    """

    def __init__(self,
                 nks: Optional[int] = None,
                 table: Optional[List[KpointsRow]] = None,
                 ):
        self._nks: Optional[int] = nks
        self._table: Optional[List[KpointsRow]] = table

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
    def table(self) -> List[KpointsRow]:
        """
        """
        return self._table

    @table.setter
    def table(self, value: List[KpointsRow]):
        self._table = value

