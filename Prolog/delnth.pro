go:-write('Enter a list :'),
    createList(L),
    printList(L),nl,
    write('Enter n :'),read(N),
    delete_nth(N,L,R),
    write('List after deleting element at nth position :'),printList(R).

delete_nth(0,[X|T],T).

delete_nth(N,[X|T],[X|R]):- N1 is N-1 ,delete_nth(N1,T,R).


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
