x = linspace(-3, 3, 10000);
f = 'sin(exp(x))';
xlabel('x'), ylabel('y');
plot(x,eval(f),x,0*x);

ends = [1 1.5 2 2.4 2.63 2.85 3]
result_2 = zeros(1, length(ends) - 1)
eps = 0.000001

for i = 1 : length(ends) - 1
    x_ = [ends(i) ends(i + 1)];
    k = 0;
    m = -1;
    while (k < 1000) 
        m = (x_(2) - x_(1)) / 2 + x_(1);
        if (abs(f2(m)) < eps)
            break;
        end
        if (sign(f2(m)) == sign(f2(x_(1))))
            x_(1) = m;
        else
            x_(2) = m;
        end
        k = k + 1;
    end
    result_2(i) = m;
end

result_3 = zeros(1, length(ends) - 1)
for i = 1 : length(ends) - 1
    x_ = [ends(i) ends(i + 1)];
    x_0 = (x_(2) - x_(1)) / 2 + x_(1);
    k = 0;
    while (k < 1000)
        x_0 = x_0 - f2(x_0) / f2_pr(x_0);
        if (abs(f2(x_0)) < eps)
            break
        end
        k = k + 1;
    end
    result_3(i) = x_0
end

check = abs(result_2 - result_3) < eps

function f = f2(x)
f = sin(exp(x));
end

function f = f2_pr(x)
f = cos(exp(x)) * exp(x);
end