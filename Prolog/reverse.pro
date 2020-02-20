go:-write('Enter a list'),nl,
    createList(L1),
    reverse(L1,L,[]),write('Reversed list is '),write(L).

enter(X):- write('Enter element:'),nl,
            read(X).

createList(L):- enter(X),createList(X,L).
createList(-1,[]):-!.
createList(X,[X|T]):- enter(X1),createList(X1,T).

reverse([],L,L).
reverse([H|T1], L2,L):- 
                                concat(T1,L2, [H|L] ).