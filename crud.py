from conn import conn

class Crud:
    
    def __init__(self, conn, data):
        
        self.conn = conn
        self.data = data
        
        
    def create(self):
        
        cursor = self.conn.cursor()
        cursor.execute("""
        INSERT INTO exam_perfomance
        (gender, race_ethnicity, parental_level_of_education, lunch, test_preparation_course, math_score, reading_score, writing_score)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, self.data)
        self.conn.commit()
        cursor.close()
        self.conn.close()
        
    def read(self):
        
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM exam_perfomance LIMIT 10;")
        rows = cursor.fetchall()
        for r in rows:
            print(r)
        cursor.close()
        self.conn.close()
        
    def update(self):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE exam_perfomance SET %s = %s WHERE id = %s;", (self.data))
        self.conn.commit()
        cursor.close()
        self.conn.close()
        
    def delete(self):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM exam_perfomance WHERE id = %s;", (self.data))
        self.conn.commit()
        cursor.close()
        self.conn.close()
        