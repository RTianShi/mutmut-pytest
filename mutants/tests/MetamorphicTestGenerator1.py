import random
import math
from typing import List


class MetamorphicTestGenerator1:

    # MR1: 数组元置换（打乱顺序）
    @staticmethod
    def applyMR1(input: List[int]) -> List[int]:
        transformed = input.copy()
        random.shuffle(transformed)
        return transformed

    # MR2: 数组元素常数加法 (+3)
    @staticmethod
    def applyMR2(input: List[int]) -> List[int]:
        transformed = [x + 3 for x in input]
        return transformed

    # MR3_1: 加入单位元不变性（加法的单位元0）
    @staticmethod
    def applyMR3_1(input: List[int]) -> List[int]:
        transformed = input.copy() + [0]
        return transformed

    # MR3_2: 加入单位元不变性（乘法的单位元1）
    @staticmethod
    def applyMR3_2(input: List[int]) -> List[int]:
        transformed = input.copy() + [1]
        return transformed

    # MR4: 数组元素取倒数
    @staticmethod
    def applyMR4(input: List[int]) -> List[float]:
        transformed = [0.0 if x == 0 else 1.0 / x for x in input]
        return transformed

    # MR5: 数组缩放变换
    @staticmethod
    def applyMR5(input: List[int], constant: int) -> List[int]:
        transformed = [x * constant for x in input]
        return transformed

    # MR6: 数组反转变换
    @staticmethod
    def applyMR6(input: List[int]) -> List[int]:
        transformed = list(reversed(input))
        return transformed

    # MR7_1: 所有元素乘以1
    @staticmethod
    def applyMR7_1(input: List[int]) -> List[int]:
        transformed = [x * 1 for x in input]
        return transformed

    # MR7_2: 所有元素加0
    @staticmethod
    def applyMR7_2(input: List[int]) -> List[int]:
        transformed = [x + 0 for x in input]
        return transformed

    # MR8: 重复输入数组
    @staticmethod
    def applyMR8(input: List[int]) -> List[int]:
        transformed = input.copy() + input.copy()
        return transformed

    # MR9: 复合转换一致性（缩放后再排序）
    @staticmethod
    def applyMR9(input: List[int], constant: int) -> List[int]:
        transformed = [x * constant for x in input]
        transformed.sort()
        return transformed

    # MR10: 单调性检验（逐个加增量）
    @staticmethod
    def applyMR10(input: List[int]) -> List[int]:
        transformed = []
        count = 0
        for x in input:
            transformed.append(x + count)
            count += 1
        return transformed

    # MR11: 边界值替换 (把最大值替换成0)
    @staticmethod
    def applyMR11(input: List[int]) -> List[int]:
        transformed = input.copy()
        if not transformed:
            return transformed
        max_val = max(transformed)
        max_index = transformed.index(max_val)
        transformed[max_index] = 0
        return transformed

    # MR12: 数值取反变换
    @staticmethod
    def applyMR12(input: List[int]) -> List[int]:
        transformed = [-x for x in input]
        return transformed

    # MR13: 微小增量调整
    @staticmethod
    def applyMR13(input: List[int]) -> List[float]:
        transformed = [x + 1e-10 for x in input]
        return transformed

    # MR14: 移除元素的效果（移除所有最大值）
    @staticmethod
    def applyMR14(input: List[int]) -> List[int]:
        if not input:
            return []
        max_val = max(input)
        transformed = [x for x in input if x != max_val]
        return transformed

    # MR15: 类三角函数的周期性 (π - x)
    @staticmethod
    def applyMR15(input: List[int]) -> List[float]:
        transformed = [math.pi - x for x in input]
        return transformed

    # MR16: 重复值稳健性（复制第一个元素）
    @staticmethod
    def applyMR16(input: List[int]) -> List[int]:
        if not input:
            return []
        transformed = input.copy() + [input[0]]
        return transformed

    # MR19: 输入重复（元素a重复多次插入）
    @staticmethod
    def applyMR19(input: List[int], count: int) -> List[int]:
        if not input:
            return []
        transformed = input.copy() + [input[0]] * count
        return transformed

    # MR20: 边界值灵敏度（给最小值增加一个极小值）
    @staticmethod
    def applyMR20(input: List[int]) -> List[float]:
        if not input:
            return []
        min_val = min(input)
        transformed = [float(x) for x in input]
        for i in range(len(transformed)):
            if transformed[i] == min_val:
                transformed[i] += 1e-10
        return transformed

    # MR22: 应用恒等变换
    @staticmethod
    def applyMR22(input: List[int]) -> List[int]:
        return input.copy()
