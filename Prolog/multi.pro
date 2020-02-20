go:-	write('Enter first number :'),
	read(X1),
	write('Enter second number :'),
	read(X2),
	multi(X1,X2,R),nl,
	write('Result is : '),write(R).

multi(A,0,1).
multi(A,1,A).
multi(A,B,R) :- A>1,
				B1 is B - 1,
				multi(A,B1,R1),
				R is A+R1.				

:-initialization(go).