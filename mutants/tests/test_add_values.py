import pytest
import pytest_check as check
from add_values import add_values
from MetamorphicTestGenerator1 import MetamorphicTestGenerator1


def applyMR_Assert(originalInput, originalResult):
    # MR2: 数组元素常数加法
    transformInput2 = MetamorphicTestGenerator1.applyMR2(originalInput)
    transformResult2 = add_values(transformInput2)

    # MR3_1: 加法单位元 0
    transformInput3_1 = MetamorphicTestGenerator1.applyMR3_1(originalInput)
    transformResult3_1 = add_values(transformInput3_1)

    # MR3_2: 乘法单位元 1
    transformInput3_2 = MetamorphicTestGenerator1.applyMR3_2(originalInput)
    transformResult3_2 = add_values(transformInput3_2)

    # MR4: 数组元素取倒数
    transformInput4 = MetamorphicTestGenerator1.applyMR4(originalInput)
    transformInput4_1 = [int(x) for x in transformInput4]
    transformResult4 = add_values(transformInput4_1)

    # MR5: 数组缩放变换
    transformInput5 = MetamorphicTestGenerator1.applyMR5(originalInput, 2)
    transformResult5 = add_values(transformInput5)

    # MR6: 数组反转变换
    transformInput6 = MetamorphicTestGenerator1.applyMR6(originalInput)
    transformResult6 = add_values(transformInput6)

    # MR7_1: 所有元素乘以1
    transformInput7_1 = MetamorphicTestGenerator1.applyMR7_1(originalInput)
    transformResult7_1 = add_values(transformInput7_1)

    # MR7_2: 所有元素加0
    transformInput7_2 = MetamorphicTestGenerator1.applyMR7_2(originalInput)
    transformResult7_2 = add_values(transformInput7_2)

    # MR8: 重复输入数组
    transformInput8 = MetamorphicTestGenerator1.applyMR8(originalInput)
    transformResult8 = add_values(transformInput8)

    # MR9: 复合转换一致性
    transformInput9 = MetamorphicTestGenerator1.applyMR9(originalInput, 3)
    transformResult9 = add_values(transformInput9)

    # MR10: 单调性检验
    transformInput10 = MetamorphicTestGenerator1.applyMR10(originalInput)
    transformResult10 = add_values(transformInput10)

    # MR11: 边界值替换(把最大值替换成0)
    transformInput11 = MetamorphicTestGenerator1.applyMR11(originalInput)
    transformResult11 = add_values(transformInput11)

    # MR12: 数值取反变换
    transformInput12 = MetamorphicTestGenerator1.applyMR12(originalInput)
    transformResult12 = add_values(transformInput12)

    # MR13: 微小增量调整
    transformInput13 = MetamorphicTestGenerator1.applyMR13(originalInput)
    transformInput13_1 = [int(x) for x in transformInput13]
    transformResult13 = add_values(transformInput13_1)

    # MR14: 移除元素的效果（移除最大值）
    transformInput14 = MetamorphicTestGenerator1.applyMR14(originalInput)
    transformResult14 = add_values(transformInput14)

    # MR16: 重复值稳健性
    transformInput16 = MetamorphicTestGenerator1.applyMR16(originalInput)
    transformResult16 = add_values(transformInput16)

    # MR20: 边界值灵敏度
    transformInput20 = MetamorphicTestGenerator1.applyMR20(originalInput)
    transformInput20_1 = [int(x) for x in transformInput20]
    transformResult20 = add_values(transformInput20_1)

    # MR22: 应用恒等变换
    transformInput22 = MetamorphicTestGenerator1.applyMR22(originalInput)
    transformResult22 = add_values(transformInput22)

    # ---------------- Assertions ----------------
    check.equal(originalResult + len(originalInput) * 3, transformResult2, "MR2 failed")
    check.equal(originalResult, transformResult3_1, "MR3_1 failed")
    check.equal(originalResult + 1, transformResult3_2, "MR3_2 failed")
    check.is_true(originalResult >= transformResult4, "MR4 failed")
    check.equal(originalResult * 2, transformResult5, "MR5 failed")
    check.equal(originalResult, transformResult6, "MR6 failed")
    check.equal(originalResult, transformResult7_1, "MR7_1 failed")
    check.equal(originalResult, transformResult7_2, "MR7_2 failed")
    check.equal(originalResult * 2, transformResult8, "MR8 failed")
    check.equal(originalResult * 3, transformResult9, "MR9 failed")
    check.is_true(originalResult <= transformResult10, "MR10 failed")
    check.is_true(originalResult >= transformResult11, "MR11 failed")
    check.equal(-originalResult, transformResult12, "MR12 failed")
    check.is_true(originalResult <= transformResult13, "MR13 failed")
    check.is_true(originalResult >= transformResult14, "MR14 failed")
    check.equal(originalResult, transformResult22, "MR22 failed")

@pytest.mark.parametrize("originalInput", [
    [1, 3, 2, 6, 9],
    [2, 1, 4, 4, 2],
    [4, -2, 4, 6, 2],
    [9, 2, 1, 5, 3, 2],
    [-1, 9, 1, -3, -3],
    [8, 3, 2, 6, 2, 3],
    [1, 2, 3, 4, -5, 6],
    [1, 2, 4, 2, 7, 5],
    [1, 1, 2, 4, 1, 2],
    [-2, 3, 1, 4, 7],
])
def test_add_values(originalInput):
    originalResult = add_values(originalInput)
    applyMR_Assert(originalInput, originalResult)
