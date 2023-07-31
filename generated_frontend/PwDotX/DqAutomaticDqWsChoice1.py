from typing import Optional
import string
from .Choice import Choice
from .Choice1 import Choice1


class DqAutomaticDqWsChoice1(Choice, Choice1):
    """
    """

    def __init__(self,
                 nk1: Optional[int] = None,
                 nk2: Optional[int] = None,
                 nk3: Optional[int] = None,
                 sk1: Optional[int] = None,
                 sk2: Optional[int] = None,
                 sk3: Optional[int] = None,
                 ):
        self._nk1: Optional[int] = nk1
        self._nk2: Optional[int] = nk2
        self._nk3: Optional[int] = nk3
        self._sk1: Optional[int] = sk1
        self._sk2: Optional[int] = sk2
        self._sk3: Optional[int] = sk3

    @property
    def nk1(self) -> int:
        """
        Info:
        ================
        
         These parameters specify the k-point grid 
         (nk1 x nk2 x nk3) as in Monkhorst-Pack grids. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._nk1

    @nk1.setter
    def nk1(self, value: int):
        self._nk1 = value

    @property
    def nk2(self) -> int:
        """
        Info:
        ================
        
         These parameters specify the k-point grid 
         (nk1 x nk2 x nk3) as in Monkhorst-Pack grids. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._nk2

    @nk2.setter
    def nk2(self, value: int):
        self._nk2 = value

    @property
    def nk3(self) -> int:
        """
        Info:
        ================
        
         These parameters specify the k-point grid 
         (nk1 x nk2 x nk3) as in Monkhorst-Pack grids. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._nk3

    @nk3.setter
    def nk3(self, value: int):
        self._nk3 = value

    @property
    def sk1(self) -> int:
        """
        Info:
        ================
        
         The grid offsets; sk1, sk2, sk3 must be 
         0 ( no offset ) or 1 ( grid displaced by 
         half a grid step in the corresponding direction ). 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._sk1

    @sk1.setter
    def sk1(self, value: int):
        self._sk1 = value

    @property
    def sk2(self) -> int:
        """
        Info:
        ================
        
         The grid offsets; sk1, sk2, sk3 must be 
         0 ( no offset ) or 1 ( grid displaced by 
         half a grid step in the corresponding direction ). 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._sk2

    @sk2.setter
    def sk2(self, value: int):
        self._sk2 = value

    @property
    def sk3(self) -> int:
        """
        Info:
        ================
        
         The grid offsets; sk1, sk2, sk3 must be 
         0 ( no offset ) or 1 ( grid displaced by 
         half a grid step in the corresponding direction ). 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._sk3

    @sk3.setter
    def sk3(self, value: int):
        self._sk3 = value

