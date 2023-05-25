# Internal Fussball ratings at Transavia
## Ratings
1. Koen Offense: 1818.5 
2. Bas Defense: 1737.1 
3. Brian Defense: 1701.9 
4. Job V Defense: 1686.7 
5. Bart Defense: 1685.8 
6. Yashin Defense: 1682.2 
7. Yashin Average: 1682.0 
8. Yashin Offense: 1681.8 
9. Bart Average: 1676.8 
10. Liveris Defense: 1668.5 
11. Bart Offense: 1667.8 
12. Koen Average: 1666.4 
13. Bas Average: 1646.6 
14. Tim Offense: 1625.1 
15. Philip Offense: 1624.7 
16. Job V Offense: 1611.5 
17. Liveris Average: 1610.2 
18. Brian Average: 1609.6 
19. Timo Offense: 1603.4 
20. Job Offense: 1600.2 
21. Oliver Offense: 1580.8 
22. Tim Average: 1571.6 
23. Philip  Defense: 1561.6 
24. Bas Offense: 1556.1 
25. Oliver Average: 1554.2 
26. Carl Offense: 1552.5 
27. Liveris Offense: 1552.0 
28. Maarten Defense: 1550.4 
29. Carl Average: 1543.0 
30. Job Average: 1535.6 
31. Carl Defense: 1533.6 
32. Floris Offense: 1531.9 
33. Philip Average: 1531.6 
34. Oliver Defense: 1527.6 
35. Mohammed Defense: 1526.9 
36. Jane Defense: 1525.0 
37. Timo Average: 1522.1 
38. Martin Offense: 1519.1 
39. Tim Defense: 1518.0 
40. Brian Offense: 1517.4 
41. Koen Defense: 1514.4 
42. Luka Defense: 1513.7 
43. Thomas Offense: 1511.1 
44. Loek Defense: 1508.6 
45. Mohammed Average: 1503.8 
46. Frenk  Defense: 1503.3 
47. Thomas Average: 1501.8 
48. Job  Defense: 1496.7 
49. Loek Average: 1494.6 
50. Floris Average: 1494.2 
51. Thomas Defense: 1492.5 
52. Rob Offense: 1490.0 
53. Donnie Offense: 1485.0 
54. Irene Offense: 1481.4 
55. Mohammed Offense: 1480.8 
56. Loek Offense: 1480.7 
57. Daan Offense: 1477.7 
58. Roy Defense: 1474.4 
59. Kassandra Offense: 1473.3 
60. Maarten Average: 1471.6 
61. Job Defense: 1471.0 
62. Lars Defense: 1470.1 
63. Bruno Defense: 1468.1 
64. Jelle Offense: 1468.0 
65. Rob Average: 1462.8 
66. Bruno Average: 1462.3 
67. Laura Defense: 1461.6 
68. Martin Average: 1460.2 
69. Irene Average: 1460.2 
70. Donnie Average: 1457.7 
71. Arjen Offense: 1457.3 
72. Floris Defense: 1456.5 
73. Bruno Offense: 1456.5 
74. Daan Ri Defense: 1445.4 
75. Vincent Offense: 1445.2 
76. Katherine Defense: 1442.9 
77. Timo Defense: 1440.8 
78. Irene Defense: 1439.1 
79. Jay Offense: 1439.1 
80. Philip Defense: 1438.5 
81. Rob Defense: 1435.6 
82. Wouter Offense: 1434.7 
83. Frenk Defense: 1434.7 
84. Donnie Defense: 1430.4 
85. Katherine Average: 1429.8 
86. Kristin Offense: 1424.3 
87. Kassandra Average: 1418.0 
88. Dennis Defense: 1417.6 
89. Frenk Average: 1416.8 
90. Katherine Offense: 1416.7 
91. Daan Ri Offense: 1413.7 
92. Laura Average: 1411.1 
93. Kristin Average: 1409.2 
94. Dennis Average: 1409.2 
95. Martin Defense: 1401.2 
96. Dennis Offense: 1400.9 
97. Frenk Offense: 1399.0 
98. Kristin Defense: 1394.0 
99. Maarten Offense: 1392.9 
100. Wouter Average: 1383.1 
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