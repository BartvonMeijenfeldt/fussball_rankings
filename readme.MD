# Internal Fussball ratings at Transavia
## Ratings
1. Koen Offense: 1818.5 
2. Bart Defense: 1726.6 
3. Yashin Offense: 1711.0 
4. Yashin Average: 1709.2 
5. Yashin Defense: 1707.4 
6. Job V Defense: 1686.7 
7. Liveris Offense: 1683.1 
8. Koen Average: 1666.4 
9. Bas Defense: 1661.5 
10. Liveris Average: 1660.6 
11. Bart Average: 1643.8 
12. Liveris Defense: 1638.2 
13. Philip Offense: 1624.7 
14. Job V Offense: 1611.5 
15. Timo Offense: 1603.4 
16. Tim Offense: 1590.3 
17. Oliver Offense: 1580.8 
18. Bas Average: 1579.1 
19. Philip  Defense: 1561.6 
20. Bart Offense: 1561.0 
21. Job Offense: 1557.8 
22. Philip Average: 1554.8 
23. Oliver Average: 1554.2 
24. Tim Average: 1554.2 
25. Maarten Defense: 1551.3 
26. Carl Offense: 1549.5 
27. Loek Defense: 1546.5 
28. Brian Defense: 1542.9 
29. Martin Offense: 1535.3 
30. Floris Offense: 1531.9 
31. Brian Average: 1530.2 
32. Carl Average: 1528.6 
33. Oliver Defense: 1527.6 
34. Mohammed Defense: 1526.9 
35. Wouter Offense: 1526.8 
36. Jane Defense: 1525.0 
37. Timo Average: 1522.1 
38. Job Average: 1521.2 
39. Tim Defense: 1518.0 
40. Brian Offense: 1517.4 
41. Koen Defense: 1514.4 
42. Luka Defense: 1513.7 
43. Loek Average: 1513.6 
44. Thomas Offense: 1511.1 
45. Carl Defense: 1507.8 
46. Mohammed Average: 1503.8 
47. Frenk  Defense: 1503.3 
48. Thomas Average: 1501.8 
49. Bas Offense: 1496.7 
50. Job  Defense: 1496.7 
51. Floris Average: 1494.2 
52. Thomas Defense: 1492.5 
53. Frenk Defense: 1488.8 
54. Philip Defense: 1484.9 
55. Job Defense: 1484.5 
56. Irene Offense: 1481.4 
57. Mohammed Offense: 1480.8 
58. Loek Offense: 1480.7 
59. Daan Offense: 1477.7 
60. Lars Defense: 1470.1 
61. Roy Defense: 1469.4 
62. Maarten Average: 1469.4 
63. Martin Average: 1468.2 
64. Bruno Defense: 1468.1 
65. Jelle Offense: 1468.0 
66. Katherine Offense: 1463.6 
67. Bruno Average: 1462.3 
68. Irene Average: 1460.2 
69. Arjen Offense: 1457.3 
70. Floris Defense: 1456.5 
71. Bruno Offense: 1456.5 
72. Katherine Average: 1453.2 
73. Daan Ri Defense: 1445.4 
74. Vincent Offense: 1445.2 
75. Frenk Average: 1443.9 
76. Katherine Defense: 1442.9 
77. Timo Defense: 1440.8 
78. Irene Defense: 1439.1 
79. Jay Offense: 1439.1 
80. Kassandra Offense: 1436.1 
81. Kassandra Average: 1423.9 
82. Donnie Defense: 1422.0 
83. Kristin Offense: 1415.5 
84. Daan Ri Offense: 1413.7 
85. Kassandra Defense: 1411.7 
86. Wouter Average: 1401.4 
87. Martin Defense: 1401.2 
88. Dennis Offense: 1400.9 
89. Donnie Average: 1400.7 
90. Frenk Offense: 1399.0 
91. Roy Average: 1398.8 
92. Laura Offense: 1390.2 
93. Maarten Offense: 1387.6 
94. Donnie Offense: 1379.4 
95. Dennis Average: 1350.8 
96. Michiel Defense: 1349.4 
97. Roy Offense: 1328.3 
98. Michiel Average: 1318.8 
99. Dennis Defense: 1300.6 
100. Michiel Offense: 1288.2 
101. Wouter Defense: 1276.0 

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