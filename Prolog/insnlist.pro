go:-write('Enter a list :'),
    createList(L),
    printList(L),nl,
    write('Enter a element to be inserted at nth position :'),read(I),nl,
    write('Enter n :'),read(N),
    insert_nth(I,N,L,R),
    write('List after entering element at nth position :'),printList(R).


insert_nth(I,0,L,[X|L]):- X is I.

insert_nth(I,N,[X|T],[X|R]):- N1 is N-1 ,insert_nth(I,N1,T,R).


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
