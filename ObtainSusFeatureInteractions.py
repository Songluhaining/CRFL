import numpy as np
import pandas as pd
from sympy import false

from ranking.Keywords import AGGREGATION_ARITHMETIC_MEAN, NORMALIZATION_ENABLE
from ranking.MultipleBugsManager import multiple_bugs_ranking
from spc import SPCsManager
from util.FileManager import list_dir, join_path
from ranking.Spectrum_Expression import JACCARD, SORENSEN_DICE, TARANTULA, OCHIAI, OP2, BARINEL, DSTAR, ROGERS_TANIMOTO, \
    AMPLE, \
    SIMPLE_MATCHING, RUSSELL_RAO, COHEN, SCOTT, ROGOT1, GEOMETRIC_MEAN, M2, WONG1, SOKAL, DICE, HUMANN, ZOLTAR, \
    WONG2, ROGOT2, EUCLID, HAMMING, FLEISS, ANDERBERG, KULCZYNSKI2, HARMONIC_MEAN, GOODMAN


def run_RQ1_and_RQ2(system, buggy_systems_folder, mutated_projects):
    runtime_df = []
    n_way_FI_df = []
    inclusion_rate_df = []
    duplication_rate_df = []
    for mutated_project_name in mutated_projects:
        mutated_project_dir = join_path(buggy_systems_folder, mutated_project_name)
        spc_log_file_path, spc_time, total_counter, nway_spc_number, inclusion_rate, duplication_rate = SPCsManager.find_SPCs(system, mutated_project_dir, 0.1)
        runtime_df.append(spc_time)
        n_way_FI_df.append(nway_spc_number)
        inclusion_rate_df.append(inclusion_rate)
        duplication_rate_df.append(duplication_rate)
    arr_spcTime = np.array(runtime_df)
    df_spcTime = pd.DataFrame(arr_spcTime)
    df_spcTime.to_csv('./experiment_results/run_time/RunTime_CRFL-' + system + '.csv')

    arr_jie = np.array(n_way_FI_df)
    df = pd.DataFrame(arr_jie, columns=['1-way', '2-way', '3-way', '4-way', '5-way', '6-way', '7-way'])
    df.to_csv('./experiment_results/spc_counter/n-way_CRFL-' + system + '.csv')

    arr = np.array(inclusion_rate_df)
    arr2 = np.array(duplication_rate_df)
    df = pd.DataFrame(arr)
    df2 = pd.DataFrame(arr2)
    df.to_csv('./experiment_results/spc_counter/InclusionRate_CRFL-' + system + '.csv')
    df2.to_csv('./experiment_results/spc_counter/DuplicationRate_CRFL-' + system + '.csv')

def run_RQ3(system, buggy_systems_folder):
    sbfl_metrics = [TARANTULA, OCHIAI, OP2, BARINEL, DSTAR,
                    RUSSELL_RAO, SIMPLE_MATCHING, ROGERS_TANIMOTO, AMPLE, JACCARD,
                    COHEN, SCOTT, ROGOT1, GEOMETRIC_MEAN, M2,
                    WONG1, SOKAL, SORENSEN_DICE, DICE, HUMANN,
                    WONG2, EUCLID, ZOLTAR,
                    ROGOT2, HAMMING, FLEISS, ANDERBERG,
                    GOODMAN, HARMONIC_MEAN, KULCZYNSKI2]
    normalization = NORMALIZATION_ENABLE
    aggregation = AGGREGATION_ARITHMETIC_MEAN
    w = 0.5
    multiple_bugs_ranking(system_name=system, buggy_systems_folder=buggy_systems_folder, sbfl_metrics=sbfl_metrics,
                          alpha=w, normalization=normalization, aggregation=aggregation)

def parse_arguments():
    import argparse

    parser = argparse.ArgumentParser(description='Run experiments')

    #Argument to run all experiments
    parser.add_argument('--RQ1', action='store_true', help='Run all experiments of RQ1', default=True)
    # Argument to run all experiments
    parser.add_argument('--RQ3', action='store_true', help='Run all experiments of RQ3', default=True)
    #Argument to run one specific experiment
    parser.add_argument('--system', help='System name', default="BankAccountTP")
    # Argument to run one specific SPL system
    parser.add_argument('--buggy_systems_folder', help='Run specific SPL', default="./examples/4wise-BankAccountTP-1BUG-Full")

    args = parser.parse_args()
    return args

def main(args):
    buggy_systems_folder = args.buggy_systems_folder
    mutated_projects = list_dir(buggy_systems_folder)
    print(mutated_projects)
    print(buggy_systems_folder)
    system_name = args.system
    # RQ1 and RQ2
    if args.RQ1:
        run_RQ1_and_RQ2(system=system_name, buggy_systems_folder=buggy_systems_folder, mutated_projects=mutated_projects)
    # RQ3
    if args.RQ3:
        run_RQ3(system=system_name, buggy_systems_folder=buggy_systems_folder)


if __name__ == '__main__':
    args = parse_arguments()
    main(args)