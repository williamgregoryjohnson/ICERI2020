# pearsonr(x, y)
#    Calculates a Pearson correlation coefficient and the p-value for testing
#   non-correlation.
#   
#    The Pearson correlation coefficient measures the linear relationship
#    between two datasets. Strictly speaking, Pearson's correlation requires
#    that each dataset be normally distributed, and not necessarily zero-mean.
#    Like other correlation coefficients, this one varies between -1 and +1
#    with 0 implying no correlation. Correlations of -1 or +1 imply an exact
#    linear relationship. Positive correlations imply that as x increases, so
#    does y. Negative correlations imply that as x increases, y decreases.
#    
#    The p-value roughly indicates the probability of an uncorrelated system
#    producing datasets that have a Pearson correlation at least as extreme
#    as the one computed from these datasets. The p-values are not entirely
#    reliable but are probably reasonable for datasets larger than 500 or so.
#    
#    Parameters
#    ----------
#    x : (N,) array_like
#        Input
#    y : (N,) array_like
#        Input
#  
#    Returns
#    -------
#    r : float
#        Pearson's correlation coefficient
#    p-value : float
#        2-tailed p-value

from scipy.stats.stats import pearsonr

# calculating with complete case analysis (no sparsity)
# MA2420
X2420=[  2.46,
        
2.21,
        
2.60,
        
2.25,
        
1.60,
        
2.46,
        
2.28,
        
2.47,
        
2.50,
        
2.57,
        
2.74,
        
2.45,
        
2.60,
        
3.06,
        
2.76,
        
2.44,
        
3.22,
        
2.38,
        
2.23,
        
2.68,
        
2.67,
        
2.44,
        
2.41,
        
2.33,
        
2.85,
        
2.78,
        
2.35,
        
3.02,
        
2.45,
        
2.97,
        
2.74,
        
2.81,
        
2.52 ]

# data structures
X2420_Y2720=[ 2.46,
        
2.60,
        
2.25,
        
1.60,
        
2.46,
        
2.28,
        
2.47,
        
2.50,
        
2.57,
        
2.74,
        
2.45,
        
2.60,
        
3.06,
        
2.76,
        
2.44,
        
3.22,
        
2.38,
        
2.23,
        
2.68,
        
2.67,
        
2.44,
        
2.41,
        
2.33,
        
2.85,
        
2.78,
        
2.35,
        
3.02,
        
2.45,
        
2.97,
        
2.74,
        
2.81,
        
2.52 ]

Y2720= [  0.00,
          3.58,
        
 3.27,
         
3.50,
         
2.63,
         
3.56,
         
4.00,
         
1.50,
         
3.50,
         
3.00,
         
2.00,
         
3.00,
         
2.78,
         
3.20,
         
2.67,
         
3.15,
         
2.82,
         
0.00,
         
3.00,
         
2.87,
         
3.30,
         
3.70,
         
2.36,
         
2.40,
         
3.53,
         
2.89,
         
2.94,
         
2.90,
         
3.18,
         
2.61,
         
0.00,
         
2.97 ]
DataStructures_r = pearsonr( X2420_Y2720, Y2720 )
print ('DataStructures = '  + str(DataStructures_r) )
############################################################################
# algorithms
Y4520 = [ 0.00,
          0.00,
          2.60,
          3.21,
          2.83,
          1.67,
          3.19,
          2.08,
          2.57,
          2.96,
          0.00,
          0.75,
          2.72,
          3.50,
          2.18,
          2.71,
          3.65,
          2.43,
          2.95,
          2.46,
          2.08,
          3.40,
          3.83,
          2.79,
          3.33,
          3.53,
          3.14,
          3.22,
          3.11,
          3.18,
          3.36,
          0.00,
          3.10 ]
Algorithms_r = pearsonr( X2420, Y4520 )
print('Algorithms = '  + str(Algorithms_r) )
###############################################################################
# computer organization and programming
Y3210 = [ 0.00,
          0.00,
          2.50,
          2.31,
          1.67,
          2.12,
          3.04,
          0.00,
          3.00,
          2.65,
          0.00,
          3.80,
          2.33,
          2.70,
          3.27,
          1.33,
          0.00,
          3.71,
          3.38,
          3.60,
          2.25,
          2.60,
          2.67,
          2.50,
          3.43,
          2.33,
          3.08,
          3.12,
          2.71,
          2.51,
          2.47,
          0.00,
          2.42 ]
ComputerOrgProg_r = pearsonr( X2420, Y3210 )
print('Computer Org & Prog = '  + str(ComputerOrgProg_r) )
###############################################################################
# systems level programming
Y3320 = [ 0.00,
          0.00,
          2.50,
          3.00,
          3.61,
          3.00,
          2.92,
          3.70,
          4.00,
          3.74,
          2.00,
          3.27,
          2.22,
          4.00,
          3.07,
          2.07,
          2.00,
          3.04,
          2.90,
          2.17,
          2.33,
          2.45,
          2.57,
          2.60,
          3.46,
          3.69,
          2.90,
          3.08,
          3.27,
          3.11,
          3.18,
          0.00,
          3.35 ]
Systems_r = pearsonr( X2420, Y3320 )
print('Systems Level Prog = '  + str(Systems_r) )
###############################################################################
# computer architecture

Y4210 = [0.00000000,
         0.00000000,
         2.30769200,
         2.66666700,
         3.85714300,
         3.00000000,
         2.82500000,
         3.00000000,
         2.57142900,
         2.80000000,
         4.00000000,
         1.50000000,
         2.80000000,
         3.50000000,
         0.00000000,
         2.62500000,
         3.00000000,
         2.75000000,
         1.98333300,
         3.50000000,
         3.01818200,
         3.00000000,
         3.33333300,
         2.86000000,
         3.15384600,
         3.46153800,
         3.28000000,
         2.87500000,
         2.84166700,
         3.05238100,
         3.04117600,
         0.00000000,
         3.008333005]
Systems_r = pearsonr( X2420, Y4210 )
print('Computer Architecture = '  + str(Systems_r) )
###############################################################################
# programming languages
X2420_Y4330 = [ 2.46,
        
2.60,
        
2.25,
        
2.46,
        
2.28,
        
2.50,
        
2.57,
        
2.45,
        
2.60,
        
2.76,
        
2.44,
        
2.38,
        
2.23,
        
2.67,
        
2.44,
        
2.33,
        
2.85,
        
2.35,
        
3.02,
        
2.45,
        
2.97,
        
2.74,
        
2.81,
        
2.52 ]
Y4330 = [ 0.00,
          2.22,
          1.91,
          1.67,
          1.83,
          2.44,
          1.85,
          2.61,
          0.83,
          0.57,
          2.28,
          2.53,
          2.56,
          2.61,
          2.50,
          2.79,
          2.86,
          2.58,
          2.50,
          2.00,
          2.64,
          3.04,
          0.00,
          3.05 ]
ProgLanguages_r = pearsonr( X2420_Y4330, Y4330 )
print('Programming Languages = '  + str(ProgLanguages_r) )
###############################################################################
# software engineering
X2420_Y4350 = [ 2.46,
        
2.60,
        
2.25,
        
2.46,
        
2.28,
        
2.50,
        
2.57,
        
2.45,
        
2.60,
        
2.76,
        
2.44,
        
2.38,
        
2.23,
        
2.67,
        
2.44,
        
2.33,
        
2.85,
        
2.35,
        
3.02,
        
2.97,
        
2.74,
        
2.81,
        
2.52 ]
Y4350 = [ 0.00,
          3.51,
          3.93,
          2.95,
          3.22,
          3.77,
          3.71,
          3.49,
          3.67,
          3.33,
          3.00,
          3.51,
          3.50,
          3.40,
          3.00,
          3.53,
          3.10,
          3.35,
          3.55,
          3.31,
          3.30,
          0.00,
          3.17 ]
SoftwareEngineer_r = pearsonr( X2420_Y4350, Y4350 )
print('SoftwareEngineering = '  + str(SoftwareEngineer_r) )


