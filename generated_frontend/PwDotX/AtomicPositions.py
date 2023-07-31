from typing import Optional, List
from .Card import Card
from .FlagAtomposUnitOptions import FlagAtomposUnitOptions
from .FlagAtomposUnitOptions import FlagAtomposUnitOptions
from .Choice0 import Choice0


class AtomicPositions(Card):
    """
    """

    def __init__(self,
                 flag_atompos_unit: Optional[FlagAtomposUnitOptions] = None,
                 choice0: Optional[Choice0] = Choice0(),
                 ):
        """
        Parameters
        ----------
        **flag_atompos_unit**: FlagAtomposUnitOptions
            *Default*:             (DEPRECATED) alat



        **choice0**: Choice0

            Quantum Espresso Version
            ------------------------
            Not yet implemented.
        """
        self._flag_atompos_unit: Optional[FlagAtomposUnitOptions] = flag_atompos_unit
        self._choice0: Optional[Choice0] = choice0

    @property
    def flag_atompos_unit(self) -> FlagAtomposUnitOptions:
        """
        Default:
        ================
        (DEPRECATED) alat



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._flag_atompos_unit

    @flag_atompos_unit.setter
    def flag_atompos_unit(self, value: FlagAtomposUnitOptions):
        self._flag_atompos_unit = value

    @property
    def choice0(self) -> Choice0:
        """
        """
        return self._choice0

    @choice0.setter
    def choice0(self, value: Choice0):
        self._choice0 = value

