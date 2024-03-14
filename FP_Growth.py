import os
import time
from tqdm import tqdm

begin_time = time.time()


# 第一次扫描数据集
def load_data(path):  # 根据路径加载数据集
    ans = []  # 将数据保存到该数组
    if path.split(".")[-1] == ("xls" or "xlsx"):  # 若路径为药方.xls
        from xlrd import open_workbook
        import xlwt
        workbook = open_workbook(path)
        sheet = workbook.sheet_by_index(0)  # 读取第一个sheet
        for i in range(1, sheet.nrows):  # 忽视header,从第二行开始读数据,第一列为处方ID,第二列为药品清单
            temp = sheet.row_values(i)[1].split(";")[:-1]  # 取该行数据的第二列并以“;”分割为数组
            if len(temp) == 0: continue
            temp = [j.split(":")[0] for j in temp]  # 将药品后跟着的药品用量去掉
            temp = list(set(temp))  # 去重，排序
            temp.sort()
            ans.append(temp)  # 将处理好的数据添加到数组
    elif path.split(".")[-1] == "csv":
        import csv
        with open(path, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                row = list(set(row))  # 去重，排序
                row.sort()
                ans.append(row)  # 将添加好的数据添加到数组
    print("ans: ", ans)
    return ans  # 返回处理好的数据集，为二维数组


def save_rule(rule, path):  # 保存结果到txt文件
    with open(path, "w") as f:
        f.write("index  confidence" + "   rules\n")
        index = 1
        for item in rule:
            if str(list(item[1])) == "['9']":
                s = " {:<4d}  {:.3f}        {}=>{}\n".format(index, item[2], str(list(item[0])), str(list(item[1])))
                index += 1
                f.write(s)
        f.close()
    print("result saved,path is:{}".format(path))


class Node:
    def __init__(self, node_name, count, parentNode):
        self.name = node_name
        self.count = count
        self.nodeLink = None  # 根据nideLink可以找到整棵树中所有nodename一样的节点
        self.parent = parentNode  # 父亲节点
        self.children = {}  # 子节点{节点名字:节点地址}


class Fp_growth():
    # 更新头结点
    def update_header(self, node, targetNode):  # 更新headertable中的node节点形成的链表
        while node.nodeLink != None:
            node = node.nodeLink
        node.nodeLink = targetNode

    # 更新树的分支
    def update_fptree(self, items, node, headerTable):  # 用于更新fptree
        if items[0] in node.children:
            # 判断items的第一个结点是否已作为子结点
            node.children[items[0]].count += 1
        else:
            # 创建新的分支
            node.children[items[0]] = Node(items[0], 1, node)
            # 更新相应频繁项集的链表，往后添加
            if headerTable[items[0]][1] == None:
                headerTable[items[0]][1] = node.children[items[0]]
            else:
                self.update_header(headerTable[items[0]][1], node.children[items[0]])
            # 递归
        if len(items) > 1:
            self.update_fptree(items[1:], node.children[items[0]], headerTable)

    # 创建树
    def create_fptree(self, data_set, min_support, flag=False):  # 建树主函数
        '''
        根据data_set创建fp树
        header_table结构为
        {"nodename":[num,node],..} 根据node.nodelink可以找到整个树中的所有nodename
        '''
        item_count = {}  # 统计各项出现次数
        for t in data_set:  # 第一次遍历，得到频繁一项集
            for item in t:
                if item not in item_count:
                    item_count[item] = 1
                else:
                    item_count[item] += 1
        headerTable = {}
        for k in item_count:  # 剔除不满足最小支持度的项
            if item_count[k] >= min_support:
                headerTable[k] = item_count[k]

        freqItemSet = set(headerTable.keys())  # 满足最小支持度的频繁项集
        if len(freqItemSet) == 0:
            return None, None
        for k in headerTable:
            headerTable[k] = [headerTable[k], None]  # element: [count, node]
        tree_header = Node('head node', 1, None)
        if flag:
            ite = tqdm(data_set)
        else:
            ite = data_set
        for t in ite:  # 第二次遍历，建树
            localD = {}
            for item in t:
                if item in freqItemSet:  # 过滤，只取该样本中满足最小支持度的频繁项
                    localD[item] = headerTable[item][0]  # element : count
            if len(localD) > 0:
                # 根据全局频数从大到小对单样本排序
                order_item = [v[0] for v in sorted(localD.items(), key=lambda x: x[1], reverse=True)]
                # 用过滤且排序后的样本更新树
                self.update_fptree(order_item, tree_header, headerTable)
        return tree_header, headerTable

    def find_path(self, node, nodepath):
        '''
        递归将node的父节点添加到路径
        '''
        if node.parent != None:
            nodepath.append(node.parent.name)
            self.find_path(node.parent, nodepath)

    # 找出条件模式基
    def find_cond_pattern_base(self, node_name, headerTable):
        '''
        根据节点名字，找出所有条件模式基
        '''
        treeNode = headerTable[node_name][1]
        cond_pat_base = {}  # 保存所有条件模式基
        while treeNode != None:
            nodepath = []
            self.find_path(treeNode, nodepath)
            if len(nodepath) > 1:
                cond_pat_base[frozenset(nodepath[:-1])] = treeNode.count
            treeNode = treeNode.nodeLink
        return cond_pat_base

    # 条件树
    def create_cond_fptree(self, headerTable, min_support, temp, freq_items, support_data):
        #print("headerTable:", headerTable)
        # 最开始的频繁项集是headerTable中的各元素
        freqs = [v[0] for v in sorted(headerTable.items(), key=lambda p: p[1][0])]  # 根据频繁项的总频次排序
        for freq in freqs:  # 对每个频繁项
            freq_set = temp.copy()
            freq_set.add(freq)
            freq_items.add(frozenset(freq_set))
            if frozenset(freq_set) not in support_data:  # 检查该频繁项是否在support_data中
                support_data[frozenset(freq_set)] = headerTable[freq][0]
            else:
                support_data[frozenset(freq_set)] += headerTable[freq][0]

            cond_pat_base = self.find_cond_pattern_base(freq, headerTable)  # 寻找到所有条件模式基
            cond_pat_dataset = []  # 将条件模式基字典转化为数组
            for item in cond_pat_base:
                item_temp = list(item)
                item_temp.sort()
                for i in range(cond_pat_base[item]):
                    cond_pat_dataset.append(item_temp)
            # 创建条件模式树
            cond_tree, cur_headtable = self.create_fptree(cond_pat_dataset, min_support)
            if cur_headtable != None:
                self.create_cond_fptree(cur_headtable, min_support, freq_set, freq_items, support_data)  # 递归挖掘条件FP树

    # 根据条件树，挖掘频繁项
    def generate_L(self, data_set, min_support):
        freqItemSet = set()
        support_data = {}
        tree_header, headerTable = self.create_fptree(data_set, min_support, flag=True)  # 创建数据集的fptree
        # 创建各频繁一项的fptree，并挖掘频繁项并保存支持度计数
        self.create_cond_fptree(headerTable, min_support, set(), freqItemSet, support_data)

        max_l = 0
        for i in freqItemSet:  # 将频繁项根据大小保存到指定的容器L中
            if len(i) > max_l: max_l = len(i)
        L = [set() for _ in range(max_l)]
        for i in freqItemSet:
            L[len(i) - 1].add(i)
        for i in range(len(L)):
            print("frequent item {}:{}".format(i + 1, len(L[i])))
        return L, support_data

        # 挖掘关联规则

    def generate_R(self, data_set, min_support, min_conf):
        L, support_data = self.generate_L(data_set, min_support)
        rule_list = []
        sub_set_list = []
        for i in range(0, len(L)):
            for freq_set in L[i]:
                for sub_set in sub_set_list:
                    if sub_set.issubset(
                            freq_set) and freq_set - sub_set in support_data:  # and freq_set-sub_set in support_data
                        conf = support_data[freq_set] / support_data[freq_set - sub_set]
                        big_rule = (freq_set - sub_set, sub_set, conf)
                        if conf >= min_conf and big_rule not in rule_list:
                            # print freq_set-sub_set, " => ", sub_set, "conf: ", conf
                            rule_list.append(big_rule)
                sub_set_list.append(freq_set)
        rule_list = sorted(rule_list, key=lambda x: (x[2]), reverse=True)
        return rule_list, sub_set_list


def get_result(data_set, min_support, min_conf):
    spc = []

    # 调用Fp_growth算法
    fp = Fp_growth()
    # 生成关联规则
    rule_list, sub_set_list = fp.generate_R(data_set, min_support, min_conf)
    # print("rule ok")
    print("type:", type(sub_set_list), sub_set_list)
    for item in sub_set_list:
        # i0 = set(item[0])
        # i1 = set(item[1])
        #
        # spc.append(i0)
        # spc.append(i1)
        # i0 = i0.union(i1)
        spc.append(item)

    print(len(spc))
    return spc
    # 保存文件
    # save_rule(rule_list, save_path)

# if __name__ == "__main__":
#
#     # config
#     filename = "/home/whn/Desktop/Email-FH-JML/4wise-Email-FH-JML-1BUG-Full/_MultipleBugs_.NOB_1.ID_2/funs_compone.csv"
#     #filename = "/home/whn/Desktop/OriginalSystem/Email-FH-JML/4wise-Email-FH-JML-Original/4wise-Email-FH-JML/config_fp.csv"
#     min_support = 1  # 最小支持度
#     min_conf = 0.9  # 最小置信度
#     spend_time = []
#     current_path = "/home/whn/Desktop/VARCOP-gh-pages_v2/VARCOP-gh-pages/experiment_results"#os.getcwd()
#     # if not os.path.exists(current_path + "/log"):
#     #     os.mkdir("log")
#
#     path = current_path + "/dataset/" + filename
#     save_path = current_path + "/log/" + "_fpgrowth_Email_Bug2_funs_conpone.txt"
#
#     # 加载数据集
#     data_set = load_data(filename)
#     print("dataset ok", data_set)
#     # print(data_set)
#     # 调用Fp_growth算法
#     fp = Fp_growth()
#     print("fp ok", fp)
#     # 生成关联规则
#     rule_list = fp.generate_R(data_set, min_support, min_conf)
#     print("rule ok")
#     print("type:", type(rule_list), rule_list)
#     print(len(rule_list))
#     # 保存文件
#     save_rule(rule_list, save_path)
# end_time = time.time()
# run_time = end_time - begin_time
# print('该循环程序运行时间：{:.2f}s'.format(run_time))  # 该循环程序运行时间：