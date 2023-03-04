import pandas as pd
import numpy as np


def build_node(color_array, size_array, save_path, length=160):
    assert len(size_array) == len(color_array) == length
    df_dress = pd.read_excel("data/destriux_160.xlsx")
    with open(save_path, "w") as f:
        for i in range(length):
            f.write("{} {} {} {} {} {}\n".format(
                str(df_dress["x"][i]),
                str(df_dress["y"][i]),
                str(df_dress["z"][i]),
                str(color_array[i]),
                str(size_array[i]),
                str(df_dress["name"][i]),
            ))


if __name__ == "__main__":
    example_color_array = np.asarray([0.0] * 30 + [1.0] * 50 + [2.0] * 80)  # numpy.ndarray
    example_size_array = [0.0 for i in range(160)]  # list
    build_node(example_color_array, example_size_array, "output/example.node")
