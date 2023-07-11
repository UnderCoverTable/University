function Bisection(f,a,b)
%Create vectors for each variable
a_list = [];
b_list = [];
c_list = [];
fa_list = [];
fb_list = [];
fc_list = [];


if f(a) * f(b) <0 %Checks the interval
    c = a+b/2;
    
   %Adds all the initial values of the variables
    a_list = [a_list,a,]; b_list = [b_list,b,]; c_list = [c_list,c,];
    fa_list = [fa_list,f(a),]; fb_list = [fb_list,f(b),]; fc_list = [fc_list,f(c),];
    
    while abs(f(c)) > 0.001
        
        %Updates a or b according to the sign of f(c)
        if (f(c) * f(a)) < 0
            b = c;
        else
            a = c;
        end
       c = (a+b)/2;
       
       %Updates the vector with each new value with every iteration
       a_list = [a_list,a,]; b_list = [b_list,b,]; c_list = [c_list,c,];
       fa_list = [fa_list,f(a),]; fb_list = [fb_list,f(b),]; fc_list = [fc_list,f(c),];
       
       
    end
    root = c;
    
    %Prints a table with the vectors made earlier
    fprintf('\t   a \t\t   b\t\t   c\t \t  f(a)\t \t  f(b)\t      f(c) \n')
    fprintf('\t   - \t\t   -\t\t   -\t \t  ---\t \t  ---\t      --- \n')
    fprintf('\t%.5f \t%.5f \t%.5f \t%.5f \t%.5f \t%.5f \n ',[a_list;b_list;c_list;fa_list;fb_list;fc_list])
    %prints each value correct to 5 decimal places.    
    
    fprintf('\n    Root is: %0.5f \n',root)
    
else
    disp("Interval is incorrect")
    
end
