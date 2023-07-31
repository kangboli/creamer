from typing import Optional, List
from .Card import Card
from .ConstraintsTableEntry import ConstraintsTableEntry


class Constraints(Card):
    """
    Label:
    ================
    
     Optional card, used for constrained dynamics or constrained optimisations 
     (only if ~ion_dynamics=='damp'~ or 'verlet', variable-cell excepted) 
     
     When this card is present the SHAKE algorithm is automatically used. 


    Message:
    ================
    
     When this card is present the SHAKE algorithm is automatically used. 


    """

    def __init__(self,
                 nconstr: Optional[int] = None,
                 constr_tol: Optional[float] = None,
                 table: Optional[List[ConstraintsTableEntry]] = List[ConstraintsTableEntry](),
                 ):
        """
        Parameters
        ----------
        **nconstr**: int
            *Info*:             Number of constraints.



        **constr_tol**: float
            *Info*:             Tolerance for keeping the constraints satisfied.



        **table**: List[ConstraintsTableEntry]

            Quantum Espresso Version
            ------------------------
            Not yet implemented.
        """
        self._nconstr: Optional[int] = nconstr
        self._constr_tol: Optional[float] = constr_tol
        self._table: Optional[List[ConstraintsTableEntry]] = table

    @property
    def nconstr(self) -> int:
        """
        Info:
        ================
        Number of constraints.



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._nconstr

    @nconstr.setter
    def nconstr(self, value: int):
        self._nconstr = value

    @property
    def constr_tol(self) -> float:
        """
        Info:
        ================
        Tolerance for keeping the constraints satisfied.



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._constr_tol

    @constr_tol.setter
    def constr_tol(self, value: float):
        self._constr_tol = value

    @property
    def table(self) -> List[ConstraintsTableEntry]:
        """
        """
        return self._table

    @table.setter
    def table(self, value: List[ConstraintsTableEntry]):
        self._table = value

