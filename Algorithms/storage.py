import os


def get_folder_Size(path):
    total_size = 0

    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size / (1024 * 1024)


def main():
    path = r'C:\AMDAcp_v6.0.0.111_id_1'
    size = get_folder_Size(path)
    print(f"Size of {path}: {size:.2f} MiB")


if __name__ == '__main__':
    main()