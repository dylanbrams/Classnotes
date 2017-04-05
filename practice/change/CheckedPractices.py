ROW_COUNT = 6
COL_COUNT = 7
def check_if_move_made(local_list, col_num, row_num):
    if (len(local_list[col_num]) > row_num):
        return True
    else:
        return False

def convert_to_color(move_number):
    if (int(move_number) % 2 == 0):
        return 'Y'
    else:
        return 'R'

def make_board_variable(local_list):
    printed_board = ''
    printed_board += print_empty_line()
    for row_num in reversed(range(ROW_COUNT)):
        for col_num in (range(COL_COUNT)):
            if(check_if_move_made(local_list,col_num, row_num)):
                printed_board += convert_to_color(local_list[col_num][row_num])
            else:
                printed_board += ' '
        printed_board += '\n'
    printed_board += print_empty_line()
    return printed_board

def print_empty_line():
    return ('-----------')
myotherlist = None
mylist = [[], [], [], [], [], [], []]
mylist[1].append("1")
mylist[1].append("2")
mylist[2].append("3")
mylist[0].append("4")
myboard = make_board_variable (mylist)
print(myboard)

