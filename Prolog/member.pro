go:-write('Enter a list'),nl,
    createList(L),
    write('Enter number to be searched'),nl,
    read(E),
    memb(E,L),write('Yes');write('No').

enter(X):- write('Enter element:'),nl,
            read(X).

createList(L):- enter(X),createList(X,L).
createList(-1,[]):-!.
createList(X,[X|T]):- enter(X1),createList(X1,T).

memb(E,[E|_]):-!.
memb(E,[_|T]):-memb(E,T).
:-initialization(go).