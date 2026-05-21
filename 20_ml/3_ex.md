# Gini Index - Decision Tree Example

## Dataset

| Row | Credit Score | Employed | Loan Status |
| --- | ------------ | -------- | ----------- |
| 1   | High         | No       | Approved    |
| 2   | High         | Yes      | Approved    |
| 3   | Low          | Yes      | Approved    |
| 4   | Low          | No       | Reject      |

---

## Step 1: Calculate Root Gini Index

```
Total Samples (N) = 4
Approved (+) = 3    |    Reject (-) = 1

Gini Formula:  G = 1 - (p+)^2 - (p-)^2

p+ = 3/4 = 0.75
p- = 1/4 = 0.25

G(root) = 1 - (0.75)^2 - (0.25)^2
        = 1 - 0.5625 - 0.0625
        = 0.375
```

---

## Step 2: Split Candidate 1 — Credit Score

### Left Branch (Credit Score = High) → Rows 1, 2

| Row | Credit Score | Loan Status |
| --- | ------------ | ----------- |
| 1   | High         | Approved    |
| 2   | High         | Approved    |

```
Approved = 2    |    Reject = 0    |    Total = 2

G(left) = 1 - (2/2)^2 - (0/2)^2
        = 1 - 1 - 0
        = 0
```

### Right Branch (Credit Score = Low) → Rows 3, 4

| Row | Credit Score | Loan Status |
| --- | ------------ | ----------- |
| 3   | Low          | Approved    |
| 4   | Low          | Reject      |

```
Approved = 1    |    Reject = 1    |    Total = 2

G(right) = 1 - (1/2)^2 - (1/2)^2
         = 1 - 0.25 - 0.25
         = 0.5
```

### Weighted Gini for Credit Score Split

```
G(Credit) = (2/4 x 0) + (2/4 x 0.5)
          = 0 + 0.25
          = 0.25
```

---

## Step 3: Split Candidate 2 — Employed

### Left Branch (Employed = Yes) → Rows 2, 3

| Row | Employed | Loan Status |
| --- | -------- | ----------- |
| 2   | Yes      | Approved    |
| 3   | Yes      | Approved    |

```
Approved = 2    |    Reject = 0    |    Total = 2

G(left) = 1 - (2/2)^2 - (0/2)^2
        = 1 - 1 - 0
        = 0
```

### Right Branch (Employed = No) → Rows 1, 4

| Row | Employed | Loan Status |
| --- | -------- | ----------- |
| 1   | No       | Approved    |
| 4   | No       | Reject      |

```
Approved = 1    |    Reject = 1    |    Total = 2

G(right) = 1 - (1/2)^2 - (1/2)^2
         = 1 - 0.25 - 0.25
         = 0.5
```

### Weighted Gini for Employed Split

```
G(Employed) = (2/4 x 0) + (2/4 x 0.5)
            = 0 + 0.25
            = 0.25
```

---

## Step 4: Compare Splits

| Split Feature  | Gini Index | Result   |
| -------------- | ---------- | -------- |
| Credit Score   | 0.25       | Tie      |
| Employed       | 0.25       | Tie      |

> Both splits have equal Gini = 0.25
> Either feature can be chosen as the root node.

---

## Decision Tree Visualization

### Tree 1: Credit Score as Root

```
                        [Credit Score?]
                         Gini = 0.375
                        /             \
                (High)                 (Low)
                  /                        \
          [Approved]                  [Employed?]
          Gini = 0                     Gini = 0.5
                                      /          \
                                (Yes)             (No)
                                 /                    \
                          [Approved]              [Reject]
                          Gini = 0               Gini = 0
```

### Tree 2: Employed as Root (Alternative)

```
                          [Employed?]
                           Gini = 0.375
                          /          \
                    (Yes)             (No)
                      /                  \
              [Approved]           [Credit Score?]
              Gini = 0               Gini = 0.5
                                    /          \
                              (High)           (Low)
                                /                 \
                         [Approved]           [Reject]
                         Gini = 0             Gini = 0
```

> In both cases, the tree correctly classifies all 4 samples.
> Leaf nodes have Gini = 0 (pure nodes — all same class).
