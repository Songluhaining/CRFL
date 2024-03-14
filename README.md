# FCFLA

## Counterfactual Reasoning based Fast Feature Interaction Fault Localization for Software Product Lines

###Overview

![](./MainFramework.pdf)

### Abstract
In Software Product Lines (SPLs), feature interaction faults are those caused by interaction of features. 
Locating such faults is challenging because the number of potential interactions are exponential in the number of features, leading to an enormous search space especially for large SPLs. 
Previous work has partially addressed this challenge by constructing (and then examining) potential feature interactions using suspicious feature selections (e.g., those appearing in failed configurations but not passed ones). 
We argue that the fault location process can be further accelerated by more accurately identifying suspicious feature selection, and systematically avoiding examination of redundant feature interactions. 
To this end, this paper proposes a fast Counterfactual Reasoning based Fault Localization (CRFL) approach for SPLs, which improves the efficiency of the approach in terms of both reducing the search space and repeated computations.
Specifically, CRFL utilizes the counterfactual reasoning to infer suspicious feature selections and symmetric uncertainty to filter irrelevant feature interactions.
In addition, cache mechanisms are used to avoiding the same feature interactions being generated and examined.
Experimental results on six publicly available SPL systems show that our approach reduces the search space by 51%~73% for SPLs with less than ten features and 84%~88% for larger SPLs.
The average detection time of our approach is accelerated about 18 times compared with a state-of-the-art approach.
Moreover, CRFL has superior localization performance when using the same statement-level localization technique with advanced approachs, which shows that CRFL can fast and efficiently localize buggy feature interactions.

This project references [VarCop](https://ttrangnguyen.github.io/VARCOP/) in its code.
And CRFL has less dependency on the platform and libraries used, both Linux and Windows systems can use it normally.
The meaning of arguments are as following:
1. **system_name**: For example Email, GPL, or ZipMe, etc
2. **buggy_systems_folder**: the path of the folder where you place the buggy versions of the systems, e.g. /Users/thu-trangnguyen/SPLSystems/Email/1Bug/4wise/
3. **sbfl_metrics**: The list of spectrum-based fault localization metrics that you would like to use for calculating suspiciousness scores of the statements
4. **w**: the weight (from 0 to 1) used to combine product-based suspiciousness score and test case-based suspiciousness score. The default value is 0.5.

### How to run CRFL?
You can download the full version of data we used at [here](https://tuanngokien.github.io/splc2021/).
Set the corresponding system_name and buggy_systems_folder in Main_BuggyStatements_Ranking.py to run it directly.

### Aggregating the average ranking result of FCFLA, SBFL, S-SBFL, and FB
In order to aggregate the ranking results of the approaches, you can simply configure the appropriate arguments in the file Main_ExperimentalResultAnalysis.py and then execute it.

The meaning of arguments are as following:
1. **experimental_dirs**: The path of excel files containing ranking results that you want to aggregate
2. **num_of_examed_stms**: The number of statements that developers will investigate before giving up. This use to evaluate Hit@X, PBL. The default value is 10.

