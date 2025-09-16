import copy
import random
import math


class MetamorphicTestGenerator4:

    # MR1: 数组元素置换（打乱顺序）
    @staticmethod
    def applyMR1(input_list):
        transformed = copy.deepcopy(input_list)
        random.shuffle(transformed)
        return transformed

    # MR2: 数组元素常数加法
    @staticmethod
    def applyMR2(input_list):
        return [x + 3 for x in input_list]

    # MR3_1: 加入单位元不变性（加法的单位元0）
    @staticmethod
    def applyMR3_1(input_list):
        return input_list + [0.0]

    # MR3_2: 加入单位元不变性（乘法的单位元1）
    @staticmethod
    def applyMR3_2(input_list):
        return input_list + [1.0]

    # MR4: 数组元素取倒数
    @staticmethod
    def applyMR4(input_list):
        transformed = []
        for x in input_list:
            if x == 0:
                transformed.append(0.0)  # 避免除零
            else:
                transformed.append(1.0 / x)
        return transformed

    # MR5: 数组缩放变换
    @staticmethod
    def applyMR5(input_list, constant):
        return [x * constant for x in input_list]

    # MR6: 数组反转变换
    @staticmethod
    def applyMR6(input_list):
        return list(reversed(input_list))

    # MR7_1: 中立操作的恒等变换（所有元素乘以1）
    @staticmethod
    def applyMR7_1(input_list):
        return [x * 1 for x in input_list]

    # MR7_2: 中立操作的恒等变换（所有元素加上0）
    @staticmethod
    def applyMR7_2(input_list):
        return [x + 0 for x in input_list]

    # MR8: 重复输入数组
    @staticmethod
    def applyMR8(input_list):
        return input_list + input_list

    # MR9: 复合转换一致性
    @staticmethod
    def applyMR9(input_list, constant):
        transformed = [x * constant for x in input_list]
        transformed.sort()
        return transformed

    # MR10: 单调性检验
    @staticmethod
    def applyMR10(input_list):
        transformed = []
        count = 0
        for x in input_list:
            transformed.append(x + count)
            count += 1
        return transformed

    # MR11: 边界值替换（把最大值替换成0）
    @staticmethod
    def applyMR11(input_list):
        transformed = copy.deepcopy(input_list)
        max_index = transformed.index(max(transformed))
        transformed[max_index] = 0.0
        return transformed

    # MR12: 数值取反变换
    @staticmethod
    def applyMR12(input_list):
        return [-x for x in input_list]

    # MR13: 微小增量调整
    @staticmethod
    def applyMR13(input_list):
        return [x + 1e-10 for x in input_list]

    # MR14: 移除元素的效果（移除最大值）
    @staticmethod
    def applyMR14(input_list):
        max_val = max(input_list)
        return [x for x in input_list if x != max_val]

    # MR15: 类三角函数的周期性
    @staticmethod
    def applyMR15(input_list):
        return [math.pi - x for x in input_list]

    # MR16: 重复值稳健性（复制输入中的一个元素）
    @staticmethod
    def applyMR16(input_list):
        return input_list + [input_list[0]]

    # MR19: 输入重复（元素复制）将元素a重复多次插入序列中
    @staticmethod
    def applyMR19(input_list, count):
        return input_list + [input_list[0]] * count

    # MR20: 边界值灵敏度（给最小值增加一个极小值）
    @staticmethod
    def applyMR20(input_list):
        transformed = input_list[:]
        min_val = min(transformed)
        return [x + 1e-10 if x == min_val else x for x in transformed]

    # MR22: 应用恒等变换
    @staticmethod
    def applyMR22(input_list):
        return input_list[:]
