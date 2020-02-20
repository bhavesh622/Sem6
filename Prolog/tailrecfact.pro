go:- write('Enter first number '),
    read(N),
    factorial(N,1,F),
    write('The factorial of '),write(N),write(' is '),write(F).

factorial(0,F,F). 

factorial(N,A,F) :-  
    N > 0, 
    A1 is N*A, 
    N1 is N -1, 
    factorial(N1,A1,F). 