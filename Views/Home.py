from Models.User import User
from Controllers.User import UserController
from flask import render_template, flash, redirect, url_for, request


def home():
    users = UserController.get_all()
    return render_template('index.html', users=users)


def add_contact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        if not fullname and not phone and not email:
            flash('Check form', 'danger')
            return redirect(url_for('home'))

        user = User(len(UserController.users) + 1, fullname, email, phone)

        UserController.add(user)

        flash('User added', 'success')

        return redirect(url_for('home'))


def get_contact(id):
    user = UserController.get_by_id(id)
    return render_template('edit-contact.html', user=user)


def update_contact(id):
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        if not fullname and not phone and not email:
            flash('Check form', 'danger')
            return redirect(url_for('home'))

        UserController.update(id, fullname, email, phone)
        flash('User Updated Successfully', 'success')
        return redirect(url_for('home'))


def delete_contact(id):
    UserController.delete(id)
    flash('Contact Removed Successfully', 'success')
    return redirect(url_for('home'))
