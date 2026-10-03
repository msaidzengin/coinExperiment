# Coin Experiment

A Monte Carlo simulation of a classic Bayes' theorem coin problem.

A bag contains 100 coins. Ninety-nine are fair and land heads or tails with probability 0.5. One coin is unfair and always lands heads. You draw a coin at random, flip it 10 times, and see heads every time. What is the probability that you drew the unfair coin?

`coin.py` repeats that experiment. Among the trials that produced 10 heads, it prints the percentage that used the unfair coin. Bayes' theorem gives about 91.18%. `coin2.py` records the two likelihoods behind that result: `(1/2)^10` for a fair coin and `1` for the unfair coin.

## Run

```bash
python3 coin.py
```

The script uses only the Python standard library. It runs 500,000 experiments and prints the fair count, the unfair count, and the estimated percentage.
