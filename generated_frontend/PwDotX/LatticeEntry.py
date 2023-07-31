from typing import Optional, List
from .Row import Row


class LatticeEntry(Row):
    """
    Others:
    ================
    -start 1 -end 3 


    Quantum Espresso Version:
    =========================
    Not yet implemented.
    """

    def __init__(self,
                 v1: Optional[float] = None,
                 v2: Optional[float] = None,
                 v3: Optional[float] = None,
                 ):
        """
        Parameters
        ----------
        **v1**: float
            *Info*:             
             Crystal lattice vectors (in cartesian axis): 
             v1(1) v1(2) v1(3) ... 1st lattice vector 
             v2(1) v2(2) v2(3) ... 2nd lattice vector 
             v3(1) v3(2) v3(3) ... 3rd lattice vector 



        **v2**: float
            *Info*:             
             Crystal lattice vectors (in cartesian axis): 
             v1(1) v1(2) v1(3) ... 1st lattice vector 
             v2(1) v2(2) v2(3) ... 2nd lattice vector 
             v3(1) v3(2) v3(3) ... 3rd lattice vector 



        **v3**: float
            *Info*:             
             Crystal lattice vectors (in cartesian axis): 
             v1(1) v1(2) v1(3) ... 1st lattice vector 
             v2(1) v2(2) v2(3) ... 2nd lattice vector 
             v3(1) v3(2) v3(3) ... 3rd lattice vector 



            Quantum Espresso Version
            ------------------------
            Not yet implemented.
        """
        self._v1: Optional[float] = v1
        self._v2: Optional[float] = v2
        self._v3: Optional[float] = v3

    @property
    def v1(self) -> float:
        """
        Info:
        ================
        
         Crystal lattice vectors (in cartesian axis): 
         v1(1) v1(2) v1(3) ... 1st lattice vector 
         v2(1) v2(2) v2(3) ... 2nd lattice vector 
         v3(1) v3(2) v3(3) ... 3rd lattice vector 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._v1

    @v1.setter
    def v1(self, value: float):
        self._v1 = value

    @property
    def v2(self) -> float:
        """
        Info:
        ================
        
         Crystal lattice vectors (in cartesian axis): 
         v1(1) v1(2) v1(3) ... 1st lattice vector 
         v2(1) v2(2) v2(3) ... 2nd lattice vector 
         v3(1) v3(2) v3(3) ... 3rd lattice vector 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._v2

    @v2.setter
    def v2(self, value: float):
        self._v2 = value

    @property
    def v3(self) -> float:
        """
        Info:
        ================
        
         Crystal lattice vectors (in cartesian axis): 
         v1(1) v1(2) v1(3) ... 1st lattice vector 
         v2(1) v2(2) v2(3) ... 2nd lattice vector 
         v3(1) v3(2) v3(3) ... 3rd lattice vector 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._v3

    @v3.setter
    def v3(self, value: float):
        self._v3 = value

