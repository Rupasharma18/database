import meradb
db = meradb.load("table.db")
# db1 = meradb.load("EKFILE.db")
db.set("num", 20)
db.set("age", 20)
db.set("name", "rupa")
db.get("age")
db.get_all()
db.rem("age")
db.exist_key("age")
db.total_keys()

# # db.dump()
# db.random_insert(10)
# db.del_db()


