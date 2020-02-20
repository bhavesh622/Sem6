go:-	write('Enter base :'),
	read(X1),
	write('Enter power :'),
	read(X2),
	power(X1,X2,R),nl,
	write('Result is : '),write(R).

power(_,0,1).
power(A,1,A).
power(A,B,R) :- A>1,
				B1 is B - 1,
				power(A,B1,R1),
				R is A*R1.
				

:-initialization(go).