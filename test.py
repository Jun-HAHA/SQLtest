import streamlit
from sqlalchemy import text

conn = streamlit.connection(
    name = "mysql",
    type = "sql"
)

conn.connect()

FamliyID = streamlit.text_input("id")
FamilyName = streamlit.text_input("name")
FamliyNum = streamlit.text_input("num")

if streamlit.button("123"):
    insertsql = "insert into Famliy (FamilyID, FamilyName, FamilyPeopleNum) values ({},{},{})".format(int(FamliyID), FamilyName, int(FamliyNum))
    with conn.session as s:
        s.execute(text(insertsql))
        s.commit()
    sql = "select * from Family"
    result = conn.query(sql)
    streamlit.write(result)
