function main()
a = 5
n = 3
m = 10

step = pi/2;
border = 2 * m * pi;
x = zeros(border / step)
y = zeros(border / step)
i = 1;
for fi = 0 : step : border
    x(i) = x_value(a, n, m, fi)
    y(i) = y_value(a, n, m, fi)
    i = i + 1
end
plot(x, y)
end

function x = x_value(a, n, m, fi)
    x = (1 + n/m) * cos(fi * n / m) - a * (n / m) * cos((1 + n/m) * fi)
end

function y = y_value(a, n, m, fi)
    y = (1 + n/m) * sin(fi * n / m) - a * (n / m) * sin((1 + n/m) * fi)
end