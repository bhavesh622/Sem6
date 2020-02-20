go:-write('Enter a list'),nl,
    createList(L1),
    write('Enter the second list'),nl,
    createList(L2),
    concat(L1,L2,L),write('Concatenated list is '),write(L).

enter(X):- write('Enter element:'),nl,
            read(X).

createList(L):- enter(X),createList(X,L).
createList(-1,[]):-!.
createList(X,[X|T]):- enter(X1),createList(X1,T).

concat([],L,L).
concat([H|T1], L2,[H|L]):- 
                                concat(T1,L2, L ).