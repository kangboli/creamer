from typing import Optional, List
from .Options import Options


class RestartModeOptions(Options):
    """
    Others:
    ================
    Available options are:


    Quantum Espresso Version:
    =========================
    Not yet implemented.
    """
    restart = 0
    """   
    From previous interrupted run. Use this switch only if you want to 
    continue, using the same number of processors and parallelization, 
    an interrupted calculation. Do not use to start a new one, or to 
    perform a non-scf calculations. Works only if the calculation was 
    cleanly stopped using variable ~max_seconds,~ or by user request 
    with an "exit file" (i.e.: create a file "prefix".EXIT, in directory 
    "outdir"; see variables ~prefix,~ ~outdir).~ Overrides ~startingwfc~ 
    and ~startingpot.~ 

    """
    from_scratch = 1
    """   
    From scratch. This is the normal way to perform a PWscf calculation 

    """
