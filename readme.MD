# Internal Fussball ratings at Transavia
## Ratings
1. Koen Offense: 1818.5 
2. Liveris Defense: 1738.8 
3. Bart Defense: 1709.7 
4. Yashin Defense: 1708.9 
5. Liveris Average: 1690.6 
6. Job V Defense: 1686.7 
7. Bart Average: 1685.4 
8. Yashin Average: 1677.0 
9. Koen Average: 1666.4 
10. Bas Defense: 1663.4 
11. Bart Offense: 1661.1 
12. Yashin Offense: 1645.0 
13. Liveris Offense: 1642.4 
14. Bas Average: 1624.8 
15. Philip Offense: 1624.7 
16. Job V Offense: 1611.5 
17. Timo Offense: 1603.4 
18. Tim Offense: 1590.3 
19. Bas Offense: 1586.1 
20. Brian Defense: 1585.0 
21. Job Offense: 1583.6 
22. Oliver Offense: 1580.8 
23. Carl Offense: 1561.8 
24. Philip  Defense: 1561.6 
25. Philip Average: 1554.8 
26. Tim Average: 1554.2 
27. Oliver Average: 1554.2 
28. Maarten Defense: 1551.3 
29. Brian Average: 1551.2 
30. Martin Offense: 1549.3 
31. Loek Defense: 1546.5 
32. Floris Offense: 1531.9 
33. Oliver Defense: 1527.6 
34. Carl Average: 1527.2 
35. Mohammed Defense: 1526.9 
36. Jane Defense: 1525.0 
37. Timo Average: 1522.1 
38. Tim Defense: 1518.0 
39. Brian Offense: 1517.4 
40. Koen Defense: 1514.4 
41. Luka Defense: 1513.7 
42. Loek Average: 1513.6 
43. Thomas Offense: 1511.1 
44. Mohammed Average: 1503.8 
45. Frenk  Defense: 1503.3 
46. Thomas Average: 1501.8 
47. Job Average: 1499.4 
48. Job  Defense: 1496.7 
49. Floris Average: 1494.2 
50. Carl Defense: 1492.5 
51. Thomas Defense: 1492.5 
52. Roy Defense: 1490.7 
53. Rob Offense: 1490.0 
54. Philip Defense: 1484.9 
55. Irene Offense: 1481.4 
56. Mohammed Offense: 1480.8 
57. Loek Offense: 1480.7 
58. Daan Offense: 1477.7 
59. Wouter Offense: 1477.1 
60. Martin Average: 1475.2 
61. Rob Average: 1473.8 
62. Lars Defense: 1470.1 
63. Bruno Defense: 1468.1 
64. Jelle Offense: 1468.0 
65. Donnie Defense: 1467.1 
66. Dennis Defense: 1464.9 
67. Maarten Average: 1464.2 
68. Katherine Offense: 1463.6 
69. Bruno Average: 1462.3 
70. Laura Defense: 1461.6 
71. Irene Average: 1460.2 
72. Rob Defense: 1457.7 
73. Arjen Offense: 1457.3 
74. Floris Defense: 1456.5 
75. Bruno Offense: 1456.5 
76. Katherine Average: 1453.2 
77. Daan Ri Defense: 1445.4 
78. Vincent Offense: 1445.2 
79. Katherine Defense: 1442.9 
80. Timo Defense: 1440.8 
81. Irene Defense: 1439.1 
82. Jay Offense: 1439.1 
83. Kassandra Offense: 1436.1 
84. Frenk Defense: 1434.7 
85. Dennis Average: 1432.9 
86. Donnie Average: 1424.6 
87. Kristin Offense: 1424.3 
88. Kristin Average: 1422.4 
89. Kristin Defense: 1420.4 
90. Frenk Average: 1416.8 
91. Job Defense: 1415.1 
92. Daan Ri Offense: 1413.7 
93. Kassandra Average: 1413.6 
94. Laura Average: 1411.8 
95. Martin Defense: 1401.2 
96. Dennis Offense: 1400.9 
97. Frenk Offense: 1399.0 
98. Kassandra Defense: 1391.2 
99. Roy Average: 1385.4 
100. Donnie Offense: 1382.2 
101. Maarten Offense: 1377.1 
102. Laura Offense: 1362.1 
103. Wouter Average: 1356.4 
104. Michiel Defense: 1349.4 
105. Michiel Average: 1318.8 
106. Michiel Offense: 1288.2 
107. Roy Offense: 1280.1 
108. Wouter Defense: 1235.7 

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