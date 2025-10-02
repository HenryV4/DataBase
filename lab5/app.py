# app.py
from pathlib import Path
import os
from dotenv import load_dotenv
from flask import Flask, jsonify, request, Response
import logging
from flask_mysqldb import MySQL
from swagger_portal import init_swagger
from flask_cors import CORS

# === blueprints ===
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

# ------------------------
# ENV & CONFIG
# ------------------------
dotenv_path = Path(__file__).with_name('.env')
load_dotenv(dotenv_path=dotenv_path, override=True)

def env(name, default=None, required=False):
    v = os.getenv(name, default)
    if required and (v is None or v == ""):
        raise RuntimeError(f"Missing required env var: {name}")
    return v

# 🔐 Креденшіали для write-операцій (у коді, без .env)
API_USER = "lab"   # змінюй як хочеш (для ЛР ок)
API_PASS = "lab"   # змінюй як хочеш (для ЛР ок)
# Якщо захочеш через .env, просто розкоментуй:
# API_USER = env("API_USER", "lab")
# API_PASS = env("API_PASS", "lab")

# ------------------------
# FLASK APP
# ------------------------
app = Flask(__name__)
app.config['DEBUG'] = False
CORS(app)

# Swagger UI з попапом Authorize (без кешування авторизації)
init_swagger(app, title="Hotel API (Lab5)", version="1.0.0")

# ------------------------
# DB CONFIG
# ------------------------
app.config['MYSQL_HOST'] = env('DB_HOST', '127.0.0.1')
app.config['MYSQL_PORT'] = int(env('DB_PORT', '3306'))
app.config['MYSQL_USER'] = env('DB_USER', required=True)
app.config['MYSQL_PASSWORD'] = env('DB_PASS', required=True)
app.config['MYSQL_DB'] = env('DB_NAME', required=True)

print("== DB settings ==",
      "HOST=", app.config['MYSQL_HOST'],
      "USER=", app.config['MYSQL_USER'],
      "PORT=", app.config['MYSQL_PORT'],
)

mysql = MySQL(app)
app.mysql = mysql

logging.basicConfig(level=logging.INFO)
app.logger.setLevel(logging.DEBUG)

# ------------------------
# SECURITY: захищаємо всі POST/PUT/PATCH/DELETE під /api
# ------------------------
WRITE_METHODS = {"POST", "PUT", "DELETE", "PATCH"}

def _unauthorized():
    return Response(
        "Auth required",
        401,
        {
            "WWW-Authenticate": 'Basic realm="API Login Required"',
            # Браузеру не треба нічого кешувати
            "Cache-Control": "no-store"
        }
    )

@app.before_request
def require_auth_for_write_under_api():
    # захищаємо лише API-шляхи і лише write-методи
    if request.path.startswith("/api") and request.method in WRITE_METHODS:
        auth = request.authorization
        if not auth or not (auth.username == API_USER and auth.password == API_PASS):
            return _unauthorized()

# ------------------------
# BLUEPRINTS
# ------------------------
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

# ------------------------
# ROUTES
# ------------------------
@app.route("/")
def show_tables():
    try:
        cur = mysql.connection.cursor()

        cur.execute("SHOW TABLES;")
        tables = [row[0] for row in cur.fetchall()]

        cur.execute("SELECT @@version, @@version_comment, @@hostname;")
        version, version_comment, hostname = cur.fetchone()

        cur.close()

        is_cloud_sql = ("-google" in str(version).lower()) or ("google" in str(version_comment).lower())

        return jsonify({
            "tables": tables,
            "db_info": {
                "version": version,
                "version_comment": version_comment,
                "hostname": hostname
            },
            "cloud_sql_proof": {
                "detected": bool(is_cloud_sql),
                "reason": "version contains '-google' or comment mentions Google"
            }
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200


if __name__ == "__main__":
    # у продакшні тебе запускає gunicorn; цей блок для локального запуску
    app.run(host="0.0.0.0", port=8000, debug=False)
