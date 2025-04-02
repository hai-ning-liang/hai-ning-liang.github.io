# import json

# # Load the JSON data
# file_path = "C:/Users/Yichuan.Zhang/Documents/Haining_Page/hai-ning-liang.github.io-main/_data/pubInfo.json"



# import json

# # Load the JSON data


# with open(file_path, "r", encoding="utf-8") as f:
#     data = json.load(f)

# # Modify the "authors" field
# for entry in data:
#     authors = entry["authors"]
#     # Split the authors at every " and ", except for the last one
#     authors_parts = authors.split(" and ")
    
#     # Reassemble the parts with ", " and only keep " and " between the last two authors
#     if len(authors_parts) > 1:
#         entry["authors"] = ", ".join(authors_parts[:-1]) + " and " + authors_parts[-1]
#     else:
#         entry["authors"] = authors_parts[0]  # In case there is only one author

# # Save the updated JSON back to a file

# with open(file_path, "w", encoding="utf-8") as f:
#     json.dump(data, f, indent=2, ensure_ascii=False)

import json

# Load the JSON data
file_path = "C:/Users/Yichuan.Zhang/Documents/Haining_Page/hai-ning-liang.github.io-main/_data/pubInfo.json"

# Load the JSON data
with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# 统计年份为2023, 2024, 2025的对象数量
years_count = {2023: 0, 2024: 0, 2025: 0}

# 遍历 JSON 数据并统计年份
for entry in data:
    year = entry.get("year")
    if year in years_count:
        years_count[year] += 1

print(years_count)
