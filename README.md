## tinyshevchenko

[tinyshakespeare](https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt) by Andrej Karpathy is a beautiful toy dataset that is widely used for lm training.

However, for a non-native English speaker, I believe it is hard to fully comprehend the quality of an lm trained on `tinyshakespeare`,
because:

a) Shakespeare's language itself is outdated;

b) because of issue (a), it is harder to clearly understand how much lm outputs drift from Shakespeare's language;

c) for a non-native speaker, it is harder to evaluate how fun :) the words made up by an lm actually are.

This repository presents a version of the `tinyshakespeare` dataset that is supposed to solve the outlined issues for Ukrainian speakers.
`tinyshevchenko` is a concatenation of poems written by the Ukrainian poet [Taras Shevchenko](https://en.wikipedia.org/wiki/Taras_Shevchenko) into one text file.

### dataset stats 

I kept only the poems and plays and joined the lines with \n. I then removed lines longer than the 99th percentile of line length (see postproc.py). In the raw dataset, the p99 line length is 37 characters, while the longest line has 1,542, so lines longer than 37 characters were dropped. This removed about 1% of lines, mostly long annotations that aren’t part of the poems.

chars count: 498,227

char: `!"'()*,-./0123456789:;<>?ABCDIMNPTUVX[]^_adegijklmnoprsuwyzЄІЇАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюяєіїҐґ–—’“”…`
