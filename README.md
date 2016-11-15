## autogram

### What are autograms?

An autogram[https://en.wikipedia.org/wiki/Autogram] is a sentence that describes itself in the sense of providing an inventory of its own characters (Source: Wikipedia).

### Purpose of this repository?

To generate some fun little autograms, automatically with a randomized brute-force approach.

### Example-1

Code example, that can be executed on a python shell -
```
>>> import autogram
>>> x = autogram.AutoGram('This sentence employs ', 'abcdefghijklmnopqrtuvyz', 3)
>>> x(25000)
```

Output of the above code -
```
==================================================
** autogram generation successful **
this sentence employs two a's, one b, two c's, two d's, twenty-five e's, six f's, two g's, five h's, nine i's, one j, one k, two l's, two m's, fifteen n's, sixteen o's, two p's, one q, four r's, eighteen t's, two u's, three v's, three y's, and one z.
--------------------------------------------------
   symbol  actual_count  accounted_count match
0       a             2                2  True
1       b             1                1  True
2       c             2                2  True
3       d             2                2  True
4       e            25               25  True
5       f             6                6  True
6       g             2                2  True
7       h             5                5  True
8       i             9                9  True
9       j             1                1  True
10      k             1                1  True
11      l             2                2  True
12      m             2                2  True
13      n            15               15  True
14      o            16               16  True
15      p             2                2  True
16      q             1                1  True
17      r             4                4  True
18      t            18               18  True
19      u             2                2  True
20      v             3                3  True
21      y             3                3  True
22      z             1                1  True
--------------------------------------------------
```

### Example-2

Code -
```
>>> import autogram
>>> from string import ascii_lowercase as letters
>>> x = autogram.AutoGram(prefix='xiao9 - my cat says this sentence contains ', suffix=' check for yourself.', symbols=letters[:13]+'pqruvxz', seed=1)
>>> x(25000)
```

Output -
```
==================================================
** autogram generation successful **
xiao9 - my cat says this sentence contains six a's, one b, six c's, two d's, twenty-three e's, six f's, one g, five h's, eleven i's, one j, two k's, three l's, two m's, one p, one q, five r's, two u's, five v's, six x's, and one z check for yourself.
--------------------------------------------------
   symbol  actual_count  accounted_count match
0       a             6                6  True
1       b             1                1  True
2       c             6                6  True
3       d             2                2  True
4       e            23               23  True
5       f             6                6  True
6       g             1                1  True
7       h             5                5  True
8       i            11               11  True
9       j             1                1  True
10      k             2                2  True
11      l             3                3  True
12      m             2                2  True
13      p             1                1  True
14      q             1                1  True
15      r             5                5  True
16      u             2                2  True
17      v             5                5  True
18      x             6                6  True
19      z             1                1  True
--------------------------------------------------
```
