from typing import Optional, List
from .Group import Group


class Group0(Group):
    """
    Label:
    ================
    Either:Or:


    """

    def __init__(self,
                 celldm: Optional[List[float]] = None,
                 A: Optional[float] = None,
                 B: Optional[float] = None,
                 C: Optional[float] = None,
                 cosAB: Optional[float] = None,
                 cosAC: Optional[float] = None,
                 cosBC: Optional[float] = None,
                 ):
        """
        Parameters
        ----------
        **celldm**: List[float]
            *Info*:             
             Crystallographic constants - see the ~ibrav~ variable. 
             Specify either these OR ~A,~ ~B,~ ~C,~ ~cosAB,~ ~cosBC,~ ~cosAC~ NOT both. 
             Only needed values (depending on "ibrav") must be specified 
             alat = ~celldm(1)~ is the lattice parameter "a" (in BOHR) 
             If ~ibrav==0,~ only ~celldm(1)~ is used if present; 
             cell vectors are read from card ~CELL_PARAMETERS~ 


            *Others*:             Start - 1; End - 6



        **A**: float
            *Info*:             
             Traditional crystallographic constants: 
             
             a,b,c in ANGSTROM 
             cosAB = cosine of the angle between axis a and b (gamma) 
             cosAC = cosine of the angle between axis a and c (beta) 
             cosBC = cosine of the angle between axis b and c (alpha) 
             
             The axis are chosen according to the value of ~ibrav.~ 
             Specify either these OR ~celldm~ but NOT both. 
             Only needed values (depending on ~ibrav)~ must be specified. 
             
             The lattice parameter alat = A (in ANGSTROM ). 
             
             If ~ibrav~ == 0, only A is used if present, and 
             cell vectors are read from card ~CELL_PARAMETERS.~ 



        **B**: float
            *Info*:             
             Traditional crystallographic constants: 
             
             a,b,c in ANGSTROM 
             cosAB = cosine of the angle between axis a and b (gamma) 
             cosAC = cosine of the angle between axis a and c (beta) 
             cosBC = cosine of the angle between axis b and c (alpha) 
             
             The axis are chosen according to the value of ~ibrav.~ 
             Specify either these OR ~celldm~ but NOT both. 
             Only needed values (depending on ~ibrav)~ must be specified. 
             
             The lattice parameter alat = A (in ANGSTROM ). 
             
             If ~ibrav~ == 0, only A is used if present, and 
             cell vectors are read from card ~CELL_PARAMETERS.~ 



        **C**: float
            *Info*:             
             Traditional crystallographic constants: 
             
             a,b,c in ANGSTROM 
             cosAB = cosine of the angle between axis a and b (gamma) 
             cosAC = cosine of the angle between axis a and c (beta) 
             cosBC = cosine of the angle between axis b and c (alpha) 
             
             The axis are chosen according to the value of ~ibrav.~ 
             Specify either these OR ~celldm~ but NOT both. 
             Only needed values (depending on ~ibrav)~ must be specified. 
             
             The lattice parameter alat = A (in ANGSTROM ). 
             
             If ~ibrav~ == 0, only A is used if present, and 
             cell vectors are read from card ~CELL_PARAMETERS.~ 



        **cosAB**: float
            *Info*:             
             Traditional crystallographic constants: 
             
             a,b,c in ANGSTROM 
             cosAB = cosine of the angle between axis a and b (gamma) 
             cosAC = cosine of the angle between axis a and c (beta) 
             cosBC = cosine of the angle between axis b and c (alpha) 
             
             The axis are chosen according to the value of ~ibrav.~ 
             Specify either these OR ~celldm~ but NOT both. 
             Only needed values (depending on ~ibrav)~ must be specified. 
             
             The lattice parameter alat = A (in ANGSTROM ). 
             
             If ~ibrav~ == 0, only A is used if present, and 
             cell vectors are read from card ~CELL_PARAMETERS.~ 



        **cosAC**: float
            *Info*:             
             Traditional crystallographic constants: 
             
             a,b,c in ANGSTROM 
             cosAB = cosine of the angle between axis a and b (gamma) 
             cosAC = cosine of the angle between axis a and c (beta) 
             cosBC = cosine of the angle between axis b and c (alpha) 
             
             The axis are chosen according to the value of ~ibrav.~ 
             Specify either these OR ~celldm~ but NOT both. 
             Only needed values (depending on ~ibrav)~ must be specified. 
             
             The lattice parameter alat = A (in ANGSTROM ). 
             
             If ~ibrav~ == 0, only A is used if present, and 
             cell vectors are read from card ~CELL_PARAMETERS.~ 



        **cosBC**: float
            *Info*:             
             Traditional crystallographic constants: 
             
             a,b,c in ANGSTROM 
             cosAB = cosine of the angle between axis a and b (gamma) 
             cosAC = cosine of the angle between axis a and c (beta) 
             cosBC = cosine of the angle between axis b and c (alpha) 
             
             The axis are chosen according to the value of ~ibrav.~ 
             Specify either these OR ~celldm~ but NOT both. 
             Only needed values (depending on ~ibrav)~ must be specified. 
             
             The lattice parameter alat = A (in ANGSTROM ). 
             
             If ~ibrav~ == 0, only A is used if present, and 
             cell vectors are read from card ~CELL_PARAMETERS.~ 



            Quantum Espresso Version
            ------------------------
            Not yet implemented.
        """
        self._celldm: Optional[List[float]] = celldm
        self._A: Optional[float] = A
        self._B: Optional[float] = B
        self._C: Optional[float] = C
        self._cosAB: Optional[float] = cosAB
        self._cosAC: Optional[float] = cosAC
        self._cosBC: Optional[float] = cosBC

    @property
    def celldm(self) -> List[float]:
        """
        Info:
        ================
        
         Crystallographic constants - see the ~ibrav~ variable. 
         Specify either these OR ~A,~ ~B,~ ~C,~ ~cosAB,~ ~cosBC,~ ~cosAC~ NOT both. 
         Only needed values (depending on "ibrav") must be specified 
         alat = ~celldm(1)~ is the lattice parameter "a" (in BOHR) 
         If ~ibrav==0,~ only ~celldm(1)~ is used if present; 
         cell vectors are read from card ~CELL_PARAMETERS~ 


        Others:
        ================
        Start - 1; End - 6

        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._celldm

    @celldm.setter
    def celldm(self, value: List[float]):
        self._celldm = value

    @property
    def A(self) -> float:
        """
        Info:
        ================
        
         Traditional crystallographic constants: 
         
         a,b,c in ANGSTROM 
         cosAB = cosine of the angle between axis a and b (gamma) 
         cosAC = cosine of the angle between axis a and c (beta) 
         cosBC = cosine of the angle between axis b and c (alpha) 
         
         The axis are chosen according to the value of ~ibrav.~ 
         Specify either these OR ~celldm~ but NOT both. 
         Only needed values (depending on ~ibrav)~ must be specified. 
         
         The lattice parameter alat = A (in ANGSTROM ). 
         
         If ~ibrav~ == 0, only A is used if present, and 
         cell vectors are read from card ~CELL_PARAMETERS.~ 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._A

    @A.setter
    def A(self, value: float):
        self._A = value

    @property
    def B(self) -> float:
        """
        Info:
        ================
        
         Traditional crystallographic constants: 
         
         a,b,c in ANGSTROM 
         cosAB = cosine of the angle between axis a and b (gamma) 
         cosAC = cosine of the angle between axis a and c (beta) 
         cosBC = cosine of the angle between axis b and c (alpha) 
         
         The axis are chosen according to the value of ~ibrav.~ 
         Specify either these OR ~celldm~ but NOT both. 
         Only needed values (depending on ~ibrav)~ must be specified. 
         
         The lattice parameter alat = A (in ANGSTROM ). 
         
         If ~ibrav~ == 0, only A is used if present, and 
         cell vectors are read from card ~CELL_PARAMETERS.~ 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._B

    @B.setter
    def B(self, value: float):
        self._B = value

    @property
    def C(self) -> float:
        """
        Info:
        ================
        
         Traditional crystallographic constants: 
         
         a,b,c in ANGSTROM 
         cosAB = cosine of the angle between axis a and b (gamma) 
         cosAC = cosine of the angle between axis a and c (beta) 
         cosBC = cosine of the angle between axis b and c (alpha) 
         
         The axis are chosen according to the value of ~ibrav.~ 
         Specify either these OR ~celldm~ but NOT both. 
         Only needed values (depending on ~ibrav)~ must be specified. 
         
         The lattice parameter alat = A (in ANGSTROM ). 
         
         If ~ibrav~ == 0, only A is used if present, and 
         cell vectors are read from card ~CELL_PARAMETERS.~ 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._C

    @C.setter
    def C(self, value: float):
        self._C = value

    @property
    def cosAB(self) -> float:
        """
        Info:
        ================
        
         Traditional crystallographic constants: 
         
         a,b,c in ANGSTROM 
         cosAB = cosine of the angle between axis a and b (gamma) 
         cosAC = cosine of the angle between axis a and c (beta) 
         cosBC = cosine of the angle between axis b and c (alpha) 
         
         The axis are chosen according to the value of ~ibrav.~ 
         Specify either these OR ~celldm~ but NOT both. 
         Only needed values (depending on ~ibrav)~ must be specified. 
         
         The lattice parameter alat = A (in ANGSTROM ). 
         
         If ~ibrav~ == 0, only A is used if present, and 
         cell vectors are read from card ~CELL_PARAMETERS.~ 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._cosAB

    @cosAB.setter
    def cosAB(self, value: float):
        self._cosAB = value

    @property
    def cosAC(self) -> float:
        """
        Info:
        ================
        
         Traditional crystallographic constants: 
         
         a,b,c in ANGSTROM 
         cosAB = cosine of the angle between axis a and b (gamma) 
         cosAC = cosine of the angle between axis a and c (beta) 
         cosBC = cosine of the angle between axis b and c (alpha) 
         
         The axis are chosen according to the value of ~ibrav.~ 
         Specify either these OR ~celldm~ but NOT both. 
         Only needed values (depending on ~ibrav)~ must be specified. 
         
         The lattice parameter alat = A (in ANGSTROM ). 
         
         If ~ibrav~ == 0, only A is used if present, and 
         cell vectors are read from card ~CELL_PARAMETERS.~ 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._cosAC

    @cosAC.setter
    def cosAC(self, value: float):
        self._cosAC = value

    @property
    def cosBC(self) -> float:
        """
        Info:
        ================
        
         Traditional crystallographic constants: 
         
         a,b,c in ANGSTROM 
         cosAB = cosine of the angle between axis a and b (gamma) 
         cosAC = cosine of the angle between axis a and c (beta) 
         cosBC = cosine of the angle between axis b and c (alpha) 
         
         The axis are chosen according to the value of ~ibrav.~ 
         Specify either these OR ~celldm~ but NOT both. 
         Only needed values (depending on ~ibrav)~ must be specified. 
         
         The lattice parameter alat = A (in ANGSTROM ). 
         
         If ~ibrav~ == 0, only A is used if present, and 
         cell vectors are read from card ~CELL_PARAMETERS.~ 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._cosBC

    @cosBC.setter
    def cosBC(self, value: float):
        self._cosBC = value

