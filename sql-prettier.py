import sys
import datetime
import uuid


while True:
    i = input()

    if "SELECT" not in i:
        continue

    print("-" * 50, end="\r\n")

    metadata, query = i.split("SELECT")
    print("[Metadata]", end="\r\n")
    utctime = metadata.strip().split(" ")[0]
    dt = datetime.datetime.fromisoformat(utctime[:len(utctime) - 2])
    dt_kst = dt + datetime.timedelta(hours=9)
    print(f"UUID: {uuid.uuid4().hex}", end="\r\n")
    print(f"KST: {dt_kst.strftime('%Y-%m-%d %H:%M:%S')}", end="\r\n")

    print("", end="\r\n")

    print("[Query]", end="\r\n")

    sql = query.replace("`", "")
    sql = sql.replace("FROM", "\r\nFROM")
    sql = sql.replace("WHERE", "\r\nWHERE")
    sql = sql.replace("ORDER BY", "\r\nORDER BY")
    sql = sql.replace("INNER JOIN", "\r\nINNER JOIN")
    sql = sql.replace("LIMIT", "\r\nLIMIT")

    sql = sql.replace(",", ",\r\n    ")

    current_indent = 0

    sql = sql.replace("(", "\r\n(\r\n")
    sql = sql.replace(")", "\r\n)")
    sql = sql.replace("AND", "\r\nAND")
    sql = sql.replace("OR", "\r\nOR")

    print("SELECT", end="\r\n")
    print("    ", end="")
    for line in sql.split("\r\n"):
        if "(" in line:
            print(" " * current_indent + line, end="\r\n")
            current_indent += 4
        elif ")" in line:
            current_indent -= 4
            print(" " * current_indent + line, end="\r\n")
        else:
            print(" " * current_indent + line, end="\r\n")
