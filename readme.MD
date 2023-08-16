# Internal Fussball ratings at Transavia
## Ratings
1. Koen Offense: 1818.5 
2. Brian Defense: 1754.6 
3. Carl Offense: 1752.4 
4. Brian Average: 1739.0 
5. Brian Offense: 1723.4 
6. Carl Average: 1692.9 
7. Job V Defense: 1686.7 
8. Yashin Defense: 1682.2 
9. Bart Defense: 1680.4 
10. Yashin Average: 1679.8 
11. Yashin Offense: 1677.4 
12. Koen Average: 1666.4 
13. Bas Defense: 1653.1 
14. Bart Average: 1651.1 
15. Liveris Defense: 1644.4 
16. Carl Defense: 1633.4 
17. Job Offense: 1632.3 
18. Tim Offense: 1625.1 
19. Bart Offense: 1621.8 
20. Liveris Average: 1617.8 
21. Job V Offense: 1611.5 
22. Timo Offense: 1603.4 
23. Martin Offense: 1602.1 
24. Loek Offense: 1593.1 
25. Liveris Offense: 1591.2 
26. Philip Offense: 1583.5 
27. Oliver Offense: 1580.8 
28. Tim Average: 1571.6 
29. Bas Average: 1564.4 
30. Philip  Defense: 1561.6 
31. Oliver Average: 1554.2 
32. Job Average: 1554.2 
33. Loek Average: 1550.2 
34. Philip Average: 1540.0 
35. Maarten Defense: 1535.4 
36. Floris Offense: 1531.9 
37. Roy Defense: 1531.8 
38. Martin Average: 1528.5 
39. Oliver Defense: 1527.6 
40. Donnie Offense: 1527.2 
41. Mohammed Defense: 1526.9 
42. Jane Defense: 1525.0 
43. Timo Average: 1522.1 
44. Tim Defense: 1518.0 
45. Koen Defense: 1514.4 
46. Luka Defense: 1513.7 
47. Donnie Average: 1512.0 
48. Loek Defense: 1507.3 
49. Mohammed Average: 1503.8 
50. Frenk  Defense: 1503.3 
51. Donnie Defense: 1496.7 
52. Job  Defense: 1496.7 
53. Philip Defense: 1496.4 
54. Floris Average: 1494.2 
55. Thomas Defense: 1492.5 
56. Thomas Average: 1482.3 
57. Irene Offense: 1481.4 
58. Mohammed Offense: 1480.8 
59. Daan Offense: 1477.7 
60. Rob Offense: 1477.0 
61. Job Defense: 1476.0 
62. Bas Offense: 1475.6 
63. Thomas Offense: 1472.1 
64. Lars Defense: 1470.1 
65. Bruno Defense: 1468.1 
66. Jelle Offense: 1468.0 
67. Boele Defense: 1464.9 
68. Bruno Average: 1462.3 
69. Irene Average: 1460.2 
70. Arjen Offense: 1457.3 
71. Brenda Defense: 1456.6 
72. Floris Defense: 1456.5 
73. Bruno Offense: 1456.5 
74. Martin Defense: 1454.9 
75. Katherine Defense: 1452.9 
76. Kassandra Defense: 1451.4 
77. Rob Average: 1446.6 
78. Daan Ri Defense: 1445.4 
79. Vincent Offense: 1445.2 
80. Andreea Offense: 1443.6 
81. Timo Defense: 1440.8 
82. Boele Average: 1439.5 
83. Irene Defense: 1439.1 
84. Jay Offense: 1439.1 
85. Katherine Average: 1434.8 
86. Frenk Defense: 1434.7 
87. Maarten Average: 1425.2 
88. Wouter Offense: 1424.5 
89. Anna Offense: 1423.9 
90. Kassandra Average: 1422.2 
91. Frenk Average: 1416.8 
92. Katherine Offense: 1416.7 
93. Rob Defense: 1416.1 
94. Boele Offense: 1414.1 
95. Daan Ri Offense: 1413.7 
96. Kristin Offense: 1403.2 
97. Laura Offense: 1399.6 
98. Frenk Offense: 1399.0 
99. Wouter Average: 1398.2 
100. Laura Average: 1396.8 
101. Laura Defense: 1394.0 
102. Kassandra Offense: 1393.0 
103. Roy Average: 1387.0 
104. Kristin Average: 1382.8 
105. Anna Average: 1374.9 
106. Wouter Defense: 1372.0 
107. Dennis Defense: 1371.6 
108. Michiel Defense: 1364.5 
109. Kristin Defense: 1362.4 
110. Dennis Average: 1355.4 
111. Dennis Offense: 1339.2 
112. Anna Defense: 1325.9 
113. Michiel Average: 1315.2 
114. Maarten Offense: 1315.0 
115. Michiel Offense: 1266.0 
116. Roy Offense: 1242.2 

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