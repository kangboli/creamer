from typing import Optional, List
from .Group import Group


class Group0(Group):
    """
    Message:
    ================
    
     **BEWARE:** atomic coordinates are read from the first file; 
     if their number is different for different files, 
     the first file must have the largest number of atoms 


    """

    def __init__(self,
                 filepp: Optional[List[str]] = None,
                 weight: Optional[List[float]] = None,
                 ):
        """
        Parameters
        ----------
        **filepp**: List[str]
            *Default*:             filepp(1)=filplot


            *Info*:             
             nfile = 1 : file containing the quantity to be plotted 
             nfile > 1 : see ~weight~ 


            *Others*:             Start - 1; End - nfile



        **weight**: List[float]
            *Default*:             weight(1)=1.0


            *Info*:             
             weighing factors: assuming that rho(i) is the quantity 
             read from filepp(i), the quantity that will be plotted is: 
             
             weight(1)*rho(1) + weight(2)*rho(2) + weight(3)*rho(3) + ... 


            *Others*:             Start - 1; End - nfile



            Quantum Espresso Version
            ------------------------
            Not yet implemented.
        """
        self._filepp: Optional[List[str]] = filepp
        self._weight: Optional[List[float]] = weight

    @property
    def filepp(self) -> List[str]:
        """
        Default:
        ================
        filepp(1)=filplot


        Info:
        ================
        
         nfile = 1 : file containing the quantity to be plotted 
         nfile > 1 : see ~weight~ 


        Others:
        ================
        Start - 1; End - nfile

        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._filepp

    @filepp.setter
    def filepp(self, value: List[str]):
        self._filepp = value

    @property
    def weight(self) -> List[float]:
        """
        Default:
        ================
        weight(1)=1.0


        Info:
        ================
        
         weighing factors: assuming that rho(i) is the quantity 
         read from filepp(i), the quantity that will be plotted is: 
         
         weight(1)*rho(1) + weight(2)*rho(2) + weight(3)*rho(3) + ... 


        Others:
        ================
        Start - 1; End - nfile

        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._weight

    @weight.setter
    def weight(self, value: List[float]):
        self._weight = value

