# Internal Fussball ratings at Transavia
## Ratings
1. Bart Offense: 1879.8 
2. Koen Offense: 1818.5 
3. Brian Defense: 1809.9 
4. Brian Average: 1792.4 
5. Bart Average: 1790.6 
6. Brian Offense: 1774.8 
7. Carl Offense: 1765.9 
8. Liveris Offense: 1701.6 
9. Bart Defense: 1701.5 
10. Liveris Average: 1696.7 
11. Liveris Defense: 1691.8 
12. Yashin Offense: 1691.8 
13. Yashin Average: 1690.7 
14. Yashin Defense: 1689.6 
15. Job V Defense: 1686.7 
16. Loek Defense: 1685.3 
17. Carl Average: 1681.6 
18. Koen Average: 1666.4 
19. Bas Defense: 1653.1 
20. Job Defense: 1651.4 
21. Wouter Offense: 1644.7 
22. Loek Average: 1632.4 
23. Tim Offense: 1625.1 
24. Job Average: 1617.8 
25. Job V Offense: 1611.5 
26. Timo Offense: 1603.4 
27. Martin Offense: 1602.1 
28. Carl Defense: 1597.2 
29. Job Offense: 1584.1 
30. Philip Offense: 1583.5 
31. Loek Offense: 1579.6 
32. Oliver Offense: 1574.2 
33. Tim Average: 1571.6 
34. Bas Average: 1564.4 
35. Philip  Defense: 1561.6 
36. Oliver Average: 1550.9 
37. Wouter Average: 1549.1 
38. Philip Average: 1540.0 
39. Floris Offense: 1531.9 
40. Martin Average: 1528.5 
41. Oliver Defense: 1527.6 
42. Mohammed Defense: 1526.9 
43. Jane Defense: 1525.0 
44. Timo Average: 1522.1 
45. Tim Defense: 1518.0 
46. Koen Defense: 1514.4 
47. Luka Defense: 1513.7 
48. Mohammed Average: 1503.8 
49. Frenk  Defense: 1503.3 
50. Donnie Offense: 1500.0 
51. Job  Defense: 1496.7 
52. Philip Defense: 1496.4 
53. Floris Average: 1494.2 
54. Katherine Defense: 1493.5 
55. Thomas Defense: 1492.5 
56. Kassandra Offense: 1484.9 
57. Maarten Defense: 1484.3 
58. Thomas Average: 1482.3 
59. Irene Offense: 1481.4 
60. Mohammed Offense: 1480.8 
61. Daan Offense: 1477.7 
62. Donnie Average: 1477.0 
63. Bas Offense: 1475.6 
64. Thomas Offense: 1472.1 
65. Lars Defense: 1470.1 
66. Bruno Defense: 1468.1 
67. Jelle Offense: 1468.0 
68. Kassandra Average: 1464.4 
69. Bruno Average: 1462.3 
70. Irene Average: 1460.2 
71. Boele Defense: 1458.1 
72. Arjen Offense: 1457.3 
73. Floris Defense: 1456.5 
74. Bruno Offense: 1456.5 
75. Martin Defense: 1454.9 
76. Donnie Defense: 1453.9 
77. Wouter Defense: 1453.5 
78. Adrian Defense: 1452.8 
79. Dennis Defense: 1451.4 
80. Timo2 Offense: 1449.7 
81. Ivar Offense: 1447.2 
82. Daan Ri Defense: 1445.4 
83. Vincent Offense: 1445.2 
84. Kassandra Defense: 1444.0 
85. Timo Defense: 1440.8 
86. Irene Defense: 1439.1 
87. Jay Offense: 1439.1 
88. Frenk Defense: 1434.7 
89. Katherine Average: 1434.2 
90. Roy Defense: 1430.9 
91. Boele Average: 1428.9 
92. Ivar Average: 1418.2 
93. Brenda Defense: 1417.0 
94. Frenk Average: 1416.8 
95. Daan Ri Offense: 1413.7 
96. Rob Defense: 1411.2 
97. Kristin Offense: 1403.2 
98. Boele Offense: 1399.7 
99. Maarten Average: 1399.6 
100. Frenk Offense: 1399.0 
101. Rob Average: 1397.8 
102. Michiel Defense: 1397.7 
103. Dennis Average: 1395.3 
104. Ivar Defense: 1389.2 
105. Laura Offense: 1388.9 
106. Rob Offense: 1384.3 
107. Kristin Average: 1382.8 
108. Anna Offense: 1380.4 
109. Katherine Offense: 1375.0 
110. Laura Average: 1373.4 
111. Timo2 Average: 1365.2 
112. Andreea Offense: 1365.0 
113. Kristin Defense: 1362.4 
114. Laura Defense: 1357.9 
115. Anna Average: 1344.9 
116. Dennis Offense: 1339.2 
117. Roy Average: 1336.6 
118. Michiel Average: 1331.8 
119. Brenda Average: 1318.7 
120. Maarten Offense: 1315.0 
121. Anna Defense: 1309.4 
122. Timo2 Defense: 1280.6 
123. Michiel Offense: 1266.0 
124. Roy Offense: 1242.2 
125. Brenda Offense: 1220.4 

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