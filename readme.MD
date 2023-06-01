# Internal Fussball ratings at Transavia
## Ratings
1. Koen Offense: 1818.5 
2. Bas Defense: 1755.5 
3. Brian Defense: 1724.7 
4. Job V Defense: 1686.7 
5. Bart Defense: 1685.8 
6. Yashin Defense: 1682.2 
7. Yashin Average: 1679.8 
8. Yashin Offense: 1677.4 
9. Bart Average: 1676.8 
10. Liveris Defense: 1668.5 
11. Bart Offense: 1667.8 
12. Koen Average: 1666.4 
13. Bas Average: 1660.2 
14. Tim Offense: 1625.1 
15. Brian Average: 1617.2 
16. Job V Offense: 1611.5 
17. Liveris Average: 1610.2 
18. Timo Offense: 1603.4 
19. Job Offense: 1598.2 
20. Maarten Defense: 1591.6 
21. Philip Offense: 1583.5 
22. Oliver Offense: 1580.8 
23. Tim Average: 1571.6 
24. Bas Offense: 1564.9 
25. Philip  Defense: 1561.6 
26. Oliver Average: 1554.2 
27. Liveris Offense: 1552.0 
28. Martin Offense: 1544.7 
29. Floris Offense: 1531.9 
30. Oliver Defense: 1527.6 
31. Mohammed Defense: 1526.9 
32. Carl Offense: 1526.9 
33. Jane Defense: 1525.0 
34. Timo Average: 1522.1 
35. Carl Average: 1519.8 
36. Tim Defense: 1518.0 
37. Job Average: 1518.0 
38. Philip Average: 1514.8 
39. Koen Defense: 1514.4 
40. Luka Defense: 1513.7 
41. Carl Defense: 1512.8 
42. Thomas Offense: 1511.1 
43. Brian Offense: 1509.7 
44. Loek Defense: 1508.6 
45. Mohammed Average: 1503.8 
46. Frenk  Defense: 1503.3 
47. Thomas Average: 1501.8 
48. Job  Defense: 1496.7 
49. Maarten Average: 1496.1 
50. Loek Average: 1494.6 
51. Floris Average: 1494.2 
52. Thomas Defense: 1492.5 
53. Rob Offense: 1490.0 
54. Martin Average: 1483.4 
55. Donnie Offense: 1482.6 
56. Irene Offense: 1481.4 
57. Mohammed Offense: 1480.8 
58. Loek Offense: 1480.7 
59. Daan Offense: 1477.7 
60. Wouter Offense: 1475.9 
61. Roy Defense: 1474.4 
62. Kassandra Offense: 1473.3 
63. Lars Defense: 1470.1 
64. Bruno Defense: 1468.1 
65. Jelle Offense: 1468.0 
66. Rob Average: 1462.8 
67. Bruno Average: 1462.3 
68. Laura Defense: 1461.6 
69. Irene Average: 1460.2 
70. Arjen Offense: 1457.3 
71. Floris Defense: 1456.5 
72. Bruno Offense: 1456.5 
73. Philip Defense: 1446.2 
74. Daan Ri Defense: 1445.4 
75. Vincent Offense: 1445.2 
76. Donnie Average: 1444.3 
77. Katherine Defense: 1442.9 
78. Timo Defense: 1440.8 
79. Irene Defense: 1439.1 
80. Jay Offense: 1439.1 
81. Job Defense: 1437.7 
82. Rob Defense: 1435.6 
83. Frenk Defense: 1434.7 
84. Katherine Average: 1429.8 
85. Kristin Offense: 1424.3 
86. Martin Defense: 1422.0 
87. Kassandra Average: 1418.0 
88. Frenk Average: 1416.8 
89. Katherine Offense: 1416.7 
90. Daan Ri Offense: 1413.7 
91. Laura Average: 1411.1 
92. Kristin Average: 1409.2 
93. Donnie Defense: 1406.0 
94. Wouter Average: 1403.7 
95. Dennis Offense: 1400.9 
96. Maarten Offense: 1400.6 
97. Frenk Offense: 1399.0 
98. Kristin Defense: 1394.0 
99. Dennis Average: 1393.1 
100. Dennis Defense: 1385.2 
101. Roy Average: 1377.2 
102. Kassandra Defense: 1362.7 
103. Laura Offense: 1360.6 
104. Michiel Defense: 1349.4 
105. Wouter Defense: 1331.5 
106. Michiel Average: 1318.8 
107. Michiel Offense: 1288.2 
108. Roy Offense: 1280.1 

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