# Creamer for Quantum Espresso 

This project makes Quantum Espresso significantly more approachable.
It aims to provide 

1. A microservice for running the calculation.
   This separates server hacking from number crunching so that people who
   don't know how to hack servers can still crunch numbers and vice versa.
2. A Python DSL for writing the input and running the calculation.
   This can be quite useful, It not only provides autocompletion 
   and error checking, but also makes automated runs and integration 
   with other tasks rather easy.
3. A database for collecting and managing the calculation for down stream analysis.
   It also helps to avoid repeated calculation, especially when the 
   program on the client side crashes.
   