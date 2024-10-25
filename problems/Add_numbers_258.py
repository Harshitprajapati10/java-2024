# add digits of number 258

"""
For every nine digits pattern repeats

1 -- 1
2 -- 2
3 -- 3
4 -- 4
5 -- 5
6 -- 6
7 -- 7
8 -- 8
9 -- 9

10 -- 1
11 -- 2
12 -- 3
13 -- 4
14 -- 5
15 -- 6
16 -- 7
17 -- 8
18 -- 9

19 -- 1
20 -- 2
21 -- 3
22 -- 4
23 -- 5
24 -- 6
25 -- 7
26 -- 8
27 -- 9

28 -- 1
29 -- 2
30 -- 3
31 -- 4
32 -- 5
33 -- 6
34 -- 7
35 -- 8
36 -- 9

37 -- 1
38 -- 2
39 -- 3
40 -- 4
41 -- 5
42 -- 6
43 -- 7
44 -- 8
45 -- 9

"""

def addDigits(num): return 0 if num == 0 else 9 if num % 9 == 0 else num % 9
for i in range(0,46):
    print(addDigits(i))