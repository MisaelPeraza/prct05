#!/usr/bin/python
#!encoding: UTF-8

import sys

def calc_xi (n, i):
  xi = (i-1.0/2.0)/n
  return xi

argumentos = sys.argv[1:]
print argumentos
if (len(argumentos) == 1):
    n = int (argumentos[0])
else:
    n=int(raw_input('introduzca el número de intervalos: '))
  

pi_35 = 3.1415926535897931159979634685441852  

if (n>0):
    sumatorio = 0.0
    inicial = 0
    intervalos = 1.0 / float(n)
    for i in range(n):
      x_i = calc_xi (n, i+1)
      fx_i = 4.0 / (1.0 ++ x_i * x_i)
      print "Subintervalo: [", inicial, ",", inicial+intervalos, "]" " x_i:",x_i, "fx_i:", fx_i	
      
      inicial += intervalos
      sumatorio += fx_i   
    aprox_pi = sumatorio / n
    print "El valor de la aproximación es: ", aprox_pi
    print "El valor de pi con 35 decimales es: %10.35f" % pi_35
    
    
    
else:
    print 'El número de intervalos debe ser positivo'

