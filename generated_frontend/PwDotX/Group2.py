from typing import Optional, List
from .Group import Group
from .IonTemperatureOptions import IonTemperatureOptions


class Group2(Group):
    """
    Label:
    ================
    
     variables used for molecular dynamics 


    """

    def __init__(self,
                 ion_temperature: Optional[IonTemperatureOptions] = None,
                 tempw: Optional[float] = None,
                 tolp: Optional[float] = None,
                 delta_t: Optional[float] = None,
                 nraise: Optional[int] = None,
                 refold_pos: Optional[bool] = None,
                 ):
        """
        Parameters
        ----------
        **ion_temperature**: IonTemperatureOptions
            *Default*:             'not_controlled'



        **tempw**: float
            *Default*:             300.D0


            *Info*:             
             Starting temperature (Kelvin) in MD runs 
             target temperature for most thermostats. 



        **tolp**: float
            *Default*:             100.D0


            *Info*:             
             Tolerance for velocity rescaling. Velocities are rescaled if 
             the run-averaged and target temperature differ more than tolp. 



        **delta_t**: float
            *Default*:             1.D0


            *Info*:             
             if ~ion_temperature~ == 'rescale-T' : 
             at each step the instantaneous temperature is multiplied 
             by delta_t; this is done rescaling all the velocities. 
             
             if ~ion_temperature~ == 'reduce-T' :
                                       every 'nraise' steps the instantaneous temperature is 
             reduced by - ~delta_t~ (i.e. ~delta_t~ < 0 is added to T) 
             
             The instantaneous temperature is calculated at the end of 
             every ionic move and BEFORE rescaling. This is the temperature 
             reported in the main output. 
             
             For ~delta_t~ < 0, the actual average rate of heating or cooling 
             should be roughly C*delta_t/(nraise*dt) (C=1 for an 
             ideal gas, C=0.5 for a harmonic solid, theorem of energy 
             equipartition between all quadratic degrees of freedom). 



        **nraise**: int
            *Default*:             1


            *Info*:             
             if ~ion_temperature~ == 'reduce-T' : 
             every ~nraise~ steps the instantaneous temperature is 
             reduced by - ~delta_t~ (i.e. ~delta_t~ is added to the temperature) 
             
             if ~ion_temperature~ == 'rescale-v' : 
             every ~nraise~ steps the average temperature, computed from 
             the last ~nraise~ steps, is rescaled to ~tempw~ 
             
             if ~ion_temperature~ == 'rescaling' and ~calculation~ == 'vc-md' : 
             every ~nraise~ steps the instantaneous temperature 
             is rescaled to ~tempw~ 
             
             if ~ion_temperature~ == 'berendsen' : 
             the "rise time" parameter is given in units of the time step: 
             tau = nraise*dt, so dt/tau = 1/nraise 
             
             if ~ion_temperature~ == 'andersen' : 
             the "collision frequency" parameter is given as nu=1/tau 
             defined above, so nu*dt = 1/nraise 
             
             if ~ion_temperature~ == 'svr' : 
             the "characteristic time" of the thermostat is set to 
             tau = nraise*dt 



        **refold_pos**: bool
            *Default*:             .FALSE.


            *Info*:             
             This keyword applies only in the case of molecular dynamics or 
             damped dynamics. If true the ions are refolded at each step into 
             the supercell. 



            Quantum Espresso Version
            ------------------------
            Not yet implemented.
        """
        self._ion_temperature: Optional[IonTemperatureOptions] = ion_temperature
        self._tempw: Optional[float] = tempw
        self._tolp: Optional[float] = tolp
        self._delta_t: Optional[float] = delta_t
        self._nraise: Optional[int] = nraise
        self._refold_pos: Optional[bool] = refold_pos

    @property
    def ion_temperature(self) -> IonTemperatureOptions:
        """
        Default:
        ================
        'not_controlled'



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._ion_temperature

    @ion_temperature.setter
    def ion_temperature(self, value: IonTemperatureOptions):
        self._ion_temperature = value

    @property
    def tempw(self) -> float:
        """
        Default:
        ================
        300.D0


        Info:
        ================
        
         Starting temperature (Kelvin) in MD runs 
         target temperature for most thermostats. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._tempw

    @tempw.setter
    def tempw(self, value: float):
        self._tempw = value

    @property
    def tolp(self) -> float:
        """
        Default:
        ================
        100.D0


        Info:
        ================
        
         Tolerance for velocity rescaling. Velocities are rescaled if 
         the run-averaged and target temperature differ more than tolp. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._tolp

    @tolp.setter
    def tolp(self, value: float):
        self._tolp = value

    @property
    def delta_t(self) -> float:
        """
        Default:
        ================
        1.D0


        Info:
        ================
        
         if ~ion_temperature~ == 'rescale-T' : 
         at each step the instantaneous temperature is multiplied 
         by delta_t; this is done rescaling all the velocities. 
         
         if ~ion_temperature~ == 'reduce-T' :
                                   every 'nraise' steps the instantaneous temperature is 
         reduced by - ~delta_t~ (i.e. ~delta_t~ < 0 is added to T) 
         
         The instantaneous temperature is calculated at the end of 
         every ionic move and BEFORE rescaling. This is the temperature 
         reported in the main output. 
         
         For ~delta_t~ < 0, the actual average rate of heating or cooling 
         should be roughly C*delta_t/(nraise*dt) (C=1 for an 
         ideal gas, C=0.5 for a harmonic solid, theorem of energy 
         equipartition between all quadratic degrees of freedom). 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._delta_t

    @delta_t.setter
    def delta_t(self, value: float):
        self._delta_t = value

    @property
    def nraise(self) -> int:
        """
        Default:
        ================
        1


        Info:
        ================
        
         if ~ion_temperature~ == 'reduce-T' : 
         every ~nraise~ steps the instantaneous temperature is 
         reduced by - ~delta_t~ (i.e. ~delta_t~ is added to the temperature) 
         
         if ~ion_temperature~ == 'rescale-v' : 
         every ~nraise~ steps the average temperature, computed from 
         the last ~nraise~ steps, is rescaled to ~tempw~ 
         
         if ~ion_temperature~ == 'rescaling' and ~calculation~ == 'vc-md' : 
         every ~nraise~ steps the instantaneous temperature 
         is rescaled to ~tempw~ 
         
         if ~ion_temperature~ == 'berendsen' : 
         the "rise time" parameter is given in units of the time step: 
         tau = nraise*dt, so dt/tau = 1/nraise 
         
         if ~ion_temperature~ == 'andersen' : 
         the "collision frequency" parameter is given as nu=1/tau 
         defined above, so nu*dt = 1/nraise 
         
         if ~ion_temperature~ == 'svr' : 
         the "characteristic time" of the thermostat is set to 
         tau = nraise*dt 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._nraise

    @nraise.setter
    def nraise(self, value: int):
        self._nraise = value

    @property
    def refold_pos(self) -> bool:
        """
        Default:
        ================
        .FALSE.


        Info:
        ================
        
         This keyword applies only in the case of molecular dynamics or 
         damped dynamics. If true the ions are refolded at each step into 
         the supercell. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._refold_pos

    @refold_pos.setter
    def refold_pos(self, value: bool):
        self._refold_pos = value

