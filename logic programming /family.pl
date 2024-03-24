% The knowledge base.
% assigning gender

male(ford).
male(Joh).
male(simba).
female(nam).
female(marry).
female(winny).

% defining parent relationship
parent(ford,joh).
parent(ford,simba).
parent(ford,winny).
parent(ford,marry).
parent(nam,joh).
parent(nam,simba).
parent(nam,winny).
parent(nam,marry).

%Emplementing the in prolog
mother(X,Y):-
  parent(X,Y),famale(X).

father(X,Y):-
  parent(X,Y),male(X).

siblings(X,Y):-
  parent(Z,X),parent(Z,Y),X\==Y.
  
brothers(X,Y):-
  parent(Z,X),parent(Z,Y),(male(X),male(Y)),X\==Y.


sisters(X,Y):-
  parent(Z,X),parent(Z,Y),(famale(X),female(Y)),X\==Y.


  %Example answering some questions
?-parent(ford,Z).
?-parent(nam,Y).
?-mother(marry,nam).% this should be false


