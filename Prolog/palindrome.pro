go:-write('Enter a list'),nl,
    createList(L1),
    rev(L1,L),
    equal(L1,L,T),write('Is the list a palindrome? '),write(T).

enter(X):- write('Enter element:'),nl,
            read(X).

createList(L):- enter(X),createList(X,L).
createList(-1,[]):-!.
createList(X,[X|T]):- enter(X1),createList(X1,T).

rev(L1,L):-reverse(L1,L,[]).
reverse([],L,L).
reverse([H|T1], L2,L):- 
                                reverse(T1,L2, [H|L] ).
equal([],[],'true').
equal([X1|T1],[X2|T2],P):-
    X1 \== X2,  P = 'false',!.
equal([X1|T1],[X2|T2],P):-
    equal(T1,T2,P).