"""
Write a bash script to calculate the frequency of each word in a text file words.txt.

For simplicity sake, you may assume:

words.txt contains only lowercase characters and space ' ' characters.
Each word must consist of lowercase characters only.
Words are separated by one or more whitespace characters.
Example:

Assume that words.txt has the following content:

the day is sunny the the
the sunny is is
Your script should output the following, sorted by descending frequency:

the 4
is 3
sunny 2
day 1
Note:

Don't worry about handling ties, it is guaranteed that each word's frequency count is unique.
Could you write it in one-line using Unix pipes?

"""

"""
The cat (short for “concatenate“) command is one of the most frequently used command in Linux/Unix like operating systems.
cat command allows us to create single or multiple files, view contain of file, concatenate files and redirect output in terminal or files.
tr命令，该命令主要用来进行字符替换或者大小写替换，详解请参见这个帖子。后面紧跟的-s参数表示如果发现连续的字符，就把它们缩减为1个，
而后面的‘ ’和‘\n'就是空格和回车，意思是把所有的空格都换成回车
下面的sort命令就是用来排序的
后面的uniq命令是表示去除重复行命令(参见这个帖子)，后面的参数-c表示在每行前加上表示相应行目出现次数的前缀编号，得到结果如下：

   1 day
   3 is
   2 sunny
   4 the

然后我们再sort一下，后面的参数-nr表示按数值进行降序排列，得到结果：

   4 the
   3 is
   2 sunny
   1 day

而最后的awk命令就是将结果输出，两列颠倒位置即可：
"""
cat words.txt | tr -s " " "\n" | sort | uniq -c | sort -r | awk '{print $2, $1}'
