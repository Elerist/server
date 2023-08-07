from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)



def get_db_connection():
    try:
        connection = psycopg2.connect(user="postgres",
                                    password="x9dr9s7n",
                                    host="localhost",
                                    port="5432",
                                    database="agenda")
        cursor = connection.cursor()
        postgreSQL_select_Query = 'select * from "Categoria"'

        cursor.execute(postgreSQL_select_Query)
        print("Selecting rows from mobile table using cursor.fetchall")
        mobile_records = cursor.fetchall()

        print("Print each row and it's columns values")
        data = []
        for row in mobile_records:
            data.append({"id": row[0], "nombre": row[1], "rubroId": row[2], "dolar": row[3]})
        return data

            

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)


get_db_connection()

@app.route("/asd")
def get_user():
    result = get_db_connection()
    return jsonify(result),


@app.route("/create-product", methods=["POST"])
def create_user():
    data = request.get_json()
    connection = psycopg2.connect(user="postgres",
                                        password="x9dr9s7n",
                                        host="localhost",
                                        port="5432",
                                        database="agenda")
    cursor = connection.cursor()
    db_query = 'INSERT INTO "Producto" (id, codigo, nombre, precio, "stockMin", "stockAct", "categoriaId", "rubroId", "genreId") VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);'
    record_to_insert = (data["id"], data["codigo"], data["nombre"], data["precio"], data["stockMin"], data["stockAct"], data["categoriaId"], data["rubroId"], data["genreId"])
    cursor.execute(db_query, record_to_insert)
    connection.commit()
    result = {"message": "Inserted successfully"}
    return jsonify(result)


if __name__ == "_main_":
    app.run(debug=True)