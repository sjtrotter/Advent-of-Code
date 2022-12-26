#!/usr/bin/python

inputfile = open("input.txt", "r")
data = inputfile.readlines()
inputfile.close()

data_list = []
for line in data:
    data_list.append(line.replace('\n',''))

# print(data_list)

box_config = data_list[:data_list.index('')]
procedure = data_list[data_list.index('')+1:]
# print(box_config)
# print(procedure)

# print(box_config[-1].split())

# lastnum = int(box_config[-1].split()[-1])
# # print(lastnum)

# box_heights = len(box_config)

# columns = {}
# for x in range(1, lastnum+1):
#     columns[x] = []
#     for y in range(0,box_heights-1):
#         columns[x].append(box_config[y][x-1(+4):x+2])


# print(columns)


class Cargo_Ops():
    def __init__(self, config):

        self.lastnum = int(config[-1].split()[-1])
        box_heights = len(config) - 2

        self.columns = {}
        for x in range(0, self.lastnum):
            self.columns[x+1] = []
            for y in range(0, box_heights + 1):
                if config[box_heights - y][x*4:x*4+3] != "   ":
                    self.columns[x+1].append(config[box_heights - y][x*4:x*4+3])

    def __str__(self):
        return str(self.columns)

    def get_top_crate(self, column):
        return self.columns[column][-1]

    def crane(self, number_of_boxes, column_from, column_to):

        move_boxes = ['a']
        for i in range(1, number_of_boxes + 1):
            move_boxes.append(self.columns[column_from].pop())
        
        for i in range(1, len(move_boxes)):
            self.columns[column_to].append(move_boxes[-i])

        # for i in range(number_of_boxes): # for part 1
        #     move_box = self.columns[column_from].pop()
        #     self.columns[column_to].append(move_box)
        #     print("moved", move_box, "from", column_from, "to", column_to)


cargo_ops = Cargo_Ops(box_config)
# print(cargo_ops)
# print(cargo_ops.get_top_crate(2))
# cargo_ops.crane(1,2,1)
# print(cargo_ops)

# print(procedure)

for line in procedure:
    move, num, fr, col_from, to, col_to = line.split()
    cargo_ops.crane(int(num), int(col_from), int(col_to))

print(cargo_ops)

tops = ""
for col in range(1, cargo_ops.lastnum +1):
    tops += cargo_ops.get_top_crate(col)[1]

print(tops)