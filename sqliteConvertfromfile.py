with open("skill2.txt", "r", encoding="utf-8") as input_file, open(
    "skill2O.txt", "w", encoding="utf-8"
) as output_file:
    for line in input_file:
        line = line.strip()
        output_file.write(
            f"insert into configuration_skill (name,active,category_id,id) values ('{line}',1,'124e7ca0ae07444b84420b01389ee7a9',(select substr(u,1,8)||''||substr(u,9,4)||'4'||substr(u,13,3)||''||v||substr(u,17,3)||''||substr(u,21,12) from (select lower(hex(randomblob(16))) as u, substr('89ab',abs(random()) % 4 + 1, 1) as v)));\n"
        )
