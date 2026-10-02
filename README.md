## tinyshevchenko

[tinyshakespeare](https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt) by Andrej Karpathy is a beautiful toy dataset that is widely used for lm training.

However, for a non-native English speaker, I believe it is hard to fully comprehend the quality of an lm trained on `tinyshakespeare`,
because:

a) Shakespeare's language itself is outdated;

b) because of issue (a), it is harder to clearly understand how much lm outputs drift from Shakespeare's language;

c) for a non-native speaker, it is harder to evaluate how fun :) the words made up by an lm actually are.

This repository presents a version of the `tinyshakespeare` dataset that is supposed to solve the outlined issues for Ukrainian speakers.
`tinyshevchenko` is a concatenation of poems written by the Ukrainian poet [Taras Shevchenko](https://en.wikipedia.org/wiki/Taras_Shevchenko) into one text file.
