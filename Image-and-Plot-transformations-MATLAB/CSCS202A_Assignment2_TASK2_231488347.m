close all
%clear all
clc


%CUBE 
cx = [40,50,50,40,40,45,55,55,45,40,50,55,55,50,55,45,45];
cy = [40,40,50,50,40,45,45,55,55,50,50,55,45,40,45,45,55];
cube = [cx;cy];
%PRISM
px = [5, 15,10,5, 20,30,25,10,15,30,20,25];
py = [20,20,25,20,25,25,30,25,20,25,25,30];
prism = [px;py];
%HEXAGONAL PYRAMID
pyx = [40,45,50,55,50,45,40,48,45,50,48,55,50,48,45];
pyy = [10,15,15,10,5,5,10,29,15,15,29,10,5,29,5];
pyramid = [pyx;pyy];
%Icosahedron
ix = [30,20,10,10,20,30,30,25,15,20,25,20,15,10,15,10,20,20,20,30,25];
iy = [45,40,45,55,60,55,45,47,47,56,47,40,47,45,47,55,56,60,56,55,47];
icos = [ix;iy];
%Letter S
sx = [13,10,8,10,14,10,7,8,10,12,10,6,10,14,13];
sy = [9,10,9,8,5,2,4,5.5,4,5,6,9,12,10,9];
s = [sx;sy];


% % % Plotting all 5 figures
% % hold on
% % axis_helper(60,55)
% % plot(ix,iy,'y');grid on
% % plot(pyx,pyy,'m')
% % plot(px,py,'c')
% % plot(cx,cy,'r')
% % plot(sx,sy,'g')


%All the transformations and their inputs:
%Shape inputs : cube, prism, icos, pyramid, s
%Transformation axis inputs : "X" or "Y". ("YX" only for reflection)
%{  

1 - Reflection(shape,transformation_axis) 
2 - Rotation(shape,angle) 
3 - Projection(shape,transformation_axis)

4 - Contraction_Dialation(shape,k)      [ Cont-> 0 =< k < 1 _ Dial-> k > 1 ]
5 - Compression_Expansion(shape,transformation_axis,k)      [Comp-> 0 =< k < 1 _ Expa-> k > 1
6 - Shear(shape,transformation_axis,k)
%}


%Performing Functions

Projection(cube,'Y')
Rotation(pyramid,180)
Reflection(s,"YX")
Shear(prism,"Y",1.5)
Compression_Expansion(icos,'Y',1.25)
Contraction_Dialation(cube,1.5)



function Shear(shape,transformation_axis,k)
figure()

if transformation_axis == 'X'
    tr_matrix = [1,k ; 0,1];
else
    tr_matrix = [1,0 ; k,1];
end

shape_name = shape_name_helper(shape);
kstr = num2str(k);
TrM = tr_matrix * shape;

axis_helper( max(TrM(1,:)), max(TrM(2,:)) )
hold on
plot(shape(1,:),shape(2,:),'DisplayName',strcat('Original-',shape_name),'color',[0 0.4470 0.7410]);grid on
plot(TrM(1,:),TrM(2,:),'DisplayName',strcat(shape_name,'-Shear ',transformation_axis,'(','k=',kstr,')'),'LineStyle','-.','Color',[0.8500, 0.3250, 0.0980]);
hold off
end

function Compression_Expansion(shape,transformation_axis,k) % C-> 0 =< k < 1 _ E-> k > 1
figure()


if transformation_axis == 'X'
    tr_matrix = [k,0 ; 0,1];
else
    tr_matrix = [1,0 ; 0,k];
end

if k > 1
    form = 'Expansion';
else
    form = 'Compression';
end

shape_name = shape_name_helper(shape);
kstr = num2str(k);
TrM = tr_matrix * shape;

axis_helper( max(TrM(1,:)), max(TrM(2,:)) )
hold on
plot(shape(1,:),shape(2,:),'DisplayName',strcat('Original-',shape_name),'color',[0 0.4470 0.7410]);grid on
plot(TrM(1,:),TrM(2,:),'DisplayName',strcat(shape_name,'-',form,transformation_axis,'(','k=',kstr,')'),'LineStyle','-.','color',[0.8500, 0.3250, 0.0980]);
hold off

end

function Contraction_Dialation(shape,k) % C-> 0 =< k < 1 _ D-> k > 1
figure()


if k > 1
    form = 'Dialation';
else
    form = 'Contraction';
end

shape_name = shape_name_helper(shape);
kstr = num2str(k);
tr_matrix = [k,0 ; 0,k]; 
TrM = tr_matrix * shape;

axis_helper( max(TrM(1,:)), max(TrM(2,:)) )
hold on
plot(shape(1,:),shape(2,:),'DisplayName',strcat('Original-',shape_name),'color',[0 0.4470 0.7410]);grid on
plot(TrM(1,:),TrM(2,:),'DisplayName',strcat(shape_name,'-',form,'(','k=',kstr,')'),'LineStyle','-.','color',[0.8500, 0.3250, 0.0980]);
hold off
end

function Rotation(shape,angle)
figure()

tr_matrix = [cosd(angle),sind(angle) ; sind(angle),cosd(angle)];

shape_name = shape_name_helper(shape);
anglestr = int2str(angle);
TrM = tr_matrix * shape;

axis_helper( max(shape(1,:)), max(shape(2,:)) )
hold on
plot(shape(1,:),shape(2,:),'DisplayName',strcat('Original-',shape_name),'color',[0 0.4470 0.7410]);grid on
plot(TrM(1,:),TrM(2,:),'DisplayName',strcat(shape_name,'-','Rotation','(',anglestr,'°',')'),'LineStyle','-.','color',[0.8500, 0.3250, 0.0980]);
hold off
end

function Reflection(shape,transformation_axis)
figure()

if transformation_axis == 'X'
    tr_matrix = [1,0;0,-1];
elseif transformation_axis == 'Y'
    tr_matrix = [-1,0;0,1];
elseif transformation_axis == 'YX'
    tr_matrix = [0,1;1,0];
end

shape_name = shape_name_helper(shape);
TrM = tr_matrix * shape;

axis_helper( abs(max(shape(1,:))), abs(max(shape(2,:))) )
hold on
plot(shape(1,:),shape(2,:),'DisplayName',strcat('Original-',shape_name),'color',[0 0.4470 0.7410]);grid on
plot(TrM(1,:),TrM(2,:),'DisplayName',strcat(shape_name,'-','Reflection',transformation_axis),'LineStyle','-.','color',[0.8500, 0.3250, 0.0980]);
hold off
end

function Projection(shape,transformation_axis)
figure()

if transformation_axis == 'X'
    tr_matrix = [1,0;0,0];
else
    tr_matrix = [0,0;0,1];
end

shape_name = shape_name_helper(shape);
TrM = tr_matrix * shape;

axis_helper( max(shape(1,:)), max(shape(2,:)) )
hold on
plot(shape(1,:),shape(2,:),'DisplayName',strcat('Original-',shape_name),'color',[0 0.4470 0.7410]);grid on
plot(TrM(1,:),TrM(2,:),'DisplayName',strcat(shape_name,'-','Projection',transformation_axis),'LineStyle','-.','color','m');
hold off
end



function shape_name = shape_name_helper(x)

if x(2,1) == 40
    shape_name = "Cube";
elseif x(2,1) == 20
    shape_name = "Prism";
elseif x(2,1) == 10
    shape_name = "Pyra";
elseif x(2,1) == 9
    shape_name = "Letter S";
else
    shape_name = "Icos..";
end

end %Helps getting the name of the shape, based on the matrix

function axis_helper(x,y)
x = x+5;
y = y+5;
axis([-x x -y y]) %Increase axis size if image does not fit
xL = xlim;
yL = ylim;
line([0 0], yL,'color','k','HandleVisibility','off','LineStyle',':');  %x-axis
line(xL, [0 0],'color','k','HandleVisibility','off','LineStyle',':');  %y-axis
legend('Location','Best')
end %Helps plotting the axis and its limits
