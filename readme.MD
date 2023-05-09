# Internal Fussball ratings at Transavia
## Ratings
1. Koen Offense: 1818.5 
2. Liveris Defense: 1738.8 
3. Bart Defense: 1709.7 
4. Yashin Defense: 1708.9 
5. Liveris Average: 1690.6 
6. Job V Defense: 1686.7 
7. Yashin Average: 1677.0 
8. Koen Average: 1666.4 
9. Bas Defense: 1663.4 
10. Bart Average: 1645.6 
11. Yashin Offense: 1645.0 
12. Liveris Offense: 1642.4 
13. Bas Average: 1624.8 
14. Philip Offense: 1624.7 
15. Job V Offense: 1611.5 
16. Timo Offense: 1603.4 
17. Tim Offense: 1590.3 
18. Bas Offense: 1586.1 
19. Brian Defense: 1585.0 
20. Job Offense: 1583.6 
21. Bart Offense: 1581.5 
22. Oliver Offense: 1580.8 
23. Carl Offense: 1561.8 
24. Philip  Defense: 1561.6 
25. Wouter Offense: 1556.7 
26. Philip Average: 1554.8 
27. Oliver Average: 1554.2 
28. Tim Average: 1554.2 
29. Maarten Defense: 1551.3 
30. Brian Average: 1551.2 
31. Martin Offense: 1549.3 
32. Loek Defense: 1546.5 
33. Floris Offense: 1531.9 
34. Oliver Defense: 1527.6 
35. Carl Average: 1527.2 
36. Mohammed Defense: 1526.9 
37. Jane Defense: 1525.0 
38. Timo Average: 1522.1 
39. Tim Defense: 1518.0 
40. Brian Offense: 1517.4 
41. Koen Defense: 1514.4 
42. Luka Defense: 1513.7 
43. Loek Average: 1513.6 
44. Thomas Offense: 1511.1 
45. Mohammed Average: 1503.8 
46. Frenk  Defense: 1503.3 
47. Thomas Average: 1501.8 
48. Job Average: 1499.4 
49. Job  Defense: 1496.7 
50. Floris Average: 1494.2 
51. Carl Defense: 1492.5 
52. Thomas Defense: 1492.5 
53. Roy Defense: 1490.7 
54. Rob Offense: 1490.0 
55. Philip Defense: 1484.9 
56. Irene Offense: 1481.4 
57. Mohammed Offense: 1480.8 
58. Loek Offense: 1480.7 
59. Daan Offense: 1477.7 
60. Martin Average: 1475.2 
61. Rob Average: 1473.8 
62. Lars Defense: 1470.1 
63. Bruno Defense: 1468.1 
64. Jelle Offense: 1468.0 
65. Donnie Defense: 1467.1 
66. Maarten Average: 1464.2 
67. Katherine Offense: 1463.6 
68. Bruno Average: 1462.3 
69. Laura Defense: 1461.6 
70. Irene Average: 1460.2 
71. Rob Defense: 1457.7 
72. Arjen Offense: 1457.3 
73. Floris Defense: 1456.5 
74. Bruno Offense: 1456.5 
75. Katherine Average: 1453.2 
76. Daan Ri Defense: 1445.4 
77. Vincent Offense: 1445.2 
78. Katherine Defense: 1442.9 
79. Timo Defense: 1440.8 
80. Irene Defense: 1439.1 
81. Jay Offense: 1439.1 
82. Kassandra Offense: 1436.1 
83. Frenk Defense: 1434.7 
84. Donnie Average: 1424.6 
85. Kristin Offense: 1424.3 
86. Frenk Average: 1416.8 
87. Job Defense: 1415.1 
88. Daan Ri Offense: 1413.7 
89. Kassandra Average: 1413.6 
90. Laura Average: 1411.8 
91. Martin Defense: 1401.2 
92. Dennis Offense: 1400.9 
93. Frenk Offense: 1399.0 
94. Wouter Average: 1396.2 
95. Dennis Average: 1393.1 
96. Kassandra Defense: 1391.2 
97. Roy Average: 1385.4 
98. Dennis Defense: 1385.3 
99. Donnie Offense: 1382.2 
100. Maarten Offense: 1377.1 
101. Laura Offense: 1362.1 
102. Michiel Defense: 1349.4 
103. Michiel Average: 1318.8 
104. Michiel Offense: 1288.2 
105. Roy Offense: 1280.1 
106. Wouter Defense: 1235.7 

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