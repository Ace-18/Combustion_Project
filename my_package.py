from sympy import Eq , solve , symbols , Function, exp, solveset
import pandas as pd


#defining functions to be used 
#
def get_key(v,dictionary):
    '''returns keys of the value provided''' 
    for key, value in dictionary.items():
         if v == value:
            return key
        

def interpolate(temp,df):
    '''returns the properties of the provided temperature using interpolation'''
     
    for t in df.index[1:]:
        if t<temp:
            t1=t
        
        elif t>temp:
            t2=t
            break
    
    y1=df.loc[t1] 
    y2=df.loc[t2]
    
    y= (y1)+(y2-y1)*(temp-t1)/(t2-t1)
    
    return y


data_dict={
    'h_f':[ None,None,0, 0 , -393520 , -241820,-110530,0],
    298: [-92.208,-103.762,0,0,0,0,0,0], 
    500: [-52.691,-57.616,5912,6088,8314,6920,5929,5883],
    1000: [-23.163,-23.529,21460,22707,33405,25978,21686,20686],
    1200: [-18.182,-17.871,28108,29765,44484,34476,28426,26794],
    1400: [-14.609,-13.842,34936,36966,55907,43447,35338,33062],
    1600: [-11.921,-10.83,41903,44279,67580,52844,42384,39522],
    1800: [-9.826,-8.497,48982,51689,79442,62609,49522,46150],
    2000: [-8.145,-6.635,56141,59199,91450,72689,56739,52932],
    2100:[None,None,59399,62653,96882,76666,60052,55840],
    2200: [-6.768,-5.12,62872,66304,102696,81345,63562,59065],
    2300: [None,None,66345,69955,108511,86024,67072,62291],
    2400: [-5.619,-3.86,69818,73607,114325,90703,70582,65516],
    2500: [None,None,73291,77258,120140,95382,74093,68741],
    2600: [-4.648,-2.801,None,None,None,None,None,None]
}


ind=['Kp1','Kp2','N2','O2','CO2','H2O','CO','H2']

'H2O ⇌ H2 + 1/2 O2 ----->Kp1'

'CO2 ⇌ CO + 1/2 O2 ----->Kp2'


data=pd.DataFrame(data_dict,index=ind)


data=data.T #dataframe having temperature as index 
data[data.columns[:3]]=data[data.columns[:3]].interpolate() #missing ln(Kp) values at certain temperatures[2100,2300,2500] are filled

