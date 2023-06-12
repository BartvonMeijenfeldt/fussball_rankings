# Internal Fussball ratings at Transavia
## Ratings
1. Koen Offense: 1818.5 
2. Brian Defense: 1785.8 
3. Job V Defense: 1686.7 
4. Bart Defense: 1685.8 
5. Yashin Defense: 1682.2 
6. Yashin Average: 1679.8 
7. Yashin Offense: 1677.4 
8. Bart Average: 1676.8 
9. Liveris Defense: 1668.5 
10. Bart Offense: 1667.8 
11. Koen Average: 1666.4 
12. Brian Average: 1661.6 
13. Bas Defense: 1644.5 
14. Job Offense: 1640.3 
15. Tim Offense: 1625.1 
16. Martin Offense: 1624.4 
17. Job V Offense: 1611.5 
18. Liveris Average: 1610.2 
19. Timo Offense: 1603.4 
20. Bas Average: 1598.0 
21. Job Average: 1595.4 
22. Philip Offense: 1583.5 
23. Oliver Offense: 1580.8 
24. Tim Average: 1571.6 
25. Carl Defense: 1567.8 
26. Carl Average: 1563.3 
27. Philip  Defense: 1561.6 
28. Carl Offense: 1558.8 
29. Maarten Defense: 1554.2 
30. Oliver Average: 1554.2 
31. Liveris Offense: 1552.0 
32. Bas Offense: 1551.5 
33. Job Defense: 1550.4 
34. Brian Offense: 1537.3 
35. Floris Offense: 1531.9 
36. Oliver Defense: 1527.6 
37. Mohammed Defense: 1526.9 
38. Jane Defense: 1525.0 
39. Martin Average: 1523.2 
40. Timo Average: 1522.1 
41. Tim Defense: 1518.0 
42. Philip Average: 1514.8 
43. Koen Defense: 1514.4 
44. Luka Defense: 1513.7 
45. Thomas Offense: 1511.1 
46. Loek Defense: 1508.6 
47. Mohammed Average: 1503.8 
48. Frenk  Defense: 1503.3 
49. Thomas Average: 1501.8 
50. Job  Defense: 1496.7 
51. Loek Average: 1494.6 
52. Floris Average: 1494.2 
53. Thomas Defense: 1492.5 
54. Donnie Offense: 1491.7 
55. Rob Offense: 1490.0 
56. Irene Offense: 1481.4 
57. Mohammed Offense: 1480.8 
58. Loek Offense: 1480.7 
59. Daan Offense: 1477.7 
60. Anna Defense: 1475.7 
61. Kassandra Offense: 1473.3 
62. Lars Defense: 1470.1 
63. Anna Average: 1469.4 
64. Bruno Defense: 1468.1 
65. Jelle Offense: 1468.0 
66. Rob Average: 1467.4 
67. Anna Offense: 1463.2 
68. Bruno Average: 1462.3 
69. Donnie Average: 1462.2 
70. Irene Average: 1460.2 
71. Wouter Offense: 1457.3 
72. Arjen Offense: 1457.3 
73. Floris Defense: 1456.5 
74. Bruno Offense: 1456.5 
75. Maarten Average: 1454.3 
76. Philip Defense: 1446.2 
77. Daan Ri Defense: 1445.4 
78. Vincent Offense: 1445.2 
79. Rob Defense: 1444.7 
80. Katherine Defense: 1442.9 
81. Timo Defense: 1440.8 
82. Irene Defense: 1439.1 
83. Jay Offense: 1439.1 
84. Frenk Defense: 1434.7 
85. Donnie Defense: 1432.6 
86. Katherine Average: 1429.8 
87. Laura Defense: 1424.8 
88. Martin Defense: 1422.0 
89. Roy Defense: 1421.6 
90. Kristin Offense: 1418.2 
91. Kassandra Average: 1418.0 
92. Frenk Average: 1416.8 
93. Katherine Offense: 1416.7 
94. Daan Ri Offense: 1413.7 
95. Wouter Average: 1409.1 
96. Dennis Offense: 1400.9 
97. Frenk Offense: 1399.0 
98. Dennis Average: 1393.1 
99. Laura Average: 1392.7 
100. Kristin Average: 1390.3 
101. Dennis Defense: 1385.2 
102. Kassandra Defense: 1362.7 
103. Kristin Defense: 1362.4 
104. Wouter Defense: 1360.9 
105. Laura Offense: 1360.6 
106. Maarten Offense: 1354.4 
107. Michiel Defense: 1349.4 
108. Michiel Average: 1318.8 
109. Roy Average: 1316.2 
110. Michiel Offense: 1288.2 
111. Roy Offense: 1210.8 

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