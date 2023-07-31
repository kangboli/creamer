from typing import Optional, List
from .Control import Control
from .System import System
from .Electrons import Electrons
from .Ions import Ions
from .Cell import Cell
from .AtomicSpecies import AtomicSpecies
from .AtomicPositions import AtomicPositions
from .KPoints import KPoints
from .CellParameters import CellParameters
from .Constraints import Constraints
from .Occupations import Occupations
from .AtomicVelocities import AtomicVelocities
from .AtomicForces import AtomicForces


class PwDotX:
    """
    Intro:
    ================
    
     **Input data format:** { } = optional, [ ] = it depends, | = or 
     
     All quantities whose dimensions are not explicitly specified are in 
     RYDBERG ATOMIC UNITS. Charge is "number" charge (i.e. not multiplied 
     by e); potentials are in energy units (i.e. they are multiplied by e). 
     
     **BEWARE:** TABS, DOS <CR><LF> CHARACTERS ARE POTENTIAL SOURCES OF TROUBLE 
     
     Namelists must appear in the order given below. 
     Comment lines in *namelists* can be introduced by a "!", exactly as in 
     fortran code. Comments lines in *cards* can be introduced by 
     either a "!" or a "#" character in the first position of a line. 
     Do not start any line in *cards* with a "/" character. 
     Leave a space between card names and card options, e.g. 
     ATOMIC_POSITIONS (bohr), not ATOMIC_POSITIONS(bohr) 
     Do not start any line in *cards* with a "/" character. 
     
     
     **Structure of the input data:** 
     =============================================================================== 
     
     **&CONTROL** 
     ... 
     **/** 
     
     **&SYSTEM** 
     ... 
     **/** 
     
     **&ELECTRONS** 
     ... 
     **/** 
     
     [ **&IONS** 
     ... 
     **/** ] 
     
     [ **&CELL** 
     ... 
     **/** ] 
     
     **ATOMIC_SPECIES** 
     X Mass_X PseudoPot_X 
     Y Mass_Y PseudoPot_Y 
     Z Mass_Z PseudoPot_Z 
     
     **ATOMIC_POSITIONS** { alat | bohr | crystal | angstrom | crystal_sg } 
     X 0.0 0.0 0.0 {if_pos(1) if_pos(2) if_pos(3)} 
     Y 0.5 0.0 0.0 
     Z O.0 0.2 0.2 
     
     **K_POINTS** { tpiba | automatic | crystal | gamma | tpiba_b | crystal_b | tpiba_c | crystal_c } 
     if (gamma) 
     nothing to read 
     if (automatic) 
     nk1, nk2, nk3, k1, k2, k3 
     if (not automatic) 
     nks 
     xk_x, xk_y, xk_z, wk 
     if (tpipa_b or crystal_b in a 'bands' calculation) see Doc/brillouin_zones.pdf 
     
     [ **CELL_PARAMETERS** { alat | bohr | angstrom } 
     v1(1) v1(2) v1(3) 
     v2(1) v2(2) v2(3) 
     v3(1) v3(2) v3(3) ] 
     
     [ **OCCUPATIONS** 
     f_inp1(1) f_inp1(2) f_inp1(3) ... f_inp1(10) 
     f_inp1(11) f_inp1(12) ... f_inp1(nbnd) 
     [ f_inp2(1) f_inp2(2) f_inp2(3) ... f_inp2(10) 
     f_inp2(11) f_inp2(12) ... f_inp2(nbnd) ] ] 
     
     [ **CONSTRAINTS** 
     nconstr { constr_tol } 
     constr_type(.) constr(1,.) constr(2,.) [ constr(3,.) constr(4,.) ] { constr_target(.) } ] 
     
     [ **ATOMIC_FORCES** 
     label_1 Fx(1) Fy(1) Fz(1) 
     ..... 
     label_n Fx(n) Fy(n) Fz(n) ] 


    """

    def __init__(self,
                 control_namelist: Optional[Control] = Control(),
                 system_namelist: Optional[System] = System(),
                 electrons_namelist: Optional[Electrons] = Electrons(),
                 ions_namelist: Optional[Ions] = Ions(),
                 cell_namelist: Optional[Cell] = Cell(),
                 atomic_species_card: Optional[AtomicSpecies] = AtomicSpecies(),
                 atomic_positions_card: Optional[AtomicPositions] = AtomicPositions(),
                 k_points_card: Optional[KPoints] = KPoints(),
                 cell_parameters_card: Optional[CellParameters] = CellParameters(),
                 constraints_card: Optional[Constraints] = Constraints(),
                 occupations_card: Optional[Occupations] = Occupations(),
                 atomic_velocities_card: Optional[AtomicVelocities] = AtomicVelocities(),
                 atomic_forces_card: Optional[AtomicForces] = AtomicForces(),
                 ):
        """
        Parameters
        ----------
        **control_namelist**: Control

        **system_namelist**: System

        **electrons_namelist**: Electrons

        **ions_namelist**: Ions

        **cell_namelist**: Cell

        **atomic_species_card**: AtomicSpecies

        **atomic_positions_card**: AtomicPositions

        **k_points_card**: KPoints

        **cell_parameters_card**: CellParameters

        **constraints_card**: Constraints

        **occupations_card**: Occupations

        **atomic_velocities_card**: AtomicVelocities

        **atomic_forces_card**: AtomicForces

            Quantum Espresso Version
            ------------------------
            Not yet implemented.
        """
        self._control_namelist: Optional[Control] = control_namelist
        self._system_namelist: Optional[System] = system_namelist
        self._electrons_namelist: Optional[Electrons] = electrons_namelist
        self._ions_namelist: Optional[Ions] = ions_namelist
        self._cell_namelist: Optional[Cell] = cell_namelist
        self._atomic_species_card: Optional[AtomicSpecies] = atomic_species_card
        self._atomic_positions_card: Optional[AtomicPositions] = atomic_positions_card
        self._k_points_card: Optional[KPoints] = k_points_card
        self._cell_parameters_card: Optional[CellParameters] = cell_parameters_card
        self._constraints_card: Optional[Constraints] = constraints_card
        self._occupations_card: Optional[Occupations] = occupations_card
        self._atomic_velocities_card: Optional[AtomicVelocities] = atomic_velocities_card
        self._atomic_forces_card: Optional[AtomicForces] = atomic_forces_card

    @property
    def control_namelist(self) -> Control:
        """
        """
        return self._control_namelist

    @control_namelist.setter
    def control_namelist(self, value: Control):
        self._control_namelist = value

    @property
    def system_namelist(self) -> System:
        """
        """
        return self._system_namelist

    @system_namelist.setter
    def system_namelist(self, value: System):
        self._system_namelist = value

    @property
    def electrons_namelist(self) -> Electrons:
        """
        """
        return self._electrons_namelist

    @electrons_namelist.setter
    def electrons_namelist(self, value: Electrons):
        self._electrons_namelist = value

    @property
    def ions_namelist(self) -> Ions:
        """
        """
        return self._ions_namelist

    @ions_namelist.setter
    def ions_namelist(self, value: Ions):
        self._ions_namelist = value

    @property
    def cell_namelist(self) -> Cell:
        """
        """
        return self._cell_namelist

    @cell_namelist.setter
    def cell_namelist(self, value: Cell):
        self._cell_namelist = value

    @property
    def atomic_species_card(self) -> AtomicSpecies:
        """
        """
        return self._atomic_species_card

    @atomic_species_card.setter
    def atomic_species_card(self, value: AtomicSpecies):
        self._atomic_species_card = value

    @property
    def atomic_positions_card(self) -> AtomicPositions:
        """
        """
        return self._atomic_positions_card

    @atomic_positions_card.setter
    def atomic_positions_card(self, value: AtomicPositions):
        self._atomic_positions_card = value

    @property
    def k_points_card(self) -> KPoints:
        """
        """
        return self._k_points_card

    @k_points_card.setter
    def k_points_card(self, value: KPoints):
        self._k_points_card = value

    @property
    def cell_parameters_card(self) -> CellParameters:
        """
        """
        return self._cell_parameters_card

    @cell_parameters_card.setter
    def cell_parameters_card(self, value: CellParameters):
        self._cell_parameters_card = value

    @property
    def constraints_card(self) -> Constraints:
        """
        """
        return self._constraints_card

    @constraints_card.setter
    def constraints_card(self, value: Constraints):
        self._constraints_card = value

    @property
    def occupations_card(self) -> Occupations:
        """
        """
        return self._occupations_card

    @occupations_card.setter
    def occupations_card(self, value: Occupations):
        self._occupations_card = value

    @property
    def atomic_velocities_card(self) -> AtomicVelocities:
        """
        """
        return self._atomic_velocities_card

    @atomic_velocities_card.setter
    def atomic_velocities_card(self, value: AtomicVelocities):
        self._atomic_velocities_card = value

    @property
    def atomic_forces_card(self) -> AtomicForces:
        """
        """
        return self._atomic_forces_card

    @atomic_forces_card.setter
    def atomic_forces_card(self, value: AtomicForces):
        self._atomic_forces_card = value

