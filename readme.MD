# Internal Fussball ratings at Transavia
## Ratings
1. Bart Offense: 1847.4 
2. Koen Offense: 1818.5 
3. Bart Average: 1767.1 
4. Brian Defense: 1762.5 
5. Brian Average: 1751.0 
6. Carl Offense: 1746.6 
7. Brian Offense: 1739.6 
8. Carl Average: 1713.6 
9. Bart Defense: 1686.8 
10. Job V Defense: 1686.7 
11. Yashin Defense: 1682.2 
12. Carl Defense: 1680.7 
13. Yashin Average: 1679.8 
14. Yashin Offense: 1677.4 
15. Liveris Defense: 1677.3 
16. Koen Average: 1666.4 
17. Bas Defense: 1653.1 
18. Liveris Average: 1648.7 
19. Job Defense: 1626.0 
20. Tim Offense: 1625.1 
21. Liveris Offense: 1620.1 
22. Donnie Offense: 1616.9 
23. Job V Offense: 1611.5 
24. Timo Offense: 1603.4 
25. Loek Defense: 1603.4 
26. Martin Offense: 1602.1 
27. Loek Average: 1596.4 
28. Loek Offense: 1589.4 
29. Philip Offense: 1583.5 
30. Job Average: 1579.0 
31. Oliver Offense: 1574.2 
32. Tim Average: 1571.6 
33. Wouter Offense: 1567.5 
34. Bas Average: 1564.4 
35. Philip  Defense: 1561.6 
36. Oliver Average: 1550.9 
37. Donnie Average: 1543.0 
38. Philip Average: 1540.0 
39. Job Offense: 1532.0 
40. Floris Offense: 1531.9 
41. Martin Average: 1528.5 
42. Oliver Defense: 1527.6 
43. Mohammed Defense: 1526.9 
44. Jane Defense: 1525.0 
45. Timo Average: 1522.1 
46. Boele Defense: 1519.9 
47. Tim Defense: 1518.0 
48. Koen Defense: 1514.4 
49. Luka Defense: 1513.7 
50. Wouter Average: 1504.9 
51. Mohammed Average: 1503.8 
52. Frenk  Defense: 1503.3 
53. Roy Defense: 1502.6 
54. Job  Defense: 1496.7 
55. Kassandra Offense: 1496.5 
56. Philip Defense: 1496.4 
57. Floris Average: 1494.2 
58. Thomas Defense: 1492.5 
59. Katherine Defense: 1482.6 
60. Thomas Average: 1482.3 
61. Irene Offense: 1481.4 
62. Mohammed Offense: 1480.8 
63. Andreea Offense: 1479.3 
64. Maarten Defense: 1477.7 
65. Daan Offense: 1477.7 
66. Bas Offense: 1475.6 
67. Kassandra Average: 1474.0 
68. Thomas Offense: 1472.1 
69. Lars Defense: 1470.1 
70. Donnie Defense: 1469.0 
71. Bruno Defense: 1468.1 
72. Jelle Offense: 1468.0 
73. Boele Average: 1463.5 
74. Bruno Average: 1462.3 
75. Irene Average: 1460.2 
76. Arjen Offense: 1457.3 
77. Floris Defense: 1456.5 
78. Bruno Offense: 1456.5 
79. Martin Defense: 1454.9 
80. Dennis Defense: 1451.4 
81. Kassandra Defense: 1451.4 
82. Daan Ri Defense: 1445.4 
83. Vincent Offense: 1445.2 
84. Wouter Defense: 1442.3 
85. Timo Defense: 1440.8 
86. Irene Defense: 1439.1 
87. Jay Offense: 1439.1 
88. Frenk Defense: 1434.7 
89. Katherine Average: 1422.8 
90. Frenk Average: 1416.8 
91. Daan Ri Offense: 1413.7 
92. Boele Offense: 1407.1 
93. Kristin Offense: 1403.2 
94. Frenk Offense: 1399.0 
95. Michiel Defense: 1397.7 
96. Rob Offense: 1396.7 
97. Maarten Average: 1396.4 
98. Dennis Average: 1395.3 
99. Rob Average: 1388.4 
100. Timo2 Offense: 1387.6 
101. Anna Offense: 1384.9 
102. Kristin Average: 1382.8 
103. Rob Defense: 1380.2 
104. Roy Average: 1372.4 
105. Katherine Offense: 1363.1 
106. Kristin Defense: 1362.4 
107. Anna Average: 1349.6 
108. Laura Defense: 1349.1 
109. Brenda Offense: 1346.6 
110. Dennis Offense: 1339.2 
111. Laura Average: 1334.1 
112. Timo2 Average: 1333.9 
113. Michiel Average: 1331.8 
114. Laura Offense: 1319.1 
115. Maarten Offense: 1315.0 
116. Anna Defense: 1314.2 
117. Brenda Average: 1310.8 
118. Timo2 Defense: 1280.2 
119. Brenda Defense: 1274.9 
120. Michiel Offense: 1266.0 
121. Roy Offense: 1242.2 

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