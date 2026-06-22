from flask import Flask, render_template, request, redirect, url_for
from flask import Flask, render_template, request, redirect, flash
import sqlite3
import csv
from flask import Response
from flask import send_from_directory

app = Flask(
    __name__,
    template_folder=".",
    static_folder="."
)
app.secret_key = "mini_crm_secret"

@app.route("/export")
def export_csv():

    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM customers
    """)

    rows = cursor.fetchall()

    conn.close()

    def generate():

        data = csv.writer(
            open("temp.csv","w",newline="")
        )

    output = []

    output.append("ID,Name,Email,Phone\n")

    for row in rows:

        output.append(
            f"{row[0]},{row[1]},{row[2]},{row[3]}\n"
        )

    return Response(
        output,
        mimetype="text/csv",
        headers={
            "Content-Disposition":
            "attachment;filename=customers.csv"
        }
    )


# =========================
# DATABASE CONNECTION
# =========================

def get_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


# =========================
# CREATE TABLE
# =========================

def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


create_table()


# =========================
# HOME PAGE
# =========================

@app.route("/")
def index():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM customers
        ORDER BY id DESC
    """)

    customers = cursor.fetchall()

    customer_count = len(customers)

    conn.close()

    return render_template(
        "index.html",
        customers=customers,
        customer_count=customer_count
    )


# =========================
# ADD CUSTOMER
# =========================

@app.route("/add", methods=["GET", "POST"])
def add_customer():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO customers
            (name, email, phone)
            VALUES (?, ?, ?)
        """, (name, email, phone))

        conn.commit()
        conn.close()

        
        flash("Customer added successfully!", "success")


        return redirect(url_for("index"))

    return render_template("add_customer.html")

# =========================
# EDIT CUSTOMER
# =========================

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_customer(id):

    conn = get_connection()
    cursor = conn.cursor()

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]

        cursor.execute("""
            UPDATE customers
            SET
                name = ?,
                email = ?,
                phone = ?
            WHERE id = ?
        """, (name, email, phone, id))

        conn.commit()
        conn.close()

        return redirect(url_for("index"))

    cursor.execute("""
        SELECT * FROM customers
        WHERE id = ?
    """, (id,))

    customer = cursor.fetchone()

    conn.close()

    flash("Customer saved successfully!", "success")

    return render_template(
        "edit_customer.html",
        customer=customer
    )


# =========================
# DELETE CUSTOMER
# =========================

@app.route("/delete/<int:id>")
def delete_customer(id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM customers
        WHERE id = ?
    """, (id,))

    conn.commit()
    conn.close()

    flash("Customer deleted successfully!", "danger")

    return redirect(url_for("index"))


# =========================
# SEARCH CUSTOMER
# =========================

@app.route("/search")
def search_customer():

    keyword = request.args.get("keyword", "")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM customers
        WHERE
            name LIKE ?
            OR email LIKE ?
            OR phone LIKE ?
        ORDER BY id DESC
    """, (
        f"%{keyword}%",
        f"%{keyword}%",
        f"%{keyword}%"
    ))

    customers = cursor.fetchall()

    customer_count = len(customers)

    conn.close()

    return render_template(
        "index.html",
        customers=customers,
        customer_count=customer_count
    )

@app.route("/style.css")
def style_css():
    return send_from_directory(".", "style.css")


@app.route("/script.js")
def script_js():
    return send_from_directory(".", "script.js")


# =========================
# RUN APP
# =========================

if __name__ == "__main__":
    app.run(debug=True)