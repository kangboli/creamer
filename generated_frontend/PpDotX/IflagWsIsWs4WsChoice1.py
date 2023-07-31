from typing import Optional, List
from .Choice import Choice
from .Choice1 import Choice1


class IflagWsIsWs4WsChoice1(Choice, Choice1):
    """
    Label:
    ================
    the following variables are REQUIRED:


    """

    def __init__(self,
                 radius: Optional[float] = None,
                 nx: Optional[int] = None,
                 ny: Optional[int] = None,
                 ):
        """
        Parameters
        ----------
        **radius**: float
            *Info*:             
             Radius of the sphere (alat units), centered at (0,0,0) 



        **nx**: int
            *Info*:             
             Number of points in the polar plane: 
             
             phi(i) = 2 pi * (i - 1)/(nx-1), i=1, nx 
             theta(j) = pi * (j - 1)/(ny-1), j=1, ny 



        **ny**: int
            *Info*:             
             Number of points in the polar plane: 
             
             phi(i) = 2 pi * (i - 1)/(nx-1), i=1, nx 
             theta(j) = pi * (j - 1)/(ny-1), j=1, ny 



            Quantum Espresso Version
            ------------------------
            Not yet implemented.
        """
        self._radius: Optional[float] = radius
        self._nx: Optional[int] = nx
        self._ny: Optional[int] = ny

    @property
    def radius(self) -> float:
        """
        Info:
        ================
        
         Radius of the sphere (alat units), centered at (0,0,0) 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._radius

    @radius.setter
    def radius(self, value: float):
        self._radius = value

    @property
    def nx(self) -> int:
        """
        Info:
        ================
        
         Number of points in the polar plane: 
         
         phi(i) = 2 pi * (i - 1)/(nx-1), i=1, nx 
         theta(j) = pi * (j - 1)/(ny-1), j=1, ny 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._nx

    @nx.setter
    def nx(self, value: int):
        self._nx = value

    @property
    def ny(self) -> int:
        """
        Info:
        ================
        
         Number of points in the polar plane: 
         
         phi(i) = 2 pi * (i - 1)/(nx-1), i=1, nx 
         theta(j) = pi * (j - 1)/(ny-1), j=1, ny 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._ny

    @ny.setter
    def ny(self, value: int):
        self._ny = value

