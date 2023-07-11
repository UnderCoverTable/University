A = input('Enter Coefficient matrix: ');
B = input('Enter Constant vector: ');
P = input('Enter initial guess:');
n = input('Number of iterations: ');
N = length(B);
X = zeros(N,1);
check = 0;

%Checks whether matrix is diagonally dominant.
for i = 1:3
    if i == 1
        if A(i) < abs(A(i,i+1)) + abs(A(i,i+2))
            break
        else 
            check = check + 1;
        end
    end
    
    if i == 2 
        
        if A(i,i) < abs(A(i,i-1)) + abs(A(i,i+1))
            break
        else 
            check = check + 1;
        end
    end
    
    if i == 3
        if A(i,i) < abs(A(i,i-1)) + abs(A(i,i-2))
            break
        else 
            check = check + 1;
        end
    end
    
end

%Iterates through the matrix n number of times.
if check == 3
    for j = 1:n
                
        for i = 1:N
            
            if i == 1 && j == 1
                %Seperated so P is used as the initial guess
                X(i) = (B(i)/A(i,i)) - (A(i,[1:i-1,i+1:N])*P([1:i-1,i+1:N]))/A(i,i);
                
            else
                P=X; %Updates the initial guess vector P, after each iteration.
                X(i) = (B(i)/A(i,i)) - (A(i,[1:i-1,i+1:N])*P([1:i-1,i+1:N]))/A(i,i);
                
            end
            
        end
       
        if abs(P - X) > 0.0001 == 0 %Stop criteria. Ends loop if answer is reached
            break                   %before the number of iterations that the user entered.
        end

    end
    fprintf('\n Number of iterations: %g',j)
    fprintf('\n X = %.4f',P(1)) %Prints correct to 4 decimal places
    fprintf('\n Y = %.4f',P(2))
    fprintf('\n Z = %.4f\n',P(3))
else
    disp('Error: Please enter a diagonally dominant matrix')
end
