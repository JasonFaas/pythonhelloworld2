#look say

def look_say(line_count):
    current_line = "1"
    return_lines = str(current_line)

    for line_itr in range(1, line_count):
        former_line = str(current_line)
        current_line = ""
        current_char = former_line[0]
        current_char_cnt = 1
        for num_itr in range(1, len(former_line)):
            if current_char == former_line[num_itr]:
                current_char_cnt += 1
            else:
                current_line += str(current_char_cnt)
                current_line += str(current_char)
                current_char_cnt = 1
                current_char = former_line[num_itr]

        current_line += str(current_char_cnt)
        current_line += str(current_char)

        return_lines += "\n"
        return_lines += current_line


    # if line_count == 2:
    print("\n\n\n" + return_lines)
    return return_lines



assert(look_say(1) == "1")
assert(look_say(2) == "1\n11")
assert(look_say(3) == "1\n11\n21")
assert(look_say(4) == "1\n11\n21\n1211")
assert(look_say(5) == "1\n11\n21\n1211\n111221")

