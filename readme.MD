# Internal Fussball ratings at Transavia
## Ratings
1. Koen Offense: 1818.5 
2. Brian Offense: 1715.8 
3. Brian Average: 1715.8 
4. Brian Defense: 1715.7 
5. Job V Defense: 1686.7 
6. Yashin Defense: 1682.2 
7. Yashin Average: 1679.8 
8. Yashin Offense: 1677.4 
9. Koen Average: 1666.4 
10. Bart Offense: 1662.3 
11. Bart Average: 1655.1 
12. Bas Defense: 1653.1 
13. Bart Defense: 1647.9 
14. Carl Defense: 1645.7 
15. Carl Average: 1645.6 
16. Carl Offense: 1645.5 
17. Liveris Defense: 1644.4 
18. Job Offense: 1635.8 
19. Tim Offense: 1625.1 
20. Job V Offense: 1611.5 
21. Liveris Average: 1606.6 
22. Timo Offense: 1603.4 
23. Martin Offense: 1602.1 
24. Philip Offense: 1583.5 
25. Oliver Offense: 1580.8 
26. Tim Average: 1571.6 
27. Liveris Offense: 1568.9 
28. Job Average: 1567.8 
29. Bas Average: 1564.4 
30. Philip  Defense: 1561.6 
31. Maarten Defense: 1554.2 
32. Oliver Average: 1554.2 
33. Philip Average: 1540.0 
34. Donnie Offense: 1539.9 
35. Roy Defense: 1539.9 
36. Floris Offense: 1531.9 
37. Martin Average: 1528.5 
38. Oliver Defense: 1527.6 
39. Mohammed Defense: 1526.9 
40. Jane Defense: 1525.0 
41. Timo Average: 1522.1 
42. Tim Defense: 1518.0 
43. Koen Defense: 1514.4 
44. Luka Defense: 1513.7 
45. Thomas Offense: 1511.1 
46. Donnie Average: 1508.9 
47. Loek Offense: 1508.7 
48. Loek Average: 1508.0 
49. Loek Defense: 1507.3 
50. Mohammed Average: 1503.8 
51. Frenk  Defense: 1503.3 
52. Thomas Average: 1501.8 
53. Job Defense: 1499.8 
54. Job  Defense: 1496.7 
55. Philip Defense: 1496.4 
56. Floris Average: 1494.2 
57. Thomas Defense: 1492.5 
58. Brenda Defense: 1488.0 
59. Wouter Offense: 1485.1 
60. Irene Offense: 1481.4 
61. Mohammed Offense: 1480.8 
62. Rob Defense: 1478.5 
63. Donnie Defense: 1477.9 
64. Daan Offense: 1477.7 
65. Boele Defense: 1477.6 
66. Bas Offense: 1475.6 
67. Dennis Defense: 1473.3 
68. Lars Defense: 1470.1 
69. Bruno Defense: 1468.1 
70. Jelle Offense: 1468.0 
71. Bruno Average: 1462.3 
72. Irene Average: 1460.2 
73. Anna Offense: 1459.0 
74. Arjen Offense: 1457.3 
75. Floris Defense: 1456.5 
76. Bruno Offense: 1456.5 
77. Martin Defense: 1454.9 
78. Boele Average: 1454.5 
79. Rob Average: 1452.7 
80. Daan Ri Defense: 1445.4 
81. Vincent Offense: 1445.2 
82. Andreea Offense: 1443.6 
83. Timo Defense: 1440.8 
84. Kassandra Offense: 1439.2 
85. Irene Defense: 1439.1 
86. Jay Offense: 1439.1 
87. Frenk Defense: 1434.7 
88. Maarten Average: 1434.6 
89. Boele Offense: 1431.4 
90. Dennis Average: 1428.9 
91. Rob Offense: 1426.9 
92. Kristin Offense: 1422.5 
93. Wouter Average: 1420.8 
94. Frenk Average: 1416.8 
95. Katherine Offense: 1416.7 
96. Daan Ri Offense: 1413.7 
97. Katherine Average: 1411.1 
98. Katherine Defense: 1405.5 
99. Anna Average: 1401.6 
100. Frenk Offense: 1399.0 
101. Laura Defense: 1394.0 
102. Kristin Average: 1392.4 
103. Kassandra Average: 1384.6 
104. Dennis Offense: 1384.5 
105. Laura Average: 1377.3 
106. Roy Average: 1375.4 
107. Kristin Defense: 1362.4 
108. Laura Offense: 1360.6 
109. Wouter Defense: 1356.6 
110. Michiel Defense: 1349.4 
111. Anna Defense: 1344.3 
112. Kassandra Defense: 1329.9 
113. Michiel Average: 1318.8 
114. Maarten Offense: 1315.0 
115. Michiel Offense: 1288.2 
116. Roy Offense: 1210.8 

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