from typing import Optional
import string
from .Choice import Choice
from .Choice0 import Choice0


class DqPlotNumIs3DqWsChoice0(Choice, Choice0):
    """
Label:
================

 Options for LDOS (plot_num=3): 
 LDOS is plotted on grid [emin, emax] with spacing delta_e. 


    """

    def __init__(self,
                 emin: Optional[float] = None,
                 emax: Optional[float] = None,
                 delta_e: Optional[float] = None,
                 degauss_ldos: Optional[float] = None,
                 ):
        self._emin: Optional[float] = emin
        self._emax: Optional[float] = emax
        self._delta_e: Optional[float] = delta_e
        self._degauss_ldos: Optional[float] = degauss_ldos

    @property
    def emin(self) -> float:
        """
Info:
================

 lower boundary of energy grid (in eV). 
 
 Defaults to Fermi energy. 


        """
        return self._emin

    @emin.setter
    def emin(self, value: float):
        self._emin = value

    @property
    def emax(self) -> float:
        """
Info:
================

 upper boundary of energy grid (in eV). 
 
 Defaults to Fermi energy. 


        """
        return self._emax

    @emax.setter
    def emax(self, value: float):
        self._emax = value

    @property
    def delta_e(self) -> float:
        """
Info:
================

 spacing of energy grid (in eV). 


        """
        return self._delta_e

    @delta_e.setter
    def delta_e(self, value: float):
        self._delta_e = value

    @property
    def degauss_ldos(self) -> float:
        """
Default:
================
degauss (converted to eV) 
 broadening of energy levels for LDOS (in eV). 
 
 Defaults to broadening degauss specified for electronic smearing 
 in pw.x calculation. 


Info:
================

 broadening of energy levels for LDOS (in eV). 
 
 Defaults to broadening degauss specified for electronic smearing 
 in pw.x calculation. 


        """
        return self._degauss_ldos

    @degauss_ldos.setter
    def degauss_ldos(self, value: float):
        self._degauss_ldos = value

