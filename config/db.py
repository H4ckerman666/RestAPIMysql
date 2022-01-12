from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://uv8vtivvz45vjxfo:7LPghzglHIv6ElYDxeyZ@byytwsh617pdmfyljgjk-mysql.services.clever-cloud.com:3306/byytwsh617pdmfyljgjk")
meta = MetaData()
conn = engine.connect()