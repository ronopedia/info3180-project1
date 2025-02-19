from . import db




class PropertyInfo(db.Model):
    __tablename__ = "property_info"

    id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    title = db.Column(db.String(255))
    bathrooms = db.Column(db.String(2))
    bedrooms = db.Column(db.String(2))
    description = db.Column(db.String(255))
    price = db.Column(db.String(80))
    prop_type = db.Column(db.String(9))
    location = db.Column(db.String(255))
    photo = db.Column(db.String(255), index = True)

    
    def __init__(self, title, bathrooms, bedrooms, description, price, prop_type, location, photo):
        self.title = title
        self.bathrooms = bathrooms
        self.bedrooms = bedrooms
        self.description = description
        self.price = price
        self.prop_type = prop_type
        self.location = location
        self.photo = photo

    