# Internal Fussball ratings at Transavia
## Ratings
1. Koen Offense: 1818.5 
2. Bart Defense: 1776.0 
3. Liveris Offense: 1712.1 
4. Bas Defense: 1700.3 
5. Job V Defense: 1686.7 
6. Liveris Average: 1675.2 
7. Bart Average: 1668.5 
8. Koen Average: 1666.4 
9. Liveris Defense: 1638.2 
10. Yashin Defense: 1631.4 
11. Philip Offense: 1624.7 
12. Yashin Average: 1617.3 
13. Bas Average: 1616.2 
14. Job V Offense: 1611.5 
15. Timo Offense: 1603.4 
16. Yashin Offense: 1603.2 
17. Oliver Offense: 1580.8 
18. Philip  Defense: 1561.6 
19. Bart Offense: 1561.0 
20. Philip Average: 1554.8 
21. Oliver Average: 1554.2 
22. Carl Defense: 1552.7 
23. Carl Average: 1551.1 
24. Carl Offense: 1549.5 
25. Maarten Defense: 1547.6 
26. Job Offense: 1546.9 
27. Brian Defense: 1542.9 
28. Loek Defense: 1541.6 
29. Bas Offense: 1532.0 
30. Floris Offense: 1531.9 
31. Brian Average: 1530.2 
32. Oliver Defense: 1527.6 
33. Mohammed Defense: 1526.9 
34. Jane Defense: 1525.0 
35. Timo Average: 1522.1 
36. Tim Offense: 1520.4 
37. Tim Average: 1519.2 
38. Tim Defense: 1518.0 
39. Brian Offense: 1517.4 
40. Koen Defense: 1514.4 
41. Loek Average: 1511.2 
42. Thomas Offense: 1511.1 
43. Frenk Defense: 1510.3 
44. Martin Offense: 1509.7 
45. Job Average: 1506.4 
46. Mohammed Average: 1503.8 
47. Frenk  Defense: 1503.3 
48. Thomas Average: 1501.8 
49. Job  Defense: 1496.7 
50. Floris Average: 1494.2 
51. Thomas Defense: 1492.5 
52. Frenk Average: 1492.5 
53. Philip Defense: 1484.9 
54. Irene Offense: 1481.4 
55. Mohammed Offense: 1480.8 
56. Loek Offense: 1480.7 
57. Roy Defense: 1477.9 
58. Frenk Offense: 1474.7 
59. Bruno Defense: 1468.1 
60. Jelle Offense: 1468.0 
61. Maarten Average: 1467.6 
62. Job Defense: 1465.9 
63. Martin Average: 1463.8 
64. Katherine Offense: 1463.6 
65. Bruno Average: 1462.3 
66. Irene Average: 1460.2 
67. Arjen Offense: 1457.3 
68. Floris Defense: 1456.5 
69. Bruno Offense: 1456.5 
70. Wouter Offense: 1448.7 
71. Daan Ri Defense: 1445.4 
72. Vincent Offense: 1445.2 
73. Katherine Average: 1443.8 
74. Timo Defense: 1440.8 
75. Irene Defense: 1439.1 
76. Jay Offense: 1439.1 
77. Kassandra Offense: 1436.1 
78. Katherine Defense: 1424.0 
79. Donnie Offense: 1422.2 
80. Martin Defense: 1418.0 
81. Daan Ri Offense: 1413.7 
82. Kassandra Average: 1402.2 
83. Roy Average: 1402.0 
84. Dennis Offense: 1400.9 
85. Laura Offense: 1395.2 
86. Maarten Offense: 1387.6 
87. Donnie Average: 1387.1 
88. Dennis Average: 1370.4 
89. Kassandra Defense: 1368.3 
90. Wouter Average: 1362.4 
91. Donnie Defense: 1352.0 
92. Michiel Defense: 1349.4 
93. Dennis Defense: 1340.0 
94. Roy Offense: 1326.0 
95. Michiel Average: 1318.8 
96. Michiel Offense: 1288.2 
97. Wouter Defense: 1276.0 

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