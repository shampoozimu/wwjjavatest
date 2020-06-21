import random
import string


# 公共工具类组件，提供各种定制化工具


class Random:
    # 随机数工具类

    def __init__(self, boolean_number=True, boolean_lower_case=True, boolean_upper_case=True):
        # 初始化随机数工具
        # 可选参数：
        # boolean_number：生成的随机数是否包含数字
        # boolean_lower_case：生成的随机数是否包含小写字母
        # boolean_upper_case：生成的随机数是否包含大写字母
        self.__universal_set = ""
        if boolean_number: self.__universal_set += string.digits
        if boolean_lower_case: self.__universal_set += string.ascii_lowercase
        if boolean_upper_case: self.__universal_set += string.ascii_uppercase

    def return_sample(self, int_number):
        # 放回抽样：返回的字符串按照放回抽样随机，可以重复
        # int_number：生成的数组长度，长度不限，因为是放回抽样，生成长度可大于样本
        return "".join([random.choice(self.__universal_set) for n in range(int_number)])


class Arrays:
    def __init__(self, list_input):
        self.list_input = list_input

    def dimensionality_reduction(self, list_input):
        # 如果该维度的孙子元素都是数组，对下一级进行降维
        if all([all([list == type(i) for i in input]) for input in list_input]):
            return [self.dimensionality_reduction(input) for input in list_input]
        else:
            l = list()
            [l.append(input) for input in list_input]
            return l

        # class TimeUtils:

    #     def delta(self, delta):
    #         time_result = datetime.datetime.now() + datetime.timedelta(days=delta)
    #         return time_result.strftime("%Y-%m-%d")
    #
    # time_util = TimeUtils()

    # 二向箔，任意维数组转换成二维数组
    def dual_vector_foil(self):
        list_result = list()
        self.__expansion(list_result, self.list_input)
        return list_result

    def __expansion(self, list_result, element):
        if list == type(element):
            [self.__expansion(list_result, e) for e in element]
        else:
            list_result.append(element)
