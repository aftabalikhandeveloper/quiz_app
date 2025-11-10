# creating all tables
from .connection import get_connection


def create_tables():
   
    try:
        conn = get_connection()
        cur = conn.cursor()


        tables_query="""


        CREATE TABLE IF NOT EXISTS teachers (
            teacher_id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            education VARCHAR(150),
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
        );



        """

        cur.execute(tables_query)
        conn.commit()
        cur.close()
        return {"success": True}
    except Exception as e:
        {"success": False, "error": e}
        
