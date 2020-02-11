iseven([]).
iseven([_|T]):-isodd(T).
isodd([_]).
isodd([_|T]):-iseven(T).