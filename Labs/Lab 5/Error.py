from sympy import symbols, diff
import numpy as np

n_0 = 1.716e-5
T_0 = 273.15
S_n = 110.4
g = 9.80665
p = 886
N = 44+17+16+10+6   # Number of data points

a, n, d, V, v_f, T, v_r = symbols("a, n, d, V, v_f, T, v_r", real=True)

d1, d2, t1, t2 = symbols("d1, d2, t1, t2", real = True)

n = n_0*(T/T_0)**(3/2)*((T_0+S_n)/(T+S_n))

a = (9/2*v_f/1000/(p*g)*n)**(1/2)

q = d/V*(4/3*np.pi*a**3*p*g-6*np.pi*n*a*v_r/1000)

# q = d/V*(4/3*np.pi*g*(9/2*v_f/(p*g)*n_0*(T/T_0)**(3/2)*(T_0 + S_n)/(T + S_n))**(3/2) -
#          6*np.pi*v_r*n_0*(T/T_0)**(3/2)*(T_0 + S_n)/(T + S_n)*(9/2*v_f/(p*g)*n_0*(T/T_0)**(3/2)*(T_0 + S_n)/(T + S_n))**(1/2))


r = ((d2 - d1)/(175.0813*1000)) / ((t2 - t1) / 15)

r_d1 = diff(r, d1)
r_d2 = diff(r, d2)
r_t1 = diff(r, t1)
r_t2 = diff(r, t2)

sigma_d = 0.01**2
sigma_t = 0.01**2 

diff_d1 = (float(r_d1.subs({d1: 300, d2: 500, t1: 300, t2: 500})))**2
diff_d2 = (float(r_d2.subs({d1: 300, d2: 500, t1: 300, t2: 500})))**2
diff_t1 = (float(r_t1.subs({d1: 300, d2: 500, t1: 300, t2: 500})))**2
diff_t2 = (float(r_t2.subs({d1: 300, d2: 500, t1: 300, t2: 500})))**2

uncertainty_velocity = np.sqrt(diff_d1*sigma_d + diff_d2*sigma_d + diff_t1*sigma_t + diff_t2*sigma_t)

print("Uncertainty in Velocity: " + str(uncertainty_velocity) + " m/s")

q_d = diff(q, d)
q_V = diff(q, V)
q_v_r = diff(q, v_r)
q_T = diff(q, T)
q_v_f = diff(q, v_f)

print(q)
# print()
# print(q_d)
# print()
# print(q_V)
# print()
# print(q_v_r)
# print()
# print(q_T)
# print()
# print(q_v_f)

T_val = (237.15+26)
r_val = 0.02763198
f_val = 0.1472828
V_val = 557 
d_val = 7.6e-3

diff_d = (float(q_d.subs({T: T_val, v_r: r_val, v_f: f_val, V: V_val, d: d_val})))**2
diff_V = (float(q_V.subs({T: T_val, v_r: r_val, v_f: f_val, V: V_val, d: d_val})))**2
diff_r = (float(q_v_r.subs({T: T_val, v_r: r_val, v_f: f_val, V: V_val, d: d_val})))**2
diff_T = (float(q_T.subs({T: T_val, v_r: r_val, v_f: f_val, V: V_val, d: d_val})))**2
diff_f = (float(q_v_f.subs({T: T_val, v_r: r_val, v_f: f_val, V: V_val, d: d_val})))**2

sigma_T = 1**2 
sigma_d = (0.1e-3)**2 
sigma_r = uncertainty_velocity**2
sigma_f = uncertainty_velocity**2
sigma_V = 1**2

uncertainty_q = np.sqrt(diff_d*sigma_d + diff_V*sigma_V + diff_r*sigma_r + diff_f*sigma_f + diff_T*sigma_T) / np.sqrt(N)

print("Uncertainty in Charge: " + str(uncertainty_q) + " C")

print(diff_d*sigma_d/N, diff_V*sigma_V/N, diff_r*sigma_r/N, diff_T*sigma_T/N, diff_f*sigma_f/N)
print(np.sqrt(diff_d*sigma_d/N + diff_V*sigma_V/N + diff_r*sigma_r/N + diff_T*sigma_T/N + diff_f*sigma_f/N))