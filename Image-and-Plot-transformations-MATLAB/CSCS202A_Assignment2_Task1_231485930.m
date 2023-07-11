%Image Merging/ Addition of two image matrices
close all
clc
%selected images
I1=imread('Image 1.jpeg');
I2=imread('Image 2.jpeg');
I3=imread('Image 3.tif');
I4=imread('Image 4.gif');


 I_add = I1+I2;
 I_sub = I1-I2;
 I_mul = I3.*I4;
I_div = I3./I4;

I_transpose = transpose(I3); 
I_eq = (I4+I3) ./ (I3-I4);
I_k = I4*5;


 f = figure(1);
 
  subplot(2,2,1);
imshow(I1)
 title('Image 1: House')
 
 subplot(2,2,2);
imshow(I2)
 title('Image 2: Tree')
 
   subplot(2,2,3);
imshow(I3)
 title('Image 3: Camera Man')
 
 subplot(2,2,4);
imshow(I4)
 title('Image 4: Orca')
 
 figure(2)
  subplot(2,2,1);
  imshow(I_add)
 title('(I1 + I2)')

  subplot(2,2,2);
  imshow(I_sub)
 title('(I1 - I2)')
 
  subplot(2,2,3);
  imshow(I_mul)
 title('(I1 x I2)')
 
  subplot(2,2,4);
  imshow(I_div)
 title('(I1 / I2)')
 
 figure(3)
   subplot(2,2,1);
  imshow(I_transpose)
 title('I3 Transpose')
 
    subplot(2,2,2);
  imshow(I_eq)
 title('(I4+I3) / (I3-I4)')

subplot(2,2,3);
  imshow(I_k)
 title('I * k')

 