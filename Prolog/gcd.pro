go:-	write('Enter first number :'),
	read(X1),
	write('Enter second number :'),
	read(X2),
	gcd(X1,X2,R),nl,
	write('GCD is : '),write(R).

gcd(0,B,B).
gcd(A,0,A).
gcd(A,A,A).
gcd(A,B,R) :- A>B,
				A1 is A-B,
				gcd(A1,B,R);
				B1 is B-A,
				gcd(A,B1,R).

:-initialization(go).