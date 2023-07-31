from typing import Optional, List
from .Row import Row
from .ConstrTypeOptions import ConstrTypeOptions


class ConstraintsTableEntry(Row):
    """
    Others:
    ================
    -start 1 -end nconstr 


    Quantum Espresso Version:
    =========================
    Not yet implemented.
    """

    def __init__(self,
                 constr_type: Optional[ConstrTypeOptions] = None,
                 constr__lp__1__rp__: Optional[str] = None,
                 constr__lp__2__rp__: Optional[str] = None,
                 constr_target: Optional[float] = None,
                 ):
        """
        Parameters
        ----------
        **constr_type**: ConstrTypeOptions

        **constr__lp__1__rp__**: str
            *Info*:             
             These variables have different meanings for different constraint types: 
             
             **'type_coord'** : 
             *constr(1)* is the first index of the atomic type involved 
             *constr(2)* is the second index of the atomic type involved 
             *constr(3)* is the cut-off radius for estimating the coordination 
             *constr(4)* is a smoothing parameter 
             
             **'atom_coord'** : 
             *constr(1)* is the atom index of the atom with constrained coordination 
             *constr(2)* is the index of the atomic type involved in the coordination 
             *constr(3)* is the cut-off radius for estimating the coordination 
             *constr(4)* is a smoothing parameter 
             
             **'distance'** : 
             atoms indices object of the constraint, as they appear in 
             the ~ATOMIC_POSITIONS~ card 
             
             **'planar_angle',** **'torsional_angle'** : 
             atoms indices object of the constraint, as they appear in the 
             ~ATOMIC_POSITIONS~ card (beware the order) 
             
             **'bennett_proj'** : 
             *constr(1)* is the index of the atom whose position is constrained. 
             *constr(2:4)* are the three coordinates of the vector that specifies 
             the constraint direction. 



        **constr__lp__2__rp__**: str
            *Info*:             
             These variables have different meanings for different constraint types: 
             
             **'type_coord'** : 
             *constr(1)* is the first index of the atomic type involved 
             *constr(2)* is the second index of the atomic type involved 
             *constr(3)* is the cut-off radius for estimating the coordination 
             *constr(4)* is a smoothing parameter 
             
             **'atom_coord'** : 
             *constr(1)* is the atom index of the atom with constrained coordination 
             *constr(2)* is the index of the atomic type involved in the coordination 
             *constr(3)* is the cut-off radius for estimating the coordination 
             *constr(4)* is a smoothing parameter 
             
             **'distance'** : 
             atoms indices object of the constraint, as they appear in 
             the ~ATOMIC_POSITIONS~ card 
             
             **'planar_angle',** **'torsional_angle'** : 
             atoms indices object of the constraint, as they appear in the 
             ~ATOMIC_POSITIONS~ card (beware the order) 
             
             **'bennett_proj'** : 
             *constr(1)* is the index of the atom whose position is constrained. 
             *constr(2:4)* are the three coordinates of the vector that specifies 
             the constraint direction. 



        **constr_target**: float
            *Info*:             
             Target for the constrain ( angles are specified in degrees ). 
             This variable is optional. 



            Quantum Espresso Version
            ------------------------
            Not yet implemented.
        """
        self._constr_type: Optional[ConstrTypeOptions] = constr_type
        self._constr__lp__1__rp__: Optional[str] = constr__lp__1__rp__
        self._constr__lp__2__rp__: Optional[str] = constr__lp__2__rp__
        self._constr_target: Optional[float] = constr_target

    @property
    def constr_type(self) -> ConstrTypeOptions:
        """
        """
        return self._constr_type

    @constr_type.setter
    def constr_type(self, value: ConstrTypeOptions):
        self._constr_type = value

    @property
    def constr__lp__1__rp__(self) -> str:
        """
        Info:
        ================
        
         These variables have different meanings for different constraint types: 
         
         **'type_coord'** : 
         *constr(1)* is the first index of the atomic type involved 
         *constr(2)* is the second index of the atomic type involved 
         *constr(3)* is the cut-off radius for estimating the coordination 
         *constr(4)* is a smoothing parameter 
         
         **'atom_coord'** : 
         *constr(1)* is the atom index of the atom with constrained coordination 
         *constr(2)* is the index of the atomic type involved in the coordination 
         *constr(3)* is the cut-off radius for estimating the coordination 
         *constr(4)* is a smoothing parameter 
         
         **'distance'** : 
         atoms indices object of the constraint, as they appear in 
         the ~ATOMIC_POSITIONS~ card 
         
         **'planar_angle',** **'torsional_angle'** : 
         atoms indices object of the constraint, as they appear in the 
         ~ATOMIC_POSITIONS~ card (beware the order) 
         
         **'bennett_proj'** : 
         *constr(1)* is the index of the atom whose position is constrained. 
         *constr(2:4)* are the three coordinates of the vector that specifies 
         the constraint direction. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._constr__lp__1__rp__

    @constr__lp__1__rp__.setter
    def constr__lp__1__rp__(self, value: str):
        self._constr__lp__1__rp__ = value

    @property
    def constr__lp__2__rp__(self) -> str:
        """
        Info:
        ================
        
         These variables have different meanings for different constraint types: 
         
         **'type_coord'** : 
         *constr(1)* is the first index of the atomic type involved 
         *constr(2)* is the second index of the atomic type involved 
         *constr(3)* is the cut-off radius for estimating the coordination 
         *constr(4)* is a smoothing parameter 
         
         **'atom_coord'** : 
         *constr(1)* is the atom index of the atom with constrained coordination 
         *constr(2)* is the index of the atomic type involved in the coordination 
         *constr(3)* is the cut-off radius for estimating the coordination 
         *constr(4)* is a smoothing parameter 
         
         **'distance'** : 
         atoms indices object of the constraint, as they appear in 
         the ~ATOMIC_POSITIONS~ card 
         
         **'planar_angle',** **'torsional_angle'** : 
         atoms indices object of the constraint, as they appear in the 
         ~ATOMIC_POSITIONS~ card (beware the order) 
         
         **'bennett_proj'** : 
         *constr(1)* is the index of the atom whose position is constrained. 
         *constr(2:4)* are the three coordinates of the vector that specifies 
         the constraint direction. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._constr__lp__2__rp__

    @constr__lp__2__rp__.setter
    def constr__lp__2__rp__(self, value: str):
        self._constr__lp__2__rp__ = value

    @property
    def constr_target(self) -> float:
        """
        Info:
        ================
        
         Target for the constrain ( angles are specified in degrees ). 
         This variable is optional. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._constr_target

    @constr_target.setter
    def constr_target(self, value: float):
        self._constr_target = value

