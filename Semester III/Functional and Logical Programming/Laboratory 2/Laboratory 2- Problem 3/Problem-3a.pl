% function which returns the number of appearences of a value E in a
% given list
% number_of_times(L-List, E-element,R- result)
% Flow model: (i,i,o)
number_of_times([], _, 0).
number_of_times([H|T],E,R) :- H=\= E, number_of_times(T,E,R).
number_of_times([H|T],E,R) :- H=:= E, number_of_times(T,E,R2), R is R2+1.


% function which removes a value E from a given list and return the
% modified list
% remove_element(L-list, E-element, R-result)
% Flow model: (i,i,o)
remove_element([], _, []).
remove_element([H|T], E, R) :- H =:= E, remove_element(T, E, R).
remove_element([H|T], E, R) :- H =\= E, remove_element(T, E, R2), R = [H|R2].


% function which removes all repetitive elements of a given list
% remove_repetitive(L- list, R- result_list)
% Flow model: (i,o)
remove_repetitive([], []).
remove_repetitive([H|T], R) :- number_of_times([H|T], H, ECNT), ECNT > 1, remove_element([H|T], H, RESLST), remove_repetitive(RESLST, R), R = RESLST.
remove_repetitive([H|T], R) :- number_of_times([H|T], H, ECNT), ECNT =:= 1, remove_repetitive(T, R2), R = [H|R2].
