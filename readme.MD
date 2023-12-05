# Internal Fussball ratings at Transavia
## Ratings
1. Bart Offense: 1879.8 
2. Carl Offense: 1831.4 
3. Koen Offense: 1818.5 
4. Brian Defense: 1809.9 
5. Brian Average: 1809.7 
6. Brian Offense: 1809.5 
7. Bart Average: 1790.6 
8. Carl Average: 1714.3 
9. Liveris Offense: 1701.6 
10. Bart Defense: 1701.5 
11. Loek Defense: 1695.1 
12. Yashin Offense: 1691.8 
13. Yashin Average: 1690.7 
14. Liveris Average: 1689.8 
15. Yashin Defense: 1689.6 
16. Job V Defense: 1686.7 
17. Liveris Defense: 1678.0 
18. Koen Average: 1666.4 
19. Bas Defense: 1653.1 
20. Job Defense: 1651.4 
21. Loek Average: 1633.1 
22. Tim Offense: 1625.1 
23. Job Average: 1612.3 
24. Job V Offense: 1611.5 
25. Timo Offense: 1603.4 
26. Martin Offense: 1602.1 
27. Carl Defense: 1597.2 
28. Philip Offense: 1583.5 
29. Oliver Offense: 1574.2 
30. Job Offense: 1573.2 
31. Wouter Offense: 1572.8 
32. Tim Average: 1571.6 
33. Loek Offense: 1571.1 
34. Bas Average: 1564.4 
35. Philip  Defense: 1561.6 
36. Oliver Average: 1550.9 
37. Philip Average: 1540.0 
38. Floris Offense: 1531.9 
39. Martin Average: 1528.5 
40. Oliver Defense: 1527.6 
41. Mohammed Defense: 1526.9 
42. Jane Defense: 1525.0 
43. Timo Average: 1522.1 
44. Tim Defense: 1518.0 
45. Koen Defense: 1514.4 
46. Luka Defense: 1513.7 
47. Mohammed Average: 1503.8 
48. Frenk  Defense: 1503.3 
49. Donnie Offense: 1500.0 
50. Job  Defense: 1496.7 
51. Philip Defense: 1496.4 
52. Floris Average: 1494.2 
53. Katherine Defense: 1493.5 
54. Thomas Defense: 1492.5 
55. Wouter Average: 1490.4 
56. Kassandra Offense: 1484.9 
57. Maarten Defense: 1484.3 
58. Thomas Average: 1482.3 
59. Irene Offense: 1481.4 
60. Mohammed Offense: 1480.8 
61. Daan Offense: 1477.7 
62. Donnie Average: 1477.0 
63. Bas Offense: 1475.6 
64. Thomas Offense: 1472.1 
65. Ivar Offense: 1471.9 
66. Lars Defense: 1470.1 
67. Bruno Defense: 1468.1 
68. Jelle Offense: 1468.0 
69. Kassandra Average: 1464.4 
70. Bruno Average: 1462.3 
71. Irene Average: 1460.2 
72. Boele Defense: 1458.1 
73. Arjen Offense: 1457.3 
74. Floris Defense: 1456.5 
75. Bruno Offense: 1456.5 
76. Roy Defense: 1455.6 
77. Martin Defense: 1454.9 
78. Donnie Defense: 1453.9 
79. Dennis Defense: 1451.4 
80. Timo2 Offense: 1449.7 
81. Ivar Average: 1447.9 
82. Daan Ri Defense: 1445.4 
83. Vincent Offense: 1445.2 
84. Kassandra Defense: 1444.0 
85. Timo Defense: 1440.8 
86. Irene Defense: 1439.1 
87. Jay Offense: 1439.1 
88. Frenk Defense: 1434.7 
89. Katherine Average: 1434.2 
90. Boele Average: 1428.9 
91. Ivar Defense: 1423.9 
92. Frenk Average: 1416.8 
93. Daan Ri Offense: 1413.7 
94. Rob Defense: 1411.2 
95. Wouter Defense: 1407.9 
96. Kristin Offense: 1403.2 
97. Boele Offense: 1399.7 
98. Maarten Average: 1399.6 
99. Frenk Offense: 1399.0 
100. Rob Average: 1397.8 
101. Michiel Defense: 1397.7 
102. Dennis Average: 1395.3 
103. Rob Offense: 1384.3 
104. Kristin Average: 1382.8 
105. Katherine Offense: 1375.0 
106. Anna Offense: 1370.6 
107. Anna Average: 1367.8 
108. Timo2 Average: 1365.2 
109. Anna Defense: 1365.1 
110. Andreea Offense: 1365.0 
111. Kristin Defense: 1362.4 
112. Laura Defense: 1357.9 
113. Laura Average: 1356.1 
114. Laura Offense: 1354.2 
115. Roy Average: 1348.9 
116. Dennis Offense: 1339.2 
117. Michiel Average: 1331.8 
118. Maarten Offense: 1315.0 
119. Brenda Defense: 1304.3 
120. Timo2 Defense: 1280.6 
121. Brenda Average: 1267.8 
122. Michiel Offense: 1266.0 
123. Roy Offense: 1242.2 
124. Brenda Offense: 1231.3 

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