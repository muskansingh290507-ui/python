from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# MySQL connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mish@04",       # add password if any
    database="college"
)

cursor = conn.cursor(dictionary=True)

@app.route("/")
def show_students():
    cursor.execute("SELECT email, name FROM student")
    students = cursor.fetchall()
    return render_template("students.html", students=students)

@app.route("/products")
def show_products():
    cursor.execute("SELECT name, price FROM product")
    products = cursor.fetchall()
    return render_template("products.html", products=products)


# Add Product
@app.route("/add-product", methods=["GET", "POST"])
def add_product():
    if request.method == "POST":
        name = request.form["name"]
        price = request.form["price"]

        cursor.execute(
            "INSERT INTO product (name, price) VALUES (%s, %s)",
            (name, price)
        )
        conn.commit()

        return redirect("/products")

    return render_template("add_product.html")

if __name__ == "__main__":
    app.run(debug=True)