function Secant(f,x0,x1)
 
 
while  abs(x1-x0) > 0.001 %Stop criteria. If difference b/w Xn-1 and Xn is <0.001

    x = (x0 - f(x0) *  (x1 - x0) / (f(x1) - f(x0)));
    
    %Updates the values. x(n=0) is updated to x(n=1) and x(n=1) to x(n+1) 
    x0 = x1; 
    x1 = x;
    
end
fprintf('\n    Root is: %.5f \n',x1) %prints correct to 5 decimal places. 