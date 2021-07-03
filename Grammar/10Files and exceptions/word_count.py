def count_words(filename):
  """ 计算一个文件大致包含多少个单词。 """
  try:
    with open(filename, encoding='utf-8') as f:
      contents = f.read()
  except FileNotFoundError:
    # 静默失败，像什么没有发生一样继续运行
    pass
    # print(f"Sorry, the file {filename} does not exist.")
  else:
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")

filenames = ['./test_files/alice.txt', './test_files/siddhartha.txt', './test_files/moby_dick.txt', './test_files/little_women.txt']
for filename in filenames:
  count_words(filename)
