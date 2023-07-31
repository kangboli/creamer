from typing import Optional, List
from .Namelist import Namelist
from .IonPositionsOptions import IonPositionsOptions
from .IonVelocitiesOptions import IonVelocitiesOptions
from .IonDynamicsOptions import IonDynamicsOptions
from .PotExtrapolationOptions import PotExtrapolationOptions
from .WfcExtrapolationOptions import WfcExtrapolationOptions
from .Group2 import Group2
from .Group3 import Group3


class Ions(Namelist):
    """
    Label:
    ================
    
     REQUIRED if ~calculation~ == 'relax', 'md', 'vc-relax', or 'vc-md' 
     OPTIONAL for ~calculation~ == 'scf' (only ~ion_positions~ is used) 


    """

    def __init__(self,
                 ion_positions: Optional[IonPositionsOptions] = None,
                 ion_velocities: Optional[IonVelocitiesOptions] = None,
                 ion_dynamics: Optional[IonDynamicsOptions] = None,
                 pot_extrapolation: Optional[PotExtrapolationOptions] = None,
                 wfc_extrapolation: Optional[WfcExtrapolationOptions] = None,
                 remove_rigid_rot: Optional[bool] = None,
                 ):
        """
        Parameters
        ----------
        **ion_positions**: IonPositionsOptions
            *Default*:             'default'



        **ion_velocities**: IonVelocitiesOptions
            *Default*:             'default'



        **ion_dynamics**: IonDynamicsOptions

        **pot_extrapolation**: PotExtrapolationOptions
            *Default*:             'atomic'



        **wfc_extrapolation**: WfcExtrapolationOptions
            *Default*:             'none'



        **remove_rigid_rot**: bool
            *Default*:             .FALSE.


            *Info*:             
             This keyword is useful when simulating the dynamics and/or the 
             thermodynamics of an isolated system. If set to true the total 
             torque of the internal forces is set to zero by adding new forces 
             that compensate the spurious interaction with the periodic 
             images. This allows for the use of smaller supercells. 
             
             BEWARE: since the potential energy is no longer consistent with 
             the forces (it still contains the spurious interaction with the 
             repeated images), the total energy is not conserved anymore. 
             However the dynamical and thermodynamical properties should be 
             in closer agreement with those of an isolated system. 
             Also the final energy of a structural relaxation will be higher, 
             but the relaxation itself should be faster. 



            Quantum Espresso Version
            ------------------------
            Not yet implemented.
        """
        self._ion_positions: Optional[IonPositionsOptions] = ion_positions
        self._ion_velocities: Optional[IonVelocitiesOptions] = ion_velocities
        self._ion_dynamics: Optional[IonDynamicsOptions] = ion_dynamics
        self._pot_extrapolation: Optional[PotExtrapolationOptions] = pot_extrapolation
        self._wfc_extrapolation: Optional[WfcExtrapolationOptions] = wfc_extrapolation
        self._remove_rigid_rot: Optional[bool] = remove_rigid_rot

    @property
    def ion_positions(self) -> IonPositionsOptions:
        """
        Default:
        ================
        'default'



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._ion_positions

    @ion_positions.setter
    def ion_positions(self, value: IonPositionsOptions):
        self._ion_positions = value

    @property
    def ion_velocities(self) -> IonVelocitiesOptions:
        """
        Default:
        ================
        'default'



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._ion_velocities

    @ion_velocities.setter
    def ion_velocities(self, value: IonVelocitiesOptions):
        self._ion_velocities = value

    @property
    def ion_dynamics(self) -> IonDynamicsOptions:
        """
        """
        return self._ion_dynamics

    @ion_dynamics.setter
    def ion_dynamics(self, value: IonDynamicsOptions):
        self._ion_dynamics = value

    @property
    def pot_extrapolation(self) -> PotExtrapolationOptions:
        """
        Default:
        ================
        'atomic'



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._pot_extrapolation

    @pot_extrapolation.setter
    def pot_extrapolation(self, value: PotExtrapolationOptions):
        self._pot_extrapolation = value

    @property
    def wfc_extrapolation(self) -> WfcExtrapolationOptions:
        """
        Default:
        ================
        'none'



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._wfc_extrapolation

    @wfc_extrapolation.setter
    def wfc_extrapolation(self, value: WfcExtrapolationOptions):
        self._wfc_extrapolation = value

    @property
    def remove_rigid_rot(self) -> bool:
        """
        Default:
        ================
        .FALSE.


        Info:
        ================
        
         This keyword is useful when simulating the dynamics and/or the 
         thermodynamics of an isolated system. If set to true the total 
         torque of the internal forces is set to zero by adding new forces 
         that compensate the spurious interaction with the periodic 
         images. This allows for the use of smaller supercells. 
         
         BEWARE: since the potential energy is no longer consistent with 
         the forces (it still contains the spurious interaction with the 
         repeated images), the total energy is not conserved anymore. 
         However the dynamical and thermodynamical properties should be 
         in closer agreement with those of an isolated system. 
         Also the final energy of a structural relaxation will be higher, 
         but the relaxation itself should be faster. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._remove_rigid_rot

    @remove_rigid_rot.setter
    def remove_rigid_rot(self, value: bool):
        self._remove_rigid_rot = value

