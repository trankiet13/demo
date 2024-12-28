from urllib.parse import quote

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote
app = Flask(__name__)
app.config['SECRET_KEY'] = '1HV98N4L#&UNg?:E;82{Ef@Bftfpl9eC#DtTP~oJ"Pufpi|V)2&}_aqM/g?Pbp2'
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://root:{quote('123@')}@localhost/clinic1?charset=utf8mb4"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app=app)
login = LoginManager(app=app)

# cloudinary.config(
#     cloud_name="duwdx2tgu",
#     api_key="646743949231237",
#     api_secret="jbac0w3FuckWA57tHsMH45ljksA",  # Click 'View API Keys' above to copy your API secret
#     secure=True
# )
