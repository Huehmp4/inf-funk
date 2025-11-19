import math
import plaskie
def cude(a:float) -> float:
    return (a**3)
def pros(a:float,b:float,c:float) -> float:
    return 2 * (a*b + b*c + a*c)
def granbokrownpodkw(a,b) -> float:
    return (2*(2*(a**2) + plaskie.kwipro(a,b)))
def ostpodkwa(a,h) -> float:
    h = a
    P_p = a**2
    h_t = math.sqrt(h**2 + (a/2)**2)
    P_t = (a * h_t)/2
    P_b = 4 * P_t
    P_c = P_p + P_b
    return P_c