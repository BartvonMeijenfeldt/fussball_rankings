# Internal Fussball ratings at Transavia
## Ratings
1. Koen Offense: 1818.5 
2. Carl Offense: 1765.2 
3. Brian Defense: 1765.1 
4. Bart Offense: 1759.8 
5. Brian Average: 1752.4 
6. Brian Offense: 1739.6 
7. Bart Average: 1728.0 
8. Carl Average: 1707.2 
9. Bart Defense: 1696.1 
10. Job V Defense: 1686.7 
11. Yashin Defense: 1682.2 
12. Yashin Average: 1679.8 
13. Yashin Offense: 1677.4 
14. Liveris Defense: 1677.3 
15. Koen Average: 1666.4 
16. Bas Defense: 1653.1 
17. Carl Defense: 1649.1 
18. Liveris Average: 1648.7 
19. Loek Offense: 1626.6 
20. Tim Offense: 1625.1 
21. Liveris Offense: 1620.1 
22. Job V Offense: 1611.5 
23. Timo Offense: 1603.4 
24. Martin Offense: 1602.1 
25. Wouter Offense: 1592.6 
26. Philip Offense: 1583.5 
27. Loek Average: 1576.4 
28. Oliver Offense: 1574.2 
29. Tim Average: 1571.6 
30. Job Offense: 1564.5 
31. Bas Average: 1564.4 
32. Philip  Defense: 1561.6 
33. Job Average: 1561.6 
34. Job Defense: 1558.8 
35. Oliver Average: 1550.9 
36. Philip Average: 1540.0 
37. Floris Offense: 1531.9 
38. Martin Average: 1528.5 
39. Oliver Defense: 1527.6 
40. Mohammed Defense: 1526.9 
41. Loek Defense: 1526.2 
42. Jane Defense: 1525.0 
43. Timo Average: 1522.1 
44. Tim Defense: 1518.0 
45. Koen Defense: 1514.4 
46. Luka Defense: 1513.7 
47. Roy Defense: 1510.6 
48. Mohammed Average: 1503.8 
49. Frenk  Defense: 1503.3 
50. Katherine Defense: 1502.4 
51. Job  Defense: 1496.7 
52. Philip Defense: 1496.4 
53. Floris Average: 1494.2 
54. Thomas Defense: 1492.5 
55. Boele Defense: 1489.5 
56. Donnie Offense: 1487.1 
57. Thomas Average: 1482.3 
58. Irene Offense: 1481.4 
59. Mohammed Offense: 1480.8 
60. Wouter Average: 1480.6 
61. Maarten Defense: 1477.7 
62. Daan Offense: 1477.7 
63. Rob Offense: 1476.0 
64. Bas Offense: 1475.6 
65. Thomas Offense: 1472.1 
66. Lars Defense: 1470.1 
67. Bruno Defense: 1468.1 
68. Jelle Offense: 1468.0 
69. Rob Average: 1465.6 
70. Bruno Average: 1462.3 
71. Irene Average: 1460.2 
72. Donnie Average: 1457.5 
73. Arjen Offense: 1457.3 
74. Floris Defense: 1456.5 
75. Bruno Offense: 1456.5 
76. Rob Defense: 1455.1 
77. Martin Defense: 1454.9 
78. Dennis Defense: 1451.4 
79. Kassandra Defense: 1451.4 
80. Boele Average: 1448.3 
81. Daan Ri Defense: 1445.4 
82. Vincent Offense: 1445.2 
83. Andreea Offense: 1443.6 
84. Katherine Average: 1443.6 
85. Timo Defense: 1440.8 
86. Irene Defense: 1439.1 
87. Jay Offense: 1439.1 
88. Kassandra Average: 1437.3 
89. Frenk Defense: 1434.7 
90. Donnie Defense: 1427.9 
91. Laura Offense: 1427.8 
92. Brenda Offense: 1427.3 
93. Laura Average: 1426.2 
94. Laura Defense: 1424.5 
95. Kassandra Offense: 1423.2 
96. Frenk Average: 1416.8 
97. Daan Ri Offense: 1413.7 
98. Boele Offense: 1407.1 
99. Kristin Offense: 1403.2 
100. Frenk Offense: 1399.0 
101. Michiel Defense: 1397.7 
102. Maarten Average: 1396.4 
103. Brenda Average: 1395.6 
104. Dennis Average: 1395.3 
105. Anna Offense: 1384.9 
106. Katherine Offense: 1384.7 
107. Kristin Average: 1382.8 
108. Roy Average: 1376.4 
109. Wouter Defense: 1368.7 
110. Brenda Defense: 1363.9 
111. Kristin Defense: 1362.4 
112. Anna Average: 1349.6 
113. Dennis Offense: 1339.2 
114. Michiel Average: 1331.8 
115. Timo2 Defense: 1322.3 
116. Timo2 Average: 1316.3 
117. Maarten Offense: 1315.0 
118. Anna Defense: 1314.2 
119. Timo2 Offense: 1310.3 
120. Michiel Offense: 1266.0 
121. Roy Offense: 1242.2 

## Barto Rating
The Barto rating system extends the Elo rating system by taking the score into account. This results in more accurate estimation of strengths of players. Another interesting property is that if a heavy-favorite team or player plays against a weaker opponent, they are expected to score the majority of points. So if the favorite only wins a narrow victory the weaker team performed better than expected and will win rating and can therefore be seen as the winner. The ratings are based on the rating system named Barto which I developed during my Master's thesis which is included in pdf-form (see barto.pdf).
## Terminology
- G: a game between 2 opposing teams (possibly consisting out of 1 player each) which is composed of multiple contests.
- c: a contest (e.g. point in Fussball) modelled as a Bernoullia trial with the outcomes team A winning or team B.
- S: true level of a player with respect to winning a contest.
- mu: estimation of true level of a player. Also referred to as rating.
- sigma_s: std. dev. of estimation of true level.
- P: game performance.
- sigma_p: std. dev. of game performance.
- p_c: probability of winning a contest.
- B_p: scaling parameter. To decide what difference in ratings means what win percentage.
## Methodology
Every player has some rating mu both for offense and defense (initialized at 1500). These ratings are estimations of the player's true level, S, with uncertainy sigma_s. When a player plays a game, they will not always play on their true level but we assume them to have good games and bad games. We model this with their game performance, P, which is a normal distribution with mean S and sigma_p. Now if two teams A and B are to play the skill of each team will be the sum of the ratings of the players in the team (taking into account whether they are defense or offense). The difference of the ratings between the teams determine the chance, p_c, of each player to win a contest. The whole game is then a Binomial distribution with N_c: the number of contests to be played, p_c the probability of team A to win a point, and x the number of contests won by team A. Additional subscripts show whether the terms refer to team A or B
- S ~ N(mu, sigma_s)
- P ~ N(S, sigma_p)
- p_c = 1 / (1 + exp(P_B - P_A) / B_p)
- G ~ B(N_c, x, p_c)

Using Bayesian statistic we determine the priors and after each single game we calculate the posterior for each true level difference between the teams. The new rating difference is the true level difference for which the posterior probability is maximized. This difference will then be split equally equally between the player. 

E.g. Team A consists out of a player 1 with 1400 defense rating and player 2 with 1500 offense rating, while team B consists out of player 3 with 1500 defense rating and player 4 with offense 1600 rating. The difference between the teams is then -100, meaning team 2 is expected to score more points. Let's say team 1 plays better than expected the posterior difference might be 80 instead of 100. Then we will update the players in team A with +5 points and in team B with -5 points making the posterior ratings: player 1 1405, player 2 1505, player 3 1495 and player 4 1595.