import re

def solve_1():
    y_req = 2000000
    ys = set()
    beacons_y = set()
    with open("input.txt", "r") as f:
        for l in f.readlines():
            sx, sy, bx, by = map(int, re.findall(r'(?<=\=)(.*?)(?=,|\:|\n)', l))

            if by == y_req:
                beacons_y.add(bx)

            d = abs(bx - sx) + abs(by - sy)
            d -= abs(y_req - sy)
            x = sx
            dx = 0
            for x in range(sx - d, sx + d + 1):
                ys.add(x)
    
    return len(ys - beacons_y)

def solve_2():
    mx = 4_000_000
    y_ranges = [[] for _ in range(mx + 1)]
    with open("input.txt", "r") as f:
        for l in f.readlines():
            sx, sy, bx, by = map(int, re.findall(r'(?<=\=)(.*?)(?=,|\:|\n)', l))

            d = abs(bx - sx) + abs(by - sy)
            dy = 0
            while d > 0:
                x_l = max(0, sx - d)
                x_r = min(mx, sx + d)
                if(sy - dy >= 0):
                    y_ranges[sy - dy].append([x_l, x_r])
                if(sy + dy <= mx and dy):
                    y_ranges[sy + dy].append([x_l, x_r])
                dy += 1
                d -= 1

        for ans_y in range(mx + 1):
            xs = y_ranges[ans_y]
            if not xs:
                continue
            xs.sort()
            
            if xs[0][0] != 0:
                ans_x = 0
                break

            last_e = xs[0][1]
            for i in range(1, len(xs)):
                if last_e >= xs[i][0] - 1:
                    last_e = max(last_e, xs[i][1])
                else:
                    break

            if last_e != mx:
                ans_x = last_e + 1
                break
        
        return 4_000_000 * ans_x + ans_y


def main():
    print(f"Part 1: {solve_1()}")
    print(f"Part 2: {solve_2()}")
    

if __name__ == '__main__':
    main()