for x in range(32):
    filename=f"puzzle3x3-{x:02d}.txt"
    with open(filename, 'r') as f:
        lines = f.readlines()

    # remove spaces
    lines = [line.replace(' ', '') for line in lines]

    # finally, write lines in the file
    with open(filename, 'w') as f:
        f.writelines(lines)