
import random
import pandas as pd

from collections import Counter
from string import ascii_lowercase as letters
from num2words import num2words


class AutoGram(object):

    def __init__(self, prefix='', symbols=letters, seed=7,
                 counts=None, suffix='.'):

        self.prefix = prefix
        if not prefix:
            self.prefix = 'This pangram contains '

        self.symbols = list(symbols)

        self.counts = counts
        if not counts:
            self.counts = {x: 1 for x in self.symbols}

        random.seed(seed)

        self.suffix = suffix
        if not suffix:
            self.suffix = '.'

    def _plural(self, symbol, comma=True):

        text = ''
        if self.counts[symbol] > 1:
            text += symbol + "'s"
        else:
            text += symbol

        if comma:
            text += ', '
        else:
            text += self.suffix

        return text

    def sentence(self):

        sentence = self.prefix
        for symbol in self.symbols[:-1]:
            sentence += num2words(self.counts[symbol]) + ' '
            sentence += self._plural(symbol, True)

        last = self.symbols[-1]
        sentence += 'and '
        sentence += num2words(self.counts[last]) + ' '
        sentence += self._plural(last, False)

        return sentence.lower()

    def check_counts(self):

        counts = Counter(self.sentence())
        counts = {x: y for x, y in counts.items() if x in self.symbols}

        _self_counts = {x: y for x, y in self.counts.items() if x in
                        self.symbols}

        if counts == _self_counts:
            return True, counts

        return False, counts

    def pretty_print(self):

        match, counts = self.check_counts()
        self.symbols.sort()

        print '='*50
        if match:
            print '** autogram generation successful **'
        else:
            print ':( autogram generation not successful'

        print self.sentence()
        print '-'*50

        count_df = pd.DataFrame({
            'symbol': self.symbols,
            'actual_count': [counts[x] for x in self.symbols],
            'accounted_count': [self.counts[x] for x in self.symbols]
        }, columns=['symbol', 'actual_count', 'accounted_count'])
        count_df['match'] = count_df.actual_count == count_df.accounted_count
        print count_df

        print '-'*50
        print 'Number of matches = %s' % count_df.match.sum()
        print '-'*50
        print counts

    def __call__(self, imax=10000):

        i = 0
        match, counts = self.check_counts()
        while not match:
            i += 1
            if i > imax:
                break
            random.shuffle(self.symbols)
            for symbol in self.symbols:
                if self.counts[symbol] != counts[symbol]:
                    self.counts[symbol] = counts[symbol]
                    print '%s updating %s count to %s' % (i, symbol, counts[symbol])
                    match, counts = self.check_counts()
                    break

        self.pretty_print()
