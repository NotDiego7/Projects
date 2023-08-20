import pandas
# --------------------------------- Read File -------------------------------- #

census_data = pandas.read_csv(filepath_or_buffer="228 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")

# ---------------------------- Get Specific Column --------------------------- #

fur_color_data = census_data["Primary Fur Color"]

# ---------------------------- Get Data in Column ---------------------------- #

color_counts = []
fur_colors = ["Black", "Gray", "Cinnamon"]

color_counts.append(len(fur_color_data[fur_color_data == "Black"]))
color_counts.append(len(fur_color_data[fur_color_data == "Gray"]))
color_counts.append(len(fur_color_data[fur_color_data == "Cinnamon"]))

# --------------------------- Create CSV from lists -------------------------- #

fur_color_analyzis = pandas.DataFrame(data=list(zip(fur_colors, color_counts)), columns=["Fur Colors", "Count"])
fur_color_analyzis.to_csv(path_or_buf="Fur Color Analysis Results")

# print(fur_color_analyzis)
