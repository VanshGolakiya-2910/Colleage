% Addition and multiplication operations
add(X, Y, Result) :- Result is X + Y.
multiply(X, Y, Result) :- Result is X * Y.
?- add(3, 5, Result).
% Result = 8.

?- multiply(4, 6, Result).
% Result = 24.


% Addition with comparison and print
add_and_compare(X, Y) :-
    Result is X + Y,
    (Result > 10 -> write('The sum is greater than 10: '), write(Result) ; write('The sum is 10 or less: '), write(Result)).

% Multiplication with comparison and print
multiply_and_compare(X, Y) :-
    Result is X * Y,
    (Result < 20 -> write('The product is less than 20: '), write(Result) ; write('The product is 20 or more: '), write(Result)).
    
?- add_and_compare(3, 8).
% The sum is greater than 10: 11

?- multiply_and_compare(4, 5).
% The product is 20 or more: 20



count_up(X) :- count_up_helper(1, X).

count_up_helper(Current, X) :-
    Current =< X,
    write(Current), nl,
    Next is Current + 1,
    count_up_helper(Next, X).
count_up_helper(Current, X) :- Current > X.
?- count_up(5).
% 1
% 2
% 3
% 4
% 5


is_even(X) :- X mod 2 =:= 0.
is_odd(X) :- X mod 2 =\= 0.
?- is_even(4).
% true.

?- is_odd(7).
% true.




max_of_three(X, Y, Z, Max) :-
    (X >= Y, X >= Z -> Max = X ;
    Y >= X, Y >= Z -> Max = Y ;
    Max = Z).
?- max_of_three(3, 7, 5, Max).
% Max = 7.



min_of_three(X, Y, Z, Min) :-
    (X =< Y, X =< Z -> Min = X ;
    Y =< X, Y =< Z -> Min = Y ;
    Min = Z).
?- min_of_three(3, 7, 5, Min).
% Min = 3.



check_sign(X) :-
    (X > 0 -> write(X), write(' is positive');
    X < 0 -> write(X), write(' is negative');
    X =:= 0 -> write(X), write(' is zero')).
?- check_sign(-5).
% -5 is negative



factorial(0, 1).
factorial(N, Result) :-
    N > 0,
    N1 is N - 1,
    factorial(N1, Result1),
    Result is N * Result1.
?- factorial(5, Result).
% Result = 120.



fibonacci(0, 0).
fibonacci(1, 1).
fibonacci(N, Result) :-
    N > 1,
    N1 is N - 1,
    N2 is N - 2,
    fibonacci(N1, Result1),
    fibonacci(N2, Result2),
    Result is Result1 + Result2.
?- fibonacci(6, Result).
% Result = 8.



print_fibonacci_series(N) :- 
    print_fibonacci_series_helper(0, N).

print_fibonacci_series_helper(Current, N) :-
    Current =< N,
    fibonacci(Current, Result),
    write(Result), nl,
    Next is Current + 1,
    print_fibonacci_series_helper(Next, N).
print_fibonacci_series_helper(Current, N) :- Current > N.
?- print_fibonacci_series(6).
% 0
% 1
% 1
% 2
% 3
% 5
% 8

