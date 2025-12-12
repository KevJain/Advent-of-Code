input = open("input.txt").read().split("\n\n")
shapes = [[l for l in s.split()[1:4]] for s in input[:6]]
regions = input[6].strip().split("\n")
shape_sizes = [sum(l.count('#') for l in s) for s in shapes]
definitely_valid = [] # can be created by using shapes as 3x3 tiles
possibly_valid = [] # might be valid by a more efficient tiling
invalid = [] # number of squares is less than total places

for region in regions:
    #print(region)
    length, width = [*map(int, region.split()[0][:5].split('x'))]
    shape_counts = [*map(int, region.split()[1:])]
    total_count = sum(shape_counts)
    if length // 3 * width // 3 >= total_count:
        definitely_valid.append(region)
    elif length * width < sum(shape_size * shape_count for (shape_size, shape_count) in zip(shape_sizes, shape_counts)):
        invalid.append(region)
    else:
        possibly_valid.append(region)

print(len(definitely_valid))
print(len(possibly_valid))
print(len(invalid))
