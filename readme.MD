# Internal Fussball ratings at Transavia
## Ratings
1. Carl Offense: 1826.1 
2. Koen Offense: 1818.5 
3. Carl Average: 1747.9 
4. Bart Offense: 1705.4 
5. Bart Average: 1700.4 
6. Bart Defense: 1695.4 
7. Brian Offense: 1688.9 
8. Job V Defense: 1686.7 
9. Brian Average: 1684.0 
10. Yashin Defense: 1682.2 
11. Yashin Average: 1679.8 
12. Brian Defense: 1679.1 
13. Yashin Offense: 1677.4 
14. Liveris Defense: 1677.3 
15. Carl Defense: 1669.7 
16. Koen Average: 1666.4 
17. Bas Defense: 1653.1 
18. Liveris Average: 1648.7 
19. Tim Offense: 1625.1 
20. Liveris Offense: 1620.1 
21. Job V Offense: 1611.5 
22. Timo Offense: 1603.4 
23. Martin Offense: 1602.1 
24. Job Offense: 1597.1 
25. Loek Offense: 1593.5 
26. Philip Offense: 1583.5 
27. Oliver Offense: 1574.2 
28. Tim Average: 1571.6 
29. Bas Average: 1564.4 
30. Philip  Defense: 1561.6 
31. Oliver Average: 1550.9 
32. Loek Average: 1550.4 
33. Philip Average: 1540.0 
34. Job Average: 1536.6 
35. Floris Offense: 1531.9 
36. Martin Average: 1528.5 
37. Oliver Defense: 1527.6 
38. Mohammed Defense: 1526.9 
39. Jane Defense: 1525.0 
40. Timo Average: 1522.1 
41. Donnie Offense: 1518.2 
42. Tim Defense: 1518.0 
43. Donnie Average: 1517.4 
44. Donnie Defense: 1516.5 
45. Koen Defense: 1514.4 
46. Luka Defense: 1513.7 
47. Loek Defense: 1507.3 
48. Mohammed Average: 1503.8 
49. Frenk  Defense: 1503.3 
50. Job  Defense: 1496.7 
51. Philip Defense: 1496.4 
52. Floris Average: 1494.2 
53. Thomas Defense: 1492.5 
54. Thomas Average: 1482.3 
55. Irene Offense: 1481.4 
56. Mohammed Offense: 1480.8 
57. Maarten Defense: 1477.7 
58. Daan Offense: 1477.7 
59. Rob Offense: 1477.0 
60. Job Defense: 1476.0 
61. Bas Offense: 1475.6 
62. Katherine Defense: 1475.4 
63. Thomas Offense: 1472.1 
64. Lars Defense: 1470.1 
65. Roy Defense: 1470.0 
66. Bruno Defense: 1468.1 
67. Jelle Offense: 1468.0 
68. Rob Average: 1466.0 
69. Bruno Average: 1462.3 
70. Irene Average: 1460.2 
71. Arjen Offense: 1457.3 
72. Brenda Defense: 1456.6 
73. Floris Defense: 1456.5 
74. Bruno Offense: 1456.5 
75. Wouter Offense: 1456.4 
76. Rob Defense: 1455.1 
77. Martin Defense: 1454.9 
78. Dennis Defense: 1451.4 
79. Kassandra Defense: 1451.4 
80. Katherine Average: 1446.1 
81. Daan Ri Defense: 1445.4 
82. Vincent Offense: 1445.2 
83. Andreea Offense: 1443.6 
84. Timo Defense: 1440.8 
85. Irene Defense: 1439.1 
86. Jay Offense: 1439.1 
87. Kassandra Average: 1437.3 
88. Frenk Defense: 1434.7 
89. Kassandra Offense: 1423.2 
90. Frenk Average: 1416.8 
91. Katherine Offense: 1416.7 
92. Wouter Average: 1414.2 
93. Daan Ri Offense: 1413.7 
94. Kristin Offense: 1403.2 
95. Timo2 Offense: 1402.0 
96. Laura Offense: 1399.6 
97. Frenk Offense: 1399.0 
98. Michiel Defense: 1397.7 
99. Laura Average: 1396.8 
100. Maarten Average: 1396.4 
101. Dennis Average: 1395.3 
102. Laura Defense: 1394.0 
103. Boele Defense: 1393.1 
104. Boele Average: 1390.4 
105. Boele Offense: 1387.7 
106. Anna Offense: 1384.9 
107. Kristin Average: 1382.8 
108. Wouter Defense: 1372.0 
109. Kristin Defense: 1362.4 
110. Roy Average: 1356.1 
111. Anna Average: 1349.6 
112. Dennis Offense: 1339.2 
113. Michiel Average: 1331.8 
114. Maarten Offense: 1315.0 
115. Anna Defense: 1314.2 
116. Michiel Offense: 1266.0 
117. Roy Offense: 1242.2 

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