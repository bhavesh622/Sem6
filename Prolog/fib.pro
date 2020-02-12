go:- write('Enter nth element'),nl,
     read(N),
     fib(N,Res),
     write('Nth term is '), write(Res).

fib(0, 0).
fib(1, 1).
fib(N,Res):-fib(N,0,1,Res).

fib(0,N,_,N).
fib(N, Prev1,Prev2,Res):- 
   N>0,
   New_Prev2 is Prev1+Prev2, 
   N1 is N-1,
   fib(N1,Prev2,New_Prev2,Res).
:- initialization(go).