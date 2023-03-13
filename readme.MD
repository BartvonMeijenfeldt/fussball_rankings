# Internal Fussball ratings at Transavia
## Ratings
1. Koen Offense: 1818.5 
2. Bart Defense: 1776.0 
3. Liveris Offense: 1712.1 
4. Job V Defense: 1686.7 
5. Liveris Average: 1675.2 
6. Bart Average: 1668.5 
7. Koen Average: 1666.4 
8. Loek Defense: 1641.6 
9. Bas Offense: 1639.5 
10. Liveris Defense: 1638.2 
11. Bas Average: 1632.8 
12. Yashin Offense: 1627.7 
13. Bas Defense: 1626.1 
14. Philip Offense: 1624.7 
15. Yashin Average: 1620.9 
16. Yashin Defense: 1614.1 
17. Job V Offense: 1611.5 
18. Timo Offense: 1603.4 
19. Oliver Offense: 1580.8 
20. Philip  Defense: 1561.6 
21. Loek Average: 1561.2 
22. Bart Offense: 1561.0 
23. Philip Average: 1554.8 
24. Oliver Average: 1554.2 
25. Job Offense: 1553.4 
26. Carl Defense: 1552.7 
27. Carl Average: 1551.1 
28. Carl Offense: 1549.5 
29. Brian Defense: 1548.4 
30. Maarten Defense: 1541.4 
31. Floris Offense: 1531.9 
32. Oliver Defense: 1527.6 
33. Mohammed Defense: 1526.9 
34. Jane Defense: 1525.0 
35. Timo Average: 1522.1 
36. Tim Offense: 1520.4 
37. Tim Average: 1519.2 
38. Tim Defense: 1518.0 
39. Martin Offense: 1515.2 
40. Koen Defense: 1514.4 
41. Brian Average: 1514.3 
42. Thomas Offense: 1511.1 
43. Frenk Defense: 1510.3 
44. Job Average: 1509.6 
45. Mohammed Average: 1503.8 
46. Frenk  Defense: 1503.3 
47. Job  Defense: 1496.7 
48. Floris Average: 1494.2 
49. Frenk Average: 1492.5 
50. Thomas Average: 1491.3 
51. Philip Defense: 1484.9 
52. Irene Offense: 1481.4 
53. Mohammed Offense: 1480.8 
54. Loek Offense: 1480.7 
55. Brian Offense: 1480.2 
56. Roy Defense: 1477.9 
57. Frenk Offense: 1474.7 
58. Thomas Defense: 1471.5 
59. Bruno Defense: 1468.1 
60. Jelle Offense: 1468.0 
61. Job Defense: 1465.9 
62. Maarten Average: 1464.5 
63. Katherine Offense: 1463.6 
64. Bruno Average: 1462.3 
65. Irene Average: 1460.2 
66. Floris Defense: 1456.5 
67. Bruno Offense: 1456.5 
68. Martin Average: 1450.0 
69. Daan Ri Defense: 1445.4 
70. Vincent Offense: 1445.2 
71. Timo Defense: 1440.8 
72. Katherine Average: 1439.4 
73. Irene Defense: 1439.1 
74. Jay Offense: 1439.1 
75. Daan Ri Offense: 1434.7 
76. Katherine Defense: 1415.2 
77. Laura Offense: 1410.9 
78. Kassandra Defense: 1409.1 
79. Donnie Offense: 1401.2 
80. Dennis Offense: 1400.9 
81. Kassandra Average: 1394.3 
82. Maarten Offense: 1387.6 
83. Martin Defense: 1384.7 
84. Roy Average: 1384.0 
85. Kassandra Offense: 1379.5 
86. Dennis Average: 1377.7 
87. Donnie Average: 1376.6 
88. Wouter Offense: 1376.1 
89. Dennis Defense: 1354.5 
90. Donnie Defense: 1352.0 
91. Michiel Defense: 1349.4 
92. Wouter Average: 1326.0 
93. Michiel Average: 1318.8 
94. Roy Offense: 1290.0 
95. Michiel Offense: 1288.2 
96. Wouter Defense: 1276.0 

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