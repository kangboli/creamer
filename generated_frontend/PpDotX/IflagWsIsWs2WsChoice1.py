from typing import Optional, List
from .Choice import Choice
from .Choice1 import Choice1


class IflagWsIsWs2WsChoice1(Choice, Choice1):
    """
    Label:
    ================
    the following variables are REQUIRED:


    """

    def __init__(self,
                 e1: Optional[List[float]] = None,
                 e2: Optional[List[float]] = None,
                 x0: Optional[List[float]] = None,
                 nx: Optional[int] = None,
                 ny: Optional[int] = None,
                 ):
        """
        Parameters
        ----------
        **e1**: List[float]
            *Info*:             
             3D vectors which determine the plotting plane (in alat units) 
             
             BEWARE: **e1** and **e2** must be orthogonal 


            *Others*:             Start - 1; End - 3



        **e2**: List[float]
            *Info*:             
             3D vectors which determine the plotting plane (in alat units) 
             
             BEWARE: **e1** and **e2** must be orthogonal 


            *Others*:             Start - 1; End - 3



        **x0**: List[float]
            *Info*:             
             3D vector, origin of the plane (in alat units) 


            *Others*:             Start - 1; End - 3



        **nx**: int
            *Info*:             
             Number of points in the plane: 
             
             rho(i,j) = rho( x0 + e1 * (i-1)/(nx-1) 
             + e2 * (j-1)/(ny-1) ), i=1,nx ; j=1,ny 



        **ny**: int
            *Info*:             
             Number of points in the plane: 
             
             rho(i,j) = rho( x0 + e1 * (i-1)/(nx-1) 
             + e2 * (j-1)/(ny-1) ), i=1,nx ; j=1,ny 



            Quantum Espresso Version
            ------------------------
            Not yet implemented.
        """
        self._e1: Optional[List[float]] = e1
        self._e2: Optional[List[float]] = e2
        self._x0: Optional[List[float]] = x0
        self._nx: Optional[int] = nx
        self._ny: Optional[int] = ny

    @property
    def e1(self) -> List[float]:
        """
        Info:
        ================
        
         3D vectors which determine the plotting plane (in alat units) 
         
         BEWARE: **e1** and **e2** must be orthogonal 


        Others:
        ================
        Start - 1; End - 3

        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._e1

    @e1.setter
    def e1(self, value: List[float]):
        self._e1 = value

    @property
    def e2(self) -> List[float]:
        """
        Info:
        ================
        
         3D vectors which determine the plotting plane (in alat units) 
         
         BEWARE: **e1** and **e2** must be orthogonal 


        Others:
        ================
        Start - 1; End - 3

        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._e2

    @e2.setter
    def e2(self, value: List[float]):
        self._e2 = value

    @property
    def x0(self) -> List[float]:
        """
        Info:
        ================
        
         3D vector, origin of the plane (in alat units) 


        Others:
        ================
        Start - 1; End - 3

        Quantum Espresso Version:
        =========================
        Not yet implemented.
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
        
         Number of points in the plane: 
         
         rho(i,j) = rho( x0 + e1 * (i-1)/(nx-1) 
         + e2 * (j-1)/(ny-1) ), i=1,nx ; j=1,ny 



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
        
         Number of points in the plane: 
         
         rho(i,j) = rho( x0 + e1 * (i-1)/(nx-1) 
         + e2 * (j-1)/(ny-1) ), i=1,nx ; j=1,ny 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._ny

    @ny.setter
    def ny(self, value: int):
        self._ny = value

