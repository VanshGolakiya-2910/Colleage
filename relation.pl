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
