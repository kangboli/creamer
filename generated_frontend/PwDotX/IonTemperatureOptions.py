from typing import Optional, List
from .Options import Options


class IonTemperatureOptions(Options):
    """
    Others:
    ================
    Available options are:


    Quantum Espresso Version:
    =========================
    Not yet implemented.
    """
    andersen = 0
    """   
    control ionic temperature using Andersen thermostat 
    see parameters ~tempw~ and ~nraise~ 

    """
    not_controlled = 1
    """   
    (default) ionic temperature is not controlled 

    """
    rescaling = 2
    """   
    control ionic temperature via velocity rescaling 
    (first method) see parameters ~tempw,~ ~tolp,~ and 
    ~nraise~ (for VC-MD only). This rescaling method 
    is the only one currently implemented in VC-MD 

    """
    reduce__dash__t = 3
    """   
    reduce temperature of the thermostat every ~nraise~ steps 
    by the (negative) value ~delta_t,~ starting from ~tempw.~ 
    If ~delta_t~ is positive, the target temperature is augmented. 
    The temperature is controlled via velocitiy rescaling. 

    """
    initial = 4
    """   
    initialize ion velocities to temperature ~tempw~ 
    and leave uncontrolled further on 

    """
    berendsen = 5
    """   
    control ionic temperature using "soft" velocity 
    rescaling - see parameters ~tempw~ and ~nraise~ 

    """
    rescale__dash__v = 6
    """   
    control ionic temperature via velocity rescaling 
    (second method) see parameters ~tempw~ and ~nraise~ 

    """
    rescale__dash__t = 7
    """   
    scale temperature of the thermostat every ~nraise~ steps 
    by ~delta_t,~ starting from ~tempw.~ 
    The temperature is controlled via velocitiy rescaling. 

    """
    svr = 8
    """   
    control ionic temperature using stochastic-velocity rescaling 
    (Donadio, Bussi, Parrinello, J. Chem. Phys. 126, 014101, 2007), 
    with parameters ~tempw~ and ~nraise.~ 

    """
