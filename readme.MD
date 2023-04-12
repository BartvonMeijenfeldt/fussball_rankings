# Internal Fussball ratings at Transavia
## Ratings
1. Koen Offense: 1818.5 
2. Bart Defense: 1726.6 
3. Yashin Defense: 1692.9 
4. Job V Defense: 1686.7 
5. Bas Defense: 1684.0 
6. Liveris Offense: 1683.1 
7. Koen Average: 1666.4 
8. Liveris Average: 1660.6 
9. Yashin Average: 1655.3 
10. Bart Average: 1643.8 
11. Liveris Defense: 1638.2 
12. Philip Offense: 1624.7 
13. Yashin Offense: 1617.7 
14. Job V Offense: 1611.5 
15. Timo Offense: 1603.4 
16. Tim Offense: 1590.3 
17. Bas Average: 1585.2 
18. Oliver Offense: 1580.8 
19. Philip  Defense: 1561.6 
20. Bart Offense: 1561.0 
21. Philip Average: 1554.8 
22. Oliver Average: 1554.2 
23. Tim Average: 1554.2 
24. Maarten Defense: 1551.3 
25. Carl Offense: 1549.5 
26. Job Offense: 1546.9 
27. Carl Average: 1546.6 
28. Loek Defense: 1546.5 
29. Carl Defense: 1543.7 
30. Brian Defense: 1542.9 
31. Floris Offense: 1531.9 
32. Brian Average: 1530.2 
33. Oliver Defense: 1527.6 
34. Mohammed Defense: 1526.9 
35. Jane Defense: 1525.0 
36. Timo Average: 1522.1 
37. Tim Defense: 1518.0 
38. Brian Offense: 1517.4 
39. Job Average: 1515.7 
40. Koen Defense: 1514.4 
41. Luka Defense: 1513.7 
42. Loek Average: 1513.6 
43. Martin Offense: 1512.8 
44. Thomas Offense: 1511.1 
45. Mohammed Average: 1503.8 
46. Frenk  Defense: 1503.3 
47. Thomas Average: 1501.8 
48. Job  Defense: 1496.7 
49. Floris Average: 1494.2 
50. Thomas Defense: 1492.5 
51. Bas Offense: 1486.5 
52. Philip Defense: 1484.9 
53. Job Defense: 1484.5 
54. Irene Offense: 1481.4 
55. Wouter Offense: 1481.3 
56. Mohammed Offense: 1480.8 
57. Loek Offense: 1480.7 
58. Roy Defense: 1477.9 
59. Daan Offense: 1477.7 
60. Frenk Offense: 1474.7 
61. Lars Defense: 1470.1 
62. Maarten Average: 1469.4 
63. Frenk Average: 1469.0 
64. Bruno Defense: 1468.1 
65. Jelle Offense: 1468.0 
66. Katherine Offense: 1463.6 
67. Frenk Defense: 1463.2 
68. Bruno Average: 1462.3 
69. Irene Average: 1460.2 
70. Arjen Offense: 1457.3 
71. Martin Average: 1457.0 
72. Floris Defense: 1456.5 
73. Bruno Offense: 1456.5 
74. Donnie Offense: 1449.1 
75. Daan Ri Defense: 1445.4 
76. Vincent Offense: 1445.2 
77. Kristin Offense: 1441.6 
78. Timo Defense: 1440.8 
79. Katherine Average: 1440.2 
80. Irene Defense: 1439.1 
81. Jay Offense: 1439.1 
82. Kassandra Offense: 1436.1 
83. Kassandra Average: 1423.9 
84. Katherine Defense: 1416.8 
85. Donnie Average: 1415.5 
86. Daan Ri Offense: 1413.7 
87. Kassandra Defense: 1411.7 
88. Roy Average: 1403.1 
89. Martin Defense: 1401.2 
90. Laura Offense: 1401.1 
91. Dennis Offense: 1400.9 
92. Maarten Offense: 1387.6 
93. Donnie Defense: 1381.9 
94. Wouter Average: 1378.6 
95. Dennis Average: 1370.4 
96. Michiel Defense: 1349.4 
97. Dennis Defense: 1340.0 
98. Roy Offense: 1328.3 
99. Michiel Average: 1318.8 
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