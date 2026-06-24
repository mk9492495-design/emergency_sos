from flask import Blueprint, render_template, request, redirect
from db import get_connection

contacts_bp = Blueprint('contacts', __name__)

@contacts_bp.route('/contacts', methods=['GET', 'POST'])
def contacts():

    message = ""
    conn = get_connection()
    cursor = conn.cursor()

    if request.method == 'POST':

        cursor.execute("SELECT COUNT(*) as total FROM emergency_contacts")
        total = cursor.fetchone()['total']

        if total >= 3:
            message = "Maximum 3 Contacts Allowed"

        else:
            name = request.form.get('contact_name')
            phone = request.form.get('contact_phone')
            rel = request.form.get('relationship')

            cursor.execute("""
                INSERT INTO emergency_contacts
                (contact_name, contact_phone, relationship)
                VALUES (%s,%s,%s)
            """, (name, phone, rel))

            conn.commit()
            message = "Contact Added Successfully"

    cursor.execute("SELECT * FROM emergency_contacts")
    contacts = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template("contacts.html", contacts=contacts, message=message)


@contacts_bp.route('/delete_contact/<int:id>')
def delete_contact(id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM emergency_contacts WHERE contact_id=%s", (id,))
    conn.commit()

    cursor.close()
    conn.close()

    return redirect('/contacts')


@contacts_bp.route('/edit_contact/<int:id>', methods=['GET', 'POST'])
def edit_contact(id):

    conn = get_connection()
    cursor = conn.cursor()

    if request.method == 'POST':

        name = request.form.get('contact_name')
        phone = request.form.get('contact_phone')
        rel = request.form.get('relationship')

        cursor.execute("""
            UPDATE emergency_contacts
            SET contact_name=%s, contact_phone=%s, relationship=%s
            WHERE contact_id=%s
        """, (name, phone, rel, id))

        conn.commit()
        return redirect('/contacts')

    cursor.execute("SELECT * FROM emergency_contacts WHERE contact_id=%s", (id,))
    contact = cursor.fetchone()

    return render_template("edit_contact.html", contact=contact)