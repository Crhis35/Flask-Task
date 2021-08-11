from Models.User import User
from Controllers.User import UserController
from flask import render_template, flash, redirect, url_for, request


def home():
    user = UserController.getInstance()
    return render_template('index.html', users=user.get_all())


def add_contact():
    if request.method == 'POST':
        print(request.form)
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        if not fullname and not phone and not email:
            flash('Check form', 'warning')
            return redirect(url_for('home'))

        user = User(len(UserController.users) + 1, fullname, email, phone)

        UserController.add(user)

        flash('User added', 'success')

        return redirect(url_for('home'))


def get_contact(id):
    user = UserController.get_by_id(id)
    return render_template('edit-contact.html', user=user)


# @app.route('/update/<id>', methods=['POST'])
def update_contact(id):
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE contacts
            SET fullname = %s,
                email = %s,
                phone = %s
            WHERE id = %s
        """, (fullname, email, phone, id))
        flash('Contact Updated Successfully')
        mysql.connection.commit()
        return redirect(url_for('Index'))

@app.route('/delete/<string:id>', methods = ['POST','GET'])
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM contacts WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Contact Removed Successfully')
    return redirect(url_for('Index'))