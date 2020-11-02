% function which returns true if first element is grater or equal than
% the second one, otherwise the result is false
% maximum_of_two_numbers(x-number, y-number, x- boolean result)
% Flow model: (i,i,o)
maximum_of_two_numbers(X,Y,X):-
    X>=Y.


% function which returns true if first element is less than
% the second one, otherwise the result is false
% maximum_of_two_numbers(x-number,y-number,y-boolean result)
% Flow model: (i,i,o)
maximum_of_two_numbers(X,Y,Y):-
    X<Y.


% fuction which returns the maximum value of a list
% we return 0 if the list is empty
% max_value(L- list,R- number)
% Flow model: (i,o)
max_value([],0).
max_value([X],X).
max_value([H|T], R):- max_value(T,R2) ,maximum_of_two_numbers(H,R2,R).


% function which removes from a list a given element E and returns the
% modified list
% remove_maxim_value(L- list, E- number, R- list)
% Flow model: (i,i,0)
remove_maxim_value([], _, []).
remove_maxim_value([H|T],E,R) :- H=:=E, remove_maxim_value(T,E,R).
remove_maxim_value([H|T],E,R) :- H=\=E, remove_maxim_value(T,E,R2), R=[H|R2].


% function which removes from a list the maximum element and returns the
% modified list
% remove_function(LST- list, R- list)
% Flow model: (i,o)
remove_function(LST, R) :- max_value(LST, MXELM), remove_maxim_value(LST, MXELM, R2), R=R2.

