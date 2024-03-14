import os
import time
from xlsxwriter import Workbook
import pandas as pd
import numpy as np
from ranking import RankingManager
from ranking.FeaturesRankingManager import features_ranking_multiple_bugs
from ranking.Keywords import *
from ranking.RankingManager import VARCOP_RANK, SBFL_RANK, \
    ranking_multiple_bugs, VARCOP_SPACE, SPACE, get_executed_stms_of_the_system, get_set_of_stms
from util.FileManager import join_path, EXPERIMENT_RESULT_FOLDER, list_dir, get_spc_log_file_path
from ranking.VarBugManager import is_var_bug_by_config
from spc import SPCsManager
from suspicious_statements_manager import SlicingManager
from suspicious_statements_manager.SuspiciousStatementManager import get_multiple_buggy_statements, \
    get_suspicious_statement_varcop, get_suspicious_statement_tc_based

BUG_ID_COL = 0
VARCOP_BUGGY_STM_COL = 1
VARCOP_RANK_COL = 2
VARCOP_EXAM_COL = 3
VARCOP_SPACE_COL = 4
VARCOP_TC_SLICED_RANK_COL = 5
VARCOP_TC_SLICED_EXAM_COL = 6
SBFL_TC_SLICED_RANK_COL = 7
SBFL_TC_SLICED_EXAM_COL = 8
FB_TC_SLICED_RANK_COL = 9
FB_TC_SLICED_EXAM_COL = 10
TC_SLICED_SPACE_COL = 11
VARCOP_DISABLE_BPC_RANK_COL = 12
VARCOP_DISABLE_BPC_EXAM_COL = 13
SBFL_RANK_COL = 14
SBFL_EXAM_COL = 15
FB_RANK_COL = 16
FB_EXAM_COL = 17
SPACE_COL = 18
IS_VAR_BUG_COL = 19

def write_header_in_result_file(row, sheet):
    sheet.write(row, BUG_ID_COL, BUG_ID)
    sheet.write(row, VARCOP_BUGGY_STM_COL, BUGGY_STM)

    sheet.write(row, VARCOP_RANK_COL, VARCOP_RANK)
    sheet.write(row, VARCOP_EXAM_COL, VARCOP_EXAM)
    sheet.write(row, VARCOP_SPACE_COL, VARCOP_SPACE)

    sheet.write(row, VARCOP_TC_SLICED_RANK_COL, VARCOP_TC_RANK)
    sheet.write(row, VARCOP_TC_SLICED_EXAM_COL, VARCOP_TC_EXAM)

    sheet.write(row, SBFL_TC_SLICED_RANK_COL, SBFL_TC_RANK)
    sheet.write(row, SBFL_TC_SLICED_EXAM_COL, SBFL_TC_EXAM)

    sheet.write(row, FB_TC_SLICED_RANK_COL, FB_TC_RANK)
    sheet.write(row, FB_TC_SLICED_EXAM_COL, FB_TC_EXAM)

    sheet.write(row, TC_SLICED_SPACE_COL, TC_SPACE)

    sheet.write(row, VARCOP_DISABLE_BPC_RANK_COL, VARCOP_DISABLE_BPC_RANK)
    sheet.write(row, VARCOP_DISABLE_BPC_EXAM_COL, VARCOP_DISABLE_BPC_EXAM)

    sheet.write(row, SBFL_RANK_COL, SBFL_RANK)
    sheet.write(row, SBFL_EXAM_COL, SBFL_EXAM)

    sheet.write(row, FB_RANK_COL, FB_RANK)
    sheet.write(row, FB_EXAM_COL, FB_EXAM)

    sheet.write(row, SPACE_COL, SPACE)
    sheet.write(row, IS_VAR_BUG_COL, "IS_VAR_BUG")


def write_result_to_file(row, sheet, ranking_results, fb_results, search_spaces, is_var_bug):
    varcop_space = len(get_set_of_stms(search_spaces[SS_VARCOP]))
    sliced_space = len(get_set_of_stms(search_spaces[SS_SLICING]))
    all_space = len(get_set_of_stms(search_spaces[SS_STMS_IN_F_PRODUCTS]))
    all_stms = len(get_set_of_stms(search_spaces[SS_ALL_STMS]))

    for stm in ranking_results[VARCOP_RANK].keys():
        sheet.write(row, VARCOP_BUGGY_STM_COL, stm)      #VARCOP_BUGGY_STM_COL = 1

        if is_var_bug:
            sheet.write(row, VARCOP_RANK_COL, ranking_results[VARCOP_RANK][stm][RANK])
            sheet.write(row, VARCOP_EXAM_COL, (ranking_results[VARCOP_RANK][stm][RANK] / all_stms) * 100)
        else:
            sheet.write(row, VARCOP_RANK_COL, ranking_results[VARCOP_DISABLE_BPC_RANK][stm][RANK])
            sheet.write(row, VARCOP_EXAM_COL, (ranking_results[VARCOP_DISABLE_BPC_RANK][stm][RANK] / all_stms) * 100)
            sheet.write(row, IS_VAR_BUG_COL, 0)

        sheet.write(row, VARCOP_SPACE_COL, varcop_space)

        sheet.write(row, VARCOP_TC_SLICED_RANK_COL, ranking_results[VARCOP_TC_RANK][stm][RANK])
        sheet.write(row, VARCOP_TC_SLICED_EXAM_COL, (ranking_results[VARCOP_TC_RANK][stm][RANK] / all_stms) * 100)
        # sheet.write(row, SBFL_TC_SLICED_RANK_COL, ranking_results[SBFL_TC_RANK][stm][RANK])
        # sheet.write(row, SBFL_TC_SLICED_EXAM_COL, (ranking_results[SBFL_TC_RANK][stm][RANK] / all_stms) * 100)
        # sheet.write(row, FB_TC_SLICED_RANK_COL, fb_results[FB_TC_RANK][stm][RANK])
        # sheet.write(row, FB_TC_SLICED_EXAM_COL, (fb_results[FB_TC_RANK][stm][RANK] / all_stms) * 100)

        sheet.write(row, TC_SLICED_SPACE_COL, sliced_space)

        sheet.write(row, VARCOP_DISABLE_BPC_RANK_COL, ranking_results[VARCOP_DISABLE_BPC_RANK][stm][RANK])
        sheet.write(row, VARCOP_DISABLE_BPC_EXAM_COL,
                    (ranking_results[VARCOP_DISABLE_BPC_RANK][stm][RANK] / all_stms) * 100)
        # sheet.write(row, SBFL_RANK_COL, ranking_results[SBFL_RANK][stm][RANK])
        # sheet.write(row, SBFL_EXAM_COL, (ranking_results[SBFL_RANK][stm][RANK] / all_stms) * 100)
        # sheet.write(row, FB_RANK_COL, fb_results[FB_RANK][stm][RANK])
        # sheet.write(row, FB_EXAM_COL, (fb_results[FB_RANK][stm][RANK] / all_stms) * 100)
        sheet.write(row, SPACE_COL, all_space)

        row += 1
    return row


def suspicious_isolation(mutated_project_dir, filtering_coverage_rate, coverage_version, mutated_project_name):
    a,spc_time, total_counter, each_jie_spc_number, switches_rate_list, saved_counter_list = SPCsManager.find_SPCs(mutated_project_dir, filtering_coverage_rate, mutated_project_name)
    # spc_log_file_path = get_spc_log_file_path(mutated_project_dir, filtering_coverage_rate)
    # SlicingManager.do_slice(spc_log_file_path, filtering_coverage_rate, coverage_version)
    return spc_time, total_counter, each_jie_spc_number, switches_rate_list, saved_counter_list


def get_suspicious_space(mutated_project_dir, filtering_coverage_rate, coverage_version):
    if coverage_version == "":
        stms_isolated_by_varcop = get_suspicious_statement_varcop(mutated_project_dir,
                                                                  filtering_coverage_rate)
    else:
        post_fix = str(filtering_coverage_rate) + "_" + coverage_version + "_"
        stms_isolated_by_varcop = get_suspicious_statement_varcop(mutated_project_dir, post_fix)

    tc_sliced_based_isolation = get_suspicious_statement_tc_based(mutated_project_dir)
    all_stms_of_the_system, all_stms_in_failing_products = get_executed_stms_of_the_system(
        mutated_project_dir, coverage_version, filtering_coverage_rate)
    search_spaces = {SS_VARCOP: stms_isolated_by_varcop, SS_SLICING: tc_sliced_based_isolation,
                     SS_ALL_STMS: all_stms_of_the_system,
                     SS_STMS_IN_F_PRODUCTS: all_stms_in_failing_products}
    return search_spaces


def multiple_bugs_ranking(system_name, buggy_systems_folder, sbfl_metrics, alpha=0.5,
                          normalization=NORMALIZATION_ENABLE,
                          aggregation=AGGREGATION_ARITHMETIC_MEAN,
                          filtering_coverage_rate=0.1, coverage_version=""):

    if os.path.exists(buggy_systems_folder):
        mutated_projects = list_dir(buggy_systems_folder)

        result_folder_dir = join_path(EXPERIMENT_RESULT_FOLDER, "w=" + str(alpha))   #EXPERIMENT_RESULT_FOLDER = experiment_results
        if not os.path.exists(result_folder_dir):
            os.makedirs(result_folder_dir)

        system_result_dir = join_path(result_folder_dir, system_name)
        if not os.path.exists(system_result_dir):
            os.makedirs(system_result_dir)

        normalization_result_dir = join_path(system_result_dir, normalization)
        if not os.path.exists(normalization_result_dir):
            os.makedirs(normalization_result_dir)

        aggregation_result_dir = join_path(normalization_result_dir, aggregation)
        if not os.path.exists(aggregation_result_dir):
            os.makedirs(aggregation_result_dir)

        sheet = []
        row = 0
        experiment_file_name = join_path(aggregation_result_dir,
                                        system_name + "_ranking_result_3Bug_Dis.xlsx")

        wb = Workbook(experiment_file_name)

        for i in range(0, len(sbfl_metrics)):
            sheet.append(wb.add_worksheet(sbfl_metrics[i]))
            write_header_in_result_file(row, sheet[i])
        row += 1
        num_of_bugs = 0
        run_time = 0
        each_bug_times_df = []
        exm2_switches_rate_df = []
        exm2_saved_rate_df = []
        for mutated_project_name in mutated_projects:

            start_time = time.time()
            num_of_bugs += 1
            mutated_project_dir = join_path(buggy_systems_folder, mutated_project_name)
            each_project_start_time = time.time()
            spc_time, total_counter, each_jie_spc_number, switches_rate, saved_counter_rate = suspicious_isolation(mutated_project_dir, filtering_coverage_rate, coverage_version, mutated_project_name)   #核心1
            # each_bug_times_df.append(each_jie_spc_number)
            exm2_switches_rate_df.append(switches_rate)
            exm2_saved_rate_df.append(saved_counter_rate)
            # print("filtering_coverage_rate为:", filtering_coverage_rate, coverage_version, mutated_project_dir)
            search_spaces = get_suspicious_space(mutated_project_dir, filtering_coverage_rate, coverage_version)
            buggy_statements = get_multiple_buggy_statements(mutated_project_name, mutated_project_dir)  #读取mutant.log文件得到异常语句

            row_temp = row

            if system_name == "ZipMe":
                is_a_var_bug = is_var_bug_by_config(mutated_project_dir, ["Base", "Compress"])
            else:
                is_a_var_bug = is_var_bug_by_config(mutated_project_dir, ["Base"])

            ranking_results, varcop_ranking_time = ranking_multiple_bugs(buggy_statements,
                                                                         mutated_project_dir,
                                                                         search_spaces,
                                                                         sbfl_metrics,
                                                                         aggregation,
                                                                         normalization,
                                                                         coverage_version,
                                                                         filtering_coverage_rate, alpha)   #返回所有bug的位置和运行时间

        #     run_time = run_time + each_project_end_time
            fb_ranking_results = features_ranking_multiple_bugs(buggy_statements, mutated_project_dir,
                                                                search_spaces,
                                                                filtering_coverage_rate, sbfl_metrics)
            each_project_end_time = time.time() - each_project_start_time
            print("each_BUG_project_time:", each_project_end_time)
            each_bug_times_df.append(each_project_end_time)

            for metric in range(0, len(sbfl_metrics)):
                sheet[metric].write(row_temp, BUG_ID_COL, mutated_project_name)
                row = write_result_to_file(row_temp, sheet[metric],
                                           ranking_results[sbfl_metrics[metric]],
                                           fb_ranking_results[sbfl_metrics[metric]], search_spaces,
                                           is_a_var_bug)
            total_time = time.time()-start_time
            print("spc_time rate: ", spc_time/total_time)
        wb.close()
        print("run_time: ", run_time)
        arr_spcTime = np.array(each_bug_times_df)
        df_spcTime = pd.DataFrame(arr_spcTime)
        df_spcTime.to_csv('/home/whn/codes/work2/VARCOP-gh-pages/run_time/RunTime_FVBFL_ZipMe_1BUG-new.csv')
        # df = pd.DataFrame(arr, columns=['1Jie', '2Jie', '3Jie', '4Jie', '5Jie', '6Jie', '7Jie'])
        # df.to_csv('/home/whn/codes/work2/VARCOP-gh-pages/spc_counter/spcNumber_ExamDB_1BUG.csv')

        # arr = np.array(exm2_switches_rate_df)
        # arr2 = np.array(exm2_saved_rate_df)
        # df = pd.DataFrame(arr)
        # df2 = pd.DataFrame(arr2)
        # df.to_csv('/home/whn/codes/work2/VARCOP-gh-pages/spc_counter/switches_rate_ExamDB_1BUG.csv')
        # df2.to_csv('/home/whn/codes/work2/VARCOP-gh-pages/spc_counter/saved_rate_ExamDB_1BUG.csv')

def write_runtime_to_file(system_result_dir, run_time, file_name):
    experiment_file_name = join_path(system_result_dir,
                                     file_name)
    if os.path.exists(experiment_file_name):
        return
    wb = Workbook(experiment_file_name)
    sheet = wb.add_worksheet("run_time")
    row = 0
    for item in run_time.keys():
        sheet.write(row, 0, item)
        col = 1
        for time in run_time[item]:
            sheet.write(row, col, time)
            col += 1
        row += 1
    wb.close()
