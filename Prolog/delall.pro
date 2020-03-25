go:-write('Enter a list :'),
    createList(L),
    printList(L),nl,
    write('Enter X :'),read(X),
    delete_all(X,L,R),
    write('List after deleting given element :'),printList(R).

delete_all(X,[],R).

delete_all(X,[X|T],R):- delete_all(X,T,R).

delete_all(N,[X|T],[X|R]):- delete_all(N,T,R).


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
