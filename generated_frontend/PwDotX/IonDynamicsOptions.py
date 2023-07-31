from typing import Optional, List
from .Options import Options


class IonDynamicsOptions(Options):
    """
    Others:
    ================
    
     Specify the type of ionic dynamics. 
     
     For different type of calculation different possibilities are 
     allowed and different default values apply: 
     
     **CASE** ( ~calculation~ == 'relax' ) 
    
     **CASE** ( ~calculation~ == 'md' ) 
    
     **CASE** ( ~calculation~ == 'vc-relax' ) 
    
     **CASE** ( ~calculation~ == 'vc-md' ) 


    Quantum Espresso Version:
    =========================
    Not yet implemented.
    """
    beeman = 0
    """   
    **(default)** use Beeman algorithm to integrate 
    Newton's equation 

    """
    verlet = 1
    """   
    **(default)** use Verlet algorithm to integrate 
    Newton's equation. For constrained 
    dynamics, see ~CONSTRAINTS~ card 

    """
    bfgs = 2
    """   
    **(default)** use BFGS quasi-newton algorithm; 
    cell_dynamics must be 'bfgs' too 

    """
    damp = 3
    """   
    use damped (Beeman) dynamics for 
    structural relaxation 

    """
    langevin__dash__smc = 4
    """   
    over-damped Langevin with Smart Monte Carlo: 
    see R.J. Rossky, JCP, 69, 4628 (1978), doi:10.1063/1.436415 

    """
    langevin = 5
    """   
    ion dynamics is over-damped Langevin 

    """
