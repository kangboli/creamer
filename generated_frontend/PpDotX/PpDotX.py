from typing import Optional, List
from .Inputpp import Inputpp
from .Plot import Plot


class PpDotX:
    """
    Intro:
    ================
    
     **Purpose of pp.x:** data analysis and plotting. 
     
     The code performs two steps: 
     
     (1) reads the output produced by **pw.x,** extracts and calculates 
     the desired quantity/quantities (rho, V, ...) 
     
     (2) writes the desired quantity to file in a suitable format for 
     various types of plotting and various plotting programs 
     
     The input data of this program is read from standard input 
     or from file and has the following format: 
     
     NAMELIST **&INPUTPP** 
     containing the variables for step (1), followed by 
     
     NAMELIST **&PLOT** 
     containing the variables for step (2) 
     
     The two steps can be performed independently. In order to perform 
     only step (2), leave namelist **&INPUTPP** blank. In order to perform 
     only step (1), do not specify namelist **&PLOT** 
     
     Intermediate results from step 1 can be saved to disk (see 
     variable ~filplot~ in **&INPUTPP)** and later read in step 2. 
     Since the file with intermediate results is formatted, it 
     can be safely transferred to a different machine. This 
     also allows plotting of a linear combination (for instance, 
     charge differences) by saving two intermediate files and 
     combining them (see variables ~weight~ and ~filepp~ in **&PLOT)** 
     
     All output quantities are in ATOMIC (RYDBERG) UNITS unless 
     otherwise explicitly specified. 
     All charge densities integrate to the NUMBER of electrons 
     not to the total charge. 
     All potentials have the dimension of an energy (e*V, not V). 


    """

    def __init__(self,
                 inputpp_namelist: Optional[Inputpp] = Inputpp(),
                 plot_namelist: Optional[Plot] = Plot(),
                 ):
        """
        Parameters
        ----------
        **inputpp_namelist**: Inputpp

        **plot_namelist**: Plot

            Quantum Espresso Version
            ------------------------
            Not yet implemented.
        """
        self._inputpp_namelist: Optional[Inputpp] = inputpp_namelist
        self._plot_namelist: Optional[Plot] = plot_namelist

    @property
    def inputpp_namelist(self) -> Inputpp:
        """
        """
        return self._inputpp_namelist

    @inputpp_namelist.setter
    def inputpp_namelist(self, value: Inputpp):
        self._inputpp_namelist = value

    @property
    def plot_namelist(self) -> Plot:
        """
        """
        return self._plot_namelist

    @plot_namelist.setter
    def plot_namelist(self, value: Plot):
        self._plot_namelist = value

