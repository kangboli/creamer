from typing import Optional, List
from .Choice import Choice
from .Choice1 import Choice1


class IflagWsIsWs3WsChoice1(Choice, Choice1):
    """
    Label:
    ================
    the following variables are OPTIONAL:


    """

    def __init__(self,
                 e1: Optional[List[float]] = None,
                 e2: Optional[List[float]] = None,
                 e3: Optional[List[float]] = None,
                 x0: Optional[List[float]] = None,
                 nx: Optional[int] = None,
                 ny: Optional[int] = None,
                 nz: Optional[int] = None,
                 ):
        """
        Parameters
        ----------
        **e1**: List[float]
            *Info*:             
             3D vectors which determine the plotting parallelepiped 
             (if present, must be orthogonal) 
             
             ~e1,~ ~e2,~ and ~e3~ are in alat units ! 


            *Others*:             Start - 1; End - 3



        **e2**: List[float]
            *Info*:             
             3D vectors which determine the plotting parallelepiped 
             (if present, must be orthogonal) 
             
             ~e1,~ ~e2,~ and ~e3~ are in alat units ! 


            *Others*:             Start - 1; End - 3



        **e3**: List[float]
            *Info*:             
             3D vectors which determine the plotting parallelepiped 
             (if present, must be orthogonal) 
             
             ~e1,~ ~e2,~ and ~e3~ are in alat units ! 


            *Others*:             Start - 1; End - 3



        **x0**: List[float]
            *Info*:             
             3D vector, origin of the parallelepiped 
             
             ~x0~ is in alat units ! 


            *Others*:             Start - 1; End - 3



        **nx**: int
            *Info*:             
             Number of points in the parallelepiped: 
             
             rho(i,j,k) = rho( x0 + e1 * (i-1)/nx 
             + e2 * (j-1)/ny 
             + e3 * (k-1)/nz ), 
             i = 1, nx ; j = 1, ny ; k = 1, nz 
             
             - If ~output_format~ = 3 (XCRYSDEN), the above variables 
             are used to determine the grid to plot. 
             
             - If ~output_format~ = 5 (XCRYSDEN), the above variables 
             are ignored, the entire FFT grid is written in the 
             XCRYSDEN format - works for any crystal axis (VERY FAST) 
             
             - If ~e1,~ ~e2,~ ~e3,~ ~x0~ are present, 
             and ~e1,~ ~e2,~ ~e3~ are parallel to xyz 
             and parallel to crystal axis, a subset of the FFT 
             grid that approximately covers the parallelepiped 
             defined by ~e1,~ ~e2,~ ~e3,~ ~x0,~ is 
             written - untested, might be obsolete 
             
             - Otherwise, the required 3D grid is generated from the 
             Fourier components (may be VERY slow) 



        **ny**: int
            *Info*:             
             Number of points in the parallelepiped: 
             
             rho(i,j,k) = rho( x0 + e1 * (i-1)/nx 
             + e2 * (j-1)/ny 
             + e3 * (k-1)/nz ), 
             i = 1, nx ; j = 1, ny ; k = 1, nz 
             
             - If ~output_format~ = 3 (XCRYSDEN), the above variables 
             are used to determine the grid to plot. 
             
             - If ~output_format~ = 5 (XCRYSDEN), the above variables 
             are ignored, the entire FFT grid is written in the 
             XCRYSDEN format - works for any crystal axis (VERY FAST) 
             
             - If ~e1,~ ~e2,~ ~e3,~ ~x0~ are present, 
             and ~e1,~ ~e2,~ ~e3~ are parallel to xyz 
             and parallel to crystal axis, a subset of the FFT 
             grid that approximately covers the parallelepiped 
             defined by ~e1,~ ~e2,~ ~e3,~ ~x0,~ is 
             written - untested, might be obsolete 
             
             - Otherwise, the required 3D grid is generated from the 
             Fourier components (may be VERY slow) 



        **nz**: int
            *Info*:             
             Number of points in the parallelepiped: 
             
             rho(i,j,k) = rho( x0 + e1 * (i-1)/nx 
             + e2 * (j-1)/ny 
             + e3 * (k-1)/nz ), 
             i = 1, nx ; j = 1, ny ; k = 1, nz 
             
             - If ~output_format~ = 3 (XCRYSDEN), the above variables 
             are used to determine the grid to plot. 
             
             - If ~output_format~ = 5 (XCRYSDEN), the above variables 
             are ignored, the entire FFT grid is written in the 
             XCRYSDEN format - works for any crystal axis (VERY FAST) 
             
             - If ~e1,~ ~e2,~ ~e3,~ ~x0~ are present, 
             and ~e1,~ ~e2,~ ~e3~ are parallel to xyz 
             and parallel to crystal axis, a subset of the FFT 
             grid that approximately covers the parallelepiped 
             defined by ~e1,~ ~e2,~ ~e3,~ ~x0,~ is 
             written - untested, might be obsolete 
             
             - Otherwise, the required 3D grid is generated from the 
             Fourier components (may be VERY slow) 



            Quantum Espresso Version
            ------------------------
            Not yet implemented.
        """
        self._e1: Optional[List[float]] = e1
        self._e2: Optional[List[float]] = e2
        self._e3: Optional[List[float]] = e3
        self._x0: Optional[List[float]] = x0
        self._nx: Optional[int] = nx
        self._ny: Optional[int] = ny
        self._nz: Optional[int] = nz

    @property
    def e1(self) -> List[float]:
        """
        Info:
        ================
        
         3D vectors which determine the plotting parallelepiped 
         (if present, must be orthogonal) 
         
         ~e1,~ ~e2,~ and ~e3~ are in alat units ! 


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
        
         3D vectors which determine the plotting parallelepiped 
         (if present, must be orthogonal) 
         
         ~e1,~ ~e2,~ and ~e3~ are in alat units ! 


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
    def e3(self) -> List[float]:
        """
        Info:
        ================
        
         3D vectors which determine the plotting parallelepiped 
         (if present, must be orthogonal) 
         
         ~e1,~ ~e2,~ and ~e3~ are in alat units ! 


        Others:
        ================
        Start - 1; End - 3

        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._e3

    @e3.setter
    def e3(self, value: List[float]):
        self._e3 = value

    @property
    def x0(self) -> List[float]:
        """
        Info:
        ================
        
         3D vector, origin of the parallelepiped 
         
         ~x0~ is in alat units ! 


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
        
         Number of points in the parallelepiped: 
         
         rho(i,j,k) = rho( x0 + e1 * (i-1)/nx 
         + e2 * (j-1)/ny 
         + e3 * (k-1)/nz ), 
         i = 1, nx ; j = 1, ny ; k = 1, nz 
         
         - If ~output_format~ = 3 (XCRYSDEN), the above variables 
         are used to determine the grid to plot. 
         
         - If ~output_format~ = 5 (XCRYSDEN), the above variables 
         are ignored, the entire FFT grid is written in the 
         XCRYSDEN format - works for any crystal axis (VERY FAST) 
         
         - If ~e1,~ ~e2,~ ~e3,~ ~x0~ are present, 
         and ~e1,~ ~e2,~ ~e3~ are parallel to xyz 
         and parallel to crystal axis, a subset of the FFT 
         grid that approximately covers the parallelepiped 
         defined by ~e1,~ ~e2,~ ~e3,~ ~x0,~ is 
         written - untested, might be obsolete 
         
         - Otherwise, the required 3D grid is generated from the 
         Fourier components (may be VERY slow) 



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
        
         Number of points in the parallelepiped: 
         
         rho(i,j,k) = rho( x0 + e1 * (i-1)/nx 
         + e2 * (j-1)/ny 
         + e3 * (k-1)/nz ), 
         i = 1, nx ; j = 1, ny ; k = 1, nz 
         
         - If ~output_format~ = 3 (XCRYSDEN), the above variables 
         are used to determine the grid to plot. 
         
         - If ~output_format~ = 5 (XCRYSDEN), the above variables 
         are ignored, the entire FFT grid is written in the 
         XCRYSDEN format - works for any crystal axis (VERY FAST) 
         
         - If ~e1,~ ~e2,~ ~e3,~ ~x0~ are present, 
         and ~e1,~ ~e2,~ ~e3~ are parallel to xyz 
         and parallel to crystal axis, a subset of the FFT 
         grid that approximately covers the parallelepiped 
         defined by ~e1,~ ~e2,~ ~e3,~ ~x0,~ is 
         written - untested, might be obsolete 
         
         - Otherwise, the required 3D grid is generated from the 
         Fourier components (may be VERY slow) 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._ny

    @ny.setter
    def ny(self, value: int):
        self._ny = value

    @property
    def nz(self) -> int:
        """
        Info:
        ================
        
         Number of points in the parallelepiped: 
         
         rho(i,j,k) = rho( x0 + e1 * (i-1)/nx 
         + e2 * (j-1)/ny 
         + e3 * (k-1)/nz ), 
         i = 1, nx ; j = 1, ny ; k = 1, nz 
         
         - If ~output_format~ = 3 (XCRYSDEN), the above variables 
         are used to determine the grid to plot. 
         
         - If ~output_format~ = 5 (XCRYSDEN), the above variables 
         are ignored, the entire FFT grid is written in the 
         XCRYSDEN format - works for any crystal axis (VERY FAST) 
         
         - If ~e1,~ ~e2,~ ~e3,~ ~x0~ are present, 
         and ~e1,~ ~e2,~ ~e3~ are parallel to xyz 
         and parallel to crystal axis, a subset of the FFT 
         grid that approximately covers the parallelepiped 
         defined by ~e1,~ ~e2,~ ~e3,~ ~x0,~ is 
         written - untested, might be obsolete 
         
         - Otherwise, the required 3D grid is generated from the 
         Fourier components (may be VERY slow) 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._nz

    @nz.setter
    def nz(self, value: int):
        self._nz = value

