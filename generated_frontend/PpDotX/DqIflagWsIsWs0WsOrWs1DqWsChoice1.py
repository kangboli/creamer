from typing import Optional
import string
from .Choice import Choice
from .Choice1 import Choice1


class DqIflagWsIsWs0WsOrWs1DqWsChoice1(Choice, Choice1):
    """
Label:
================
the following variables are REQUIRED:

    """

    def __init__(self,
                 e1: Optional[List[float]] = None,
                 x0: Optional[List[float]] = None,
                 nx: Optional[int] = None,
                 ):
        self._e1: Optional[List[float]] = e1
        self._x0: Optional[List[float]] = x0
        self._nx: Optional[int] = nx

    @property
    def e1(self) -> List[float]:
        """
Info:
================

 3D vector which determines the plotting line (in alat units) 


Others:
================
Start - 1; End - 3

        """
        return self._e1

    @e1.setter
    def e1(self, value: List[float]):
        self._e1 = value

    @property
    def x0(self) -> List[float]:
        """
Info:
================

 3D vector, origin of the line (in alat units) 


Others:
================
Start - 1; End - 3

        """
        return self._x0

    @x0.setter
    def x0(self, value: List[float]):
        self._x0 = value

    @property
    def nx(self) -> int:
        """
Info:
================

 number of points in the line: 
 
 rho(i) = rho( x0 + e1 * (i-1)/(nx-1) ), i=1, nx 


        """
        return self._nx

    @nx.setter
    def nx(self, value: int):
        self._nx = value

