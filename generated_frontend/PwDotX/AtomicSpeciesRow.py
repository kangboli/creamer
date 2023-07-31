from typing import Optional, List
import string
from .Row import Row


class AtomicSpeciesRow(Row):
    """
    Others:
    ================
    -start 1 -end ntyp 


    Quantum Espresso Version:
    =========================
    Not yet implemented.
    """

    def __init__(self,
                 X: Optional[string] = None,
                 Mass_X: Optional[float] = None,
                 PseudoPot_X: Optional[string] = None,
                 ):
        """
        Parameters
        ----------
        **X**: string
            *Info*:             
             label of the atom. Acceptable syntax: 
             chemical symbol X (1 or 2 characters, case-insensitive) 
             or chemical symbol plus a number or a letter, as in 
             "Xn" (e.g. Fe1) or "X_*" or "X-*" (e.g. C1, C_h; 
             max total length cannot exceed 3 characters) 



        **Mass_X**: float
            *Info*:             
             mass of the atomic species [amu: mass of C = 12] 
             Used only when performing Molecular Dynamics run 
             or structural optimization runs using Damped MD. 
             Not actually used in all other cases (but stored 
             in data files, so phonon calculations will use 
             these values unless other values are provided) 



        **PseudoPot_X**: string
            *Info*:             
             File containing PP for this species. 
             
             The pseudopotential file is assumed to be in the new UPF format. 
             If it doesn't work, the pseudopotential format is determined by 
             the file name: 
             
             *.vdb or *.van Vanderbilt US pseudopotential code 
             *.RRKJ3 Andrea Dal Corso's code (old format) 
             none of the above old PWscf norm-conserving format 



            Quantum Espresso Version
            ------------------------
            Not yet implemented.
        """
        self._X: Optional[string] = X
        self._Mass_X: Optional[float] = Mass_X
        self._PseudoPot_X: Optional[string] = PseudoPot_X

    @property
    def X(self) -> string:
        """
        Info:
        ================
        
         label of the atom. Acceptable syntax: 
         chemical symbol X (1 or 2 characters, case-insensitive) 
         or chemical symbol plus a number or a letter, as in 
         "Xn" (e.g. Fe1) or "X_*" or "X-*" (e.g. C1, C_h; 
         max total length cannot exceed 3 characters) 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._X

    @X.setter
    def X(self, value: string):
        self._X = value

    @property
    def Mass_X(self) -> float:
        """
        Info:
        ================
        
         mass of the atomic species [amu: mass of C = 12] 
         Used only when performing Molecular Dynamics run 
         or structural optimization runs using Damped MD. 
         Not actually used in all other cases (but stored 
         in data files, so phonon calculations will use 
         these values unless other values are provided) 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._Mass_X

    @Mass_X.setter
    def Mass_X(self, value: float):
        self._Mass_X = value

    @property
    def PseudoPot_X(self) -> string:
        """
        Info:
        ================
        
         File containing PP for this species. 
         
         The pseudopotential file is assumed to be in the new UPF format. 
         If it doesn't work, the pseudopotential format is determined by 
         the file name: 
         
         *.vdb or *.van Vanderbilt US pseudopotential code 
         *.RRKJ3 Andrea Dal Corso's code (old format) 
         none of the above old PWscf norm-conserving format 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._PseudoPot_X

    @PseudoPot_X.setter
    def PseudoPot_X(self, value: string):
        self._PseudoPot_X = value

