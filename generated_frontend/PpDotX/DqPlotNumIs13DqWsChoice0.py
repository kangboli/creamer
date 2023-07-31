from typing import Optional
import string
from .Choice import Choice
from .Choice0 import Choice0


class DqPlotNumIs13DqWsChoice0(Choice, Choice0):
    """
Label:
================

 Options for noncollinear magnetization (plot_num=13): 


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

 0 = absolute value (default value) 
 1 = x component of the magnetization 
 2 = y component of the magnetization 
 3 = z component of the magnetization 


        """
        return self._spin_component

    @spin_component.setter
    def spin_component(self, value: int):
        self._spin_component = value

