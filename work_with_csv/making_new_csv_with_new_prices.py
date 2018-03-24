destination_old_file = "catalog_sample.csv"
destination_new_file = "catalog_sample_new.csv"

with open(destination_old_file, encoding = "utf-8") as old_f:
    with open(destination_new_file, "w", encoding = "utf-8") as new_f:
        for line in old_f:
            old_line = line.strip()
            old_line_split = old_line.split(",")[::-1]
            old_line_split[0] = "%.2f" %(float(old_line_split[0]) * 1.75)
            old_line_split.reverse()
            new_line = ",".join(old_line_split)
            new_f.write(new_line+"\n")