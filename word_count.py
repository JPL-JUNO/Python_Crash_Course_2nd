def count_words(filenames):
    """
    该函数可以实现输入文件的字数统计
    :param filenames: 需要计数的文件名
    :return: 没有问价则返回错误并提示文件不存在，如果文件存在则统计文件中的单词数量
    """
    try:
        with open(filenames, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        # print(f'Sorry, the file {filenames} does not exist.')
        pass  # 静默失败
    else:
        words = contents.split()
        num_words = len(words)
        print(f'The file {filenames} has about {num_words} words.')


file_name = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']

for filename in file_name:
    count_words(filename)
