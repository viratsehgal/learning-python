students = {
    "Virat": [95, 96, 98 ,99],
    "John": [78, 67, 87, 91],
    "Yash": [27, 45, 99, 33],
}

for name, scores in students.items():
    avg = round(sum(scores) / len(scores))
    label = "Pass" if avg >= 50 else "Fail"
    print(f"{name}: Scores = {scores}, Average = {avg}, Result = {label}")