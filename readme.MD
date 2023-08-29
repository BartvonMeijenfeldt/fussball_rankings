# Internal Fussball ratings at Transavia
## Ratings
1. Carl Offense: 1819.9 
2. Koen Offense: 1818.5 
3. Brian Defense: 1754.6 
4. Carl Average: 1723.6 
5. Brian Average: 1721.8 
6. Bart Defense: 1701.6 
7. Brian Offense: 1688.9 
8. Job V Defense: 1686.7 
9. Yashin Defense: 1682.2 
10. Yashin Average: 1679.8 
11. Yashin Offense: 1677.4 
12. Liveris Defense: 1677.3 
13. Koen Average: 1666.4 
14. Bart Average: 1656.2 
15. Bas Defense: 1653.1 
16. Liveris Average: 1648.7 
17. Job Offense: 1632.3 
18. Carl Defense: 1627.4 
19. Tim Offense: 1625.1 
20. Liveris Offense: 1620.1 
21. Job V Offense: 1611.5 
22. Bart Offense: 1610.7 
23. Timo Offense: 1603.4 
24. Martin Offense: 1602.1 
25. Loek Offense: 1593.1 
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
37. Martin Average: 1528.5 
38. Oliver Defense: 1527.6 
39. Mohammed Defense: 1526.9 
40. Jane Defense: 1525.0 
41. Donnie Defense: 1523.1 
42. Timo Average: 1522.1 
43. Donnie Average: 1520.6 
44. Donnie Offense: 1518.2 
45. Tim Defense: 1518.0 
46. Koen Defense: 1514.4 
47. Luka Defense: 1513.7 
48. Loek Defense: 1507.3 
49. Mohammed Average: 1503.8 
50. Frenk  Defense: 1503.3 
51. Job  Defense: 1496.7 
52. Philip Defense: 1496.4 
53. Floris Average: 1494.2 
54. Thomas Defense: 1492.5 
55. Thomas Average: 1482.3 
56. Irene Offense: 1481.4 
57. Mohammed Offense: 1480.8 
58. Daan Offense: 1477.7 
59. Rob Offense: 1477.0 
60. Job Defense: 1476.0 
61. Bas Offense: 1475.6 
62. Thomas Offense: 1472.1 
63. Lars Defense: 1470.1 
64. Roy Defense: 1470.0 
65. Bruno Defense: 1468.1 
66. Jelle Offense: 1468.0 
67. Bruno Average: 1462.3 
68. Irene Average: 1460.2 
69. Arjen Offense: 1457.3 
70. Brenda Defense: 1456.6 
71. Floris Defense: 1456.5 
72. Bruno Offense: 1456.5 
73. Martin Defense: 1454.9 
74. Katherine Defense: 1452.9 
75. Dennis Defense: 1451.4 
76. Kassandra Defense: 1451.4 
77. Rob Average: 1446.6 
78. Daan Ri Defense: 1445.4 
79. Vincent Offense: 1445.2 
80. Andreea Offense: 1443.6 
81. Timo Defense: 1440.8 
82. Irene Defense: 1439.1 
83. Jay Offense: 1439.1 
84. Kassandra Average: 1437.3 
85. Katherine Average: 1434.8 
86. Frenk Defense: 1434.7 
87. Maarten Average: 1425.2 
88. Anna Offense: 1423.9 
89. Kassandra Offense: 1423.2 
90. Frenk Average: 1416.8 
91. Katherine Offense: 1416.7 
92. Rob Defense: 1416.1 
93. Daan Ri Offense: 1413.7 
94. Kristin Offense: 1403.2 
95. Laura Offense: 1399.6 
96. Frenk Offense: 1399.0 
97. Laura Average: 1396.8 
98. Dennis Average: 1395.3 
99. Laura Defense: 1394.0 
100. Boele Defense: 1390.7 
101. Boele Average: 1389.2 
102. Boele Offense: 1387.7 
103. Kristin Average: 1382.8 
104. Wouter Offense: 1378.9 
105. Wouter Average: 1375.4 
106. Wouter Defense: 1372.0 
107. Anna Average: 1365.8 
108. Michiel Defense: 1364.5 
109. Kristin Defense: 1362.4 
110. Roy Average: 1356.1 
111. Dennis Offense: 1339.2 
112. Michiel Average: 1315.2 
113. Maarten Offense: 1315.0 
114. Anna Defense: 1307.6 
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