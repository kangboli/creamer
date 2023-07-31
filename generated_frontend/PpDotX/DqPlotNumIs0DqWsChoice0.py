from typing import Optional
import string
from .Choice import Choice
from .Choice0 import Choice0


class DqPlotNumIs0DqWsChoice0(Choice, Choice0):
    """
Label:
================

 Options for total charge (plot_num=0): 


    """

    def __init__(self,
                 spin_component: Optional[int] = None,
                 ):
        self._spin_component: Optional[int] = spin_component

    @property
    def spin_component(self) -> int:
        """
Info:
================

 0 = total charge (default value), 
 1 = spin up charge, 
 2 = spin down charge. 


        """
        return self._spin_component

    @spin_component.setter
    def spin_component(self, value: int):
        self._spin_component = value

