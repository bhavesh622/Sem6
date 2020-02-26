go:-
    write('Enter a list'),nl,
    createList(L),nl,
    write('The list is : '),
    printList(L),nl,nl,
    write('Sum of the list is:'),
    sum_list(L,R),
    write(R).

sum_list(L,R):-
    sumlist(L,R1),
    R is 0 + R1.

sumlist([],0).
sumlist([X|T],R):-
    R = R1 + X,
    sumlist(T,R1).

enter(X):-
    write('Enter element:'),
    read(X).

createList(L):-
    enter(X),createList(X,L).
createList(-1,[]):-!.
createList(X,[X|T]):-
    enter(X1),createList(X1,T).

printList([]):-!.
printList([H|T]):-
    write(' '),write(H),printList(T).

:-initialization(go).