from typing import Optional
import string
from .Choice import Choice
from .Choice0 import Choice0


class DqPlotNumIs5DqWsChoice0(Choice, Choice0):
    """
Label:
================

 Options for STM images (plot_num=5): 


    """

    def __init__(self,
                 sample_bias: Optional[float] = None,
                 ):
        self._sample_bias: Optional[float] = sample_bias

    @property
    def sample_bias(self) -> float:
        """
Info:
================

 the bias of the sample (Ry) in stm images 


        """
        return self._sample_bias

    @sample_bias.setter
    def sample_bias(self, value: float):
        self._sample_bias = value

