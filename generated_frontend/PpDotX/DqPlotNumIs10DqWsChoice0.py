from typing import Optional
import string
from .Choice import Choice
from .Choice0 import Choice0


class DqPlotNumIs10DqWsChoice0(Choice, Choice0):
    """
Label:
================

 Options for ILDOS (plot_num=10): 


    """

    def __init__(self,
                 emin: Optional[float] = None,
                 emax: Optional[float] = None,
                 spin_component: Optional[int] = None,
                 ):
        self._emin: Optional[float] = emin
        self._emax: Optional[float] = emax
        self._spin_component: Optional[int] = spin_component

    @property
    def emin(self) -> float:
        """
Info:
================

 lower energy boundary (in eV) 


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

 upper energy boundary (in eV), 
 i.e. compute ILDOS from __emin__ to __emax__ 


        """
        return self._emax

    @emax.setter
    def emax(self, value: float):
        self._emax = value

    @property
    def spin_component(self) -> int:
        """
Info:
================

 for LSDA case only: plot the contribution to ILDOS of 
 0 = spin-up + spin-down (default) 
 1 = spin-up only 
 2 = spin-down only 


        """
        return self._spin_component

    @spin_component.setter
    def spin_component(self, value: int):
        self._spin_component = value

