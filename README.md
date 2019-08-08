# simple-linear-regression

In statistics, a collection of tools used to model and explore relationships between variables that are related in a nondeterministic manner is called regession analysis.

A linear regression model is "most probable" or "most accurate" linear relationship between variables. In simple linear regression we are therefore concerned about finding linear relationship between a dependent variable and an independent variable. For doing this we generally use the technique of ordinary least squares (OLS).

OLS method works by minimising the sum of squares of errors(SSE), we do it as follows:

y = αx + β  (Supposed model)

ε_i = y_i - (αx_i + β)  (Residual ε_i is difference between actual value and predicted value of y_i)

∑_i▒〖ε_i〗^2 = ∑_i▒〖y_i - (αx_i + β)〗^2 (SSE)

Minimising SSE, will give:

α = (∑_i▒〖(x_i- (x')) ̌(y- (y'))〗)/(∑_i▒〖(x_i- (x'))〗^2 ) (x' and y' are mean of x and y)

β = y' - αx' (x' and y' are mean of x and y)
