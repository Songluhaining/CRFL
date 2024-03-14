import time
import os
from ranking import RankingManager
from ranking.Keywords import *
from util.FileManager import join_path
from ranking.MultipleBugsManager import multiple_bugs_ranking
from ranking.Spectrum_Expression import JACCARD, SORENSEN_DICE, TARANTULA, OCHIAI, OP2, BARINEL, DSTAR, ROGERS_TANIMOTO, \
    AMPLE, \
    SIMPLE_MATCHING, RUSSELL_RAO, COHEN, SCOTT, ROGOT1, GEOMETRIC_MEAN, M2, WONG1, SOKAL, DICE, HUMANN, ZOLTAR, \
    WONG2, ROGOT2, EUCLID, HAMMING, FLEISS, ANDERBERG, KULCZYNSKI2, HARMONIC_MEAN, GOODMAN


sys_name = "ZipMe"
dataset_folder = "/home/whn/Desktop/4wise-ZipMe-1BUG-Full"  # system path




def delete_files_with_name(directory, file_name):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file == file_name:
                file_path = os.path.join(root, file)
                os.remove(file_path)
                print(f"Deleted file: {file_path}")




if __name__ == "__main__":

    file_name_to_delete = "spc_10.log"      # 替换为要删除的文件名
    file_name_to_delete_2 = "slicing_10.log"

    if not os.path.exists(dataset_folder):
        print(f"Folder {dataset_folder} not found.")
    else:
        delete_files_with_name(dataset_folder, file_name_to_delete)
        delete_files_with_name(dataset_folder, file_name_to_delete_2)


    file_name_1 = '/home/whn/codes/CRFL-gh-pages/run_time/pages_new_ZipMeTest.txt'
    file_name_2 = '/home/whn/codes/CRFL-gh-pages/SPC_set_new_ZipMeTest.txt'

    # 检查文件是否存在
    if os.path.exists(file_name_1):
        os.remove(file_name_1)
    if os.path.exists(file_name_2):
        os.remove(file_name_2)


    # parameter configuration
    system_name = sys_name
    buggy_systems_folder = dataset_folder
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
    # -----------------------
    start_time = time.time()
    multiple_bugs_ranking(system_name=system_name, buggy_systems_folder= buggy_systems_folder, sbfl_metrics=sbfl_metrics,
                          alpha=w, normalization=normalization, aggregation=aggregation)
    total_time = time.time()-start_time
    print("total time:"+str(total_time))
