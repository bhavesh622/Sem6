go:- write('Enter first number '),
    read(X1),
    fact(X1,N),
    write('The factorial of '),write(X1),write(' is '),write(N).

fact(0,1):-!.
fact(1,1):-!.
fact(X1,N):- X2 is X1-1,
             fact(X2,N2),
             N is N2*X1.