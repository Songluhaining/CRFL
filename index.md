## A Variability Fault Localization Approach for Software Product Lines

Software fault localization is one of the most expensive, tedious, and time-consuming activities in program debugging. This activity becomes even much more challenging in Software Product Line (SPL) systems due to variability of failures. These unexpected behaviors are induced by variability faults which can only be exposed under some combinations of system features. The interaction among these features causes the failures of the system.  Although localizing bugs in single-system engineering has been studied in-depth, variability fault localization in SPL systems still remains mostly unexplored. In this article, we present VarCop, a novel and effective variability fault localization approach.  For an SPL system failed by variability bugs, VarCop isolates suspicious code statements by analyzing the overall test results of the sampled products and their source code. The isolated suspicious statements are the statements related to the interaction among the features which are necessary for the visibility of the bugs in the system. In VarCop, the suspiciousness of each isolated statement is assessed based on both the overall test results of the products containing the statement as well as the detailed results of the test cases executed by the statement in these products. On a large public dataset of buggy SPL systems, our empirical evaluation shows that VarCop significantly improves two state-of-the-art fault localization techniques by 33% and 50% in ranking the incorrect statements in the systems containing a single bug each. In about two-thirds of the cases, VarCop correctly ranks the buggy statements at the top-3 positions in the resulting lists.  Moreover, for the cases containing multiple bugs,  VarCop outperforms the state-of-the-art approaches 2 times and 10 times in the proportion of bugs localized at the top-1 positions. Especially, in 22% and 65% of the buggy versions, VarCop correctly ranks at least one bug in a system at the top-1 and top-5 positions.  

### Empirical results
1. Performance Comparison
    1. VarCop's performance compared to the state-of-the-art approaches 
        1. [By Rank and EXAM](https://github.com/ttrangnguyen/VARCOP/blob/gh-pages/experiment_results/Analysis/SINGLE_BUG/PERFORMANCE%20COMPARISON/performance_comparsion.xlsx)
        2. [By Hit@X](https://github.com/ttrangnguyen/VARCOP/blob/gh-pages/experiment_results/Analysis/SINGLE_BUG/PERFORMANCE%20COMPARISON/Hit%40X.xlsx)
    1. [VarCop's performance by Mutation Operators causing bugs](https://github.com/ttrangnguyen/VARCOP/blob/gh-pages/experiment_results/Analysis/SINGLE_BUG/PERFORMANCE%20COMPARISON/performance_mutation_operators.xlsx)
    1. [VarCop's performance by bugs' code elements](https://github.com/ttrangnguyen/VARCOP/blob/gh-pages/experiment_results/Analysis/SINGLE_BUG/PERFORMANCE%20COMPARISON/performance_code_elements.xlsx)
    1. [VarCop's performance by the number of involving features](https://github.com/ttrangnguyen/VARCOP/blob/gh-pages/experiment_results/Analysis/SINGLE_BUG/PERFORMANCE%20COMPARISON/performance_num_of_involving_features.xlsx)
1. Intrinsic Analysis
    1. [Impact of Suspicious Statement Isolation on performance](https://github.com/ttrangnguyen/VARCOP/blob/gh-pages/experiment_results/Analysis/SINGLE_BUG/INTRINSIC%20ANALYSIS/Suspicious_statements_isolation_impact.xlsx)
    1. [Impact of choosing Metric of Local Suspiciousness Measurement on performance](https://github.com/ttrangnguyen/VARCOP/blob/gh-pages/experiment_results/Analysis/SINGLE_BUG/PERFORMANCE%20COMPARISON/performance_comparsion.xlsx)
    1. [Impact of Normalization on performance](https://github.com/ttrangnguyen/VARCOP/blob/gh-pages/experiment_results/Analysis/SINGLE_BUG/INTRINSIC%20ANALYSIS/Normalization%20Impact.xlsx)
    1. [Impact of choosing Aggreation Function of Global Suspiciousness Measurement on performance](https://github.com/ttrangnguyen/VARCOP/blob/gh-pages/experiment_results/Analysis/SINGLE_BUG/INTRINSIC%20ANALYSIS/Aggreation_function_impact.xlsx)
    2. [Impact of choosing Combination Weight when combining Suspiciousness scores](https://github.com/ttrangnguyen/VARCOP/blob/gh-pages/experiment_results/Analysis/SINGLE_BUG/INTRINSIC%20ANALYSIS/Combination_weight_impact.xlsx)
1. Sensitivity Analysis
    1. [Impact of Sample Size on performance](https://github.com/ttrangnguyen/VARCOP/blob/gh-pages/experiment_results/Analysis/SINGLE_BUG/SENSITIVITY%20ANALYSIS/sample_size_impact.xlsx)
    1. [Impact of Test Suite's Size on performance](https://github.com/ttrangnguyen/VARCOP/blob/gh-pages/experiment_results/Analysis/SINGLE_BUG/SENSITIVITY%20ANALYSIS/test_suite_size_impact.xlsx)
1. [Performance In Localizing Multiple Bugs](https://github.com/ttrangnguyen/VARCOP/tree/gh-pages/experiment_results/Analysis/MULTIPLE_BUG)
1. [Time Complexity](https://github.com/ttrangnguyen/VARCOP/tree/gh-pages/experiment_results/Analysis/RUNTIME)

#### VarCop's source code [Link](https://github.com/ttrangnguyen/VARCOP)
#### Dataset [Link](https://tuanngokien.github.io/splc2021/)
#### Slicing tool [Link](https://github.com/ttrangnguyen/Static_Slicing)

