. fix the outliers to be "." (missing)
replace tta = . if tta > 22
replace tta = . if tta < 0

generate int ttarange = 1 if tta<4, before(tta)
replace ttarange = 2 if tta==4 | tta==5
replace ttarange = 3 if tta>5
 

replace  = . if  > 22
replace  = . if  < 0

generate int range = 1 if <4, before()
replace range = 2 if ==4 | ==5
replace range = 3 if >5
 
replace  = . if ==99
replace cs2510 = . if cs2510==99
replace ma2420 = . if ma2420==99

replace sex = . if sex==99
replace race = . if race==99
replace transfer = . if transfer==99


. first regresion model (RM) on Cohort_CS

regress cs4520 cs2510

regress cs4520 cs2510

regress cs4520 cs2510  tta 

regress cs4520 cs2510  tta 

regress cs4520 cs2510  tta  transfer

. second regresion model (RM) on Cohort_CS

regress cs4520 

regress cs4520  cs2510  

regress cs4520  cs2510    

regress cs4520  cs2510  tta 

regress cs4520  cs2510  tta transfer

codebook cs4520 cs2510  tta  transfer


. first regresion model (RM) on Cohort_Math

regress cs4520 ma2420 

regress cs4520 ma2420  

regress cs4520 ma2420 tta   

regress cs4520 ma2420  ttamed 

regress cs4520 ma2420  ttahi

regress cs4520 ma2420  tta 

regress cs4520 ma2420  tta  transfer



. second regresion model (RM) on Cohort_Math

regress cs4520 i.ttarange##transfer ma2420 i.ttarange#c.ma2420

regress cs4520 ma2420   

regress cs4520 ma2420     

regress cs4520 ma2420   tta 

regress cs4520 ma2420   tta transfer

codebook cs4520 ma2420  tta  transfer