from typing import Optional, List
from .Card import Card
from .FlagLatticeTypeOptions import FlagLatticeTypeOptions
from .LatticeEntry import LatticeEntry


class CellParameters(Card):
    """
    Label:
    ================
    
     Optional card, needed only if ~ibrav~ == 0 is specified, ignored otherwise ! 


    """

    def __init__(self,
                 flag_lattice_type: Optional[FlagLatticeTypeOptions] = None,
                 table: Optional[List[LatticeEntry]] = List[LatticeEntry](),
                 ):
        """
        Parameters
        ----------
        **flag_lattice_type**: FlagLatticeTypeOptions
            *Info*:             
             Unit for lattice vectors; options are: 
             
             **'bohr'** / **'angstrom':** 
             lattice vectors in bohr-radii / angstrom. 
             In this case the lattice parameter alat = sqrt(v1*v1). 
             
             **'alat'** / nothing specified: 
             lattice vectors in units of the lattice parameter (either 
             ~celldm(1)~ or ~A).~ Not specifying units is DEPRECATED 
             and will not be allowed in the future. 
             
             If neither unit nor lattice parameter are specified, 
             'bohr' is assumed - DEPRECATED, will no longer be allowed 



        **table**: List[LatticeEntry]

            Quantum Espresso Version
            ------------------------
            Not yet implemented.
        """
        self._flag_lattice_type: Optional[FlagLatticeTypeOptions] = flag_lattice_type
        self._table: Optional[List[LatticeEntry]] = table

    @property
    def flag_lattice_type(self) -> FlagLatticeTypeOptions:
        """
        Info:
        ================
        
         Unit for lattice vectors; options are: 
         
         **'bohr'** / **'angstrom':** 
         lattice vectors in bohr-radii / angstrom. 
         In this case the lattice parameter alat = sqrt(v1*v1). 
         
         **'alat'** / nothing specified: 
         lattice vectors in units of the lattice parameter (either 
         ~celldm(1)~ or ~A).~ Not specifying units is DEPRECATED 
         and will not be allowed in the future. 
         
         If neither unit nor lattice parameter are specified, 
         'bohr' is assumed - DEPRECATED, will no longer be allowed 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._flag_lattice_type

    @flag_lattice_type.setter
    def flag_lattice_type(self, value: FlagLatticeTypeOptions):
        self._flag_lattice_type = value

    @property
    def table(self) -> List[LatticeEntry]:
        """
        """
        return self._table

    @table.setter
    def table(self, value: List[LatticeEntry]):
        self._table = value

