import os

from otree.api import *


doc = """
Survey
"""


class Constants(BaseConstants):
    name_in_url = 'App_auction'
    players_per_group = None
    num_rounds = 1
    current_working_path = os.getcwd()
    txtFileName = 'survey.txt'
    appFolderName = 'App_auction'
    txtPathName = "%s/%s/%s" % (current_working_path, appFolderName, txtFileName)
    with open(txtPathName, 'r', encoding='utf-8') as file_object:
        text = []
        for line in file_object.readlines():
            text.append(line.strip())
    answer1 = [[1, '非常不同意'], [2, '比较不同意'], [3, '中立'], [4, '比较同意'], [5, '非常同意']]
    answer2 = [[1, '非常低或没有'], [2, '比较低'], [3, '中等'], [4, '比较高'], [5, '非常高']]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    constants = Constants()
    text = constants.text
    answer1 = constants.answer1
    answer2 = constants.answer2

    name = models.StringField(label='请输入你的姓名')
    age = models.IntegerField(label='请选择你的性别', choices=[[1, '男'], [2, '女']])
    gender = models.StringField(label='请输入你的年龄')
    school = models.StringField(label='请输入你的学校名称')
    major = models.StringField(label='请输入你的专业名称')
    MBTI = models.StringField(label='请输入你的MBTI（未测试过请填0）')
    income = models.StringField(label='请输入你的月可支配收入')
    frequency = models.IntegerField(
        label='请选择你购买盲盒的频率（“1”代表购买频率非常低，“5”代表购买频率非常高）',
        choices=answer2,
        widget=widgets.RadioSelectHorizontal
    )
    preference = models.IntegerField(
        label='请选择你喜爱购买盲盒的程度',
        choices=answer2,
        widget=widgets.RadioSelectHorizontal
    )

    risk1 = models.IntegerField(
        choices=[[1, '1/10的概率得20元，9/10的概率得16元'], [2, '1/10的概率得38.5元，9/10的概率得1元']],
        label='风险偏好问卷 Q1',
        widget=widgets.RadioSelect,
    )
    risk2 = models.IntegerField(
        choices=[[1, '2/10的概率得20元，8/10的概率得16元'], [2, '2/10的概率得38.5元，8/10的概率得1元']],
        label='风险偏好问卷 Q2',
        widget=widgets.RadioSelect,
    )
    risk3 = models.IntegerField(
        choices=[[1, '3/10的概率得20元，7/10的概率得16元'], [2, '3/10的概率得38.5元，7/10的概率得1元']],
        label='风险偏好问卷 Q3',
        widget=widgets.RadioSelect,
    )
    risk4 = models.IntegerField(
        choices=[[1, '4/10的概率得20元，6/10的概率得16元'], [2, '4/10的概率得38.5元，6/10的概率得1元']],
        label='风险偏好问卷 Q4',
        widget=widgets.RadioSelect,
    )
    risk5 = models.IntegerField(
        choices=[[1, '5/10的概率得20元，5/10的概率得16元'], [2, '5/10的概率得38.5元，5/10的概率得1元']],
        label='风险偏好问卷 Q5',
        widget=widgets.RadioSelect,
    )
    risk6 = models.IntegerField(
        choices=[[1, '6/10的概率得20元，4/10的概率得16元'], [2, '6/10的概率得38.5元，4/10的概率得1元']],
        label='风险偏好问卷 Q6',
        widget=widgets.RadioSelect,
    )
    risk7 = models.IntegerField(
        choices=[[1, '7/10的概率得20元，3/10的概率得16元'], [2, '7/10的概率得38.5元，3/10的概率得1元']],
        label='风险偏好问卷 Q7',
        widget=widgets.RadioSelect,
    )
    risk8 = models.IntegerField(
        choices=[[1, '8/10的概率得20元，2/10的概率得16元'], [2, '8/10的概率得38.5元，2/10的概率得1元']],
        label='风险偏好问卷 Q8',
        widget=widgets.RadioSelect,
    )
    risk9 = models.IntegerField(
        choices=[[1, '9/10的概率得20元，5/10的概率得16元'], [2, '1/10的概率得38.5元，5/10的概率得1元']],
        label='风险偏好问卷 Q9',
        widget=widgets.RadioSelect,
    )
    risk10 = models.IntegerField(
        choices=[[1, '10/10的概率得20元，0/10的概率得16元'], [2, '10/10的概率得38.5元，0/10的概率得1元']],
        label='风险偏好问卷 Q10',
        widget=widgets.RadioSelect,
    )

    crt1 = models.FloatField(label='Q1：一只球和一把球拍的总价值是1.10元，球拍的价值比球贵1元。那么球的价值是多少元？')
    crt2 = models.IntegerField(label='Q2：如果有5台机器可以在5分钟内制造5个零件，那么用100台机器制造100个零件需要多少分钟？')
    crt3 = models.IntegerField(label='Q3：在一个湖里，睡莲每天增长一倍。如果需要48天将湖泛满，那么从开始到湖泛满需要多少天？')

    q22 = models.IntegerField(label=text[21], choices=answer1, widget=widgets.RadioSelectHorizontal)
    q23 = models.IntegerField(label=text[22], choices=answer1, widget=widgets.RadioSelectHorizontal)
    q24 = models.IntegerField(label=text[23], choices=answer1, widget=widgets.RadioSelectHorizontal)
    q25 = models.IntegerField(label=text[24], choices=answer1, widget=widgets.RadioSelectHorizontal)
    q26 = models.IntegerField(label=text[25], choices=answer1, widget=widgets.RadioSelectHorizontal)
    q27 = models.IntegerField(label=text[26], choices=answer1, widget=widgets.RadioSelectHorizontal)
    q28 = models.IntegerField(label=text[27], choices=answer1, widget=widgets.RadioSelectHorizontal)
    q29 = models.IntegerField(label=text[28], choices=answer1, widget=widgets.RadioSelectHorizontal)
    q30 = models.IntegerField(label=text[29], choices=answer1, widget=widgets.RadioSelectHorizontal)
    q31 = models.IntegerField(label=text[30], choices=answer1, widget=widgets.RadioSelectHorizontal)
    q32 = models.IntegerField(label=text[31], choices=answer1, widget=widgets.RadioSelectHorizontal)
    q33 = models.IntegerField(label=text[32], choices=answer1, widget=widgets.RadioSelectHorizontal)
    q34 = models.IntegerField(label=text[33], choices=answer1, widget=widgets.RadioSelectHorizontal)
    q35 = models.IntegerField(label=text[34], choices=answer1, widget=widgets.RadioSelectHorizontal)
    q36 = models.IntegerField(label=text[35], choices=answer1, widget=widgets.RadioSelectHorizontal)
    q37 = models.IntegerField(label=text[36], choices=answer2, widget=widgets.RadioSelectHorizontal)
    q38 = models.IntegerField(label=text[37], choices=answer2, widget=widgets.RadioSelectHorizontal)
    q39 = models.IntegerField(label=text[38], choices=answer1, widget=widgets.RadioSelectHorizontal)
    q40 = models.IntegerField(label=text[39], choices=answer1, widget=widgets.RadioSelectHorizontal)
    q41 = models.IntegerField(label=text[40], choices=answer1, widget=widgets.RadioSelectHorizontal)


# PAGES
class MyPage(Page):
    form_model = 'player'
    form_fields = ['name', 'gender', 'age', 'school', 'major', 'MBTI', 'income', 'frequency', 'preference']


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


class BlindboxSurvey(Page):
    form_model = 'player'
    form_fields = ['q22', 'q23', 'q24', 'q25', 'q26', 'q27', 'q28', 'q29', 'q30', 'q31', 'q32', 'q33', 'q34', 'q35',
                   'q36', 'q37', 'q38', 'q39', 'q40', 'q41']


class RiskSurvey(Page):
    form_model = 'player'
    form_fields = ['risk1', 'risk2', 'risk3', 'risk4', 'risk5', 'risk6', 'risk7', 'risk8', 'risk9', 'risk10']


class CRTSurvey(Page):
    form_model = 'player'
    form_fields = ['crt1', 'crt2', 'crt3']


page_sequence = [MyPage, CRTSurvey, RiskSurvey, BlindboxSurvey, Results]
