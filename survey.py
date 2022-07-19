class AnonymousSurvey:
    """
    收集匿名调差问卷的答案
    """
    def __init__(self, question):
        """
        存储一个问题， 并为存储答案做准备
        :param question:
        """
        self.question = question
        self.responses = []

    def show_question(self):
        """
        显示调查问卷
        :return:
        """
        print(self.question)

    def store_response(self, new_response):
        """
        存储单份调查问卷
        :param new_response: 
        :return:
        """
        self.responses.append(new_response)

    def show_result(self):
        """
        显示收集到的所有问卷
        :return:
        """
        print('Survey results:')
        for response in self.responses:
            print(f'-{response}')

