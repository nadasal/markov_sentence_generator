# markov_sentence_generator


With the rise of automation and machine learning, many programs that predict future instances based on past appearances are popping up. A great deal of these programs utilize the concept of a Markov Chain, which is a model that describes a sequence of possible events in which the probability of each even depends on the state attained in the previous event <sup>[1](http://www.businessdictionary.com/definition/Markov-chain.html)</sup>. A few years ago, a Facebook application called 'What Would I Say?' that utilized Markov Chains went viral. It claimed that it could automatically generate Facebook posts that sound like you from studying your previous status posts. While most of the sentences it generated were utterly meaningless, the concept behind it has many useful applications. Beyond generating gibbrish, Markov Chains can generate a large number of spam emails, can help create piano compositions, and can even predict baseball pitches.

This code creates a basic Markov Chain that attempts to generate text in the same manner as the 'What Would I Say?' application.

- Code: [markov py](https://github.com/nadasal/markov_sentence_generator/blob/master/src/markov.py)
- Data: [alice txt](https://github.com/nadasal/markov_sentence_generator/blob/master/data/alice.txt)

### Implementation:

```

In [1]: markov = markov('../data/alice.txt')
In [2]: markov.text_generator(25)

```

```

Out [2]: 'again with a teacup in one hand and a crash of broken glass from which she had forgotten the little door so either way get'

```


### Dependencies:

#### Packages:

- random

- re

#### Version:

- Python 3.5
