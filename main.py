import random

FLOW = {
    "root": (None, {"Categorical response variable": "cat",
                    "Numerical response variable": "num"}),
    ## categorical
    "cat": ("How much empirical data", {"1 group empirical data": "cat1",
                                        ">1 group empirical data": "cat_multi"}),
    "cat1": ("Events", {"Dichotomous": "Binomial distribution",
                        "Rate": "Poisson distribution",
                        "Proportions": "Proportions test"}),
    "cat_multi": ("Counts?", {"Yes": "cat_paired",
                              "No": "Proportions Test"}),
    "cat_paired": ("Paired?", {"Paired": "McNemar's test",
                               "Independent": "cat_strat"}),
    "cat_strat": ("Stratification?", {"Yes": "Cochrane-Mantel-Haenszel test",
                                      "No": "cat_expect"}),
    "cat_expect": ("Expectation size?", {"Small": "Fisher's test",
                                         "Not small": "Chi-squared test"}),

    ## numerical
    "num": ("How much empirical data", {">1 group": "num_count",
                                        "1 group": "num_know"}),
    "num_count": ("How many?", {"2 groups": "num_paired",
                                ">2 groups": "num_norm1"}),
    "num_know": ("Know sigma?", {"Yes": "Z-test",
                                 "No": "t-Test"}),
    "num_paired": ("Paired?", {"Paired": "num_norm2",
                               "Independent": "num_norm3"}),
    "num_norm1": ("Normal?", {"Yes": "num_predictors",
                              "No": "Kruskal-Wallis"}),
    "num_norm2": ("Normal?", {"Yes": "Paired t-test",
                              "No": "Sign-rank test"}),
    "num_norm3": ("Normal?", {"Yes": "num_variances",
                              "No": "Rank-sum test"}),
    "num_predictors": ("N predictors", {"1": "One-way ANOVA",
                                        ">1": "Multi-way ANOVA"}),
    "num_variances": ("Variances?", {"Not equal": "nEVIT",
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
    print("-------------------------------------------")
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