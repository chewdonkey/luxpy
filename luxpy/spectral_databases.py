# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 20:25:52 2017

@author: kevin.smet
"""

###############################################################################
# load spd and rfl databases
###############################################################################
#
# _S_dir: Folder with light source spectra data.
#
# _R_dir: Folder with spectral reflectance data
#
# _iestm30: Database with spectral reflectances related to and light source spectra contained excel calculator of [IES TM30-15](https://www.ies.org/store/technical-memoranda/ies-method-for-evaluating-light-source-color-rendition/) publication.
#
# _iestm30_S: Database with only light source spectra contained in IES TM30-15 excel calculator.
#
# _cie_illuminants: Database with CIE illuminants: 'E','D65','A','C','F1','F2','F3','F4','F5','F6','F7','F8','F9','F10','F11','F12'
#
# _cri_rfl: Database with spectral reflectance functions for various color rendition calculators
#           * [CIE 13.3-1995 (8, 14 munsell samples)](http://www.cie.co.at/index.php/index.php?i_ca_id=303), 
#           * [CIE 224:2015 (99 set)](http://www.cie.co.at/index.php?i_ca_id=1027)
#           * [CRI2012 (HL17 & HL1000 spetcrally uniform and 210 real samples)](http://journals.sagepub.com/doi/abs/10.1177/1477153513481375))
#           * [IES TM30 (99, 4880 sepctrally uniform samples)](https://www.ies.org/store/technical-memoranda/ies-method-for-evaluating-light-source-color-rendition/)
#           * [MCRI (10 familiar object set)](http://www.sciencedirect.com/science/article/pii/S0378778812000837)
#           * [CQS (v7.5 and v9.0 sets)](http://spie.org/Publications/Journal/10.1117/1.3360335)
#
# _munsell: Database with 1269 Munsell spectral reflectance functions + Value (V), Chroma (C), hue (h) and (ab) specifications.
#
#
#------------------------------------------------------------------------------

from luxpy import *
__all__ = ['_R_dir','_S_dir', '_iestm30','_iestm30_S','_cri_rfl','_cie_illuminants','_munsell']


#_C_dir = _pckg_dir + _sep + 'data'+ _sep + 'cmfs' + _sep #folder with cmf data
_S_dir = _pckg_dir + _sep + 'data'+ _sep + 'spds' + _sep #folder with spd data
_R_dir = _pckg_dir + _sep + 'data'+ _sep + 'rfls' + _sep #folder with rfl data



###############################################################################
# spectral power distributions:
    
# load TM30 spd data base:
_iestm30 = {'S': {'data': getdata(_S_dir + 'IESTM30_Sspds.dat',kind='np').transpose()}}
_iestm30['S']['info'] = getdata(_S_dir + 'IESTM30_Sinfo.txt',kind='np',header='infer',verbosity = False)
_iestm30_S = _iestm30['S']




#------------------------------------------------------------------------------
# Illuminant library: set some typical CIE illuminants:
E = np.array([np.linspace(380,780,81),np.ones(81)])
D65 = np.array([[380,381,382,383,384,385,386,387,388,389,390,391,392,393,394,395,396,397,398,399,400,401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416,417,418,419,420,421,422,423,424,425,426,427,428,429,430,431,432,433,434,435,436,437,438,439,440,441,442,443,444,445,446,447,448,449,450,451,452,453,454,455,456,457,458,459,460,461,462,463,464,465,466,467,468,469,470,471,472,473,474,475,476,477,478,479,480,481,482,483,484,485,486,487,488,489,490,491,492,493,494,495,496,497,498,499,500,501,502,503,504,505,506,507,508,509,510,511,512,513,514,515,516,517,518,519,520,521,522,523,524,525,526,527,528,529,530,531,532,533,534,535,536,537,538,539,540,541,542,543,544,545,546,547,548,549,550,551,552,553,554,555,556,557,558,559,560,561,562,563,564,565,566,567,568,569,570,571,572,573,574,575,576,577,578,579,580,581,582,583,584,585,586,587,588,589,590,591,592,593,594,595,596,597,598,599,600,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633,634,635,636,637,638,639,640,641,642,643,644,645,646,647,648,649,650,651,652,653,654,655,656,657,658,659,660,661,662,663,664,665,666,667,668,669,670,671,672,673,674,675,676,677,678,679,680,681,682,683,684,685,686,687,688,689,690,691,692,693,694,695,696,697,698,699,700,701,702,703,704,705,706,707,708,709,710,711,712,713,714,715,716,717,718,719,720,721,722,723,724,725,726,727,728,729,730,731,732,733,734,735,736,737,738,739,740,741,742,743,744,745,746,747,748,749,750,751,752,753,754,755,756,757,758,759,760,761,762,763,764,765,766,767,768,769,770,771,772,773,774,775,776,777,778,779,780],
              [49.98,50.33,50.84,51.42,51.94,52.31,52.47,52.58,52.84,53.46,54.65,56.56,59.08,62.05,65.31,68.7,72.06,75.26,78.19,80.73,82.75,84.2,85.18,85.89,86.47,87.12,87.95,88.91,89.89,90.78,91.49,91.92,92.15,92.26,92.33,92.46,92.69,92.99,93.26,93.44,93.43,93.18,92.7,92,91.11,90.06,88.89,87.78,86.91,86.48,86.68,87.64,89.23,91.24,93.49,95.77,97.93,99.92,101.7,103.4,104.9,106.2,107.4,108.5,109.7,110.9,112.3,113.7,115,116.2,117,117.5,117.6,117.6,117.5,117.4,117.4,117.6,117.7,117.8,117.8,117.7,117.4,117.1,116.7,116.3,115.9,115.6,115.3,115,114.9,114.8,114.8,115,115.2,115.4,115.7,115.9,116.1,116.1,115.9,115.5,114.9,114.1,113.3,112.4,111.5,110.6,109.8,109.2,108.8,108.6,108.6,108.7,108.9,109.1,109.2,109.3,109.4,109.4,109.4,109.2,109.1,108.9,108.7,108.6,108.4,108.3,108.1,108,107.8,107.6,107.3,107,106.7,106.3,105.9,105.5,105.1,104.9,104.8,104.9,105.1,105.4,105.8,106.2,106.7,107.1,107.4,107.6,107.7,107.6,107.3,106.9,106.5,106,105.6,105.2,104.9,104.6,104.4,104.3,104.2,104.2,104.2,104.2,104.3,104.3,104.3,104.2,104,103.8,103.4,103,102.5,102,101.6,101.2,100.8,100.4,100,99.64,99.29,98.93,98.56,98.17,97.76,97.34,96.95,96.61,96.33,96.15,96.04,96,96.01,96.06,96.13,96.19,96.18,96.06,95.79,95.33,94.71,93.96,93.13,92.24,91.33,90.47,89.7,89.08,88.69,88.54,88.59,88.79,89.06,89.35,89.58,89.76,89.89,89.97,90.01,90,89.96,89.9,89.85,89.8,89.78,89.76,89.74,89.69,89.6,89.45,89.27,89.06,88.85,88.65,88.48,88.32,88.16,87.96,87.7,87.37,86.97,86.52,86.02,85.49,84.95,84.43,83.95,83.56,83.29,83.15,83.14,83.21,83.34,83.49,83.64,83.76,83.82,83.81,83.7,83.48,83.16,82.77,82.33,81.86,81.4,80.95,80.56,80.24,80.03,79.93,79.92,79.98,80.06,80.12,80.15,80.15,80.15,80.16,80.21,80.32,80.48,80.69,80.95,81.25,81.58,81.9,82.15,82.3,82.28,82.06,81.7,81.23,80.74,80.28,79.89,79.54,79.19,78.79,78.28,77.64,76.88,76,75.04,74,72.93,71.88,70.95,70.2,69.72,69.56,69.67,69.95,70.31,70.67,70.95,71.16,71.33,71.47,71.61,71.77,71.96,72.22,72.55,72.98,73.5,74.02,74.41,74.56,74.35,73.69,72.64,71.28,69.7,67.98,66.22,64.56,63.14,62.1,61.6,61.73,62.38,63.37,64.55,65.74,66.83,67.77,68.59,69.29,69.89,70.39,70.84,71.31,71.84,72.49,73.27,74.08,74.75,75.14,75.09,74.5,73.47,72.17,70.74,69.34,68.09,66.95,65.87,64.77,63.59,62.27,60.77,59.08,57.17,55.01,52.63,50.28,48.27,46.88,46.42,47.09,48.72,51.03,53.75,56.61,59.36,61.86,64.01,65.69,66.81,67.28,67.21,66.73,65.98,65.09,64.21,63.46,62.98,62.91,63.38]])
A = np.array([[380,381,382,383,384,385,386,387,388,389,390,391,392,393,394,395,396,397,398,399,400,401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416,417,418,419,420,421,422,423,424,425,426,427,428,429,430,431,432,433,434,435,436,437,438,439,440,441,442,443,444,445,446,447,448,449,450,451,452,453,454,455,456,457,458,459,460,461,462,463,464,465,466,467,468,469,470,471,472,473,474,475,476,477,478,479,480,481,482,483,484,485,486,487,488,489,490,491,492,493,494,495,496,497,498,499,500,501,502,503,504,505,506,507,508,509,510,511,512,513,514,515,516,517,518,519,520,521,522,523,524,525,526,527,528,529,530,531,532,533,534,535,536,537,538,539,540,541,542,543,544,545,546,547,548,549,550,551,552,553,554,555,556,557,558,559,560,561,562,563,564,565,566,567,568,569,570,571,572,573,574,575,576,577,578,579,580,581,582,583,584,585,586,587,588,589,590,591,592,593,594,595,596,597,598,599,600,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633,634,635,636,637,638,639,640,641,642,643,644,645,646,647,648,649,650,651,652,653,654,655,656,657,658,659,660,661,662,663,664,665,666,667,668,669,670,671,672,673,674,675,676,677,678,679,680,681,682,683,684,685,686,687,688,689,690,691,692,693,694,695,696,697,698,699,700,701,702,703,704,705,706,707,708,709,710,711,712,713,714,715,716,717,718,719,720,721,722,723,724,725,726,727,728,729,730,731,732,733,734,735,736,737,738,739,740,741,742,743,744,745,746,747,748,749,750,751,752,753,754,755,756,757,758,759,760,761,762,763,764,765,766,767,768,769,770,771,772,773,774,775,776,777,778,779,780],
               [9.795,10.01,10.23,10.45,10.67,10.9,11.13,11.36,11.6,11.84,12.09,12.33,12.58,12.84,13.09,13.35,13.62,13.89,14.16,14.43,14.71,14.99,15.27,15.56,15.85,16.15,16.45,16.75,17.05,17.36,17.68,17.99,18.31,18.63,18.96,19.29,19.62,19.96,20.3,20.65,21,21.35,21.7,22.06,22.42,22.79,23.16,23.53,23.91,24.29,24.67,25.06,25.45,25.84,26.24,26.64,27.05,27.46,27.87,28.28,28.7,29.13,29.55,29.98,30.41,30.85,31.29,31.73,32.18,32.63,33.09,33.54,34,34.47,34.94,35.41,35.88,36.36,36.84,37.32,37.81,38.3,38.8,39.3,39.8,40.3,40.81,41.32,41.83,42.35,42.87,43.39,43.92,44.45,44.98,45.52,46.06,46.6,47.14,47.69,48.24,48.8,49.35,49.91,50.48,51.04,51.61,52.18,52.76,53.33,53.91,54.5,55.08,55.67,56.26,56.85,57.45,58.05,58.65,59.26,59.86,60.47,61.08,61.7,62.31,62.93,63.55,64.18,64.8,65.43,66.06,66.7,67.33,67.97,68.61,69.25,69.9,70.54,71.19,71.84,72.5,73.15,73.81,74.47,75.13,75.79,76.45,77.12,77.79,78.46,79.13,79.81,80.48,81.16,81.84,82.52,83.2,83.89,84.57,85.26,85.95,86.64,87.33,88.02,88.72,89.41,90.11,90.81,91.51,92.21,92.91,93.62,94.32,95.03,95.73,96.44,97.15,97.86,98.57,99.29,100,100.7,101.4,102.2,102.9,103.6,104.3,105,105.7,106.5,107.2,107.9,108.6,109.3,110.1,110.8,111.5,112.3,113,113.7,114.4,115.2,115.9,116.6,117.3,118.1,118.8,119.5,120.3,121,121.7,122.5,123.2,123.9,124.7,125.4,126.1,126.8,127.6,128.3,129,129.8,130.5,131.2,132,132.7,133.4,134.2,134.9,135.6,136.3,137.1,137.8,138.5,139.3,140,140.7,141.4,142.2,142.9,143.6,144.3,145.1,145.8,146.5,147.2,148,148.7,149.4,150.1,150.8,151.6,152.3,153,153.7,154.4,155.1,155.8,156.6,157.3,158,158.7,159.4,160.1,160.8,161.5,162.2,162.9,163.6,164.3,165,165.7,166.4,167.1,167.8,168.5,169.2,169.9,170.6,171.3,172,172.7,173.3,174,174.7,175.4,176.1,176.7,177.4,178.1,178.8,179.4,180.1,180.8,181.4,182.1,182.8,183.4,184.1,184.8,185.4,186.1,186.7,187.4,188.1,188.7,189.3,190,190.6,191.3,191.9,192.6,193.2,193.8,194.5,195.1,195.8,196.4,197,197.6,198.3,198.9,199.5,200.1,200.7,201.4,202,202.6,203.2,203.8,204.4,205,205.6,206.2,206.8,207.4,208,208.6,209.2,209.8,210.4,210.9,211.5,212.1,212.7,213.3,213.8,214.4,215,215.6,216.1,216.7,217.3,217.8,218.4,218.9,219.5,220,220.6,221.1,221.7,222.2,222.8,223.3,223.8,224.4,224.9,225.4,225.9,226.5,227,227.5,228,228.6,229.1,229.6,230.1,230.6,231.1,231.6,232.1,232.6,233.1,233.6,234.1,234.6,235.1,235.6,236.1,236.5,237,237.5,238,238.4,238.9,239.4,239.8,240.3,240.8,241.2,241.7]])
F4 = np.array([[380,381,382,383,384,385,386,387,388,389,390,391,392,393,394,395,396,397,398,399,400,401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416,417,418,419,420,421,422,423,424,425,426,427,428,429,430,431,432,433,434,435,436,437,438,439,440,441,442,443,444,445,446,447,448,449,450,451,452,453,454,455,456,457,458,459,460,461,462,463,464,465,466,467,468,469,470,471,472,473,474,475,476,477,478,479,480,481,482,483,484,485,486,487,488,489,490,491,492,493,494,495,496,497,498,499,500,501,502,503,504,505,506,507,508,509,510,511,512,513,514,515,516,517,518,519,520,521,522,523,524,525,526,527,528,529,530,531,532,533,534,535,536,537,538,539,540,541,542,543,544,545,546,547,548,549,550,551,552,553,554,555,556,557,558,559,560,561,562,563,564,565,566,567,568,569,570,571,572,573,574,575,576,577,578,579,580,581,582,583,584,585,586,587,588,589,590,591,592,593,594,595,596,597,598,599,600,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633,634,635,636,637,638,639,640,641,642,643,644,645,646,647,648,649,650,651,652,653,654,655,656,657,658,659,660,661,662,663,664,665,666,667,668,669,670,671,672,673,674,675,676,677,678,679,680,681,682,683,684,685,686,687,688,689,690,691,692,693,694,695,696,697,698,699,700,701,702,703,704,705,706,707,708,709,710,711,712,713,714,715,716,717,718,719,720,721,722,723,724,725,726,727,728,729,730,731,732,733,734,735,736,737,738,739,740,741,742,743,744,745,746,747,748,749,750,751,752,753,754,755,756,757,758,759,760,761,762,763,764,765,766,767,768,769,770,771,772,773,774,775,776,777,778,779,780],
                [0.57,0.596,0.622,0.648,0.674,0.7,0.734,0.768,0.802,0.836,0.87,0.892,0.914,0.936,0.958,0.98,1.186,1.392,1.598,1.804,2.01,4.358,6.706,9.054,11.4,13.75,11.39,9.03,6.67,4.31,1.95,1.878,1.806,1.734,1.662,1.59,1.624,1.658,1.692,1.726,1.76,1.794,1.828,1.862,1.896,1.93,1.964,1.998,2.032,2.066,2.1,7.736,13.37,19.01,24.64,30.28,25.83,21.38,16.93,12.48,8.03,6.934,5.838,4.742,3.646,2.55,2.58,2.61,2.64,2.67,2.7,2.724,2.748,2.772,2.796,2.82,2.838,2.856,2.874,2.892,2.91,2.926,2.942,2.958,2.974,2.99,3,3.01,3.02,3.03,3.04,3.048,3.056,3.064,3.072,3.08,3.082,3.084,3.086,3.088,3.09,3.09,3.09,3.09,3.09,3.09,3.1,3.11,3.12,3.13,3.14,3.124,3.108,3.092,3.076,3.06,3.048,3.036,3.024,3.012,3,2.996,2.992,2.988,2.984,2.98,2.986,2.992,2.998,3.004,3.01,3.036,3.062,3.088,3.114,3.14,3.194,3.248,3.302,3.356,3.41,3.508,3.606,3.704,3.802,3.9,4.058,4.216,4.374,4.532,4.69,4.914,5.138,5.362,5.586,5.81,6.112,6.414,6.716,7.018,7.32,10.37,13.43,16.48,19.54,22.59,21.09,19.6,18.1,16.61,15.11,14.86,14.62,14.37,14.13,13.88,14.37,14.86,15.35,15.84,16.33,16.8,17.27,17.74,18.21,18.68,19.07,19.46,19.86,20.25,20.64,21.37,22.1,22.82,23.55,24.28,24.68,25.07,25.47,25.86,26.26,25.66,25.07,24.47,23.88,23.28,23.21,23.14,23.08,23.01,22.94,22.78,22.62,22.46,22.3,22.14,21.89,21.65,21.4,21.16,20.91,20.61,20.32,20.02,19.73,19.43,19.09,18.75,18.42,18.08,17.74,17.39,17.04,16.7,16.35,16,15.68,15.37,15.05,14.74,14.42,14.05,13.68,13.3,12.93,12.56,12.23,11.91,11.58,11.26,10.93,10.65,10.37,10.08,9.802,9.52,9.252,8.984,8.716,8.448,8.18,7.946,7.712,7.478,7.244,7.01,6.808,6.606,6.404,6.202,6,5.822,5.644,5.466,5.288,5.11,4.96,4.81,4.66,4.51,4.36,4.226,4.092,3.958,3.824,3.69,3.578,3.466,3.354,3.242,3.13,3.032,2.934,2.836,2.738,2.64,2.56,2.48,2.4,2.32,2.24,2.174,2.108,2.042,1.976,1.91,1.868,1.826,1.784,1.742,1.7,1.638,1.576,1.514,1.452,1.39,1.348,1.306,1.264,1.222,1.18,1.15,1.12,1.09,1.06,1.03,1,0.97,0.94,0.91,0.88,0.852,0.824,0.796,0.768,0.74,0.72,0.7,0.68,0.66,0.64,0.62,0.6,0.58,0.56,0.54,0.53,0.52,0.51,0.5,0.49,0.484,0.478,0.472,0.466,0.46,0.452,0.444,0.436,0.428,0.42,0.41,0.4,0.39,0.38,0.37,0.37,0.37,0.37,0.37,0.37,0.362,0.354,0.346,0.338,0.33,0.334,0.338,0.342,0.346,0.35,0.352,0.354,0.356,0.358,0.36,0.35,0.34,0.33,0.32,0.31,0.3,0.29,0.28,0.27,0.26,0.246,0.232,0.218,0.204,0.19]])
C = np.array([[360,361,362,363,364,365,366,367,368,369,370,371,372,373,374,375,376,377,378,379,380,381,382,383,384,385,386,387,388,389,390,391,392,393,394,395,396,397,398,399,400,401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416,417,418,419,420,421,422,423,424,425,426,427,428,429,430,431,432,433,434,435,436,437,438,439,440,441,442,443,444,445,446,447,448,449,450,451,452,453,454,455,456,457,458,459,460,461,462,463,464,465,466,467,468,469,470,471,472,473,474,475,476,477,478,479,480,481,482,483,484,485,486,487,488,489,490,491,492,493,494,495,496,497,498,499,500,501,502,503,504,505,506,507,508,509,510,511,512,513,514,515,516,517,518,519,520,521,522,523,524,525,526,527,528,529,530,531,532,533,534,535,536,537,538,539,540,541,542,543,544,545,546,547,548,549,550,551,552,553,554,555,556,557,558,559,560,561,562,563,564,565,566,567,568,569,570,571,572,573,574,575,576,577,578,579,580,581,582,583,584,585,586,587,588,589,590,591,592,593,594,595,596,597,598,599,600,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633,634,635,636,637,638,639,640,641,642,643,644,645,646,647,648,649,650,651,652,653,654,655,656,657,658,659,660,661,662,663,664,665,666,667,668,669,670,671,672,673,674,675,676,677,678,679,680,681,682,683,684,685,686,687,688,689,690,691,692,693,694,695,696,697,698,699,700,701,702,703,704,705,706,707,708,709,710,711,712,713,714,715,716,717,718,719,720,721,722,723,724,725,726,727,728,729,730,731,732,733,734,735,736,737,738,739,740,741,742,743,744,745,746,747,748,749,750,751,752,753,754,755,756,757,758,759,760,761,762,763,764,765,766,767,768,769,770,771,772,773,774,775,776,777,778,779,780,781,782,783,784,785,786,787,788,789,790,791,792,793,794,795,796,797,798,799,800,801,802,803,804,805,806,807,808,809,810,811,812,813,814,815,816,817,818,819,820,821,822,823,824,825,826,827,828,829,830],
               [0.00045381,0.00045381,0.00045381,0.00045381,0.00045381,0.00045381,0.00045381,0.00045381,0.00045381,0.00045381,0.00045381,0.00045381,0.00045381,0.00045381,0.00045381,0.00045381,0.00045381,0.00045381,0.00045381,0.00045381,0.00045381,0.00047198,0.00049063,0.0005097,0.00052916,0.00054897,0.00056908,0.00058947,0.00061008,0.00063088,0.00065183,0.0006729,0.0006941,0.00071545,0.00073697,0.00075868,0.0007806,0.00080274,0.0008251,0.00084768,0.00087048,0.0008935,0.00091673,0.00094016,0.00096375,0.00098751,0.0010114,0.0010354,0.0010596,0.0010839,0.0011084,0.001133,0.0011576,0.0011822,0.0012068,0.0012312,0.0012554,0.0012794,0.001303,0.0013262,0.001349,0.0013713,0.0013931,0.0014143,0.0014349,0.0014549,0.0014743,0.0014931,0.0015113,0.0015288,0.0015457,0.0015619,0.0015774,0.0015922,0.0016061,0.0016193,0.0016315,0.0016428,0.0016532,0.0016625,0.0016708,0.0016781,0.0016843,0.0016896,0.001694,0.0016976,0.0017005,0.0017027,0.0017042,0.001705,0.0017052,0.0017049,0.001704,0.0017028,0.0017014,0.0016997,0.001698,0.0016963,0.0016948,0.0016936,0.0016928,0.0016926,0.0016928,0.0016935,0.0016944,0.0016956,0.0016969,0.0016983,0.0016997,0.0017011,0.0017025,0.0017036,0.0017046,0.0017055,0.0017061,0.0017064,0.0017066,0.0017064,0.0017059,0.0017051,0.0017038,0.0017022,0.0017001,0.0016974,0.0016942,0.0016904,0.0016859,0.0016806,0.0016746,0.0016677,0.0016598,0.001651,0.0016413,0.0016307,0.0016195,0.0016076,0.0015952,0.0015823,0.001569,0.0015554,0.0015416,0.0015275,0.0015134,0.0014992,0.0014851,0.0014712,0.0014574,0.0014441,0.0014311,0.0014186,0.0014068,0.0013957,0.0013853,0.0013756,0.0013668,0.0013588,0.0013517,0.0013454,0.0013401,0.0013358,0.0013325,0.0013303,0.0013291,0.0013289,0.0013295,0.0013309,0.0013331,0.0013359,0.0013393,0.0013433,0.0013477,0.0013524,0.0013575,0.0013629,0.0013685,0.0013743,0.0013803,0.0013863,0.0013923,0.0013982,0.001404,0.0014096,0.001415,0.0014201,0.001425,0.0014295,0.0014337,0.0014375,0.001441,0.001444,0.0014467,0.0014489,0.0014506,0.0014519,0.0014528,0.0014531,0.0014531,0.0014525,0.0014515,0.00145,0.0014481,0.0014456,0.0014428,0.0014395,0.0014358,0.0014317,0.0014273,0.0014225,0.0014175,0.0014123,0.0014068,0.0014012,0.0013954,0.0013895,0.0013834,0.0013772,0.0013709,0.0013645,0.001358,0.0013515,0.0013449,0.0013383,0.0013318,0.0013252,0.0013187,0.0013123,0.001306,0.0012997,0.0012936,0.0012876,0.0012817,0.0012759,0.0012702,0.0012648,0.0012595,0.0012544,0.0012496,0.0012451,0.0012409,0.001237,0.0012335,0.0012304,0.0012277,0.0012254,0.0012233,0.0012216,0.00122,0.0012187,0.0012175,0.0012165,0.0012156,0.0012149,0.0012142,0.0012137,0.0012132,0.0012128,0.0012124,0.0012121,0.0012119,0.0012117,0.0012115,0.0012114,0.0012113,0.0012112,0.0012111,0.001211,0.0012109,0.0012108,0.0012106,0.0012104,0.0012101,0.0012098,0.0012094,0.001209,0.0012086,0.0012082,0.0012079,0.0012076,0.0012074,0.0012073,0.0012074,0.0012077,0.0012081,0.0012087,0.0012093,0.00121,0.0012107,0.0012114,0.001212,0.0012125,0.0012129,0.0012132,0.0012133,0.0012133,0.0012132,0.0012129,0.0012125,0.0012118,0.001211,0.00121,0.0012088,0.0012073,0.0012056,0.0012037,0.0012017,0.0011994,0.0011971,0.0011946,0.001192,0.0011894,0.0011868,0.0011841,0.0011815,0.0011788,0.001176,0.001173,0.0011699,0.0011666,0.0011631,0.0011593,0.0011551,0.0011507,0.001146,0.001141,0.0011359,0.0011305,0.0011251,0.0011196,0.001114,0.0011084,0.0011029,0.0010974,0.001092,0.0010866,0.0010813,0.0010759,0.0010706,0.0010653,0.0010599,0.0010546,0.0010493,0.0010439,0.0010386,0.0010333,0.0010279,0.0010226,0.0010172,0.0010118,0.0010064,0.001001,0.00099562,0.00099021,0.00098478,0.0009793,0.00097375,0.00096812,0.00096239,0.00095659,0.00095077,0.00094497,0.00093924,0.0009336,0.00092805,0.00092257,0.00091714,0.00091174,0.00090635,0.00090101,0.00089575,0.0008906,0.00088561,0.0008808,0.00087618,0.00087178,0.00086758,0.00086361,0.00085985,0.00085625,0.00085275,0.00084926,0.00084573,0.0008421,0.00083843,0.00083478,0.00083123,0.00082785,0.0008247,0.00082176,0.00081903,0.00081648,0.0008141,0.00081186,0.00080978,0.00080784,0.00080608,0.00080447,0.00080304,0.00080178,0.00080069,0.00079975,0.00079897,0.00079835,0.00079788,0.0007976,0.0007975,0.0007976,0.0007979,0.00079837,0.00079897,0.00079964,0.00080035,0.00080105,0.00080179,0.00080258,0.00080346,0.00080447,0.00080565,0.00080703,0.00080865,0.00081053,0.00081272,0.00081272,0.00081272,0.00081272,0.00081272,0.00081272,0.00081272,0.00081272,0.00081272,0.00081272,0.00081272,0.00081272,0.00081272,0.00081272,0.00081272,0.00081272,0.00081272,0.00081272,0.00081272,0.00081272,0.00081272,0.00081272,0.00081272,0.00081272,0.00081272,0.00081272,0.00081272,0.00081272,0.00081272,0.00081272,0.00081272,0.00081272,0.00081272,0.00081272,0.00081272,0.00081272,0.00081272,0.00081272,0.00081272,0.00081272,0.00081272,0.00081272,0.00081272,0.00081272,0.00081272,0.00081272,0.00081272,0.00081272,0.00081272,0.00081272,0.00081272]])

F1,F2,F3,F4_,F5,F6,F7,F8,F9,F10,F11,F12 = [np.vstack((_iestm30['S']['data'][0],_iestm30['S']['data'][i+1])) for i in range(12)]
_cie_illuminants={'types':['E','D65','A','C','F1','F2','F3','F4','F5','F6','F7','F8','F9','F10','F11','F12'],
                  'E':E,'D65':D65,'A':A ,'C':C,
                  'F1':F1,'F2':F2,'F3':F3,'F4':F4,'F5':F5,'F6':F6,'F7':F7,'F8':F8,'F9':F9,'F10':F10,'F11':F11,'F12':F12}
del E, D65, A, C, F1, F2, F3, F4, F5, F6, F7, F8, F9, F10, F11, F12


###############################################################################
# spectral reflectance functions:

#------------------------------------------------------------------------------
# CIE 13.3-1995 color rendering index:
_cie133_1995 = {'14': getdata(_R_dir + 'CIE_13_3_1995_R14.dat',kind='np').T}
_cie133_1995['8'] = _cie133_1995['14'][0:9].copy()
   
 
#------------------------------------------------------------------------------  
# IES TM30-15 color fidelity and color galut indices:
_iestm30['R'] = {'4880' : {'5nm': getdata(_R_dir + 'IESTM30_R4880.dat',kind='np').T}}
_iestm30['R']['99'] = {'5nm' : getdata(_R_dir + 'IESTM30_R99.dat',kind='np').T}
temp = getdata(_R_dir + 'IESTM30_R99info.dat',kind='df').values[0]
ies99categories = ['nature','skin','textiles','paints','plastic','printed','color system']
_iestm30['R']['99']['info'] = [ies99categories[int(i-1)] for i in temp]


#------------------------------------------------------------------------------
# cie 224:2017 (color fidelity index based on IES TM-30-15):
_cie224_2017 = {'99': {'1nm' : getdata(_R_dir + 'CIE224_2017_R99_1nm.dat',kind='np').T}}
_cie224_2017['99']['5nm'] = getdata(_R_dir + 'CIE224_2017_R99_5nm.dat',kind='np').T
_cie224_2017['99']['info'] = _iestm30['R']['99']['info']

#------------------------------------------------------------------------------
# CRI2012 spectrally uniform mathematical sampleset:
_cri2012 = {'HL17' : getdata(_R_dir + 'CRI2012_HL17.dat',kind='np').T}
_cri2012['HL1000'] = getdata(_R_dir +'CRI2012_Hybrid14_1000.dat',kind='np').T
_cri2012['Real210'] = getdata(_R_dir +'CRI2012_R210.dat',kind='np').T

#------------------------------------------------------------------------------
# MCRI (memory color rendition index, Rm) sampleset:
_mcri = {'R' : getdata(_R_dir + 'MCRI_R10.dat',kind='np').T}
_mcri['info'] = ['apple','banana','orange','lavender','smurf','strawberry yoghurt','sliced cucumber', 'cauliflower','caucasian skin','N4'] # familiar objects, N4: neutral (approx. N4) gray sphere 


#------------------------------------------------------------------------------
# CQS versions 7.5 and 9.0:
_cqs = {'v7.5': getdata(_R_dir + 'CQSv7dot5.dat',kind='np').T}
_cqs['v9.0'] =  getdata(_R_dir + 'CQSv9dot0.dat',kind='np').T

#------------------------------------------------------------------------------
# collect in one dict:
_cri_rfl = {'cie-13.3-1995': _cie133_1995}
_cri_rfl['cie-224-2017'] = _cie224_2017
_cri_rfl['cri2012'] = _cri2012
_cri_rfl['ies-tm30-15'] = _iestm30['R']
_cri_rfl['mcri'] = _mcri['R']
_cri_rfl['cqs'] = _cqs

#------------------------------------------------------------------------------
# 1269 Munsell spectral reflectance functions:
_munsell = {'cieobs':'1931_2', 'Lw' : 400.0, 'Yb':0.2}
_munsell['R'] = getdata(_R_dir + 'Munsell1269.dat',kind='np').T
temp = getdata(_R_dir + 'Munsell_VabCh.dat',kind='np')
_munsell['V'] = temp[:,0,None]
_munsell['ab'] = temp[:,1:2]
_munsell['C'] = temp[:,3,None]
_munsell['h'] = temp[:,4,None]

del temp, ies99categories
