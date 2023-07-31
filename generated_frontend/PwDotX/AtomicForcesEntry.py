from typing import Optional, List
from .Row import Row


class AtomicForcesEntry(Row):
    """
    Others:
    ================
    -start 1 -end nat 


    Quantum Espresso Version:
    =========================
    Not yet implemented.
    """

    def __init__(self,
                 X: Optional[str] = None,
                 fx: Optional[float] = None,
                 fy: Optional[float] = None,
                 fz: Optional[float] = None,
                 ):
        """
        Parameters
        ----------
        **X**: str
            *Info*:             label of the atom as specified in ~ATOMIC_SPECIES~



        **fx**: float
            *Info*:             external force on atom X (cartesian components, Ry/a.u. units) 



        **fy**: float
            *Info*:             external force on atom X (cartesian components, Ry/a.u. units) 



        **fz**: float
            *Info*:             external force on atom X (cartesian components, Ry/a.u. units) 



            Quantum Espresso Version
            ------------------------
            Not yet implemented.
        """
        self._X: Optional[str] = X
        self._fx: Optional[float] = fx
        self._fy: Optional[float] = fy
        self._fz: Optional[float] = fz

    @property
    def X(self) -> str:
        """
        Info:
        ================
        label of the atom as specified in ~ATOMIC_SPECIES~



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._X

    @X.setter
    def X(self, value: str):
        self._X = value

    @property
    def fx(self) -> float:
        """
        Info:
        ================
        external force on atom X (cartesian components, Ry/a.u. units) 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._fx

    @fx.setter
    def fx(self, value: float):
        self._fx = value

    @property
    def fy(self) -> float:
        """
        Info:
        ================
        external force on atom X (cartesian components, Ry/a.u. units) 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._fy

    @fy.setter
    def fy(self, value: float):
        self._fy = value

    @property
    def fz(self) -> float:
        """
        Info:
        ================
        external force on atom X (cartesian components, Ry/a.u. units) 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._fz

    @fz.setter
    def fz(self, value: float):
        self._fz = value

