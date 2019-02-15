#dari github 
#install python
#install numpy
#-> pip install numpy

x1= input ('x1 = ');
x2= input ('x2 = ');
w1 = input ('bobot w1 = ');
w2 = input ('bobot w2 = ');
b = input ('bias = ');
theta = input ('theta = ');
t = [1 0 0 0];
kondisi = 1;
while kondisi
    y_in = (x1*w1)+(x2*w2)+ b;
    for i= 1:4
    if y_in >= 0
        y (i) = 1;
    else
        y(i)= 0;
    end
end
disp(x1);
disp(x2);
disp(t);
disp('y net = ' ); disp(y);

if y==t;
    kondisi=0
    disp('interasi berhenti');
else
    disp('terjadi perubahan bobot');
    deltaw1 = x1(i)*y;
    deltaw2 = x2(i)*y;
    deltab  = 1*t;
    disp('Delta w1 = '); disp(deltaw1);
    disp('Delta w2 = '); disp(deltaw2);
    disp('Delta bias = '); disp(deltab);
    
    neww1 = w1*deltaw1;
    neww2 = w2*deltaw2;
    newb = b*y;
    disp('Bobot w1 baru = '); disp(neww1);
    disp('Bobot w2 baru = '); disp(neww2);
    disp('Bobot bias baru = '); disp(newb);
    theta = input('Input kembali theta = ');
    end
end
disp('Didapat jaringan Hebb sebagai berikut.. ');
disp('Bobot syaraf : ');
disp('Bobot w1 : '); disp(w1);
disp('Bobot w2 : '); disp(w2);
disp('Bias : '); disp(b);
disp('theta : '); disp(theta);
