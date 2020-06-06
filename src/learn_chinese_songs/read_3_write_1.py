

print("Hello World!")


from os import listdir
from os.path import isfile, join, exists
mypath = 'songs/'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

print(onlyfiles)

english_extension = 'english'
for file_name in onlyfiles:
    if file_name.endswith(english_extension):
        english_file = 'songs/{}'.format(file_name)

        output_file = 'songs/{}'.format(file_name[0:-1 * len(english_extension)] + 'html')

        if not exists(output_file):
            hanzi_file = 'songs/{}'.format(file_name[0:-1 * len(english_extension)] + 'hanzi')
            pinyin_file = 'songs/{}'.format(file_name[0:-1 * len(english_extension)] + 'pinyin')

            hanzi_str = open(hanzi_file, 'r').read()
            pinyin_str = open(pinyin_file, 'r').read()
            english_str = open(english_file, 'r').read()

            hanzi_arr = hanzi_str.split('\n')
            pinyin_arr = pinyin_str.split('\n')
            english_arr = english_str.split('\n')

            th_format = '<th>'
            assert len(english_arr) == len(hanzi_arr) == len(pinyin_arr)
            with open(output_file, 'w') as output_fh:
                output_fh.write('<meta charset="utf-8">')
                output_fh.write('<table cellspacing="10">')

                for itr in range(len(english_arr)):
                    output_fh.write('<tr>')

                    output_fh.write(th_format)
                    output_fh.write(pinyin_arr[itr])
                    output_fh.write('<br>')

                    hanzi_double_space = hanzi_arr[itr].replace(' ', '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;')
                    output_fh.write(hanzi_double_space)
                    # # Table for hanzi to better align with pinyin
                    # output_fh.write('<table align="center" cellspacing="20">')
                    # output_fh.write('<tr>')
                    # print(hanzi_arr[itr])
                    # for hanzi_breakdown in hanzi_arr[itr].split(' '):
                    #     output_fh.write(th_format)
                    #     print(hanzi_breakdown)
                    #     output_fh.write(hanzi_breakdown)
                    #     output_fh.write('</th>')
                    # output_fh.write('</tr>')
                    # output_fh.write('</table>')

                    output_fh.write('</th>')

                    # output_fh.write('<th>')
                    # output_fh.write('</th>')

                    output_fh.write(th_format)
                    output_fh.write(english_arr[itr])
                    output_fh.write('</th>')

                    output_fh.write('</tr>')

                output_fh.write('</table>')



