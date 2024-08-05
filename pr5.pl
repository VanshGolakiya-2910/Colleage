% Base case: The item is the head of the list
member(Item, [Item|_]).

% Recursive case: The item is in the tail of the list
member(Item, [_|Tail]) :-
    member(Item, Tail).



% Base case: The size of an empty list is 0
list_size([], 0).

% Recursive case: The size is 1 plus the size of the tail
list_size([_|Tail], Size) :-
    list_size(Tail, TailSize),
    Size is TailSize + 1.



% Base case: The last element of a list with one element is that element
last_element([Element], Element).

% Recursive case: The last element is in the tail of the list
last_element([_|Tail], Last) :-
    last_element(Tail, Last).



% Base case: Deleting an element from an empty list results in an empty list
delete_element(_, [], []).

% Case: The element to delete is the head of the list
delete_element(Element, [Element|Tail], Tail).

% Recursive case: The element to delete is not the head
delete_element(Element, [Head|Tail], [Head|ResultTail]) :-
    delete_element(Element, Tail, ResultTail).





% Base case: Appending an empty list to L2 results in L2
append([], L2, L2).

% Recursive case: Append the head of L1 to the result of appending the tail of L1 to L2
append([Head|Tail1], L2, [Head|TailResult]) :-
    append(Tail1, L2, TailResult).





% Display a list
display_list([]) :- nl.
display_list([Head|Tail]) :-
    write(Head), write(' '),
    display_list(Tail).

% Reverse a list
reverse_list(L, R) :-
    reverse_list(L, [], R).

reverse_list([], Acc, Acc).
reverse_list([Head|Tail], Acc, R) :-
    reverse_list(Tail, [Head|Acc], R).

% Display a list in reverse order
display_list_reverse(List) :-
    reverse_list(List, Reversed),
    display_list(Reversed).






?- member(3, [1, 2, 3, 4]).
true.

?- list_size([1, 2, 3, 4], Size).
Size = 4.

?- last_element([1, 2, 3, 4], Last).
Last = 4.

?- delete_element(3, [1, 2, 3, 4], Result).
Result = [1, 2, 4].

?- append([1, 2], [3, 4], Result).
Result = [1, 2, 3, 4].

?- display_list([1, 2, 3, 4]).
1 2 3 4 
true.

?- display_list_reverse([1, 2, 3, 4]).
4 3 2 1 
true.
