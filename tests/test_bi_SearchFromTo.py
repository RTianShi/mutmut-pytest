import pytest
import pytest_check as check
from bi_SearchFromTo import bi_SearchFromTo
from MetamorphicTestGenerator4 import MetamorphicTestGenerator4


def applyMR_Assert(originalInput, originalResult, key, from_, to):
    # MR1: 数组元素置换
    #transformInput1 = MetamorphicTestGenerator4.applyMR1(originalInput)
    #transformResult1 = bi_SearchFromTo(transformInput1, key, from_, to)

    # MR2: 数组元素常数加法
    #transformInput2 = MetamorphicTestGenerator4.applyMR2(originalInput)
    #transformResult2 = bi_SearchFromTo(transformInput2, key, from_, to)

    # MR3_1: 加法单位元 0
    transformInput3_1 = MetamorphicTestGenerator4.applyMR3_1(originalInput)
    transformResult3_1 = bi_SearchFromTo(transformInput3_1, key, from_, to)

    # MR3_2: 乘法单位元 1
    transformInput3_2 = MetamorphicTestGenerator4.applyMR3_2(originalInput)
    transformResult3_2 = bi_SearchFromTo(transformInput3_2, key, from_, to)

    # MR4: 数组元素取倒数
    #transformInput4 = MetamorphicTestGenerator4.applyMR4(originalInput)
    #transformResult4 = bi_SearchFromTo(transformInput4, key, from_, to)

    # MR5: 数组缩放变换
   # transformInput5 = MetamorphicTestGenerator4.applyMR5(originalInput)
    #transformResult5 = bi_SearchFromTo(transformInput5, key, from_, to)

    # MR6: 数组反转变换
    #transformInput6 = MetamorphicTestGenerator4.applyMR6(originalInput)
    #transformResult6 = bi_SearchFromTo(transformInput6, key, from_, to)

    # MR7_1: 所有元素乘以1
    transformInput7_1 = MetamorphicTestGenerator4.applyMR7_1(originalInput)
    transformResult7_1 = bi_SearchFromTo(transformInput7_1, key, from_, to)

    # MR7_2: 所有元素加0
    transformInput7_2 = MetamorphicTestGenerator4.applyMR7_2(originalInput)
    transformResult7_2 = bi_SearchFromTo(transformInput7_2, key, from_, to)

    # MR8: 重复输入数组
    transformInput8 = MetamorphicTestGenerator4.applyMR8(originalInput)
    transformResult8 = bi_SearchFromTo(transformInput8, key, from_, to)

    # MR9: 复合转换一致性
    #transformInput9 = MetamorphicTestGenerator4.applyMR9(originalInput)
   # transformResult9 = bi_SearchFromTo(transformInput9, key, from_, to)

    # MR10: 单调性检验
    transformInput10 = MetamorphicTestGenerator4.applyMR10(originalInput)
    transformResult10 = bi_SearchFromTo(transformInput10, key, from_, to)

    # MR11: 边界值替换
    #transformInput11 = MetamorphicTestGenerator4.applyMR11(originalInput)
    #transformResult11 = bi_SearchFromTo(transformInput11, key, from_, to)

    # MR12: 数值取反变换
    #transformInput12 = MetamorphicTestGenerator4.applyMR12(originalInput)
    #transformResult12 = bi_SearchFromTo(transformInput12, key, from_, to)

    # MR13: 微小增量调整
    transformInput13 = MetamorphicTestGenerator4.applyMR13(originalInput)
    transformResult13 = bi_SearchFromTo(transformInput13, key, from_, to)

    # MR14: 移除元素（移除最大值）
   # transformInput14 = MetamorphicTestGenerator4.applyMR14(originalInput)
    #transformResult14 = bi_SearchFromTo(transformInput14, key, from_, to)

    # MR15: 随机置乱
    #transformInput15 = MetamorphicTestGenerator4.applyMR15(originalInput)
    #transformResult15 = bi_SearchFromTo(transformInput15, key, from_, to)

    # MR16: 重复值稳健性
   # transformInput16 = MetamorphicTestGenerator4.applyMR16(originalInput)
    #transformResult16 = bi_SearchFromTo(transformInput16, key, from_, to)

    # MR19: 插入无关元素
    #transformInput19 = MetamorphicTestGenerator4.applyMR19(originalInput)
    #transformResult19 = bi_SearchFromTo(transformInput19, key, from_, to)

    # MR20: 边界值灵敏度
   # transformInput20 = MetamorphicTestGenerator4.applyMR20(originalInput)
    #transformResult20 = bi_SearchFromTo(transformInput20, key, from_, to)

    # MR22: 恒等变换
    transformInput22 = MetamorphicTestGenerator4.applyMR22(originalInput)
    transformResult22 = bi_SearchFromTo(transformInput22, key, from_, to)

    # ---------------- Assertions ----------------
    # 这里直接翻译 Java 的断言逻辑，示例几条，其他保持一致
   # check.equal(originalResult, transformResult1, "MR1 failed")
    #check.equal(originalResult, transformResult2, "MR2 failed")
    check.equal(originalResult, transformResult3_1, "MR3_1 failed")
    check.equal(originalResult, transformResult3_2, "MR3_2 failed")
    #check.is_true(originalResult >= transformResult4, "MR4 failed")
    #check.equal(originalResult, transformResult5, "MR5 failed")
    #check.equal(originalResult, transformResult6, "MR6 failed")
    check.equal(originalResult, transformResult7_1, "MR7_1 failed")
    check.equal(originalResult, transformResult7_2, "MR7_2 failed")
    check.equal(originalResult, transformResult8, "MR8 failed")
    #check.equal(originalResult, transformResult9, "MR9 failed")
    check.is_true(originalResult >= transformResult10, "MR10 failed")
    #check.is_true(originalResult == transformResult11, "MR11 failed")
    #check.equal(-originalResult, transformResult12, "MR12 failed")
    check.is_true(originalResult >= transformResult13, "MR13 failed")
   # check.is_true(originalResult >= transformResult14, "MR14 failed")
    #check.equal(originalResult, transformResult15, "MR15 failed")
    #check.equal(originalResult, transformResult16, "MR16 failed")
   # check.equal(originalResult, transformResult19, "MR19 failed")
    #check.is_true(originalResult <= transformResult20, "MR20 failed")
    check.equal(originalResult, transformResult22, "MR22 failed")


@pytest.mark.parametrize("originalInput, key, from_, to", [
    ([1, 2, 3, 6, 9], 3, 0, 4),
    ([1, 2, 2, 4, 4], 4, 0, 4),
    ([-2, -2, 2, 6, 8], 6, 0, 4),
    ([1, 2, 3, 5, 9], 1, 0, 5) ,
    ([-3, -3, -1, 1, 9], -3, 0, 4) ,
    ([2, 2, 3, 3, 6, 8], 6, 0, 5) ,
    ([-5, 1, 2, 3, 4, 6], -5, 0, 5) ,
    ([2, 2, 4, 5, 7], 7, 0, 5) ,
    ([1, 1, 2, 2, 4], 2, 0, 5) ,
    ([-2, 1, 3, 4, 7], 4, 0, 4),
])
def test_bi_SearchFromTo(originalInput, key, from_, to):
    originalResult = bi_SearchFromTo(originalInput, key, from_, to)
    applyMR_Assert(originalInput, originalResult, key, from_, to)
