import random
import synonyms
import jieba
import jieba.posseg as pseg

common_words = [
        "朋友", "生活", "工作", "学习", "时间", "家庭", "孩子", "父母", "爱人", "家庭",
        "健康", "快乐", "幸福", "成功", "梦想", "目标", "计划", "行动", "努力", "坚持",
        "勇敢", "自信", "乐观", "积极", "消极", "压力", "挑战", "困难", "问题", "解决",
        "思考", "想法", "意见", "建议", "反馈", "沟通", "交流", "合作", "团队", "领导",
        "管理", "创新", "创造", "改变", "改变", "进步", "发展", "成长", "成熟", "经验",
        "知识", "技能", "能力", "水平", "提高", "提升", "培训", "教育", "学习", "学校",
        "老师", "学生", "课程", "考试", "成绩", "结果", "过程", "方法", "策略", "技巧",
        "工具", "资源", "信息", "消息", "新闻", "报纸", "杂志", "书籍", "文章", "报告",
        "论文", "研究", "科学", "技术", "科技", "工程", "项目", "产品", "服务", "客户",
        "市场", "营销", "销售", "广告", "宣传", "推广", "品牌", "公司", "企业", "组织",
        "政府", "政策", "法律", "法规", "制度", "规则", "标准", "规范", "流程", "程序"
    ]

def WordReplace(string):
    words = pseg.cut(string)
    verbs = [word for word, tag in words if tag.startswith("v")]
    random_verb = random.choice(verbs)
    synonyms_verb = []
    syns = synonyms.nearby(random_verb)
    for i in range(1, len(syns[0])):
        if syns[1][i] >= 0.7:
            synonyms_verb.append(syns[0][i])
        else:
            break
    sy_word = random.choice(synonyms_verb)
    string_replaced = string.replace(random_verb, sy_word)
    return string_replaced

def WordAdd(string):
    word_to_add = random.choice(common_words)
    words = jieba.lcut(string)
    pos = random.randint(1, len(words))
    words.insert(pos, word_to_add)
    return "".join(words)

def WordDelete(string):
    words = jieba.lcut(string)
    to_delete = random.randint(0, len(words) - 1)
    del words[to_delete]
    return "".join(words)

def WordSwap(string):
    words = jieba.lcut(string)
    while True:
        rand_1 = random.randint(0, len(words) - 1)
        rand_2 = random.randint(0, len(words) - 1)
        if words[rand_1] != words[rand_2]:
            words[rand_1], words[rand_2] = words[rand_2], words[rand_1]
            break
    return "".join(words)

a = "他毕业于清华大学，是一名优秀的学生。"
print(WordReplace(a))
