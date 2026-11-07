
import os
import psycopg2
from dotenv import load_dotenv
from pyspark.sql import functions as F

load_dotenv()


def load_data(df):
    print("\n========== CARGA DE DATOS ==========")

    connection = None
    cursor = None

    try:
        connection = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )

        cursor = connection.cursor()

        df = df.withColumnRenamed("price_per_m2", "precio_por_m2") \
               .withColumnRenamed("living_area_m2", "superficie_m2") \
               .withColumn("zipcode", F.col("zipcode").cast("string"))

        columns = [
            "id", "date", "price", "bedrooms", "bathrooms",
            "sqft_living", "sqft_lot", "floors", "waterfront",
            "view", "condition", "grade", "sqft_above",
            "sqft_basement", "yr_built", "yr_renovated",
            "zipcode", "lat", "long", "sqft_living15",
            "sqft_lot15", "precio_por_m2", "superficie_m2"
        ]

        insert_sql = """
            INSERT INTO public.viviendas (
                id, date, price, bedrooms, bathrooms,
                sqft_living, sqft_lot, floors, waterfront,
                view, condition, grade, sqft_above,
                sqft_basement, yr_built, yr_renovated,
                zipcode, lat, long, sqft_living15,
                sqft_lot15, precio_por_m2, superficie_m2
            )
            VALUES (
                %s, %s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s, %s, %s
            )
        """

        rows = df.select(*columns).collect()

        for row in rows:
            cursor.execute(insert_sql, tuple(row))

        connection.commit()

        print(f"Registros cargados correctamente: {len(rows)}")

    except Exception as error:
        if connection:
            connection.rollback()
        print(f"Error durante la carga: {error}")
        raise

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
