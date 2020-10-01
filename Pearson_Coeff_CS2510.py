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
# CSC2510
X2510=[ 2.85,
2.67,
2.77,
2.82,
2.73,
3.09,
2.42,
2.71,
2.57,
2.74,
3.38,
2.82,
2.94,
3.26,
2.48,
3.12,
3.00,
2.71,
3.11,
3.02,
2.80,
2.72,
3.14,
3.02,
2.93,
3.21,
2.93,
3.26,
0.00,
2.55 ]

# data structures
Y2720= [ 3.08,
3.40,
2.58,
2.44,
2.91,
2.33,
2.90,
3.17,
2.82,
3.34,
3.25,
2.51,
3.09,
2.82,
2.86,
2.36,
2.79,
2.77,
2.09,
2.51,
2.34,
2.18,
3.02,
2.45,
2.63,
2.88,
3.17,
2.71,
0.00,
2.89 ]
# algorithms
Y4520= [ 3.00,
1.00,
3.43,
2.81,
2.50,
3.16,
2.32,
2.34,
3.25,
3.16,
1.76,
3.22,
2.90,
3.06,
3.12,
3.21,
2.33,
3.16,
3.15,
2.48,
3.15,
2.97,
2.74,
3.09,
2.90,
3.24,
2.88,
0.00,
3.10 ]
# computer organization and programming
Y3210= [ 2.62,
3.33,
2.94,
2.59,
3.30,
2.55,
2.43,
3.86,
3.41,
2.49,
3.11,
3.24,
2.04,
2.89,
3.21,
3.05,
2.75,
2.31,
1.95,
2.61,
2.32,
2.71,
1.88,
2.90,
2.88,
2.43,
2.60,
2.37,
0.00,
2.12 ]
# systems level programming
Y3320= [ 2.33,
3.62,
2.69,
2.56,
3.65,
3.05,
1.97,
2.80,
3.56,
2.34,
3.06,
3.34,
2.85,
3.00,
2.99,
3.49,
3.42,
2.74,
2.36,
2.66,
2.80,
3.16,
3.54,
2.90,
3.00,
2.70,
3.19,
2.82,
0.00,
2.87 ]
# computer architecture
Y4210= [3.000,
        3.667,
        3.800,
        3.250,
        2.669,
        2.214,
        3.330,
        3.018,
        3.039,
        3.250,
        3.025,
        2.667,
        2.500,
        2.848,
        2.236,
        2.900,
        3.176,
        2.750,
        2.500,
        2.819,
        3.134,
        2.664,
        2.833,
        2.526,
        2.613,
        3.037,
        2.695,
        0.000,
        2.647
        ]
#sparse 2510 related to computer architecture: 4210
X2510_4210= [2.67,
              2.77,
              2.82,
              2.73,
              3.09,
              2.42,
              2.71,
              2.57,
              2.74,
              3.38,
              2.82,
              2.94,
              3.26,
              2.48,
              3.12,
              3.00,
              2.71,
              3.11,
              3.02,
              2.80,
              2.72,
              3.14,
              3.02,
              2.93,
              3.21,
              2.93,
              3.26,
              0.00,
              2.55
    ]
# programming languages
Y4330= [ 2.15,
2.43,
3.08,
1.47,
1.64,
2.41,
2.31,
1.98,
2.54,
2.41,
2.06,
2.61,
2.46,
2.25,
2.42,
2.42,
2.42,
2.47,
2.52,
0.00,
2.53 ]
# software engineering
Y4350= [ 3.67,
3.50,
3.46,
3.18,
3.52,
3.33,
3.26,
3.36,
3.07,
3.22,
3.35,
3.03,
3.51,
3.06,
3.28,
3.36,
2.95,
2.93,
0.00,
2.68 ]
# sparse 2510, specific to 4330 and 4350
X2510_4330_4350= [ 3.08, 2.58,
2.44, 2.33,
2.90, 2.82,
3.34, 2.51,
3.09, 2.86,
2.36, 2.77,
2.09, 2.34,
2.18, 2.45,
2.63, 3.17,
2.71,
0.00,
2.89 ]

DataStructures_r = pearsonr( X2510, Y2720 )
Algorithms_r = pearsonr( X2510[1: ], Y4520 )
ComputerOrgProg_r = pearsonr( X2510, Y3210 )
Systems_r = pearsonr( X2510, Y3320 )
CompArchitecture_r = pearsonr( X2510_4210, Y4210)
ProgLanguages_r = pearsonr( X2510_4330_4350, Y4330 )
SoftwareEngineer_r = pearsonr( X2510_4330_4350[1: ], Y4350 )
print ('DataStructures = '  + str(DataStructures_r) )
print('Computer Org & Prog = '  + str(ComputerOrgProg_r) )
print('Systems Level Prog = '  + str(Systems_r) )
print('Computer Architecture = '  + str(CompArchitecture_r) )
print('Programming Languages = '  + str(ProgLanguages_r) )
print('SoftwareEngineering = '  + str(SoftwareEngineer_r) )
print('Algorithms = '  + str(Algorithms_r) )

