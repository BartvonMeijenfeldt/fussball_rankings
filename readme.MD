# Internal Fussball ratings at Transavia
## Ratings
1. Carl Offense: 1868.0 
2. Bart Offense: 1847.4 
3. Koen Offense: 1818.5 
4. Brian Offense: 1792.1 
5. Brian Average: 1777.8 
6. Carl Average: 1763.6 
7. Brian Defense: 1763.5 
8. Bart Average: 1760.4 
9. Liveris Defense: 1698.6 
10. Yashin Offense: 1691.8 
11. Yashin Average: 1690.7 
12. Yashin Defense: 1689.6 
13. Job V Defense: 1686.7 
14. Bart Defense: 1673.4 
15. Koen Average: 1666.4 
16. Liveris Average: 1659.4 
17. Carl Defense: 1659.2 
18. Loek Defense: 1656.4 
19. Bas Defense: 1653.1 
20. Tim Offense: 1625.1 
21. Liveris Offense: 1620.1 
22. Job V Offense: 1611.5 
23. Loek Average: 1608.1 
24. Timo Offense: 1603.4 
25. Martin Offense: 1602.1 
26. Job Defense: 1592.6 
27. Philip Offense: 1583.5 
28. Wouter Offense: 1581.8 
29. Oliver Offense: 1574.2 
30. Tim Average: 1571.6 
31. Bas Average: 1564.4 
32. Philip  Defense: 1561.6 
33. Loek Offense: 1559.8 
34. Oliver Average: 1550.9 
35. Boele Defense: 1547.6 
36. Job Average: 1547.3 
37. Philip Average: 1540.0 
38. Donnie Offense: 1538.5 
39. Floris Offense: 1531.9 
40. Martin Average: 1528.5 
41. Oliver Defense: 1527.6 
42. Mohammed Defense: 1526.9 
43. Jane Defense: 1525.0 
44. Timo Average: 1522.1 
45. Tim Defense: 1518.0 
46. Koen Defense: 1514.4 
47. Luka Defense: 1513.7 
48. Wouter Average: 1505.0 
49. Mohammed Average: 1503.8 
50. Frenk  Defense: 1503.3 
51. Job Offense: 1502.0 
52. Job  Defense: 1496.7 
53. Philip Defense: 1496.4 
54. Floris Average: 1494.2 
55. Thomas Defense: 1492.5 
56. Andreea Offense: 1488.3 
57. Kassandra Offense: 1484.9 
58. Katherine Defense: 1482.6 
59. Ivar Defense: 1482.5 
60. Thomas Average: 1482.3 
61. Irene Offense: 1481.4 
62. Mohammed Offense: 1480.8 
63. Maarten Defense: 1477.7 
64. Daan Offense: 1477.7 
65. Bas Offense: 1475.6 
66. Boele Average: 1473.6 
67. Thomas Offense: 1472.1 
68. Lars Defense: 1470.1 
69. Bruno Defense: 1468.1 
70. Jelle Offense: 1468.0 
71. Kassandra Average: 1464.4 
72. Bruno Average: 1462.3 
73. Irene Average: 1460.2 
74. Arjen Offense: 1457.3 
75. Floris Defense: 1456.5 
76. Bruno Offense: 1456.5 
77. Donnie Average: 1455.1 
78. Martin Defense: 1454.9 
79. Dennis Defense: 1451.4 
80. Ivar Average: 1449.4 
81. Daan Ri Defense: 1445.4 
82. Vincent Offense: 1445.2 
83. Kassandra Defense: 1444.0 
84. Roy Defense: 1443.7 
85. Timo Defense: 1440.8 
86. Irene Defense: 1439.1 
87. Jay Offense: 1439.1 
88. Frenk Defense: 1434.7 
89. Timo2 Offense: 1431.7 
90. Katherine Average: 1428.8 
91. Wouter Defense: 1428.3 
92. Frenk Average: 1416.8 
93. Ivar Offense: 1416.2 
94. Daan Ri Offense: 1413.7 
95. Kristin Offense: 1403.2 
96. Boele Offense: 1399.7 
97. Frenk Offense: 1399.0 
98. Michiel Defense: 1397.7 
99. Maarten Average: 1396.4 
100. Dennis Average: 1395.3 
101. Rob Offense: 1393.8 
102. Timo2 Average: 1389.7 
103. Rob Average: 1387.0 
104. Kristin Average: 1382.8 
105. Rob Defense: 1380.2 
106. Katherine Offense: 1375.0 
107. Donnie Defense: 1371.7 
108. Anna Offense: 1370.6 
109. Anna Average: 1367.8 
110. Anna Defense: 1365.1 
111. Kristin Defense: 1362.4 
112. Laura Defense: 1349.1 
113. Timo2 Defense: 1347.7 
114. Laura Average: 1344.6 
115. Roy Average: 1343.0 
116. Laura Offense: 1340.2 
117. Dennis Offense: 1339.2 
118. Michiel Average: 1331.8 
119. Brenda Offense: 1315.9 
120. Maarten Offense: 1315.0 
121. Brenda Average: 1312.7 
122. Brenda Defense: 1309.5 
123. Michiel Offense: 1266.0 
124. Roy Offense: 1242.2 

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