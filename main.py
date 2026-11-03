import random

FLOW = {
    "root": (None, {"Categorical response variable\n": "cat",
                    "Numerical response variable\n": "num"}),
    ## categorical
    "cat": ("How much empirical data", {"1 group empirical data\n": "cat1",
                                        ">1 group empirical data\n": "cat_multi"}),
    "cat1": ("Events", {"Dichotomous\n": "Binomial distribution",
                        "Rate\n": "Poisson distribution",
                        "Proportions\n": "Proportions test"}),
    "cat_multi": ("Counts?", {"Yes\n": "cat_paired",
                              "No\n": "Proportions Test"}),
    "cat_paired": ("Paired?", {"Paired\n": "McNemar's test",
                               "Independent\n": "cat_strat"}),
    "cat_strat": ("Stratification?", {"Yes\n": "Cochrane-Mantel-Haenszel test",
                                      "No\n": "cat_expect"}),
    "cat_expect": ("Expectation size?", {"Small\n": "Fisher's test",
                                         "Not small\n": "Chi-squared test"}),

    ## numerical
    "num": ("How much empirical data", {">1 group\n": "num_count",
                                        "1 group\n": "num_know"}),
    "num_count": ("How many?", {"2 groups\n": "num_paired",
                                ">2 groups\n": "num_norm1"}),
    "num_know": ("Know sigma?", {"Yes\n": "Z-test",
                                 "No\n": "t-Test"}),
    "num_paired": ("Paired?", {"Paired\n": "num_norm2",
                               "Independent\n": "num_norm3"}),
    "num_norm1": ("Normal?", {"Yes\n": "num_predictors",
                              "No\n": "Kruskal-Wallis"}),
    "num_norm2": ("Normal?", {"Yes\n": "Paired t-test",
                              "No\n": "Sign-rank test"}),
    "num_norm3": ("Normal?", {"Yes\n": "num_variances",
                              "No\n": "Rank-sum test"}),
    "num_predictors": ("N predictors", {"1\n": "One-way ANOVA",
                                        ">1\n": "Multi-way ANOVA"}),
    "num_variances": ("Variances?", {"Not equal\n": "nEVIT",
                                     "Equal": "EVIT"})
}

def prompt(correct_answer: str):
    tries = 0

    while (answer := input().strip().casefold()) != correct_answer.casefold():
        if tries and answer == 'y':
            print(f"Correct answer: {correct_answer}")
            return False
        tries += 1
        print("Incorrect. If you would like to see the solution, type 'y', if you would like to try again, enter your answer: ")
    return tries == 0

def main():
    print("Hi Corinn I miss you good luck on your test")
    print("-------------------------------------------\n")
    key, score, total = 'root', 0, 0

    while True:
        question, branches = FLOW.get(key, (key, None))
        if question:
            score += prompt(question)
            total += 1
        if not branches:
            break
        choice = random.choice(list(branches))
        print(choice)
        key = branches[choice]
    print(f"Score: {score}/{total}")

if __name__ == "__main__":
    main()