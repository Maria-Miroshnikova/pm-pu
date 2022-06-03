
x = linspace(0, 4*pi, 10000);
f = 'x.*sin(x)-cos(x)';
xlabel('x'), ylabel('y');
plot(x,eval(f),x,0*x);

ends = [0 2 4 8 10];
result = zeros(1, length(ends) - 1);

for i = 1 : length(ends) - 1
    x_ = [ends(i) ends(i + 1)];
    [result(i), f_value, flag] = fzero(f, x_);
end

