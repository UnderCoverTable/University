f =@(x) x*sin(x)+cos(x);
fp =@(x) x*cos(x);
x0 = 2; %Initial guess
x1 = 0; %To store Xn-1 

while  abs(x0-x1) > 0.001 %Stop criteria. If difference b/w Xn-1 and Xn is <0.001

    x = x0 - f(x0)/fp(x0);
    
    % Store Xn-1 in x1 and update X0 to Xn+1
    x1 = x0;
    x0 = x;
end
fprintf('\n    Root is: %.5f \n',x0) %prints correct to 5 decimal places. 