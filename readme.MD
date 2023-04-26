# Internal Fussball ratings at Transavia
## Ratings
1. Koen Offense: 1818.5 
2. Bart Defense: 1726.6 
3. Liveris Defense: 1698.6 
4. Yashin Offense: 1694.5 
5. Liveris Average: 1687.6 
6. Job V Defense: 1686.7 
7. Yashin Average: 1686.0 
8. Yashin Defense: 1677.5 
9. Liveris Offense: 1676.6 
10. Bas Defense: 1674.7 
11. Koen Average: 1666.4 
12. Bart Average: 1643.8 
13. Philip Offense: 1624.7 
14. Job V Offense: 1611.5 
15. Timo Offense: 1603.4 
16. Martin Offense: 1602.6 
17. Tim Offense: 1590.3 
18. Bas Average: 1585.7 
19. Oliver Offense: 1580.8 
20. Philip  Defense: 1561.6 
21. Bart Offense: 1561.0 
22. Job Offense: 1557.8 
23. Wouter Offense: 1556.7 
24. Philip Average: 1554.8 
25. Oliver Average: 1554.2 
26. Tim Average: 1554.2 
27. Maarten Defense: 1551.3 
28. Loek Defense: 1546.5 
29. Carl Offense: 1543.2 
30. Brian Defense: 1542.9 
31. Floris Offense: 1531.9 
32. Brian Average: 1530.2 
33. Oliver Defense: 1527.6 
34. Mohammed Defense: 1526.9 
35. Jane Defense: 1525.0 
36. Carl Average: 1522.2 
37. Timo Average: 1522.1 
38. Job Average: 1521.2 
39. Tim Defense: 1518.0 
40. Brian Offense: 1517.4 
41. Koen Defense: 1514.4 
42. Luka Defense: 1513.7 
43. Loek Average: 1513.6 
44. Thomas Offense: 1511.1 
45. Mohammed Average: 1503.8 
46. Frenk  Defense: 1503.3 
47. Martin Average: 1501.9 
48. Thomas Average: 1501.8 
49. Carl Defense: 1501.3 
50. Bas Offense: 1496.7 
51. Job  Defense: 1496.7 
52. Floris Average: 1494.2 
53. Thomas Defense: 1492.5 
54. Philip Defense: 1484.9 
55. Job Defense: 1484.5 
56. Irene Offense: 1481.4 
57. Mohammed Offense: 1480.8 
58. Loek Offense: 1480.7 
59. Daan Offense: 1477.7 
60. Donnie Defense: 1475.4 
61. Roy Defense: 1473.2 
62. Lars Defense: 1470.1 
63. Bruno Defense: 1468.1 
64. Jelle Offense: 1468.0 
65. Maarten Average: 1464.2 
66. Katherine Offense: 1463.6 
67. Bruno Average: 1462.3 
68. Irene Average: 1460.2 
69. Arjen Offense: 1457.3 
70. Floris Defense: 1456.5 
71. Bruno Offense: 1456.5 
72. Katherine Average: 1453.2 
73. Daan Ri Defense: 1445.4 
74. Vincent Offense: 1445.2 
75. Katherine Defense: 1442.9 
76. Timo Defense: 1440.8 
77. Irene Defense: 1439.1 
78. Jay Offense: 1439.1 
79. Kassandra Offense: 1436.1 
80. Frenk Defense: 1434.7 
81. Donnie Average: 1430.6 
82. Kassandra Average: 1423.9 
83. Frenk Average: 1416.8 
84. Kristin Offense: 1415.5 
85. Daan Ri Offense: 1413.7 
86. Kassandra Defense: 1411.7 
87. Roy Average: 1403.9 
88. Martin Defense: 1401.2 
89. Dennis Offense: 1400.9 
90. Frenk Offense: 1399.0 
91. Wouter Average: 1396.2 
92. Donnie Offense: 1385.9 
93. Maarten Offense: 1377.1 
94. Dennis Average: 1350.8 
95. Michiel Defense: 1349.4 
96. Roy Offense: 1334.6 
97. Laura Offense: 1320.0 
98. Michiel Average: 1318.8 
99. Dennis Defense: 1300.6 
100. Michiel Offense: 1288.2 
101. Wouter Defense: 1235.7 

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