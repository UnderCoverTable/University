mother(pam,bob).
mother(pat,jim).
father(tom,bob).
father(tom,liz).
father(bob,ann).
father(bob,pat).
father(joe,jim).
male(tom).
male(bob).
male(jim).
male(joe).
female(liz).
female(pat).
female(ann).
female(pam).
parent(pam,bob).
parent(tom,bob).
parent(bob,ann).
parent(bob,pat).
parent(tom,liz).
parent(pat,jim).
parent(joe,jim).

is_male(X):- male(X).
is_female(X):- female(X).

is_mother(X,Y):-mother(X,Y).
is_father(X,Y):-father(X,Y).

parent_of(X,Y):-parent(X,Y).

grandparent_of(X,Y):-parent(X,Z),parent(Z,Y).
grandchildren_of(X,Y):-parent(Z,X),parent(Y,Z).

