# app.py
from flask import Flask, jsonify
import logging
from flask_mysqldb import MySQL
from routes.LocationRoute import location_bp
from routes.ChainRoute import chain_bp
from routes.HotelRoute import hotel_bp
from routes.RoomRoute import room_bp
from routes.DiscountCardRoute import discount_card_bp
from routes.ClientRoute import client_bp
from routes.PaymentRoute import payment_bp
from routes.BookingRoute import booking_bp
from routes.ReviewRoute import review_bp
from routes.AmenitiesRoute import amenities_bp
from routes.HotelAmenitiesRoute import hotel_amenities_bp
from routes.ClientHotelRoute import client_hotel_bp
from routes.DistributeDataRoute import distribute_data_bp
from routes.BookingLogRoute import booking_log_bp
from routes.StatRoute import stat_bp


# Initialize Flask app
app = Flask(__name__)
app.config['DEBUG'] = True
mysql = MySQL(app) 

# MySQL configurations
app.config['MYSQL_USER'] = 'root'  # Your MySQL username
app.config['MYSQL_PASSWORD'] = ''  # Your MySQL password
app.config['MYSQL_DB'] = 'lab5'  # Your database name
app.config['MYSQL_HOST'] = 'localhost'  # MySQL host

app.mysql = mysql

logging.basicConfig(level=logging.INFO)
app.logger.setLevel(logging.DEBUG)

# Register blueprints for routes
app.register_blueprint(location_bp, url_prefix='/api')
app.register_blueprint(chain_bp, url_prefix='/api')
app.register_blueprint(hotel_bp, url_prefix='/api')
app.register_blueprint(room_bp, url_prefix='/api')
app.register_blueprint(discount_card_bp, url_prefix='/api')
app.register_blueprint(client_bp, url_prefix='/api')
app.register_blueprint(payment_bp, url_prefix='/api')
app.register_blueprint(booking_bp, url_prefix='/api')
app.register_blueprint(review_bp, url_prefix='/api')
app.register_blueprint(amenities_bp, url_prefix='/api')
app.register_blueprint(hotel_amenities_bp, url_prefix='/api')
app.register_blueprint(client_hotel_bp, url_prefix='/api')
app.register_blueprint(distribute_data_bp, url_prefix='/api')
app.register_blueprint(booking_log_bp, url_prefix='/api')
app.register_blueprint(stat_bp, url_prefix='/api')

@app.route('/')
def show_tables():
    try:
        # Create a cursor to execute the query
        cursor = mysql.connection.cursor()
        cursor.execute("SHOW TABLES;")  # This query will fetch all tables in the database
        tables = cursor.fetchall()  # Fetch all results
        cursor.close()  # Close the cursor

        # Return the list of table names as a JSON response
        return jsonify({"tables": [table[0] for table in tables]}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # If there's an error, return an error message


# Test route to verify the MySQL connection
@app.route('/test_db')
def test_db():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT 1")
        return "Database connection is working!"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
