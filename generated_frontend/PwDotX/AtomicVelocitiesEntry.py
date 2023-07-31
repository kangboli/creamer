from typing import Optional, List
from .Row import Row


class AtomicVelocitiesEntry(Row):
    """
    Others:
    ================
    -start 1 -end nat 


    Quantum Espresso Version:
    =========================
    Not yet implemented.
    """

    def __init__(self,
                 V: Optional[str] = None,
                 vx: Optional[float] = None,
                 vy: Optional[float] = None,
                 vz: Optional[float] = None,
                 ):
        """
        Parameters
        ----------
        **V**: str
            *Info*:             label of the atom as specified in ATOMIC_SPECIES



        **vx**: float
            *Info*:             atomic velocities along x y and z direction



        **vy**: float
            *Info*:             atomic velocities along x y and z direction



        **vz**: float
            *Info*:             atomic velocities along x y and z direction



            Quantum Espresso Version
            ------------------------
            Not yet implemented.
        """
        self._V: Optional[str] = V
        self._vx: Optional[float] = vx
        self._vy: Optional[float] = vy
        self._vz: Optional[float] = vz

    @property
    def V(self) -> str:
        """
        Info:
        ================
        label of the atom as specified in ATOMIC_SPECIES



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._V

    @V.setter
    def V(self, value: str):
        self._V = value

    @property
    def vx(self) -> float:
        """
        Info:
        ================
        atomic velocities along x y and z direction



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._vx

    @vx.setter
    def vx(self, value: float):
        self._vx = value

    @property
    def vy(self) -> float:
        """
        Info:
        ================
        atomic velocities along x y and z direction



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._vy

    @vy.setter
    def vy(self, value: float):
        self._vy = value

    @property
    def vz(self) -> float:
        """
        Info:
        ================
        atomic velocities along x y and z direction



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._vz

    @vz.setter
    def vz(self, value: float):
        self._vz = value

