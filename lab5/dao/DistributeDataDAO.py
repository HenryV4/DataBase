from flask import current_app

class DistributeDataDAO:
    @staticmethod
    def distribute_randomly():
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.callproc('distribute_data_randomly')
            current_app.mysql.connection.commit()
            cursor.close()
            return {"status": "success", "message": "Data distributed randomly into new tables"}
        except Exception as e:
            current_app.mysql.connection.rollback()
            raise Exception(f"Error distributing data: {str(e)}")
