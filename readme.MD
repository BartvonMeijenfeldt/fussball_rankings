# Internal Fussball ratings at Transavia
## Ratings
1. Koen Offense: 1818.5 
2. Brian Defense: 1756.0 
3. Brian Average: 1703.8 
4. Job V Defense: 1686.7 
5. Bas Defense: 1686.2 
6. Yashin Defense: 1682.2 
7. Yashin Average: 1679.8 
8. Yashin Offense: 1677.4 
9. Koen Average: 1666.4 
10. Bart Offense: 1662.3 
11. Bart Average: 1655.1 
12. Brian Offense: 1651.6 
13. Bart Defense: 1647.9 
14. Liveris Defense: 1644.5 
15. Job Offense: 1644.2 
16. Tim Offense: 1625.1 
17. Martin Offense: 1624.4 
18. Bas Average: 1614.4 
19. Job V Offense: 1611.5 
20. Carl Offense: 1610.0 
21. Timo Offense: 1603.4 
22. Carl Average: 1603.0 
23. Liveris Average: 1600.6 
24. Job Average: 1599.6 
25. Carl Defense: 1596.1 
26. Philip Offense: 1583.5 
27. Oliver Offense: 1580.8 
28. Tim Average: 1571.6 
29. Donnie Defense: 1569.9 
30. Philip  Defense: 1561.6 
31. Liveris Offense: 1556.8 
32. Job Defense: 1555.0 
33. Maarten Defense: 1554.2 
34. Oliver Average: 1554.2 
35. Loek Offense: 1548.1 
36. Bas Offense: 1542.5 
37. Philip Average: 1540.0 
38. Floris Offense: 1531.9 
39. Loek Average: 1529.2 
40. Oliver Defense: 1527.6 
41. Mohammed Defense: 1526.9 
42. Jane Defense: 1525.0 
43. Martin Average: 1523.2 
44. Timo Average: 1522.1 
45. Donnie Average: 1520.6 
46. Tim Defense: 1518.0 
47. Koen Defense: 1514.4 
48. Luka Defense: 1513.7 
49. Thomas Offense: 1511.1 
50. Loek Defense: 1510.2 
51. Mohammed Average: 1503.8 
52. Frenk  Defense: 1503.3 
53. Thomas Average: 1501.8 
54. Job  Defense: 1496.7 
55. Philip Defense: 1496.4 
56. Floris Average: 1494.2 
57. Thomas Defense: 1492.5 
58. Andreea Offense: 1489.8 
59. Irene Offense: 1481.4 
60. Mohammed Offense: 1480.8 
61. Daan Offense: 1477.7 
62. Donnie Offense: 1471.4 
63. Lars Defense: 1470.1 
64. Kassandra Offense: 1468.4 
65. Bruno Defense: 1468.1 
66. Jelle Offense: 1468.0 
67. Bruno Average: 1462.3 
68. Irene Average: 1460.2 
69. Arjen Offense: 1457.3 
70. Floris Defense: 1456.5 
71. Bruno Offense: 1456.5 
72. Wouter Offense: 1454.1 
73. Boele Offense: 1448.3 
74. Daan Ri Defense: 1445.4 
75. Vincent Offense: 1445.2 
76. Timo Defense: 1440.8 
77. Irene Defense: 1439.1 
78. Jay Offense: 1439.1 
79. Anna Offense: 1436.6 
80. Frenk Defense: 1434.7 
81. Maarten Average: 1434.6 
82. Dennis Defense: 1433.3 
83. Rob Defense: 1432.9 
84. Roy Defense: 1425.9 
85. Rob Average: 1423.9 
86. Kristin Offense: 1422.5 
87. Martin Defense: 1422.0 
88. Dennis Average: 1417.1 
89. Frenk Average: 1416.8 
90. Katherine Offense: 1416.7 
91. Rob Offense: 1414.9 
92. Daan Ri Offense: 1413.7 
93. Wouter Average: 1412.9 
94. Katherine Average: 1411.1 
95. Katherine Defense: 1405.5 
96. Anna Average: 1404.9 
97. Dennis Offense: 1400.9 
98. Frenk Offense: 1399.0 
99. Laura Defense: 1393.9 
100. Kristin Average: 1392.4 
101. Kassandra Average: 1389.2 
102. Laura Average: 1377.2 
103. Anna Defense: 1373.3 
104. Wouter Defense: 1371.7 
105. Kristin Defense: 1362.4 
106. Laura Offense: 1360.6 
107. Michiel Defense: 1349.4 
108. Michiel Average: 1318.8 
109. Roy Average: 1318.4 
110. Maarten Offense: 1315.0 
111. Kassandra Defense: 1310.0 
112. Michiel Offense: 1288.2 
113. Roy Offense: 1210.8 

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