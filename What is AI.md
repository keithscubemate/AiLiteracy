# Overview

This page will cover:

- Symbolic AI (rules, expert systems)
- Statistical ML (regression, clustering, trees, SVMs, boosting)
- Neural networks (perceptrons, CNNs, RNNs)
- Genetic / evolutionary algorithms
- Exercises:
	+ Train a simple decision tree on a CSV (e.g., iris dataset).
	+ Implement a tiny neural net from scratch (e.g., XOR problem).
    + P5 rockets

## Genetic / evolutionary algorithms

Genetic algs work by taking Darwinian principles and applying them to pieces of an algorithm:

- Heredity: A parent instance of the parameters must be able to give traits to a child instance.
- Variation: There has to be population variation for there to be enough "genetic information" for some traits to win or lose.
- Selection: There has to be an "environment" for these instances to be "fit" for.

### Step 1: Population Creation

You need a population for evolution.
This means you need a way to create a population.
Each of these creatures/instances/elements need a collection of "traits" or "DNA" to:

1. Exhibit behavior.
2. Pass successful traits to offspring.

Here the genetic ideas of genotype and phenotype are useful.
Genotype could be considered as the collection of traits that any one of your instances hold.
The phenotype would then be how these "genes" present.

In a basic example, a genotype could be a byte and the phenotype could be the 256 bit color it represents.
