go:-write('Enter first ordered list :'),
    createList(L1),
    printList(L1),nl,
    write('Enter second ordered list :'),
    createList(L2),
    printList(L2),nl,
    merge(L1,L2,L3),
    write('List after merge :'),printList(L3).

merge([],[],[]).
merge([],L2,L2).
merge(L1,[],L1).

merge([X1|T1],[X2|T2],[X3|T3]) :-
    X1<X2,
    X3 is X1,
    merge(T1,[X2|T2],T3);
    X3 is X2,
    merge([X1|T1],T2,T3).

enterEl(X):-
    nl, write('Enter a Element :'),
    read(X).

createList(L):- 
    enterEl(X),
    createList(X,L).

createList(-1,[]):-!.
createList(X,[X|T]):-
    enterEl(X1),
    createList(X1,T).

printList([]).
printList([H|T]):-  
    write(' '),
    write(H),
    printList(T).