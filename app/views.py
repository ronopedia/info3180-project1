"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
from app import app, db
from flask import render_template, request, redirect, url_for, flash, session, abort, send_from_directory
from .config import Config
from werkzeug.utils import secure_filename
from app.forms import PropertyForm
from app.model import PropertyInfo
from flask_wtf.csrf import CSRFProtect



###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route('/property', methods=["GET", "POST"])
def property1():
    form = PropertyForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            title = form.title.data
            bedrooms = form.bedroom.data
            bathrooms = form.bathroom.data
            location = form.location.data
            price = form.price.data
            proptype = form.proptype.data
            description = form.description.data
            image = form.photo.data

            property = PropertyInfo(title, bedrooms, bathrooms, location, price, proptype, description, filename)
            db.session.add(property)
            db.session.commit()

            filename = secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        flash('Your Property Has been Uploaded!','success')
        return redirect(url_for('properties'))
            
    return render_template('property.html', form=form)

@app.route('/properties', methods=['GET'])
def properties():
    #image_list = get_uploaded_images()
    #return render_template('properties.html', image_list=image_list)
    properties = PropertyInfo.query.all()
    if request.method=='GET':
        return render_template('properties.html', properties=properties)


@app.route('/property/<propertyid>')
def propid(propertyid):
    #root_dir = os.getcwd()
    #return send_from_directory(os.path.join(root_dir,app.config['UPLOAD_FOLDER']),filename)
    #properties = db.session.query(PropertyInfo).filter(PropertyInfo.id==propertyid).first()
    properties = PropertyInfo.query.filter_by(id = propertyid).first()
    if request.method=='GET':
        return render_template('property_by_id.html',properties=properties)


@app.route('/upload/<filename>')
def get_image(filename):
    root_dir = os.getcwd()
    return send_from_directory(os.path.join(root_dir, app.config['UPLOAD_FOLDER']), filename)

def get_uploaded_images():
    rootdir = os.getcwd()
    print(rootdir)
    fileslst = []
    for subdir, dirs, files in os.walk(rootdir + '/uploads'):
        for image in files:
            #fileslst.append(image)
            if image!=".gitkeep":
                fileslst.append(image)
    return fileslst


###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
