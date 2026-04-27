Working on 2ent_2rel
device: cuda
dataset path: ..\data_exploration\synthetic_data\2ent_2rel.json
num timesteps: 300
x_global shape: (400, 64)
num relations: 2
relations: {0: 'contact', 1: 'negotiate'}
example edge_index shape: (2, 817)
example edge_type shape: (817,)
example edge_relative_time shape: (817,)
train timesteps: 0 to 289
validation timesteps: 290 to 299
epoch 001 | time 91.71s | train del 0.6349 | train add 0.5027 | train add prop 0.0002 | val del 0.5895 | val add 0.6152 | val add prop 0.0002 | del F1 0.5042 | add F1 0.9654
epoch 002 | time 146.16s | train del 0.6044 | train add 0.2376 | train add prop 0.0002 | val del 0.6061 | val add 0.1068 | val add prop 0.0001 | del F1 0.5069 | add F1 0.9790
epoch 003 | time 123.64s | train del 0.5310 | train add 0.1295 | train add prop 0.0002 | val del 0.4823 | val add 0.1478 | val add prop 0.0004 | del F1 0.6240 | add F1 0.9856
epoch 004 | time 154.49s | train del 0.3582 | train add 0.1067 | train add prop 0.0002 | val del 0.3155 | val add 0.2055 | val add prop 0.0003 | del F1 0.9983 | add F1 0.9896
epoch 005 | time 104.01s | train del 0.2396 | train add 0.1068 | train add prop 0.0002 | val del 0.1770 | val add 0.0680 | val add prop 0.0003 | del F1 1.0000 | add F1 0.9893
epoch 006 | time 110.19s | train del 0.1613 | train add 0.0957 | train add prop 0.0003 | val del 0.1262 | val add 0.0916 | val add prop 0.0005 | del F1 1.0000 | add F1 0.9899
epoch 007 | time 114.64s | train del 0.1090 | train add 0.0971 | train add prop 0.0003 | val del 0.1057 | val add 0.0675 | val add prop 0.0004 | del F1 1.0000 | add F1 0.9893
epoch 008 | time 114.66s | train del 0.0738 | train add 0.0904 | train add prop 0.0002 | val del 0.0972 | val add 0.0760 | val add prop 0.0003 | del F1 1.0000 | add F1 0.9907
epoch 009 | time 155.73s | train del 0.0841 | train add 0.0897 | train add prop 0.0002 | val del 0.0711 | val add 0.1218 | val add prop 0.0007 | del F1 1.0000 | add F1 0.9906
epoch 010 | time 128.82s | train del 0.0474 | train add 0.0870 | train add prop 0.0003 | val del 0.0521 | val add 0.0627 | val add prop 0.0002 | del F1 1.0000 | add F1 0.9917
epoch 011 | time 119.51s | train del 0.0366 | train add 0.0851 | train add prop 0.0002 | val del 0.0290 | val add 0.0993 | val add prop 0.0000 | del F1 1.0000 | add F1 0.9922
epoch 012 | time 149.49s | train del 0.0421 | train add 0.0809 | train add prop 0.0003 | val del 0.0293 | val add 0.0668 | val add prop 0.0001 | del F1 1.0000 | add F1 0.9913
epoch 013 | time 151.25s | train del 0.0232 | train add 0.0822 | train add prop 0.0003 | val del 0.0159 | val add 0.1215 | val add prop 0.0004 | del F1 1.0000 | add F1 0.9931
epoch 014 | time 143.38s | train del 0.0233 | train add 0.0804 | train add prop 0.0003 | val del 0.0331 | val add 0.0636 | val add prop 0.0002 | del F1 1.0000 | add F1 0.9920
epoch 015 | time 110.67s | train del 0.0230 | train add 0.0774 | train add prop 0.0002 | val del 0.0265 | val add 0.0546 | val add prop 0.0002 | del F1 1.0000 | add F1 0.9911
epoch 016 | time 127.59s | train del 0.0185 | train add 0.0788 | train add prop 0.0002 | val del 0.0106 | val add 0.0904 | val add prop 0.0004 | del F1 1.0000 | add F1 0.9924
epoch 017 | time 145.17s | train del 0.0164 | train add 0.0736 | train add prop 0.0003 | val del 0.0078 | val add 0.0601 | val add prop 0.0004 | del F1 1.0000 | add F1 0.9915
epoch 018 | time 119.94s | train del 0.0119 | train add 0.0749 | train add prop 0.0003 | val del 0.0107 | val add 0.0744 | val add prop 0.0002 | del F1 1.0000 | add F1 0.9920
epoch 019 | time 132.23s | train del 0.0108 | train add 0.0760 | train add prop 0.0002 | val del 0.0223 | val add 0.0567 | val add prop 0.0003 | del F1 1.0000 | add F1 0.9917
epoch 020 | time 121.71s | train del 0.0228 | train add 0.0757 | train add prop 0.0003 | val del 0.0063 | val add 0.0474 | val add prop 0.0005 | del F1 1.0000 | add F1 0.9930
epoch 021 | time 155.51s | train del 0.0044 | train add 0.0747 | train add prop 0.0003 | val del 0.0042 | val add 0.0611 | val add prop 0.0002 | del F1 1.0000 | add F1 0.9927
epoch 022 | time 131.62s | train del 0.0036 | train add 0.0745 | train add prop 0.0003 | val del 0.0031 | val add 0.0676 | val add prop 0.0005 | del F1 1.0000 | add F1 0.9926
epoch 023 | time 159.44s | train del 0.0028 | train add 0.0735 | train add prop 0.0003 | val del 0.0020 | val add 0.0567 | val add prop 0.0002 | del F1 1.0000 | add F1 0.9901
epoch 024 | time 123.18s | train del 0.0019 | train add 0.0728 | train add prop 0.0003 | val del 0.0013 | val add 0.0880 | val add prop 0.0002 | del F1 1.0000 | add F1 0.9919
epoch 025 | time 145.56s | train del 0.0015 | train add 0.0757 | train add prop 0.0002 | val del 0.0021 | val add 0.0528 | val add prop 0.0002 | del F1 1.0000 | add F1 0.9932
epoch 026 | time 134.89s | train del 0.0010 | train add 0.0744 | train add prop 0.0002 | val del 0.0008 | val add 0.0897 | val add prop 0.0001 | del F1 1.0000 | add F1 0.9901
epoch 027 | time 127.15s | train del 0.0009 | train add 0.0749 | train add prop 0.0002 | val del 0.0009 | val add 0.0482 | val add prop 0.0001 | del F1 1.0000 | add F1 0.9926
epoch 028 | time 125.41s | train del 0.0006 | train add 0.0730 | train add prop 0.0003 | val del 0.0008 | val add 0.0504 | val add prop 0.0002 | del F1 1.0000 | add F1 0.9926
epoch 029 | time 121.13s | train del 0.0005 | train add 0.0728 | train add prop 0.0003 | val del 0.0004 | val add 0.0534 | val add prop 0.0002 | del F1 1.0000 | add F1 0.9933
epoch 030 | time 169.55s | train del 0.0004 | train add 0.0723 | train add prop 0.0003 | val del 0.0003 | val add 0.0948 | val add prop 0.0002 | del F1 1.0000 | add F1 0.9917
epoch 031 | time 146.35s | train del 0.0004 | train add 0.0713 | train add prop 0.0003 | val del 0.0004 | val add 0.0595 | val add prop 0.0004 | del F1 1.0000 | add F1 0.9921
epoch 032 | time 161.31s | train del 0.0003 | train add 0.0696 | train add prop 0.0003 | val del 0.0002 | val add 0.0564 | val add prop 0.0004 | del F1 1.0000 | add F1 0.9932
epoch 033 | time 151.49s | train del 0.0002 | train add 0.0697 | train add prop 0.0003 | val del 0.0002 | val add 0.0583 | val add prop 0.0001 | del F1 1.0000 | add F1 0.9931
epoch 034 | time 144.27s | train del 0.0002 | train add 0.0697 | train add prop 0.0002 | val del 0.0002 | val add 0.0729 | val add prop 0.0002 | del F1 1.0000 | add F1 0.9930
epoch 035 | time 164.44s | train del 0.0002 | train add 0.0680 | train add prop 0.0002 | val del 0.0002 | val add 0.0576 | val add prop 0.0002 | del F1 1.0000 | add F1 0.9938
epoch 036 | time 124.42s | train del 0.0001 | train add 0.0676 | train add prop 0.0002 | val del 0.0001 | val add 0.0643 | val add prop 0.0001 | del F1 1.0000 | add F1 0.9929
epoch 037 | time 126.97s | train del 0.0001 | train add 0.0655 | train add prop 0.0002 | val del 0.0001 | val add 0.0499 | val add prop 0.0003 | del F1 1.0000 | add F1 0.9928
epoch 038 | time 146.70s | train del 0.0001 | train add 0.0677 | train add prop 0.0002 | val del 0.0001 | val add 0.0560 | val add prop 0.0004 | del F1 1.0000 | add F1 0.9940
epoch 039 | time 146.70s | train del 0.0001 | train add 0.0664 | train add prop 0.0003 | val del 0.0001 | val add 0.0617 | val add prop 0.0004 | del F1 1.0000 | add F1 0.9939
epoch 040 | time 123.95s | train del 0.0001 | train add 0.0642 | train add prop 0.0003 | val del 0.0001 | val add 0.0624 | val add prop 0.0004 | del F1 1.0000 | add F1 0.9939
epoch 041 | time 132.11s | train del 0.0001 | train add 0.0652 | train add prop 0.0003 | val del 0.0001 | val add 0.0441 | val add prop 0.0002 | del F1 1.0000 | add F1 0.9949
epoch 042 | time 141.42s | train del 0.0001 | train add 0.0659 | train add prop 0.0002 | val del 0.0001 | val add 0.0560 | val add prop 0.0001 | del F1 1.0000 | add F1 0.9935
epoch 043 | time 165.94s | train del 0.0001 | train add 0.0640 | train add prop 0.0002 | val del 0.0001 | val add 0.0554 | val add prop 0.0001 | del F1 1.0000 | add F1 0.9943
epoch 044 | time 117.81s | train del 0.0001 | train add 0.0622 | train add prop 0.0002 | val del 0.0001 | val add 0.0617 | val add prop 0.0001 | del F1 1.0000 | add F1 0.9943
epoch 045 | time 131.15s | train del 0.0001 | train add 0.0638 | train add prop 0.0002 | val del 0.0000 | val add 0.0493 | val add prop 0.0001 | del F1 1.0000 | add F1 0.9936
epoch 046 | time 123.33s | train del 0.0000 | train add 0.0634 | train add prop 0.0002 | val del 0.0000 | val add 0.0419 | val add prop 0.0001 | del F1 1.0000 | add F1 0.9948
epoch 047 | time 147.19s | train del 0.0000 | train add 0.0635 | train add prop 0.0003 | val del 0.0000 | val add 0.0446 | val add prop 0.0001 | del F1 1.0000 | add F1 0.9949
epoch 048 | time 124.05s | train del 0.0000 | train add 0.0614 | train add prop 0.0002 | val del 0.0000 | val add 0.0458 | val add prop 0.0001 | del F1 1.0000 | add F1 0.9945
epoch 049 | time 162.12s | train del 0.0000 | train add 0.0615 | train add prop 0.0002 | val del 0.0000 | val add 0.0514 | val add prop 0.0002 | del F1 1.0000 | add F1 0.9949
epoch 050 | time 149.63s | train del 0.0000 | train add 0.0632 | train add prop 0.0003 | val del 0.0000 | val add 0.0458 | val add prop 0.0001 | del F1 1.0000 | add F1 0.9944
saved plots/2ent_2rel.png

Working on 2ent_9rel
device: cuda
dataset path: ..\data_exploration\synthetic_data\2ent_9rel.json
num timesteps: 300
x_global shape: (400, 64)
num relations: 9
relations: {0: 'contact', 1: 'negotiate', 2: 'bonded', 3: 'strained', 4: 'recovery', 5: 'conflict', 6: 'repair', 7: 'maintain', 8: 'decay'}
example edge_index shape: (2, 809)
example edge_type shape: (809,)
example edge_relative_time shape: (809,)
train timesteps: 0 to 289
validation timesteps: 290 to 299
epoch 001 | time 153.72s | train del 0.6441 | train add 0.4267 | train add prop 0.0000 | val del 0.6285 | val add 0.0874 | val add prop 0.0001 | del F1 0.5832 | add F1 0.9873
epoch 002 | time 154.69s | train del 0.5992 | train add 0.1568 | train add prop 0.0000 | val del 0.5762 | val add 0.0261 | val add prop 0.0000 | del F1 0.6482 | add F1 0.9990
epoch 003 | time 191.26s | train del 0.5220 | train add 0.0580 | train add prop 0.0000 | val del 0.4658 | val add 0.0184 | val add prop 0.0000 | del F1 0.7196 | add F1 0.9984
epoch 004 | time 195.59s | train del 0.4250 | train add 0.0364 | train add prop 0.0000 | val del 0.3470 | val add 0.0548 | val add prop 0.0000 | del F1 0.7891 | add F1 0.9987
epoch 005 | time 195.50s | train del 0.3547 | train add 0.0344 | train add prop 0.0000 | val del 0.3182 | val add 0.0103 | val add prop 0.0000 | del F1 0.7921 | add F1 0.9993
epoch 006 | time 182.99s | train del 0.2915 | train add 0.0337 | train add prop 0.0000 | val del 0.2621 | val add 0.0331 | val add prop 0.0001 | del F1 0.8055 | add F1 0.9988
epoch 007 | time 197.35s | train del 0.2674 | train add 0.0283 | train add prop 0.0000 | val del 0.2440 | val add 0.0826 | val add prop 0.0000 | del F1 0.8050 | add F1 0.9991
epoch 008 | time 195.77s | train del 0.2671 | train add 0.0280 | train add prop 0.0000 | val del 0.2425 | val add 0.0236 | val add prop 0.0000 | del F1 0.8018 | add F1 0.9994
epoch 009 | time 195.08s | train del 0.2683 | train add 0.0263 | train add prop 0.0000 | val del 0.2399 | val add 0.0179 | val add prop 0.0000 | del F1 0.8054 | add F1 0.9990
epoch 010 | time 192.97s | train del 0.2491 | train add 0.0234 | train add prop 0.0000 | val del 0.2434 | val add 0.0165 | val add prop 0.0001 | del F1 0.8043 | add F1 0.9989
epoch 011 | time 189.00s | train del 0.2512 | train add 0.0249 | train add prop 0.0000 | val del 0.2521 | val add 0.1674 | val add prop 0.0000 | del F1 0.8066 | add F1 0.9992
epoch 012 | time 195.99s | train del 0.2593 | train add 0.0270 | train add prop 0.0000 | val del 0.2718 | val add 0.0127 | val add prop 0.0000 | del F1 0.8273 | add F1 0.9989
epoch 013 | time 192.19s | train del 0.2497 | train add 0.0243 | train add prop 0.0000 | val del 0.2709 | val add 0.0304 | val add prop 0.0000 | del F1 0.8010 | add F1 0.9995
epoch 014 | time 197.31s | train del 0.2499 | train add 0.0209 | train add prop 0.0000 | val del 0.2808 | val add 0.0216 | val add prop 0.0000 | del F1 0.8061 | add F1 0.9992
epoch 015 | time 194.68s | train del 0.2467 | train add 0.0209 | train add prop 0.0000 | val del 0.2772 | val add 0.0276 | val add prop 0.0001 | del F1 0.7903 | add F1 0.9993
epoch 016 | time 192.78s | train del 0.2498 | train add 0.0224 | train add prop 0.0000 | val del 0.2344 | val add 0.0206 | val add prop 0.0000 | del F1 0.8058 | add F1 0.9992
epoch 017 | time 192.62s | train del 0.2448 | train add 0.0192 | train add prop 0.0000 | val del 0.2608 | val add 0.0331 | val add prop 0.0001 | del F1 0.8238 | add F1 0.9991
epoch 018 | time 197.71s | train del 0.2396 | train add 0.0223 | train add prop 0.0000 | val del 0.2277 | val add 0.0404 | val add prop 0.0000 | del F1 0.8043 | add F1 0.9991
epoch 019 | time 198.72s | train del 0.2453 | train add 0.0208 | train add prop 0.0000 | val del 0.2464 | val add 0.0282 | val add prop 0.0000 | del F1 0.8078 | add F1 0.9991
epoch 020 | time 187.29s | train del 0.2428 | train add 0.0202 | train add prop 0.0000 | val del 0.2654 | val add 0.0140 | val add prop 0.0000 | del F1 0.8049 | add F1 0.9990
epoch 021 | time 144.93s | train del 0.2362 | train add 0.0213 | train add prop 0.0000 | val del 0.2418 | val add 0.0282 | val add prop 0.0000 | del F1 0.8047 | add F1 0.9996
epoch 022 | time 194.05s | train del 0.2525 | train add 0.0211 | train add prop 0.0000 | val del 0.2225 | val add 0.0228 | val add prop 0.0000 | del F1 0.8063 | add F1 0.9993
epoch 023 | time 198.35s | train del 0.2366 | train add 0.0631 | train add prop 0.0000 | val del 0.2568 | val add 0.0191 | val add prop 0.0000 | del F1 0.7855 | add F1 0.9991
epoch 024 | time 197.88s | train del 0.2328 | train add 0.0279 | train add prop 0.0000 | val del 0.2377 | val add 0.0127 | val add prop 0.0000 | del F1 0.8362 | add F1 0.9992
epoch 025 | time 198.89s | train del 0.2173 | train add 0.0276 | train add prop 0.0000 | val del 0.3483 | val add 0.0464 | val add prop 0.0000 | del F1 0.7963 | add F1 0.9993
epoch 026 | time 195.03s | train del 0.2216 | train add 0.0257 | train add prop 0.0000 | val del 0.1996 | val add 0.0148 | val add prop 0.0000 | del F1 0.8487 | add F1 0.9994
epoch 027 | time 203.08s | train del 0.1942 | train add 0.0250 | train add prop 0.0000 | val del 0.3091 | val add 0.0161 | val add prop 0.0000 | del F1 0.8306 | add F1 0.9993
epoch 028 | time 195.89s | train del 0.1901 | train add 0.0242 | train add prop 0.0000 | val del 0.2673 | val add 0.0219 | val add prop 0.0001 | del F1 0.8425 | add F1 0.9991
epoch 029 | time 190.08s | train del 0.1871 | train add 0.0251 | train add prop 0.0000 | val del 0.2038 | val add 0.0316 | val add prop 0.0000 | del F1 0.8710 | add F1 0.9990
epoch 030 | time 181.98s | train del 0.1411 | train add 0.0241 | train add prop 0.0000 | val del 0.4516 | val add 0.0396 | val add prop 0.0000 | del F1 0.8132 | add F1 0.9992
epoch 031 | time 151.15s | train del 0.2187 | train add 0.0240 | train add prop 0.0000 | val del 0.2095 | val add 0.0182 | val add prop 0.0000 | del F1 0.8448 | add F1 0.9995
epoch 032 | time 173.56s | train del 0.0922 | train add 0.0239 | train add prop 0.0000 | val del 0.3301 | val add 0.0378 | val add prop 0.0000 | del F1 0.8295 | add F1 0.9993
epoch 033 | time 119.08s | train del 0.0919 | train add 0.0261 | train add prop 0.0000 | val del 0.3504 | val add 0.0157 | val add prop 0.0000 | del F1 0.8348 | add F1 0.9992
epoch 034 | time 134.52s | train del 0.1307 | train add 0.0238 | train add prop 0.0000 | val del 0.4772 | val add 0.0105 | val add prop 0.0001 | del F1 0.7972 | add F1 0.9994
epoch 035 | time 157.87s | train del 0.1102 | train add 0.0275 | train add prop 0.0000 | val del 0.5684 | val add 0.0196 | val add prop 0.0000 | del F1 0.7913 | add F1 0.9991
epoch 036 | time 219.35s | train del 0.1643 | train add 0.0255 | train add prop 0.0000 | val del 0.2946 | val add 0.0941 | val add prop 0.0000 | del F1 0.8475 | add F1 0.9989
epoch 037 | time 311.24s | train del 0.0923 | train add 0.0272 | train add prop 0.0000 | val del 0.3139 | val add 0.0122 | val add prop 0.0000 | del F1 0.8323 | add F1 0.9990
epoch 038 | time 360.56s | train del 0.1201 | train add 0.0287 | train add prop 0.0000 | val del 0.4828 | val add 0.0181 | val add prop 0.0000 | del F1 0.8210 | add F1 0.9987
epoch 039 | time 173.33s | train del 0.0895 | train add 0.0259 | train add prop 0.0000 | val del 0.3451 | val add 0.0122 | val add prop 0.0001 | del F1 0.8179 | add F1 0.9989
epoch 040 | time 145.78s | train del 0.0623 | train add 0.0284 | train add prop 0.0000 | val del 0.4969 | val add 0.0154 | val add prop 0.0000 | del F1 0.8289 | add F1 0.9990
epoch 041 | time 367.16s | train del 0.0790 | train add 0.0278 | train add prop 0.0000 | val del 0.3067 | val add 0.0158 | val add prop 0.0000 | del F1 0.8394 | add F1 0.9988
epoch 042 | time 376.56s | train del 0.0508 | train add 0.0269 | train add prop 0.0000 | val del 0.4818 | val add 0.0346 | val add prop 0.0000 | del F1 0.8327 | add F1 0.9991
epoch 043 | time 189.55s | train del 0.0607 | train add 0.0263 | train add prop 0.0000 | val del 0.3452 | val add 0.0152 | val add prop 0.0000 | del F1 0.8515 | add F1 0.9990
epoch 044 | time 167.42s | train del 0.0430 | train add 0.0274 | train add prop 0.0000 | val del 0.2468 | val add 0.0749 | val add prop 0.0000 | del F1 0.8803 | add F1 0.9987
epoch 045 | time 114.99s | train del 0.0383 | train add 0.0266 | train add prop 0.0000 | val del 0.4001 | val add 0.0201 | val add prop 0.0001 | del F1 0.7945 | add F1 0.9986
epoch 046 | time 195.43s | train del 0.0517 | train add 0.0291 | train add prop 0.0000 | val del 0.3561 | val add 0.0605 | val add prop 0.0001 | del F1 0.8316 | add F1 0.9986
epoch 047 | time 160.98s | train del 0.0611 | train add 0.0278 | train add prop 0.0000 | val del 0.5695 | val add 0.0419 | val add prop 0.0000 | del F1 0.8057 | add F1 0.9986
epoch 048 | time 174.96s | train del 0.0967 | train add 0.0267 | train add prop 0.0000 | val del 0.3811 | val add 0.0399 | val add prop 0.0000 | del F1 0.8191 | add F1 0.9989
epoch 049 | time 206.21s | train del 0.0623 | train add 0.0254 | train add prop 0.0000 | val del 0.4486 | val add 0.0471 | val add prop 0.0000 | del F1 0.8159 | add F1 0.9989
epoch 050 | time 185.79s | train del 0.0498 | train add 0.0259 | train add prop 0.0000 | val del 0.4222 | val add 0.0168 | val add prop 0.0000 | del F1 0.8321 | add F1 0.9988
saved plots/2ent_9rel.png
Working on 5ent_5rel
device: cuda
dataset path: ..\data_exploration\synthetic_data\5ent_5rel.json
num timesteps: 300
x_global shape: (400, 64)
num relations: 5
relations: {0: 'contact', 1: 'negotiate', 2: 'bonded', 3: 'strained', 4: 'recovery'}
example edge_index shape: (2, 116)
example edge_type shape: (116,)
example edge_relative_time shape: (116,)
train timesteps: 0 to 289
validation timesteps: 290 to 299
epoch 001 | time 109.33s | train del 0.6476 | train add 0.4514 | train add prop 0.0001 | val del 0.6427 | val add 0.2261 | val add prop 0.0000 | del F1 0.6084 | add F1 0.9198
epoch 002 | time 109.00s | train del 0.5925 | train add 0.1632 | train add prop 0.0000 | val del 0.5507 | val add 0.0975 | val add prop 0.0000 | del F1 0.6832 | add F1 0.9754
epoch 003 | time 108.10s | train del 0.4880 | train add 0.0808 | train add prop 0.0000 | val del 0.4071 | val add 0.0542 | val add prop 0.0000 | del F1 0.7515 | add F1 0.9876
epoch 004 | time 138.82s | train del 0.3641 | train add 0.0622 | train add prop 0.0001 | val del 0.3181 | val add 0.0489 | val add prop 0.0000 | del F1 0.7935 | add F1 0.9889
epoch 005 | time 134.08s | train del 0.3211 | train add 0.0540 | train add prop 0.0000 | val del 0.2892 | val add 0.0519 | val add prop 0.0000 | del F1 0.8141 | add F1 0.9901
epoch 006 | time 102.25s | train del 0.2885 | train add 0.0505 | train add prop 0.0001 | val del 0.2727 | val add 0.0578 | val add prop 0.0002 | del F1 0.8038 | add F1 0.9882
epoch 007 | time 156.51s | train del 0.2745 | train add 0.0495 | train add prop 0.0000 | val del 0.2917 | val add 0.0413 | val add prop 0.0000 | del F1 0.7943 | add F1 0.9903
epoch 008 | time 92.87s | train del 0.2620 | train add 0.0494 | train add prop 0.0000 | val del 0.2620 | val add 0.0754 | val add prop 0.0000 | del F1 0.7977 | add F1 0.9891
epoch 009 | time 108.44s | train del 0.2531 | train add 0.0483 | train add prop 0.0000 | val del 0.2442 | val add 0.0723 | val add prop 0.0000 | del F1 0.8185 | add F1 0.9878
epoch 010 | time 99.69s | train del 0.2495 | train add 0.0445 | train add prop 0.0001 | val del 0.2394 | val add 0.0524 | val add prop 0.0002 | del F1 0.8361 | add F1 0.9901
epoch 011 | time 103.57s | train del 0.2428 | train add 0.0453 | train add prop 0.0000 | val del 0.2679 | val add 0.0444 | val add prop 0.0004 | del F1 0.8391 | add F1 0.9889
epoch 012 | time 92.69s | train del 0.2328 | train add 0.0441 | train add prop 0.0000 | val del 0.2447 | val add 0.0356 | val add prop 0.0000 | del F1 0.8330 | add F1 0.9910
epoch 013 | time 145.98s | train del 0.2307 | train add 0.0435 | train add prop 0.0000 | val del 0.2385 | val add 0.0414 | val add prop 0.0000 | del F1 0.8393 | add F1 0.9897
epoch 014 | time 100.81s | train del 0.2236 | train add 0.0422 | train add prop 0.0001 | val del 0.2176 | val add 0.0436 | val add prop 0.0000 | del F1 0.8437 | add F1 0.9889
epoch 015 | time 113.37s | train del 0.2196 | train add 0.0465 | train add prop 0.0001 | val del 0.2433 | val add 0.0644 | val add prop 0.0000 | del F1 0.8475 | add F1 0.9901
epoch 016 | time 105.45s | train del 0.2155 | train add 0.0407 | train add prop 0.0001 | val del 0.2467 | val add 0.0431 | val add prop 0.0000 | del F1 0.8496 | add F1 0.9887
epoch 017 | time 100.37s | train del 0.2171 | train add 0.0402 | train add prop 0.0000 | val del 0.2537 | val add 0.0392 | val add prop 0.0000 | del F1 0.8485 | add F1 0.9899
epoch 018 | time 102.86s | train del 0.2089 | train add 0.0387 | train add prop 0.0000 | val del 0.2029 | val add 0.0414 | val add prop 0.0002 | del F1 0.8458 | add F1 0.9910
epoch 019 | time 118.90s | train del 0.2102 | train add 0.0379 | train add prop 0.0000 | val del 0.2235 | val add 0.0347 | val add prop 0.0000 | del F1 0.8580 | add F1 0.9918
epoch 020 | time 104.98s | train del 0.2001 | train add 0.0415 | train add prop 0.0001 | val del 0.2010 | val add 0.0373 | val add prop 0.0002 | del F1 0.8582 | add F1 0.9910
epoch 021 | time 95.89s | train del 0.1978 | train add 0.0388 | train add prop 0.0001 | val del 0.1969 | val add 0.0373 | val add prop 0.0002 | del F1 0.8506 | add F1 0.9901
epoch 022 | time 90.73s | train del 0.1965 | train add 0.0389 | train add prop 0.0000 | val del 0.1972 | val add 0.0380 | val add prop 0.0002 | del F1 0.8639 | add F1 0.9916
epoch 023 | time 54.81s | train del 0.2020 | train add 0.0402 | train add prop 0.0000 | val del 0.2246 | val add 0.0438 | val add prop 0.0000 | del F1 0.8464 | add F1 0.9878
epoch 024 | time 101.31s | train del 0.1942 | train add 0.0400 | train add prop 0.0000 | val del 0.1897 | val add 0.0448 | val add prop 0.0000 | del F1 0.8599 | add F1 0.9895
epoch 025 | time 148.55s | train del 0.1900 | train add 0.0381 | train add prop 0.0000 | val del 0.1852 | val add 0.0418 | val add prop 0.0000 | del F1 0.8679 | add F1 0.9908
epoch 026 | time 119.37s | train del 0.1868 | train add 0.0363 | train add prop 0.0000 | val del 0.1984 | val add 0.0383 | val add prop 0.0002 | del F1 0.8532 | add F1 0.9918
epoch 027 | time 107.42s | train del 0.1920 | train add 0.0375 | train add prop 0.0000 | val del 0.2268 | val add 0.0340 | val add prop 0.0000 | del F1 0.8706 | add F1 0.9926
epoch 028 | time 113.93s | train del 0.1854 | train add 0.0365 | train add prop 0.0000 | val del 0.1897 | val add 0.0447 | val add prop 0.0002 | del F1 0.8664 | add F1 0.9908
epoch 029 | time 105.72s | train del 0.1821 | train add 0.0347 | train add prop 0.0001 | val del 0.2297 | val add 0.0355 | val add prop 0.0002 | del F1 0.8731 | add F1 0.9916
epoch 030 | time 95.87s | train del 0.1777 | train add 0.0363 | train add prop 0.0001 | val del 0.1886 | val add 0.0371 | val add prop 0.0000 | del F1 0.8603 | add F1 0.9924
epoch 031 | time 108.86s | train del 0.1724 | train add 0.0357 | train add prop 0.0000 | val del 0.1706 | val add 0.0661 | val add prop 0.0000 | del F1 0.8809 | add F1 0.9912
epoch 032 | time 118.85s | train del 0.1588 | train add 0.0364 | train add prop 0.0001 | val del 0.2183 | val add 0.0372 | val add prop 0.0000 | del F1 0.8672 | add F1 0.9922
epoch 033 | time 146.76s | train del 0.1447 | train add 0.0336 | train add prop 0.0000 | val del 0.1886 | val add 0.0369 | val add prop 0.0000 | del F1 0.8994 | add F1 0.9926
epoch 034 | time 117.64s | train del 0.1330 | train add 0.0380 | train add prop 0.0000 | val del 0.1918 | val add 0.0302 | val add prop 0.0000 | del F1 0.8935 | add F1 0.9931
epoch 035 | time 157.15s | train del 0.1127 | train add 0.0376 | train add prop 0.0000 | val del 0.1577 | val add 0.0335 | val add prop 0.0000 | del F1 0.8971 | add F1 0.9916
epoch 036 | time 150.62s | train del 0.1122 | train add 0.0325 | train add prop 0.0000 | val del 0.1527 | val add 0.0334 | val add prop 0.0000 | del F1 0.9038 | add F1 0.9912
epoch 037 | time 159.10s | train del 0.0706 | train add 0.0329 | train add prop 0.0000 | val del 0.1328 | val add 0.0338 | val add prop 0.0000 | del F1 0.9311 | add F1 0.9912
epoch 038 | time 155.53s | train del 0.0461 | train add 0.0308 | train add prop 0.0000 | val del 0.1384 | val add 0.0369 | val add prop 0.0000 | del F1 0.9317 | add F1 0.9916
epoch 039 | time 98.08s | train del 0.0366 | train add 0.0320 | train add prop 0.0000 | val del 0.1585 | val add 0.0356 | val add prop 0.0002 | del F1 0.9139 | add F1 0.9912
epoch 040 | time 103.03s | train del 0.0403 | train add 0.0302 | train add prop 0.0000 | val del 0.1512 | val add 0.0345 | val add prop 0.0000 | del F1 0.9174 | add F1 0.9918
epoch 041 | time 158.83s | train del 0.0358 | train add 0.0306 | train add prop 0.0001 | val del 0.1657 | val add 0.0321 | val add prop 0.0000 | del F1 0.9109 | add F1 0.9926
epoch 042 | time 120.46s | train del 0.0295 | train add 0.0316 | train add prop 0.0000 | val del 0.1091 | val add 0.0401 | val add prop 0.0000 | del F1 0.9431 | add F1 0.9939
epoch 043 | time 103.56s | train del 0.0203 | train add 0.0291 | train add prop 0.0000 | val del 0.0794 | val add 0.0294 | val add prop 0.0002 | del F1 0.9613 | add F1 0.9926
epoch 044 | time 110.25s | train del 0.0238 | train add 0.0264 | train add prop 0.0000 | val del 0.1601 | val add 0.0225 | val add prop 0.0000 | del F1 0.9418 | add F1 0.9950
epoch 045 | time 107.86s | train del 0.0115 | train add 0.0217 | train add prop 0.0000 | val del 0.0972 | val add 0.0606 | val add prop 0.0000 | del F1 0.9475 | add F1 0.9939
epoch 046 | time 129.12s | train del 0.0038 | train add 0.0229 | train add prop 0.0000 | val del 0.1026 | val add 0.0495 | val add prop 0.0002 | del F1 0.9447 | add F1 0.9929
epoch 047 | time 134.20s | train del 0.0038 | train add 0.0207 | train add prop 0.0000 | val del 0.2117 | val add 0.0219 | val add prop 0.0002 | del F1 0.9053 | add F1 0.9956
epoch 048 | time 103.75s | train del 0.0372 | train add 0.0179 | train add prop 0.0000 | val del 0.1632 | val add 0.0349 | val add prop 0.0002 | del F1 0.9122 | add F1 0.9926
epoch 049 | time 165.89s | train del 0.0136 | train add 0.0161 | train add prop 0.0000 | val del 0.1630 | val add 0.0216 | val add prop 0.0000 | del F1 0.9197 | add F1 0.9956
epoch 050 | time 155.38s | train del 0.0056 | train add 0.0170 | train add prop 0.0001 | val del 0.2045 | val add 0.0309 | val add prop 0.0000 | del F1 0.9090 | add F1 0.9939
saved plots/5ent_5rel.png
Working on 10ent_10rel
device: cuda
dataset path: ..\data_exploration\synthetic_data\10ent_10rel.json
num timesteps: 300
x_global shape: (400, 64)
num relations: 10
relations: {0: 'contact', 1: 'negotiate', 2: 'bonded', 3: 'strained', 4: 'recovery', 5: 'conflict', 6: 'repair', 7: 'maintain', 8: 'decay', 9: 'scale'}
example edge_index shape: (2, 22)
example edge_type shape: (22,)
example edge_relative_time shape: (22,)
train timesteps: 0 to 289
validation timesteps: 290 to 299
epoch 001 | time 94.19s | train del 0.6574 | train add 0.4162 | train add prop 0.0000 | val del 0.6418 | val add 0.2993 | val add prop 0.0000 | del F1 0.5915 | add F1 0.8929
epoch 002 | time 99.87s | train del 0.5717 | train add 0.1419 | train add prop 0.0001 | val del 0.4918 | val add 0.0975 | val add prop 0.0000 | del F1 0.6742 | add F1 0.9521
epoch 003 | time 117.80s | train del 0.4311 | train add 0.0812 | train add prop 0.0000 | val del 0.3716 | val add 0.0761 | val add prop 0.0000 | del F1 0.7809 | add F1 0.9554
epoch 004 | time 116.76s | train del 0.3354 | train add 0.0692 | train add prop 0.0000 | val del 0.3154 | val add 0.0622 | val add prop 0.0000 | del F1 0.7873 | add F1 0.9659
epoch 005 | time 87.93s | train del 0.2733 | train add 0.0601 | train add prop 0.0000 | val del 0.2762 | val add 0.0740 | val add prop 0.0000 | del F1 0.8379 | add F1 0.9619
epoch 006 | time 91.59s | train del 0.2428 | train add 0.0577 | train add prop 0.0000 | val del 0.2508 | val add 0.0640 | val add prop 0.0000 | del F1 0.8724 | add F1 0.9594
epoch 007 | time 110.84s | train del 0.2043 | train add 0.0564 | train add prop 0.0000 | val del 0.2301 | val add 0.0701 | val add prop 0.0000 | del F1 0.8668 | add F1 0.9570
epoch 008 | time 88.81s | train del 0.1916 | train add 0.0549 | train add prop 0.0000 | val del 0.1963 | val add 0.0795 | val add prop 0.0000 | del F1 0.8748 | add F1 0.9586
epoch 009 | time 89.12s | train del 0.1631 | train add 0.0569 | train add prop 0.0000 | val del 0.1825 | val add 0.0886 | val add prop 0.0000 | del F1 0.8925 | add F1 0.9619
epoch 010 | time 114.88s | train del 0.1430 | train add 0.0534 | train add prop 0.0000 | val del 0.1586 | val add 0.0619 | val add prop 0.0000 | del F1 0.9093 | add F1 0.9651
epoch 011 | time 90.90s | train del 0.1312 | train add 0.0527 | train add prop 0.0000 | val del 0.1513 | val add 0.0609 | val add prop 0.0000 | del F1 0.9109 | add F1 0.9619
epoch 012 | time 86.32s | train del 0.1160 | train add 0.0504 | train add prop 0.0000 | val del 0.1352 | val add 0.0691 | val add prop 0.0000 | del F1 0.9149 | add F1 0.9578
epoch 013 | time 84.24s | train del 0.1132 | train add 0.0507 | train add prop 0.0000 | val del 0.1632 | val add 0.0669 | val add prop 0.0000 | del F1 0.9021 | add F1 0.9627
epoch 014 | time 103.92s | train del 0.1218 | train add 0.0482 | train add prop 0.0000 | val del 0.1310 | val add 0.0740 | val add prop 0.0000 | del F1 0.9238 | add F1 0.9603
epoch 015 | time 89.16s | train del 0.1004 | train add 0.0493 | train add prop 0.0000 | val del 0.1357 | val add 0.0787 | val add prop 0.0000 | del F1 0.9230 | add F1 0.9676
epoch 016 | time 89.45s | train del 0.0963 | train add 0.0476 | train add prop 0.0000 | val del 0.1628 | val add 0.0636 | val add prop 0.0000 | del F1 0.9230 | add F1 0.9619
epoch 017 | time 87.25s | train del 0.0868 | train add 0.0460 | train add prop 0.0000 | val del 0.1377 | val add 0.0656 | val add prop 0.0000 | del F1 0.9230 | add F1 0.9603
epoch 018 | time 87.81s | train del 0.0859 | train add 0.0473 | train add prop 0.0000 | val del 0.1472 | val add 0.0611 | val add prop 0.0000 | del F1 0.9318 | add F1 0.9635
epoch 019 | time 90.44s | train del 0.0788 | train add 0.0440 | train add prop 0.0001 | val del 0.1417 | val add 0.1005 | val add prop 0.0000 | del F1 0.9286 | add F1 0.9578
epoch 020 | time 90.84s | train del 0.0775 | train add 0.0489 | train add prop 0.0000 | val del 0.1222 | val add 0.0503 | val add prop 0.0000 | del F1 0.9262 | add F1 0.9700
epoch 021 | time 87.60s | train del 0.0730 | train add 0.0440 | train add prop 0.0000 | val del 0.1258 | val add 0.0623 | val add prop 0.0000 | del F1 0.9246 | add F1 0.9594
epoch 022 | time 88.26s | train del 0.0678 | train add 0.0425 | train add prop 0.0000 | val del 0.1459 | val add 0.0634 | val add prop 0.0000 | del F1 0.9181 | add F1 0.9611
epoch 023 | time 124.42s | train del 0.0677 | train add 0.0427 | train add prop 0.0001 | val del 0.1241 | val add 0.0648 | val add prop 0.0000 | del F1 0.9262 | add F1 0.9651
epoch 024 | time 85.57s | train del 0.0687 | train add 0.0411 | train add prop 0.0000 | val del 0.1336 | val add 0.0605 | val add prop 0.0000 | del F1 0.9238 | add F1 0.9627
epoch 025 | time 97.87s | train del 0.0633 | train add 0.0415 | train add prop 0.0000 | val del 0.1429 | val add 0.0631 | val add prop 0.0008 | del F1 0.9254 | add F1 0.9635
epoch 026 | time 88.73s | train del 0.0674 | train add 0.0430 | train add prop 0.0000 | val del 0.1525 | val add 0.0604 | val add prop 0.0000 | del F1 0.9326 | add F1 0.9651
epoch 027 | time 90.43s | train del 0.0584 | train add 0.0412 | train add prop 0.0000 | val del 0.1364 | val add 0.0606 | val add prop 0.0000 | del F1 0.9302 | add F1 0.9676
epoch 028 | time 94.94s | train del 0.0537 | train add 0.0419 | train add prop 0.0000 | val del 0.1644 | val add 0.0629 | val add prop 0.0000 | del F1 0.9230 | add F1 0.9611
epoch 029 | time 113.67s | train del 0.0521 | train add 0.0395 | train add prop 0.0001 | val del 0.1641 | val add 0.0756 | val add prop 0.0000 | del F1 0.9310 | add F1 0.9586
epoch 030 | time 86.12s | train del 0.0591 | train add 0.0401 | train add prop 0.0000 | val del 0.1405 | val add 0.0712 | val add prop 0.0000 | del F1 0.9270 | add F1 0.9611
epoch 031 | time 109.00s | train del 0.0490 | train add 0.0391 | train add prop 0.0000 | val del 0.1373 | val add 0.0626 | val add prop 0.0000 | del F1 0.9342 | add F1 0.9659
epoch 032 | time 85.15s | train del 0.0511 | train add 0.0367 | train add prop 0.0000 | val del 0.1523 | val add 0.0726 | val add prop 0.0000 | del F1 0.9326 | add F1 0.9651
epoch 033 | time 104.19s | train del 0.0469 | train add 0.0375 | train add prop 0.0000 | val del 0.1600 | val add 0.0675 | val add prop 0.0000 | del F1 0.9262 | add F1 0.9708
epoch 034 | time 88.04s | train del 0.0450 | train add 0.0377 | train add prop 0.0000 | val del 0.1608 | val add 0.0735 | val add prop 0.0000 | del F1 0.9238 | add F1 0.9578
epoch 035 | time 78.06s | train del 0.0460 | train add 0.0384 | train add prop 0.0000 | val del 0.1413 | val add 0.0621 | val add prop 0.0000 | del F1 0.9310 | add F1 0.9676
epoch 036 | time 88.64s | train del 0.0429 | train add 0.0386 | train add prop 0.0000 | val del 0.1479 | val add 0.0739 | val add prop 0.0000 | del F1 0.9326 | add F1 0.9643
epoch 037 | time 106.72s | train del 0.0498 | train add 0.0374 | train add prop 0.0000 | val del 0.1724 | val add 0.0654 | val add prop 0.0000 | del F1 0.9238 | add F1 0.9651
epoch 038 | time 90.36s | train del 0.0470 | train add 0.0391 | train add prop 0.0000 | val del 0.1524 | val add 0.0786 | val add prop 0.0000 | del F1 0.9310 | add F1 0.9538
epoch 039 | time 144.71s | train del 0.0411 | train add 0.0395 | train add prop 0.0000 | val del 0.1628 | val add 0.0757 | val add prop 0.0000 | del F1 0.9318 | add F1 0.9611
epoch 040 | time 96.08s | train del 0.0443 | train add 0.0389 | train add prop 0.0000 | val del 0.1614 | val add 0.0593 | val add prop 0.0000 | del F1 0.9286 | add F1 0.9684
epoch 041 | time 106.63s | train del 0.0359 | train add 0.0363 | train add prop 0.0000 | val del 0.1723 | val add 0.0643 | val add prop 0.0000 | del F1 0.9246 | add F1 0.9651
epoch 042 | time 89.70s | train del 0.0386 | train add 0.0357 | train add prop 0.0000 | val del 0.1784 | val add 0.0768 | val add prop 0.0000 | del F1 0.9246 | add F1 0.9570
epoch 043 | time 114.23s | train del 0.0347 | train add 0.0368 | train add prop 0.0000 | val del 0.2485 | val add 0.0713 | val add prop 0.0000 | del F1 0.9294 | add F1 0.9659
epoch 044 | time 73.51s | train del 0.0530 | train add 0.0358 | train add prop 0.0000 | val del 0.1817 | val add 0.0799 | val add prop 0.0000 | del F1 0.9390 | add F1 0.9700
epoch 045 | time 26.09s | train del 0.0456 | train add 0.0370 | train add prop 0.0001 | val del 0.1904 | val add 0.0670 | val add prop 0.0000 | del F1 0.9382 | add F1 0.9635
epoch 046 | time 24.85s | train del 0.0388 | train add 0.0362 | train add prop 0.0001 | val del 0.2317 | val add 0.0730 | val add prop 0.0000 | del F1 0.9350 | add F1 0.9635
epoch 047 | time 26.29s | train del 0.0346 | train add 0.0352 | train add prop 0.0000 | val del 0.1807 | val add 0.0767 | val add prop 0.0000 | del F1 0.9294 | add F1 0.9594
epoch 048 | time 31.55s | train del 0.0287 | train add 0.0352 | train add prop 0.0000 | val del 0.1746 | val add 0.0833 | val add prop 0.0000 | del F1 0.9318 | add F1 0.9570
epoch 049 | time 17.70s | train del 0.0314 | train add 0.0357 | train add prop 0.0000 | val del 0.1850 | val add 0.1014 | val add prop 0.0000 | del F1 0.9286 | add F1 0.9627
epoch 050 | time 18.32s | train del 0.0283 | train add 0.0361 | train add prop 0.0000 | val del 0.1855 | val add 0.0737 | val add prop 0.0008 | del F1 0.9294 | add F1 0.9594
saved plots/10ent_10rel.png
Working on 2ent_2rel_noise
device: cuda
dataset path: ..\data_exploration\synthetic_data\2ent_2rel_noise.json
num timesteps: 300
x_global shape: (400, 64)
num relations: 2
relations: {0: 'contact', 1: 'negotiate'}
example edge_index shape: (2, 861)
example edge_type shape: (861,)
example edge_relative_time shape: (861,)
train timesteps: 0 to 289
validation timesteps: 290 to 299
epoch 001 | time 115.31s | train del 0.6344 | train add 0.5109 | train add prop 0.0007 | val del 0.5747 | val add 0.4407 | val add prop 0.0006 | del F1 0.5306 | add F1 0.9606
epoch 002 | time 141.32s | train del 0.6015 | train add 0.2806 | train add prop 0.0007 | val del 0.5784 | val add 0.1258 | val add prop 0.0008 | del F1 0.5428 | add F1 0.9732
epoch 003 | time 127.05s | train del 0.5407 | train add 0.1898 | train add prop 0.0007 | val del 0.4810 | val add 0.1174 | val add prop 0.0008 | del F1 0.7688 | add F1 0.9778
epoch 004 | time 149.22s | train del 0.4679 | train add 0.1608 | train add prop 0.0007 | val del 0.4324 | val add 0.1314 | val add prop 0.0006 | del F1 0.8649 | add F1 0.9762
epoch 005 | time 141.73s | train del 0.4037 | train add 0.1566 | train add prop 0.0007 | val del 0.3582 | val add 0.1441 | val add prop 0.0006 | del F1 0.8655 | add F1 0.9773
epoch 006 | time 148.71s | train del 0.3646 | train add 0.1546 | train add prop 0.0007 | val del 0.3951 | val add 0.1383 | val add prop 0.0005 | del F1 0.8649 | add F1 0.9795
epoch 007 | time 150.70s | train del 0.3502 | train add 0.1470 | train add prop 0.0007 | val del 0.2947 | val add 0.1525 | val add prop 0.0008 | del F1 0.8657 | add F1 0.9784
epoch 008 | time 132.08s | train del 0.3310 | train add 0.1400 | train add prop 0.0007 | val del 0.2778 | val add 0.1178 | val add prop 0.0006 | del F1 0.8640 | add F1 0.9787
epoch 009 | time 124.90s | train del 0.3190 | train add 0.1412 | train add prop 0.0008 | val del 0.2699 | val add 0.1145 | val add prop 0.0006 | del F1 0.8653 | add F1 0.9810
epoch 010 | time 99.19s | train del 0.3158 | train add 0.1382 | train add prop 0.0008 | val del 0.2886 | val add 0.1043 | val add prop 0.0007 | del F1 0.8649 | add F1 0.9796
epoch 011 | time 123.39s | train del 0.3022 | train add 0.1352 | train add prop 0.0008 | val del 0.2775 | val add 0.1889 | val add prop 0.0006 | del F1 0.8646 | add F1 0.9801
epoch 012 | time 155.78s | train del 0.2940 | train add 0.1386 | train add prop 0.0008 | val del 0.2550 | val add 0.1441 | val add prop 0.0007 | del F1 0.8656 | add F1 0.9793
epoch 013 | time 116.85s | train del 0.2884 | train add 0.1405 | train add prop 0.0007 | val del 0.2682 | val add 0.1056 | val add prop 0.0007 | del F1 0.8647 | add F1 0.9803
epoch 014 | time 127.44s | train del 0.2892 | train add 0.1364 | train add prop 0.0008 | val del 0.2575 | val add 0.1389 | val add prop 0.0007 | del F1 0.8645 | add F1 0.9789
epoch 015 | time 144.05s | train del 0.2820 | train add 0.1344 | train add prop 0.0008 | val del 0.2447 | val add 0.1665 | val add prop 0.0010 | del F1 0.8654 | add F1 0.9789
epoch 016 | time 138.00s | train del 0.2813 | train add 0.1320 | train add prop 0.0007 | val del 0.2508 | val add 0.2086 | val add prop 0.0004 | del F1 0.8674 | add F1 0.9780
epoch 017 | time 124.98s | train del 0.2810 | train add 0.1334 | train add prop 0.0008 | val del 0.2521 | val add 0.1218 | val add prop 0.0003 | del F1 0.8678 | add F1 0.9803
epoch 018 | time 122.10s | train del 0.2827 | train add 0.1354 | train add prop 0.0008 | val del 0.2480 | val add 0.1145 | val add prop 0.0008 | del F1 0.8669 | add F1 0.9796
epoch 019 | time 140.82s | train del 0.2831 | train add 0.1278 | train add prop 0.0008 | val del 0.2720 | val add 0.1605 | val add prop 0.0010 | del F1 0.8653 | add F1 0.9779
epoch 020 | time 136.34s | train del 0.2791 | train add 0.1288 | train add prop 0.0007 | val del 0.2481 | val add 0.1371 | val add prop 0.0010 | del F1 0.8658 | add F1 0.9772
epoch 021 | time 127.78s | train del 0.2800 | train add 0.1307 | train add prop 0.0007 | val del 0.2574 | val add 0.1083 | val add prop 0.0005 | del F1 0.8658 | add F1 0.9809
epoch 022 | time 140.18s | train del 0.2747 | train add 0.1291 | train add prop 0.0007 | val del 0.2379 | val add 0.1529 | val add prop 0.0010 | del F1 0.8665 | add F1 0.9787
epoch 023 | time 139.69s | train del 0.2714 | train add 0.1307 | train add prop 0.0007 | val del 0.2623 | val add 0.1257 | val add prop 0.0004 | del F1 0.8649 | add F1 0.9806
epoch 024 | time 127.25s | train del 0.2832 | train add 0.1305 | train add prop 0.0007 | val del 0.2699 | val add 0.1126 | val add prop 0.0008 | del F1 0.8643 | add F1 0.9798
epoch 025 | time 156.60s | train del 0.2785 | train add 0.1273 | train add prop 0.0007 | val del 0.2609 | val add 0.1010 | val add prop 0.0010 | del F1 0.8655 | add F1 0.9795
epoch 026 | time 128.09s | train del 0.2771 | train add 0.1278 | train add prop 0.0008 | val del 0.2447 | val add 0.1113 | val add prop 0.0008 | del F1 0.8673 | add F1 0.9803
epoch 027 | time 126.40s | train del 0.2818 | train add 0.1290 | train add prop 0.0008 | val del 0.2377 | val add 0.0972 | val add prop 0.0005 | del F1 0.8673 | add F1 0.9796
epoch 028 | time 145.65s | train del 0.2778 | train add 0.1266 | train add prop 0.0008 | val del 0.2430 | val add 0.1615 | val add prop 0.0006 | del F1 0.8662 | add F1 0.9798
epoch 029 | time 126.68s | train del 0.2759 | train add 0.1313 | train add prop 0.0007 | val del 0.2562 | val add 0.1412 | val add prop 0.0008 | del F1 0.8675 | add F1 0.9798
epoch 030 | time 122.83s | train del 0.2773 | train add 0.1287 | train add prop 0.0008 | val del 0.2549 | val add 0.1011 | val add prop 0.0010 | del F1 0.8655 | add F1 0.9807
epoch 031 | time 123.25s | train del 0.2840 | train add 0.1272 | train add prop 0.0007 | val del 0.2568 | val add 0.1361 | val add prop 0.0006 | del F1 0.8658 | add F1 0.9799
epoch 032 | time 123.51s | train del 0.2715 | train add 0.1325 | train add prop 0.0007 | val del 0.2531 | val add 0.1043 | val add prop 0.0011 | del F1 0.8654 | add F1 0.9806
epoch 033 | time 127.73s | train del 0.2778 | train add 0.1302 | train add prop 0.0007 | val del 0.2594 | val add 0.1212 | val add prop 0.0003 | del F1 0.8648 | add F1 0.9803
epoch 034 | time 130.48s | train del 0.2792 | train add 0.1293 | train add prop 0.0007 | val del 0.2742 | val add 0.1365 | val add prop 0.0003 | del F1 0.8641 | add F1 0.9807
epoch 035 | time 130.56s | train del 0.2796 | train add 0.1291 | train add prop 0.0007 | val del 0.2430 | val add 0.0993 | val add prop 0.0004 | del F1 0.8681 | add F1 0.9812
epoch 036 | time 137.38s | train del 0.2743 | train add 0.1264 | train add prop 0.0007 | val del 0.2560 | val add 0.1971 | val add prop 0.0012 | del F1 0.8656 | add F1 0.9818
epoch 037 | time 114.60s | train del 0.2724 | train add 0.1276 | train add prop 0.0007 | val del 0.2362 | val add 0.1528 | val add prop 0.0006 | del F1 0.8677 | add F1 0.9800
epoch 038 | time 152.00s | train del 0.2751 | train add 0.1274 | train add prop 0.0008 | val del 0.2629 | val add 0.1437 | val add prop 0.0005 | del F1 0.8673 | add F1 0.9803
epoch 039 | time 138.48s | train del 0.2763 | train add 0.1247 | train add prop 0.0007 | val del 0.2561 | val add 0.1337 | val add prop 0.0003 | del F1 0.8666 | add F1 0.9800
epoch 040 | time 124.53s | train del 0.2778 | train add 0.1280 | train add prop 0.0008 | val del 0.2444 | val add 0.1358 | val add prop 0.0006 | del F1 0.8683 | add F1 0.9802
epoch 041 | time 153.21s | train del 0.2688 | train add 0.1260 | train add prop 0.0008 | val del 0.2423 | val add 0.1172 | val add prop 0.0006 | del F1 0.8686 | add F1 0.9803
epoch 042 | time 148.32s | train del 0.2758 | train add 0.1294 | train add prop 0.0007 | val del 0.2533 | val add 0.1283 | val add prop 0.0005 | del F1 0.8671 | add F1 0.9810
epoch 043 | time 138.42s | train del 0.2743 | train add 0.1299 | train add prop 0.0008 | val del 0.2750 | val add 0.1499 | val add prop 0.0010 | del F1 0.8658 | add F1 0.9789
epoch 044 | time 118.05s | train del 0.2750 | train add 0.1262 | train add prop 0.0007 | val del 0.2365 | val add 0.1399 | val add prop 0.0005 | del F1 0.8690 | add F1 0.9800
epoch 045 | time 120.13s | train del 0.2778 | train add 0.1244 | train add prop 0.0008 | val del 0.2397 | val add 0.1247 | val add prop 0.0006 | del F1 0.8678 | add F1 0.9795
epoch 046 | time 131.42s | train del 0.2740 | train add 0.1223 | train add prop 0.0007 | val del 0.2663 | val add 0.1070 | val add prop 0.0007 | del F1 0.8647 | add F1 0.9805
epoch 047 | time 140.62s | train del 0.2762 | train add 0.1219 | train add prop 0.0008 | val del 0.2480 | val add 0.1199 | val add prop 0.0006 | del F1 0.8673 | add F1 0.9794
epoch 048 | time 127.41s | train del 0.2749 | train add 0.1254 | train add prop 0.0008 | val del 0.2447 | val add 0.1228 | val add prop 0.0007 | del F1 0.8685 | add F1 0.9809
epoch 049 | time 138.83s | train del 0.2726 | train add 0.1255 | train add prop 0.0007 | val del 0.2407 | val add 0.1249 | val add prop 0.0005 | del F1 0.8678 | add F1 0.9802
epoch 050 | time 149.71s | train del 0.2755 | train add 0.1260 | train add prop 0.0008 | val del 0.2412 | val add 0.1102 | val add prop 0.0006 | del F1 0.8673 | add F1 0.9801
saved plots/2ent_2rel_noise.png
Working on 2ent_5rel_noise
Dataset 2ent_5rel_noise broken, skipping
Working on 2ent_9rel_noise
device: cuda
dataset path: ..\data_exploration\synthetic_data\2ent_9rel_noise.json
num timesteps: 300
x_global shape: (400, 64)
num relations: 9
relations: {0: 'contact', 1: 'negotiate', 2: 'bonded', 3: 'strained', 4: 'recovery', 5: 'conflict', 6: 'repair', 7: 'maintain', 8: 'decay'}
example edge_index shape: (2, 877)
example edge_type shape: (877,)
example edge_relative_time shape: (877,)
train timesteps: 0 to 289
validation timesteps: 290 to 299
epoch 001 | time 167.27s | train del 0.6549 | train add 0.4587 | train add prop 0.0002 | val del 0.6285 | val add 0.4902 | val add prop 0.0002 | del F1 0.5653 | add F1 0.9831
epoch 002 | time 176.72s | train del 0.6290 | train add 0.2567 | train add prop 0.0002 | val del 0.5818 | val add 0.1325 | val add prop 0.0000 | del F1 0.6198 | add F1 0.9859
epoch 003 | time 181.37s | train del 0.5689 | train add 0.1645 | train add prop 0.0002 | val del 0.5021 | val add 0.1181 | val add prop 0.0002 | del F1 0.7292 | add F1 0.9861
epoch 004 | time 181.56s | train del 0.5142 | train add 0.1346 | train add prop 0.0002 | val del 0.4633 | val add 0.1566 | val add prop 0.0002 | del F1 0.7399 | add F1 0.9874
epoch 005 | time 182.10s | train del 0.4819 | train add 0.1188 | train add prop 0.0002 | val del 0.4595 | val add 0.0666 | val add prop 0.0003 | del F1 0.7390 | add F1 0.9892
epoch 006 | time 172.43s | train del 0.4653 | train add 0.1165 | train add prop 0.0002 | val del 0.4578 | val add 0.1759 | val add prop 0.0000 | del F1 0.7366 | add F1 0.9902
epoch 007 | time 164.67s | train del 0.4540 | train add 0.1061 | train add prop 0.0002 | val del 0.4419 | val add 0.0879 | val add prop 0.0002 | del F1 0.7464 | add F1 0.9899
epoch 008 | time 145.73s | train del 0.4528 | train add 0.1026 | train add prop 0.0002 | val del 0.4273 | val add 0.2396 | val add prop 0.0001 | del F1 0.7471 | add F1 0.9899
epoch 009 | time 167.25s | train del 0.4444 | train add 0.1064 | train add prop 0.0002 | val del 0.4545 | val add 0.1008 | val add prop 0.0002 | del F1 0.7467 | add F1 0.9891
epoch 010 | time 160.75s | train del 0.4388 | train add 0.0990 | train add prop 0.0002 | val del 0.4240 | val add 0.1165 | val add prop 0.0003 | del F1 0.7576 | add F1 0.9896
epoch 011 | time 182.83s | train del 0.4370 | train add 0.0962 | train add prop 0.0002 | val del 0.4224 | val add 0.0995 | val add prop 0.0001 | del F1 0.7562 | add F1 0.9908
epoch 012 | time 172.16s | train del 0.4354 | train add 0.0916 | train add prop 0.0002 | val del 0.4121 | val add 0.0738 | val add prop 0.0003 | del F1 0.7532 | add F1 0.9895
epoch 013 | time 139.18s | train del 0.4311 | train add 0.0915 | train add prop 0.0002 | val del 0.4021 | val add 0.1032 | val add prop 0.0001 | del F1 0.7560 | add F1 0.9899
epoch 014 | time 167.82s | train del 0.4307 | train add 0.0898 | train add prop 0.0002 | val del 0.4144 | val add 0.0650 | val add prop 0.0002 | del F1 0.7568 | add F1 0.9893
epoch 015 | time 180.65s | train del 0.4262 | train add 0.0900 | train add prop 0.0002 | val del 0.4081 | val add 0.0822 | val add prop 0.0000 | del F1 0.7543 | add F1 0.9907
epoch 016 | time 162.46s | train del 0.4304 | train add 0.0857 | train add prop 0.0002 | val del 0.4173 | val add 0.0577 | val add prop 0.0001 | del F1 0.7558 | add F1 0.9910
epoch 017 | time 168.82s | train del 0.4247 | train add 0.0898 | train add prop 0.0002 | val del 0.4178 | val add 0.0666 | val add prop 0.0002 | del F1 0.7572 | add F1 0.9914
epoch 018 | time 167.99s | train del 0.4239 | train add 0.0876 | train add prop 0.0002 | val del 0.4112 | val add 0.0893 | val add prop 0.0001 | del F1 0.7566 | add F1 0.9913
epoch 019 | time 174.36s | train del 0.4207 | train add 0.0906 | train add prop 0.0002 | val del 0.4050 | val add 0.1067 | val add prop 0.0001 | del F1 0.7569 | add F1 0.9914
epoch 020 | time 178.91s | train del 0.4190 | train add 0.0879 | train add prop 0.0002 | val del 0.4129 | val add 0.0668 | val add prop 0.0001 | del F1 0.7583 | add F1 0.9896
epoch 021 | time 169.92s | train del 0.4239 | train add 0.0847 | train add prop 0.0002 | val del 0.4139 | val add 0.0700 | val add prop 0.0001 | del F1 0.7575 | add F1 0.9902
epoch 022 | time 167.04s | train del 0.4225 | train add 0.0849 | train add prop 0.0002 | val del 0.4033 | val add 0.0962 | val add prop 0.0001 | del F1 0.7575 | add F1 0.9915
epoch 023 | time 179.16s | train del 0.4156 | train add 0.0856 | train add prop 0.0002 | val del 0.4355 | val add 0.0673 | val add prop 0.0002 | del F1 0.7584 | add F1 0.9905
epoch 024 | time 176.88s | train del 0.4195 | train add 0.0870 | train add prop 0.0002 | val del 0.4029 | val add 0.0613 | val add prop 0.0003 | del F1 0.7564 | add F1 0.9919
epoch 025 | time 167.79s | train del 0.4216 | train add 0.0837 | train add prop 0.0002 | val del 0.4141 | val add 0.1228 | val add prop 0.0004 | del F1 0.7574 | add F1 0.9910
epoch 026 | time 186.34s | train del 0.4175 | train add 0.0890 | train add prop 0.0002 | val del 0.3939 | val add 0.1256 | val add prop 0.0003 | del F1 0.7592 | add F1 0.9912
epoch 027 | time 179.24s | train del 0.4210 | train add 0.0846 | train add prop 0.0002 | val del 0.4031 | val add 0.0753 | val add prop 0.0001 | del F1 0.7549 | add F1 0.9906
epoch 028 | time 164.88s | train del 0.4221 | train add 0.0821 | train add prop 0.0002 | val del 0.4020 | val add 0.0689 | val add prop 0.0002 | del F1 0.7597 | add F1 0.9918
epoch 029 | time 181.56s | train del 0.4142 | train add 0.0866 | train add prop 0.0002 | val del 0.4079 | val add 0.0801 | val add prop 0.0002 | del F1 0.7655 | add F1 0.9918
epoch 030 | time 171.39s | train del 0.4081 | train add 0.0815 | train add prop 0.0002 | val del 0.3778 | val add 0.0932 | val add prop 0.0002 | del F1 0.7985 | add F1 0.9909
epoch 031 | time 177.23s | train del 0.3669 | train add 0.0826 | train add prop 0.0002 | val del 0.3478 | val add 0.0622 | val add prop 0.0004 | del F1 0.8297 | add F1 0.9912
epoch 032 | time 181.78s | train del 0.3458 | train add 0.0822 | train add prop 0.0002 | val del 0.3405 | val add 0.0816 | val add prop 0.0000 | del F1 0.8419 | add F1 0.9913
epoch 033 | time 187.89s | train del 0.3376 | train add 0.0837 | train add prop 0.0002 | val del 0.3438 | val add 0.0871 | val add prop 0.0002 | del F1 0.8424 | add F1 0.9908
epoch 034 | time 186.35s | train del 0.3352 | train add 0.0798 | train add prop 0.0002 | val del 0.3496 | val add 0.0627 | val add prop 0.0001 | del F1 0.8447 | add F1 0.9901
epoch 035 | time 188.00s | train del 0.3314 | train add 0.0817 | train add prop 0.0002 | val del 0.3424 | val add 0.0900 | val add prop 0.0002 | del F1 0.8507 | add F1 0.9917
epoch 036 | time 181.76s | train del 0.3255 | train add 0.0823 | train add prop 0.0002 | val del 0.3178 | val add 0.0933 | val add prop 0.0002 | del F1 0.8562 | add F1 0.9911
epoch 037 | time 169.37s | train del 0.3360 | train add 0.0825 | train add prop 0.0002 | val del 0.3333 | val add 0.0643 | val add prop 0.0001 | del F1 0.8547 | add F1 0.9908
epoch 038 | time 151.66s | train del 0.3342 | train add 0.0816 | train add prop 0.0002 | val del 0.3318 | val add 0.0692 | val add prop 0.0000 | del F1 0.8524 | add F1 0.9915
epoch 039 | time 175.06s | train del 0.3333 | train add 0.0776 | train add prop 0.0002 | val del 0.3268 | val add 0.0677 | val add prop 0.0001 | del F1 0.8528 | add F1 0.9918
epoch 040 | time 182.10s | train del 0.3275 | train add 0.0812 | train add prop 0.0002 | val del 0.3301 | val add 0.0705 | val add prop 0.0001 | del F1 0.8540 | add F1 0.9914
epoch 041 | time 166.07s | train del 0.3331 | train add 0.0829 | train add prop 0.0002 | val del 0.3283 | val add 0.1540 | val add prop 0.0001 | del F1 0.8541 | add F1 0.9916
epoch 042 | time 176.88s | train del 0.3237 | train add 0.0824 | train add prop 0.0002 | val del 0.3184 | val add 0.0467 | val add prop 0.0002 | del F1 0.8550 | add F1 0.9907
epoch 043 | time 178.48s | train del 0.3287 | train add 0.0844 | train add prop 0.0002 | val del 0.3293 | val add 0.0648 | val add prop 0.0003 | del F1 0.8520 | add F1 0.9924
epoch 044 | time 181.93s | train del 0.3259 | train add 0.0777 | train add prop 0.0002 | val del 0.3167 | val add 0.0633 | val add prop 0.0001 | del F1 0.8533 | add F1 0.9919
epoch 045 | time 164.24s | train del 0.3232 | train add 0.0802 | train add prop 0.0002 | val del 0.3186 | val add 0.0833 | val add prop 0.0002 | del F1 0.8540 | add F1 0.9920
epoch 046 | time 180.32s | train del 0.3260 | train add 0.0819 | train add prop 0.0002 | val del 0.3341 | val add 0.0768 | val add prop 0.0001 | del F1 0.8511 | add F1 0.9912
epoch 047 | time 178.39s | train del 0.3228 | train add 0.0811 | train add prop 0.0001 | val del 0.3271 | val add 0.0703 | val add prop 0.0000 | del F1 0.8455 | add F1 0.9917
epoch 048 | time 172.43s | train del 0.3308 | train add 0.0791 | train add prop 0.0002 | val del 0.3277 | val add 0.0604 | val add prop 0.0002 | del F1 0.8475 | add F1 0.9920
epoch 049 | time 158.35s | train del 0.3236 | train add 0.0791 | train add prop 0.0002 | val del 0.3341 | val add 0.0697 | val add prop 0.0001 | del F1 0.8481 | add F1 0.9914
epoch 050 | time 162.50s | train del 0.3292 | train add 0.0774 | train add prop 0.0002 | val del 0.3303 | val add 0.0521 | val add prop 0.0002 | del F1 0.8473 | add F1 0.9913
saved plots/2ent_9rel_noise.png
Working on 5ent_5rel_noise
device: cuda
dataset path: ..\data_exploration\synthetic_data\5ent_5rel_noise.json
num timesteps: 300
x_global shape: (400, 64)
num relations: 5
relations: {0: 'contact', 1: 'negotiate', 2: 'bonded', 3: 'strained', 4: 'recovery'}
example edge_index shape: (2, 133)
example edge_type shape: (133,)
example edge_relative_time shape: (133,)
train timesteps: 0 to 289
validation timesteps: 290 to 299
epoch 001 | time 103.38s | train del 0.6550 | train add 0.4639 | train add prop 0.0011 | val del 0.6683 | val add 0.2708 | val add prop 0.0010 | del F1 0.5886 | add F1 0.9095
epoch 002 | time 108.72s | train del 0.6400 | train add 0.2344 | train add prop 0.0009 | val del 0.6087 | val add 0.1581 | val add prop 0.0012 | del F1 0.6188 | add F1 0.9552
epoch 003 | time 100.00s | train del 0.5870 | train add 0.1607 | train add prop 0.0011 | val del 0.5210 | val add 0.1549 | val add prop 0.0016 | del F1 0.7123 | add F1 0.9616
epoch 004 | time 99.50s | train del 0.5270 | train add 0.1590 | train add prop 0.0009 | val del 0.4714 | val add 0.1760 | val add prop 0.0012 | del F1 0.7255 | add F1 0.9634
epoch 005 | time 103.60s | train del 0.4764 | train add 0.1401 | train add prop 0.0010 | val del 0.4921 | val add 0.1332 | val add prop 0.0012 | del F1 0.7355 | add F1 0.9618
epoch 006 | time 101.94s | train del 0.4585 | train add 0.1333 | train add prop 0.0008 | val del 0.4522 | val add 0.1268 | val add prop 0.0004 | del F1 0.7481 | add F1 0.9662
epoch 007 | time 104.45s | train del 0.4532 | train add 0.1239 | train add prop 0.0010 | val del 0.4273 | val add 0.1227 | val add prop 0.0004 | del F1 0.7423 | add F1 0.9654
epoch 008 | time 103.19s | train del 0.4505 | train add 0.1208 | train add prop 0.0009 | val del 0.4228 | val add 0.1147 | val add prop 0.0012 | del F1 0.7419 | add F1 0.9674
epoch 009 | time 100.58s | train del 0.4437 | train add 0.1181 | train add prop 0.0010 | val del 0.4315 | val add 0.1227 | val add prop 0.0004 | del F1 0.7367 | add F1 0.9682
epoch 010 | time 102.81s | train del 0.4380 | train add 0.1180 | train add prop 0.0010 | val del 0.4310 | val add 0.1658 | val add prop 0.0004 | del F1 0.7568 | add F1 0.9686
epoch 011 | time 98.88s | train del 0.4405 | train add 0.1150 | train add prop 0.0010 | val del 0.4548 | val add 0.1156 | val add prop 0.0008 | del F1 0.7546 | add F1 0.9704
epoch 012 | time 101.35s | train del 0.4367 | train add 0.1173 | train add prop 0.0009 | val del 0.4407 | val add 0.1135 | val add prop 0.0010 | del F1 0.7417 | add F1 0.9692
epoch 013 | time 100.11s | train del 0.4342 | train add 0.1110 | train add prop 0.0009 | val del 0.4159 | val add 0.1392 | val add prop 0.0008 | del F1 0.7530 | add F1 0.9696
epoch 014 | time 98.99s | train del 0.4380 | train add 0.1091 | train add prop 0.0011 | val del 0.4188 | val add 0.1025 | val add prop 0.0012 | del F1 0.7499 | add F1 0.9702
epoch 015 | time 70.41s | train del 0.4318 | train add 0.1043 | train add prop 0.0010 | val del 0.4168 | val add 0.1064 | val add prop 0.0002 | del F1 0.7558 | add F1 0.9720
epoch 016 | time 109.32s | train del 0.4223 | train add 0.1050 | train add prop 0.0010 | val del 0.4093 | val add 0.1037 | val add prop 0.0008 | del F1 0.7616 | add F1 0.9714
epoch 017 | time 99.73s | train del 0.4220 | train add 0.1070 | train add prop 0.0010 | val del 0.4297 | val add 0.1036 | val add prop 0.0002 | del F1 0.7552 | add F1 0.9706
epoch 018 | time 103.44s | train del 0.4252 | train add 0.1017 | train add prop 0.0009 | val del 0.4077 | val add 0.1008 | val add prop 0.0014 | del F1 0.7664 | add F1 0.9722
epoch 019 | time 102.07s | train del 0.4201 | train add 0.1025 | train add prop 0.0011 | val del 0.4190 | val add 0.1107 | val add prop 0.0002 | del F1 0.7742 | add F1 0.9730
epoch 020 | time 100.23s | train del 0.4169 | train add 0.0979 | train add prop 0.0009 | val del 0.4093 | val add 0.1045 | val add prop 0.0004 | del F1 0.7676 | add F1 0.9734
epoch 021 | time 104.21s | train del 0.4203 | train add 0.1013 | train add prop 0.0009 | val del 0.4269 | val add 0.0990 | val add prop 0.0018 | del F1 0.7688 | add F1 0.9742
epoch 022 | time 108.25s | train del 0.4168 | train add 0.0960 | train add prop 0.0008 | val del 0.4071 | val add 0.1074 | val add prop 0.0012 | del F1 0.7656 | add F1 0.9704
epoch 023 | time 100.25s | train del 0.4139 | train add 0.0962 | train add prop 0.0009 | val del 0.4022 | val add 0.0973 | val add prop 0.0008 | del F1 0.7754 | add F1 0.9728
epoch 024 | time 102.65s | train del 0.4131 | train add 0.0928 | train add prop 0.0010 | val del 0.4033 | val add 0.0994 | val add prop 0.0004 | del F1 0.7722 | add F1 0.9718
epoch 025 | time 103.63s | train del 0.4119 | train add 0.0945 | train add prop 0.0008 | val del 0.3912 | val add 0.1089 | val add prop 0.0020 | del F1 0.7730 | add F1 0.9720
epoch 026 | time 92.92s | train del 0.4073 | train add 0.0936 | train add prop 0.0010 | val del 0.3984 | val add 0.1064 | val add prop 0.0008 | del F1 0.7632 | add F1 0.9758
epoch 027 | time 103.36s | train del 0.4095 | train add 0.0889 | train add prop 0.0008 | val del 0.3970 | val add 0.0856 | val add prop 0.0004 | del F1 0.7730 | add F1 0.9772
epoch 028 | time 103.99s | train del 0.4059 | train add 0.0840 | train add prop 0.0009 | val del 0.3951 | val add 0.1068 | val add prop 0.0006 | del F1 0.7764 | add F1 0.9758
epoch 029 | time 101.86s | train del 0.4064 | train add 0.0810 | train add prop 0.0009 | val del 0.4037 | val add 0.0976 | val add prop 0.0010 | del F1 0.7788 | add F1 0.9754
epoch 030 | time 113.52s | train del 0.4053 | train add 0.0800 | train add prop 0.0009 | val del 0.4238 | val add 0.1000 | val add prop 0.0006 | del F1 0.7832 | add F1 0.9722
epoch 031 | time 109.59s | train del 0.4006 | train add 0.0805 | train add prop 0.0010 | val del 0.3953 | val add 0.1294 | val add prop 0.0002 | del F1 0.7772 | add F1 0.9792
epoch 032 | time 103.03s | train del 0.4028 | train add 0.0776 | train add prop 0.0011 | val del 0.3930 | val add 0.0780 | val add prop 0.0006 | del F1 0.7796 | add F1 0.9784
epoch 033 | time 97.88s | train del 0.3975 | train add 0.0749 | train add prop 0.0010 | val del 0.4087 | val add 0.1060 | val add prop 0.0012 | del F1 0.7740 | add F1 0.9754
epoch 034 | time 105.25s | train del 0.3969 | train add 0.0736 | train add prop 0.0009 | val del 0.4127 | val add 0.0991 | val add prop 0.0010 | del F1 0.7746 | add F1 0.9802
epoch 035 | time 116.40s | train del 0.3985 | train add 0.0716 | train add prop 0.0009 | val del 0.4002 | val add 0.0819 | val add prop 0.0016 | del F1 0.7706 | add F1 0.9804
epoch 036 | time 110.47s | train del 0.3956 | train add 0.0693 | train add prop 0.0010 | val del 0.4103 | val add 0.0785 | val add prop 0.0004 | del F1 0.7728 | add F1 0.9810
epoch 037 | time 102.10s | train del 0.3986 | train add 0.0686 | train add prop 0.0009 | val del 0.3891 | val add 0.1228 | val add prop 0.0010 | del F1 0.7828 | add F1 0.9798
epoch 038 | time 104.43s | train del 0.3962 | train add 0.0695 | train add prop 0.0010 | val del 0.3893 | val add 0.0837 | val add prop 0.0008 | del F1 0.7790 | add F1 0.9792
epoch 039 | time 101.70s | train del 0.4005 | train add 0.0735 | train add prop 0.0009 | val del 0.3873 | val add 0.0831 | val add prop 0.0014 | del F1 0.7846 | add F1 0.9790
epoch 040 | time 103.97s | train del 0.3898 | train add 0.0693 | train add prop 0.0010 | val del 0.3921 | val add 0.0908 | val add prop 0.0014 | del F1 0.7790 | add F1 0.9806
epoch 041 | time 97.43s | train del 0.3917 | train add 0.0675 | train add prop 0.0009 | val del 0.3944 | val add 0.0769 | val add prop 0.0012 | del F1 0.7836 | add F1 0.9796
epoch 042 | time 105.08s | train del 0.3948 | train add 0.0669 | train add prop 0.0009 | val del 0.3910 | val add 0.1024 | val add prop 0.0006 | del F1 0.7832 | add F1 0.9776
epoch 043 | time 101.56s | train del 0.3914 | train add 0.0684 | train add prop 0.0009 | val del 0.3930 | val add 0.0793 | val add prop 0.0010 | del F1 0.7842 | add F1 0.9790
epoch 044 | time 101.89s | train del 0.3821 | train add 0.0717 | train add prop 0.0010 | val del 0.3843 | val add 0.0844 | val add prop 0.0012 | del F1 0.7970 | add F1 0.9802
epoch 045 | time 104.00s | train del 0.3778 | train add 0.0659 | train add prop 0.0009 | val del 0.4066 | val add 0.0677 | val add prop 0.0006 | del F1 0.7954 | add F1 0.9814
epoch 046 | time 98.33s | train del 0.3723 | train add 0.0646 | train add prop 0.0009 | val del 0.3752 | val add 0.0768 | val add prop 0.0004 | del F1 0.8008 | add F1 0.9818
epoch 047 | time 99.92s | train del 0.3600 | train add 0.0662 | train add prop 0.0009 | val del 0.3795 | val add 0.0699 | val add prop 0.0006 | del F1 0.8050 | add F1 0.9804
epoch 048 | time 94.81s | train del 0.3471 | train add 0.0683 | train add prop 0.0010 | val del 0.3584 | val add 0.0813 | val add prop 0.0014 | del F1 0.8188 | add F1 0.9808
epoch 049 | time 100.66s | train del 0.3342 | train add 0.0643 | train add prop 0.0008 | val del 0.3724 | val add 0.0761 | val add prop 0.0010 | del F1 0.8196 | add F1 0.9806
epoch 050 | time 95.12s | train del 0.3250 | train add 0.0638 | train add prop 0.0009 | val del 0.3685 | val add 0.0673 | val add prop 0.0004 | del F1 0.8306 | add F1 0.9822
saved plots/5ent_5rel_noise.png
Working on 10ent_10rel_noise
device: cuda
dataset path: ..\data_exploration\synthetic_data\10ent_10rel_noise.json
num timesteps: 300
x_global shape: (400, 64)
num relations: 10
relations: {0: 'contact', 1: 'negotiate', 2: 'bonded', 3: 'strained', 4: 'recovery', 5: 'conflict', 6: 'repair', 7: 'maintain', 8: 'decay', 9: 'scale'}
example edge_index shape: (2, 36)
example edge_type shape: (36,)
example edge_relative_time shape: (36,)
train timesteps: 0 to 289
validation timesteps: 290 to 299
epoch 001 | time 67.84s | train del 0.6706 | train add 0.4370 | train add prop 0.0026 | val del 0.6418 | val add 0.6587 | val add prop 0.0026 | del F1 0.5337 | add F1 0.8694
epoch 002 | time 79.57s | train del 0.6382 | train add 0.2580 | train add prop 0.0034 | val del 0.6152 | val add 0.2485 | val add prop 0.0033 | del F1 0.6202 | add F1 0.9052
epoch 003 | time 70.79s | train del 0.5640 | train add 0.1867 | train add prop 0.0033 | val del 0.5068 | val add 0.1609 | val add prop 0.0046 | del F1 0.6916 | add F1 0.9258
epoch 004 | time 82.18s | train del 0.5142 | train add 0.1628 | train add prop 0.0030 | val del 0.5189 | val add 0.1448 | val add prop 0.0034 | del F1 0.7145 | add F1 0.9298
epoch 005 | time 58.46s | train del 0.4873 | train add 0.1451 | train add prop 0.0032 | val del 0.5304 | val add 0.1324 | val add prop 0.0026 | del F1 0.7328 | add F1 0.9304
epoch 006 | time 83.50s | train del 0.4637 | train add 0.1393 | train add prop 0.0027 | val del 0.4605 | val add 0.1503 | val add prop 0.0014 | del F1 0.7498 | add F1 0.9311
epoch 007 | time 70.68s | train del 0.4512 | train add 0.1297 | train add prop 0.0032 | val del 0.4282 | val add 0.1260 | val add prop 0.0013 | del F1 0.7583 | add F1 0.9357
epoch 008 | time 81.81s | train del 0.4324 | train add 0.1234 | train add prop 0.0031 | val del 0.4470 | val add 0.1226 | val add prop 0.0020 | del F1 0.7544 | add F1 0.9397
epoch 009 | time 74.92s | train del 0.4218 | train add 0.1177 | train add prop 0.0027 | val del 0.4283 | val add 0.1170 | val add prop 0.0033 | del F1 0.7682 | add F1 0.9397
epoch 010 | time 75.48s | train del 0.4110 | train add 0.1158 | train add prop 0.0029 | val del 0.4424 | val add 0.1182 | val add prop 0.0026 | del F1 0.7734 | add F1 0.9397
epoch 011 | time 81.86s | train del 0.3994 | train add 0.1137 | train add prop 0.0031 | val del 0.4329 | val add 0.1312 | val add prop 0.0013 | del F1 0.7714 | add F1 0.9337
epoch 012 | time 83.59s | train del 0.3904 | train add 0.1117 | train add prop 0.0029 | val del 0.4146 | val add 0.1231 | val add prop 0.0020 | del F1 0.7787 | add F1 0.9377
epoch 013 | time 81.38s | train del 0.3763 | train add 0.1080 | train add prop 0.0030 | val del 0.4811 | val add 0.1167 | val add prop 0.0026 | del F1 0.7806 | add F1 0.9404
epoch 014 | time 70.04s | train del 0.3701 | train add 0.1067 | train add prop 0.0035 | val del 0.4553 | val add 0.1266 | val add prop 0.0034 | del F1 0.7767 | add F1 0.9357
epoch 015 | time 85.33s | train del 0.3619 | train add 0.1021 | train add prop 0.0027 | val del 0.4659 | val add 0.1151 | val add prop 0.0020 | del F1 0.7800 | add F1 0.9443
epoch 016 | time 70.41s | train del 0.3613 | train add 0.1012 | train add prop 0.0033 | val del 0.4703 | val add 0.1153 | val add prop 0.0039 | del F1 0.7885 | add F1 0.9443
epoch 017 | time 83.36s | train del 0.3493 | train add 0.0998 | train add prop 0.0033 | val del 0.4143 | val add 0.1242 | val add prop 0.0033 | del F1 0.7839 | add F1 0.9384
epoch 018 | time 85.75s | train del 0.3407 | train add 0.0967 | train add prop 0.0029 | val del 0.4524 | val add 0.1287 | val add prop 0.0027 | del F1 0.7845 | add F1 0.9357
epoch 019 | time 82.51s | train del 0.3337 | train add 0.0947 | train add prop 0.0031 | val del 0.4470 | val add 0.1277 | val add prop 0.0027 | del F1 0.7904 | add F1 0.9370
epoch 020 | time 72.93s | train del 0.3341 | train add 0.0930 | train add prop 0.0026 | val del 0.4251 | val add 0.1299 | val add prop 0.0026 | del F1 0.7754 | add F1 0.9364
epoch 021 | time 87.15s | train del 0.3239 | train add 0.0892 | train add prop 0.0028 | val del 0.4839 | val add 0.1271 | val add prop 0.0034 | del F1 0.7741 | add F1 0.9390
epoch 022 | time 85.39s | train del 0.3158 | train add 0.0910 | train add prop 0.0030 | val del 0.4215 | val add 0.1323 | val add prop 0.0047 | del F1 0.7787 | add F1 0.9364
epoch 023 | time 70.19s | train del 0.3186 | train add 0.0874 | train add prop 0.0029 | val del 0.4470 | val add 0.1268 | val add prop 0.0046 | del F1 0.7629 | add F1 0.9404
epoch 024 | time 79.90s | train del 0.3126 | train add 0.0865 | train add prop 0.0028 | val del 0.4730 | val add 0.1500 | val add prop 0.0026 | del F1 0.7793 | add F1 0.9410
epoch 025 | time 78.26s | train del 0.2960 | train add 0.0891 | train add prop 0.0033 | val del 0.5109 | val add 0.1209 | val add prop 0.0047 | del F1 0.7813 | add F1 0.9417
epoch 026 | time 84.98s | train del 0.2857 | train add 0.0829 | train add prop 0.0025 | val del 0.4904 | val add 0.1361 | val add prop 0.0040 | del F1 0.7714 | add F1 0.9337
epoch 027 | time 84.30s | train del 0.2884 | train add 0.0830 | train add prop 0.0035 | val del 0.4914 | val add 0.1225 | val add prop 0.0020 | del F1 0.7701 | add F1 0.9423
epoch 028 | time 72.06s | train del 0.2849 | train add 0.0816 | train add prop 0.0031 | val del 0.4881 | val add 0.1406 | val add prop 0.0013 | del F1 0.7728 | add F1 0.9390
epoch 029 | time 95.04s | train del 0.2744 | train add 0.0805 | train add prop 0.0032 | val del 0.4687 | val add 0.1364 | val add prop 0.0020 | del F1 0.7649 | add F1 0.9364
epoch 030 | time 83.12s | train del 0.2652 | train add 0.0792 | train add prop 0.0029 | val del 0.4858 | val add 0.1323 | val add prop 0.0026 | del F1 0.7642 | add F1 0.9384
epoch 031 | time 85.13s | train del 0.2604 | train add 0.0844 | train add prop 0.0023 | val del 0.4897 | val add 0.1377 | val add prop 0.0013 | del F1 0.7747 | add F1 0.9364
epoch 032 | time 72.01s | train del 0.2476 | train add 0.0862 | train add prop 0.0024 | val del 0.4961 | val add 0.1467 | val add prop 0.0006 | del F1 0.7616 | add F1 0.9410
epoch 033 | time 84.53s | train del 0.2442 | train add 0.0775 | train add prop 0.0027 | val del 0.5307 | val add 0.1420 | val add prop 0.0027 | del F1 0.7472 | add F1 0.9384
epoch 034 | time 77.49s | train del 0.2549 | train add 0.0746 | train add prop 0.0026 | val del 0.6023 | val add 0.1464 | val add prop 0.0020 | del F1 0.7636 | add F1 0.9377
epoch 035 | time 83.48s | train del 0.2629 | train add 0.0718 | train add prop 0.0028 | val del 0.5228 | val add 0.1334 | val add prop 0.0066 | del F1 0.7525 | add F1 0.9417
epoch 036 | time 77.96s | train del 0.2357 | train add 0.0699 | train add prop 0.0029 | val del 0.5554 | val add 0.1429 | val add prop 0.0033 | del F1 0.7577 | add F1 0.9423
epoch 037 | time 78.69s | train del 0.2336 | train add 0.0705 | train add prop 0.0027 | val del 0.5586 | val add 0.1406 | val add prop 0.0020 | del F1 0.7525 | add F1 0.9404
epoch 038 | time 69.16s | train del 0.2357 | train add 0.0721 | train add prop 0.0028 | val del 0.6253 | val add 0.1438 | val add prop 0.0019 | del F1 0.7623 | add F1 0.9370
epoch 039 | time 80.15s | train del 0.2369 | train add 0.0700 | train add prop 0.0031 | val del 0.5532 | val add 0.1382 | val add prop 0.0007 | del F1 0.7629 | add F1 0.9364
epoch 040 | time 81.61s | train del 0.2164 | train add 0.0707 | train add prop 0.0028 | val del 0.5736 | val add 0.1501 | val add prop 0.0026 | del F1 0.7623 | add F1 0.9377
epoch 041 | time 68.18s | train del 0.2334 | train add 0.0863 | train add prop 0.0032 | val del 0.7628 | val add 0.1533 | val add prop 0.0027 | del F1 0.7669 | add F1 0.9390
epoch 042 | time 82.47s | train del 0.2434 | train add 0.0702 | train add prop 0.0022 | val del 0.6415 | val add 0.1832 | val add prop 0.0026 | del F1 0.7728 | add F1 0.9377
epoch 043 | time 58.97s | train del 0.2245 | train add 0.0734 | train add prop 0.0025 | val del 0.6144 | val add 0.1413 | val add prop 0.0019 | del F1 0.7682 | add F1 0.9397
epoch 044 | time 83.06s | train del 0.1883 | train add 0.0644 | train add prop 0.0027 | val del 0.6076 | val add 0.1461 | val add prop 0.0040 | del F1 0.7623 | add F1 0.9417
epoch 045 | time 78.16s | train del 0.2078 | train add 0.0660 | train add prop 0.0031 | val del 0.6198 | val add 0.1640 | val add prop 0.0026 | del F1 0.7688 | add F1 0.9304
epoch 046 | time 67.81s | train del 0.1917 | train add 0.0695 | train add prop 0.0031 | val del 0.6065 | val add 0.1524 | val add prop 0.0020 | del F1 0.7505 | add F1 0.9384
epoch 047 | time 75.31s | train del 0.1953 | train add 0.0686 | train add prop 0.0030 | val del 0.6541 | val add 0.1540 | val add prop 0.0033 | del F1 0.7590 | add F1 0.9324
epoch 048 | time 79.66s | train del 0.1745 | train add 0.0617 | train add prop 0.0030 | val del 0.6621 | val add 0.1528 | val add prop 0.0033 | del F1 0.7636 | add F1 0.9397
epoch 049 | time 83.09s | train del 0.1868 | train add 0.0634 | train add prop 0.0029 | val del 0.6399 | val add 0.1518 | val add prop 0.0072 | del F1 0.7616 | add F1 0.9410
epoch 050 | time 71.65s | train del 0.1871 | train add 0.0677 | train add prop 0.0031 | val del 0.6727 | val add 0.1596 | val add prop 0.0020 | del F1 0.7656 | add F1 0.9377
saved plots/10ent_10rel_noise.png

C:\Users\jaden\OneDrive\Yale Classes\CPSC 4520\Temporal_Knowledge_Graph_GNN\models> "C:\Users\jaden\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\python.exe" deltas_v7_synthetic.py
Training on device: cuda
Working on 2ent_5rel
device: cuda
dataset path: ..\data_exploration\synthetic_data\2ent_5rel.json
num timesteps: 300
x_global shape: (400, 64)
num relations: 5
relations: {0: 'contact', 1: 'negotiate', 2: 'bonded', 3: 'strained', 4: 'recovery'}
example edge_index shape: (2, 817)
example edge_type shape: (817,)
example edge_relative_time shape: (817,)
train timesteps: 0 to 289
validation timesteps: 290 to 299
epoch 001 | time 91.24s | train del 0.6477 | train add 0.4600 | train add prop 0.0001 | val del 0.6171 | val add 0.2242 | val add prop 0.0000 | del F1 0.6001 | add F1 0.9808
epoch 002 | time 88.80s | train del 0.6208 | train add 0.1792 | train add prop 0.0000 | val del 0.6002 | val add 0.0842 | val add prop 0.0001 | del F1 0.6475 | add F1 0.9956
epoch 003 | time 92.90s | train del 0.5450 | train add 0.0715 | train add prop 0.0001 | val del 0.4899 | val add 0.0253 | val add prop 0.0000 | del F1 0.7202 | add F1 0.9971
epoch 004 | time 88.28s | train del 0.4166 | train add 0.0559 | train add prop 0.0000 | val del 0.3703 | val add 0.0930 | val add prop 0.0001 | del F1 0.7815 | add F1 0.9970
epoch 005 | time 89.55s | train del 0.3347 | train add 0.0490 | train add prop 0.0001 | val del 0.2966 | val add 0.0291 | val add prop 0.0000 | del F1 0.8007 | add F1 0.9977
epoch 006 | time 89.15s | train del 0.2921 | train add 0.0475 | train add prop 0.0001 | val del 0.2720 | val add 0.0243 | val add prop 0.0001 | del F1 0.7949 | add F1 0.9971
epoch 007 | time 90.00s | train del 0.3101 | train add 0.0456 | train add prop 0.0001 | val del 0.2957 | val add 0.0686 | val add prop 0.0000 | del F1 0.8048 | add F1 0.9977
epoch 008 | time 96.98s | train del 0.2986 | train add 0.0443 | train add prop 0.0001 | val del 0.2669 | val add 0.0871 | val add prop 0.0000 | del F1 0.8108 | add F1 0.9979
epoch 009 | time 92.97s | train del 0.2881 | train add 0.0446 | train add prop 0.0001 | val del 0.2789 | val add 0.0197 | val add prop 0.0000 | del F1 0.8062 | add F1 0.9975
epoch 010 | time 97.05s | train del 0.2744 | train add 0.0469 | train add prop 0.0001 | val del 0.3112 | val add 0.0235 | val add prop 0.0000 | del F1 0.8080 | add F1 0.9977
epoch 011 | time 90.40s | train del 0.2711 | train add 0.0442 | train add prop 0.0001 | val del 0.2953 | val add 0.0240 | val add prop 0.0000 | del F1 0.7912 | add F1 0.9976
epoch 012 | time 94.61s | train del 0.2707 | train add 0.0411 | train add prop 0.0001 | val del 0.2959 | val add 0.0396 | val add prop 0.0001 | del F1 0.7825 | add F1 0.9977
epoch 013 | time 99.62s | train del 0.2665 | train add 0.0401 | train add prop 0.0001 | val del 0.3042 | val add 0.0194 | val add prop 0.0001 | del F1 0.8117 | add F1 0.9977
epoch 014 | time 100.35s | train del 0.2644 | train add 0.0410 | train add prop 0.0001 | val del 0.2498 | val add 0.0282 | val add prop 0.0000 | del F1 0.8103 | add F1 0.9975
epoch 015 | time 92.73s | train del 0.2616 | train add 0.0418 | train add prop 0.0000 | val del 0.2637 | val add 0.0208 | val add prop 0.0000 | del F1 0.8091 | add F1 0.9978
epoch 016 | time 94.40s | train del 0.2623 | train add 0.0417 | train add prop 0.0001 | val del 0.2501 | val add 0.0183 | val add prop 0.0000 | del F1 0.8096 | add F1 0.9976
epoch 017 | time 94.56s | train del 0.2600 | train add 0.0447 | train add prop 0.0001 | val del 0.2724 | val add 0.0193 | val add prop 0.0000 | del F1 0.7972 | add F1 0.9979
epoch 018 | time 92.39s | train del 0.2606 | train add 0.0411 | train add prop 0.0001 | val del 0.2652 | val add 0.0387 | val add prop 0.0001 | del F1 0.8053 | add F1 0.9976
epoch 019 | time 93.08s | train del 0.2583 | train add 0.0398 | train add prop 0.0001 | val del 0.2468 | val add 0.0366 | val add prop 0.0001 | del F1 0.8080 | add F1 0.9976
epoch 020 | time 98.17s | train del 0.2642 | train add 0.0363 | train add prop 0.0001 | val del 0.2923 | val add 0.0208 | val add prop 0.0000 | del F1 0.8029 | add F1 0.9973
epoch 021 | time 98.71s | train del 0.2625 | train add 0.0403 | train add prop 0.0001 | val del 0.2657 | val add 0.0442 | val add prop 0.0000 | del F1 0.7596 | add F1 0.9976
epoch 022 | time 96.20s | train del 0.2654 | train add 0.0399 | train add prop 0.0001 | val del 0.2980 | val add 0.0331 | val add prop 0.0001 | del F1 0.8112 | add F1 0.9978
epoch 023 | time 93.45s | train del 0.2593 | train add 0.0382 | train add prop 0.0001 | val del 0.3025 | val add 0.0757 | val add prop 0.0000 | del F1 0.7924 | add F1 0.9979
epoch 024 | time 92.36s | train del 0.2609 | train add 0.0393 | train add prop 0.0001 | val del 0.3082 | val add 0.0555 | val add prop 0.0000 | del F1 0.7835 | add F1 0.9976
epoch 025 | time 95.72s | train del 0.2649 | train add 0.0399 | train add prop 0.0001 | val del 0.2449 | val add 0.0374 | val add prop 0.0001 | del F1 0.8109 | add F1 0.9977
epoch 026 | time 92.69s | train del 0.2615 | train add 0.0355 | train add prop 0.0001 | val del 0.2562 | val add 0.0272 | val add prop 0.0001 | del F1 0.8125 | add F1 0.9977
epoch 027 | time 92.02s | train del 0.2574 | train add 0.0381 | train add prop 0.0000 | val del 0.2453 | val add 0.0393 | val add prop 0.0001 | del F1 0.8133 | add F1 0.9975
epoch 028 | time 95.97s | train del 0.2635 | train add 0.0398 | train add prop 0.0001 | val del 0.2677 | val add 0.0225 | val add prop 0.0000 | del F1 0.8132 | add F1 0.9976
epoch 029 | time 99.01s | train del 0.2545 | train add 0.0384 | train add prop 0.0001 | val del 0.2532 | val add 0.0926 | val add prop 0.0000 | del F1 0.7984 | add F1 0.9976
epoch 030 | time 96.89s | train del 0.2576 | train add 0.0412 | train add prop 0.0001 | val del 0.2479 | val add 0.0306 | val add prop 0.0001 | del F1 0.8200 | add F1 0.9973
epoch 031 | time 97.38s | train del 0.2396 | train add 0.0356 | train add prop 0.0001 | val del 0.2865 | val add 0.0400 | val add prop 0.0001 | del F1 0.8376 | add F1 0.9977
epoch 032 | time 96.70s | train del 0.2036 | train add 0.0371 | train add prop 0.0000 | val del 0.1663 | val add 0.0392 | val add prop 0.0001 | del F1 0.9147 | add F1 0.9970
epoch 033 | time 92.94s | train del 0.1007 | train add 0.0368 | train add prop 0.0000 | val del 0.0879 | val add 0.0295 | val add prop 0.0001 | del F1 0.9774 | add F1 0.9974
epoch 034 | time 97.09s | train del 0.0375 | train add 0.0347 | train add prop 0.0001 | val del 0.0506 | val add 0.0289 | val add prop 0.0000 | del F1 0.9893 | add F1 0.9978
epoch 035 | time 100.18s | train del 0.0223 | train add 0.0360 | train add prop 0.0000 | val del 0.0244 | val add 0.0376 | val add prop 0.0000 | del F1 0.9945 | add F1 0.9979
epoch 036 | time 95.52s | train del 0.0183 | train add 0.0398 | train add prop 0.0000 | val del 0.0253 | val add 0.0258 | val add prop 0.0000 | del F1 0.9909 | add F1 0.9980
epoch 037 | time 96.23s | train del 0.0141 | train add 0.0363 | train add prop 0.0001 | val del 0.0549 | val add 0.0270 | val add prop 0.0000 | del F1 0.9861 | add F1 0.9971
epoch 038 | time 111.96s | train del 0.0160 | train add 0.0358 | train add prop 0.0001 | val del 0.0532 | val add 0.0432 | val add prop 0.0001 | del F1 0.9910 | add F1 0.9979
epoch 039 | time 207.78s | train del 0.0137 | train add 0.0367 | train add prop 0.0001 | val del 0.0160 | val add 0.0253 | val add prop 0.0000 | del F1 0.9936 | add F1 0.9967
epoch 040 | time 206.99s | train del 0.0042 | train add 0.0387 | train add prop 0.0000 | val del 0.0245 | val add 0.0266 | val add prop 0.0000 | del F1 0.9910 | add F1 0.9980
epoch 041 | time 207.12s | train del 0.0062 | train add 0.0371 | train add prop 0.0001 | val del 0.0148 | val add 0.0268 | val add prop 0.0001 | del F1 0.9951 | add F1 0.9982
epoch 042 | time 205.73s | train del 0.0091 | train add 0.0347 | train add prop 0.0000 | val del 0.0245 | val add 0.0375 | val add prop 0.0002 | del F1 0.9917 | add F1 0.9975
epoch 043 | time 211.42s | train del 0.0064 | train add 0.0344 | train add prop 0.0001 | val del 0.0265 | val add 0.0243 | val add prop 0.0000 | del F1 0.9918 | add F1 0.9978
epoch 044 | time 172.68s | train del 0.0031 | train add 0.0372 | train add prop 0.0000 | val del 0.0433 | val add 0.0432 | val add prop 0.0001 | del F1 0.9853 | add F1 0.9979
epoch 045 | time 183.40s | train del 0.0052 | train add 0.0358 | train add prop 0.0001 | val del 0.0152 | val add 0.0259 | val add prop 0.0000 | del F1 0.9944 | add F1 0.9976
epoch 046 | time 193.27s | train del 0.0070 | train add 0.0359 | train add prop 0.0001 | val del 0.0400 | val add 0.0263 | val add prop 0.0000 | del F1 0.9868 | add F1 0.9977
epoch 047 | time 181.18s | train del 0.0040 | train add 0.0337 | train add prop 0.0000 | val del 0.0208 | val add 0.0226 | val add prop 0.0000 | del F1 0.9913 | add F1 0.9979
epoch 048 | time 187.94s | train del 0.0025 | train add 0.0334 | train add prop 0.0001 | val del 0.0058 | val add 0.0194 | val add prop 0.0000 | del F1 0.9979 | add F1 0.9978
epoch 049 | time 181.74s | train del 0.0021 | train add 0.0338 | train add prop 0.0001 | val del 0.0333 | val add 0.0359 | val add prop 0.0000 | del F1 0.9891 | add F1 0.9981
epoch 050 | time 185.10s | train del 0.0045 | train add 0.0346 | train add prop 0.0001 | val del 0.0772 | val add 0.0334 | val add prop 0.0000 | del F1 0.9754 | add F1 0.9979
saved plots/2ent_5rel.png
Working on 2ent_5rel_noise
device: cuda
dataset path: ..\data_exploration\synthetic_data\2ent_5rel_noise.json
num timesteps: 300
x_global shape: (400, 64)
num relations: 5
relations: {0: 'contact', 1: 'negotiate', 2: 'bonded', 3: 'strained', 4: 'recovery'}
example edge_index shape: (2, 863)
example edge_type shape: (863,)
example edge_relative_time shape: (863,)
train timesteps: 0 to 289
validation timesteps: 290 to 299
epoch 001 | time 196.21s | train del 0.6560 | train add 0.4833 | train add prop 0.0002 | val del 0.6486 | val add 0.3209 | val add prop 0.0002 | del F1 0.6042 | add F1 0.9806
epoch 002 | time 192.04s | train del 0.6367 | train add 0.2572 | train add prop 0.0002 | val del 0.6225 | val add 0.1587 | val add prop 0.0003 | del F1 0.6338 | add F1 0.9846
epoch 003 | time 196.65s | train del 0.6182 | train add 0.1793 | train add prop 0.0002 | val del 0.5873 | val add 0.1385 | val add prop 0.0002 | del F1 0.6586 | add F1 0.9840
epoch 004 | time 188.70s | train del 0.5739 | train add 0.1559 | train add prop 0.0002 | val del 0.5826 | val add 0.1117 | val add prop 0.0002 | del F1 0.6911 | add F1 0.9862
epoch 005 | time 184.52s | train del 0.5000 | train add 0.1259 | train add prop 0.0002 | val del 0.4774 | val add 0.1113 | val add prop 0.0002 | del F1 0.7305 | add F1 0.9865
epoch 006 | time 194.63s | train del 0.4642 | train add 0.1172 | train add prop 0.0002 | val del 0.4672 | val add 0.1149 | val add prop 0.0002 | del F1 0.7417 | add F1 0.9875
epoch 007 | time 191.38s | train del 0.4515 | train add 0.1161 | train add prop 0.0003 | val del 0.4566 | val add 0.0978 | val add prop 0.0003 | del F1 0.7517 | add F1 0.9872
epoch 008 | time 201.18s | train del 0.4453 | train add 0.1118 | train add prop 0.0002 | val del 0.4465 | val add 0.1077 | val add prop 0.0002 | del F1 0.7248 | add F1 0.9880
epoch 009 | time 195.08s | train del 0.4433 | train add 0.1101 | train add prop 0.0002 | val del 0.4439 | val add 0.1608 | val add prop 0.0002 | del F1 0.7377 | add F1 0.9881
epoch 010 | time 192.05s | train del 0.4417 | train add 0.1065 | train add prop 0.0002 | val del 0.4399 | val add 0.0959 | val add prop 0.0003 | del F1 0.7334 | add F1 0.9879
epoch 011 | time 183.29s | train del 0.4441 | train add 0.1038 | train add prop 0.0002 | val del 0.4229 | val add 0.1833 | val add prop 0.0002 | del F1 0.7461 | add F1 0.9881
epoch 012 | time 196.44s | train del 0.4336 | train add 0.1060 | train add prop 0.0002 | val del 0.4214 | val add 0.1027 | val add prop 0.0001 | del F1 0.7487 | add F1 0.9882
epoch 013 | time 198.94s | train del 0.4355 | train add 0.1049 | train add prop 0.0002 | val del 0.4327 | val add 0.1251 | val add prop 0.0002 | del F1 0.7483 | add F1 0.9880
epoch 014 | time 199.59s | train del 0.4319 | train add 0.1019 | train add prop 0.0002 | val del 0.4367 | val add 0.1059 | val add prop 0.0003 | del F1 0.7485 | add F1 0.9883
epoch 015 | time 205.21s | train del 0.4344 | train add 0.0971 | train add prop 0.0002 | val del 0.4344 | val add 0.1035 | val add prop 0.0003 | del F1 0.7341 | add F1 0.9877
epoch 016 | time 201.37s | train del 0.4385 | train add 0.0977 | train add prop 0.0002 | val del 0.4255 | val add 0.0845 | val add prop 0.0001 | del F1 0.7289 | add F1 0.9879
epoch 017 | time 204.11s | train del 0.4359 | train add 0.1012 | train add prop 0.0002 | val del 0.4274 | val add 0.0763 | val add prop 0.0002 | del F1 0.7353 | add F1 0.9883
epoch 018 | time 195.71s | train del 0.4325 | train add 0.0990 | train add prop 0.0002 | val del 0.4345 | val add 0.1244 | val add prop 0.0002 | del F1 0.7424 | add F1 0.9892
epoch 019 | time 199.55s | train del 0.4290 | train add 0.0931 | train add prop 0.0002 | val del 0.4323 | val add 0.0619 | val add prop 0.0003 | del F1 0.7519 | add F1 0.9884
epoch 020 | time 181.14s | train del 0.4310 | train add 0.0995 | train add prop 0.0003 | val del 0.4222 | val add 0.0922 | val add prop 0.0004 | del F1 0.7533 | add F1 0.9885
epoch 021 | time 171.90s | train del 0.4297 | train add 0.0955 | train add prop 0.0002 | val del 0.4311 | val add 0.0854 | val add prop 0.0001 | del F1 0.7539 | add F1 0.9885
epoch 022 | time 171.64s | train del 0.4262 | train add 0.0969 | train add prop 0.0002 | val del 0.4205 | val add 0.1027 | val add prop 0.0004 | del F1 0.7593 | add F1 0.9893
epoch 023 | time 159.14s | train del 0.4217 | train add 0.0949 | train add prop 0.0002 | val del 0.4206 | val add 0.0889 | val add prop 0.0003 | del F1 0.7643 | add F1 0.9890
epoch 024 | time 198.94s | train del 0.4069 | train add 0.0916 | train add prop 0.0002 | val del 0.4002 | val add 0.0996 | val add prop 0.0001 | del F1 0.7841 | add F1 0.9883
epoch 025 | time 197.26s | train del 0.4060 | train add 0.0925 | train add prop 0.0002 | val del 0.3827 | val add 0.1037 | val add prop 0.0001 | del F1 0.7999 | add F1 0.9892
epoch 026 | time 200.64s | train del 0.3805 | train add 0.0953 | train add prop 0.0002 | val del 0.3527 | val add 0.1041 | val add prop 0.0004 | del F1 0.8393 | add F1 0.9894
epoch 027 | time 194.45s | train del 0.3276 | train add 0.0929 | train add prop 0.0002 | val del 0.3099 | val add 0.1066 | val add prop 0.0003 | del F1 0.8661 | add F1 0.9888
epoch 028 | time 197.23s | train del 0.3022 | train add 0.0929 | train add prop 0.0002 | val del 0.2947 | val add 0.0776 | val add prop 0.0002 | del F1 0.8675 | add F1 0.9898
epoch 029 | time 199.36s | train del 0.2927 | train add 0.0905 | train add prop 0.0002 | val del 0.2876 | val add 0.1388 | val add prop 0.0001 | del F1 0.8699 | add F1 0.9890
epoch 030 | time 203.63s | train del 0.2896 | train add 0.0938 | train add prop 0.0002 | val del 0.2907 | val add 0.0663 | val add prop 0.0002 | del F1 0.8684 | add F1 0.9892
epoch 031 | time 197.55s | train del 0.2869 | train add 0.0937 | train add prop 0.0002 | val del 0.2882 | val add 0.1072 | val add prop 0.0001 | del F1 0.8692 | add F1 0.9893
epoch 032 | time 190.78s | train del 0.2900 | train add 0.0914 | train add prop 0.0002 | val del 0.2828 | val add 0.1012 | val add prop 0.0003 | del F1 0.8698 | add F1 0.9887
epoch 033 | time 203.11s | train del 0.2878 | train add 0.0924 | train add prop 0.0002 | val del 0.2821 | val add 0.0831 | val add prop 0.0001 | del F1 0.8694 | add F1 0.9886
epoch 034 | time 202.65s | train del 0.2838 | train add 0.0924 | train add prop 0.0002 | val del 0.2876 | val add 0.1051 | val add prop 0.0002 | del F1 0.8688 | add F1 0.9902
epoch 035 | time 193.62s | train del 0.2854 | train add 0.0889 | train add prop 0.0002 | val del 0.2862 | val add 0.0817 | val add prop 0.0003 | del F1 0.8697 | add F1 0.9886
epoch 036 | time 192.37s | train del 0.2855 | train add 0.0910 | train add prop 0.0002 | val del 0.2830 | val add 0.1156 | val add prop 0.0002 | del F1 0.8698 | add F1 0.9894
epoch 037 | time 196.57s | train del 0.2827 | train add 0.0901 | train add prop 0.0002 | val del 0.2984 | val add 0.0719 | val add prop 0.0001 | del F1 0.8686 | add F1 0.9894
epoch 038 | time 201.49s | train del 0.2887 | train add 0.0874 | train add prop 0.0002 | val del 0.2745 | val add 0.0974 | val add prop 0.0001 | del F1 0.8714 | add F1 0.9896
epoch 039 | time 197.24s | train del 0.2840 | train add 0.0908 | train add prop 0.0002 | val del 0.2868 | val add 0.0868 | val add prop 0.0002 | del F1 0.8710 | add F1 0.9892
epoch 040 | time 203.43s | train del 0.2835 | train add 0.0900 | train add prop 0.0002 | val del 0.2860 | val add 0.1058 | val add prop 0.0003 | del F1 0.8720 | add F1 0.9901
epoch 041 | time 182.11s | train del 0.2855 | train add 0.0900 | train add prop 0.0002 | val del 0.2868 | val add 0.0891 | val add prop 0.0003 | del F1 0.8702 | add F1 0.9897
epoch 042 | time 152.97s | train del 0.2847 | train add 0.0885 | train add prop 0.0002 | val del 0.2767 | val add 0.1030 | val add prop 0.0002 | del F1 0.8718 | add F1 0.9899
epoch 043 | time 118.14s | train del 0.2850 | train add 0.0892 | train add prop 0.0002 | val del 0.2741 | val add 0.0797 | val add prop 0.0002 | del F1 0.8712 | add F1 0.9896
epoch 044 | time 181.22s | train del 0.2813 | train add 0.0879 | train add prop 0.0002 | val del 0.2788 | val add 0.0937 | val add prop 0.0004 | del F1 0.8715 | add F1 0.9892
epoch 045 | time 261.26s | train del 0.2860 | train add 0.0885 | train add prop 0.0002 | val del 0.2815 | val add 0.1001 | val add prop 0.0001 | del F1 0.8708 | add F1 0.9897
epoch 046 | time 267.70s | train del 0.2819 | train add 0.0889 | train add prop 0.0002 | val del 0.2912 | val add 0.0993 | val add prop 0.0001 | del F1 0.8709 | add F1 0.9896
epoch 047 | time 263.37s | train del 0.2841 | train add 0.0914 | train add prop 0.0002 | val del 0.2797 | val add 0.1011 | val add prop 0.0002 | del F1 0.8717 | add F1 0.9894
epoch 048 | time 245.88s | train del 0.2824 | train add 0.0901 | train add prop 0.0002 | val del 0.2991 | val add 0.1215 | val add prop 0.0002 | del F1 0.8700 | add F1 0.9910
epoch 049 | time 73.78s | train del 0.2856 | train add 0.0885 | train add prop 0.0002 | val del 0.2795 | val add 0.0847 | val add prop 0.0004 | del F1 0.8720 | add F1 0.9900
epoch 050 | time 89.74s | train del 0.2814 | train add 0.0901 | train add prop 0.0002 | val del 0.2776 | val add 0.0973 | val add prop 0.0002 | del F1 0.8717 | add F1 0.9902
saved plots/2ent_5rel_noise.png


