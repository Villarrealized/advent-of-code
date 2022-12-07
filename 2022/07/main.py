def puzzle(part_two=False):
    filesystem = {}
    current_path = []

    for line in open("input.txt"):
        parts = line.split()
        if parts[1] == "cd":
            # Go back a dir by removing last path
            if parts[2] == "..":
                current_path.pop()
            else:
                # Add to current path
                current_path.append(parts[2])

        # Add up the file sizes
        elif parts[0].isnumeric():
            size = int(parts[0])
            # Add the value to all directories in the path
            # so that the parent directories hold the size of the children
            for index in range(1, len(current_path) + 1):
                key = "/".join(current_path[:index])
                # remove the second leading slash
                if len(key) > 1:
                    key = key[1:]

                # Add size to dir (and create if doesn't exist yet)
                if key in filesystem:
                    filesystem[key] += size
                else:
                    filesystem[key] = size

    if not part_two:
        total = 0
        for _, filesize in filesystem.items():
            if filesize <= 100_000:
                total += filesize

        print(f"Part 1: {total}")
    else:
        # The amount of space available for our files
        space_to_free = filesystem["/"] - 40_000_000
        # Find the smallest directory size that we can delete
        # that will free up enough space for our update
        smallest = sorted(
            list(
                filter(
                    lambda size: True if size >= space_to_free else False,
                    filesystem.values(),
                )
            )
        )[0]
        print(f"Part 2: {smallest}")


puzzle()
puzzle(part_two=True)
