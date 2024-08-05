% Define the parent relationships
parent(paul, lili).
parent(helen, lili).
parent(paul, petunia).
parent(helen, petunia).
parent(vernon, dudley).
parent(petunia, dudley).
parent(albert, james).
parent(ruth, james).
parent(james, harry).
parent(lili, harry).

% Define the spouse relationships
spouse(paul, helen).
spouse(helen, paul).
spouse(vernon, petunia).
spouse(petunia, vernon).
spouse(albert, ruth).
spouse(ruth, albert).
spouse(james, lili).
spouse(lili, james).

% Define the sibling relationship based on the parent relationship
sibling(X, Y) :-
    parent(P, X),
    parent(P, Y),
    X \= Y.

% Define mother and father relationships
mother(M, C) :-
    parent(M, C),
    female(M).

father(F, C) :-
    parent(F, C),
    male(F).

% Define male and female (assuming known data or facts)
male(paul).
male(vernon).
male(albert).
male(james).
male(dudley).
male(harry).

female(helen).
female(petunia).
female(ruth).
female(lili).
female(lili). % ensuring lili is listed as female


% Define uncle and aunt relationships
uncle(U, N) :-
    sibling(U, P),
    parent(P, N),
    male(U).

aunt(A, N) :-
    sibling(A, P),
    parent(P, N),
    female(A).

% Define nephew and niece relationships
nephew(N, A) :-
    aunt(A, N),
    male(N).

niece(N, A) :-
    aunt(A, N),
    female(N).

% Define grandfather and grandmother relationships
grandfather(GF, GC) :-
    parent(GF, P),
    parent(P, GC),
    male(GF).

grandmother(GM, GC) :-
    parent(GM, P),
    parent(P, GC),
    female(GM).

% Define cousin relationship
cousin(C1, C2) :-
    parent(P1, C1),
    parent(P2, C2),
    sibling(P1, P2).
% Define ancestor and descendant relationships
ancestor(A, D) :-
    parent(A, D).

ancestor(A, D) :-
    parent(A, P),
    ancestor(P, D).

descendant(D, A) :-
    ancestor(A, D).


% Define directed edges
edge(a, b).
edge(b, c).
edge(c, d).
edge(d, e).
edge(a, e).
edge(e, f).
edge(f, g).
edge(g, h).
edge(a, f).
edge(b, e).
edge(d, g).

% Base case: There is a direct edge from X to Y
path(X, Y) :- edge(X, Y).

% Recursive case: There is a path from X to Y if there is a path from X to some Z and an edge from Z to Y
path(X, Y) :- edge(X, Z), path(Z, Y).
