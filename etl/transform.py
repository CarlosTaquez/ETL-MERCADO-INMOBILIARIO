
from pyspark.sql import functions as F


def audit_data(df):

    print("\n========== AUDITORÍA DE CALIDAD ==========")

    # 1. Cantidad de registros y columnas
    print(f"\nTotal de registros: {df.count()}")
    print(f"Total de columnas: {len(df.columns)}")

    # 2. Revisar valores nulos
    print("\n--- VALORES NULOS ---")

    null_counts = df.select([
        F.sum(
            F.when(F.col(column).isNull(), 1).otherwise(0)
        ).alias(column)
        for column in df.columns
    ])

    null_counts.show(truncate=False)

    # 3. Revisar identificadores duplicados
    print("\n--- REGISTROS DUPLICADOS ---")

    duplicate_ids = (
        df.groupBy("id")
        .count()
        .filter(F.col("count") > 1)
    )

    print(f"IDs duplicados: {duplicate_ids.count()}")

    # 4. Revisar valores inválidos
    print("\n--- VALORES INCONSISTENTES ---")

    invalid_conditions = {
        "Precio menor o igual a cero": F.col("price") <= 0,
        "Superficie habitable menor o igual a cero": F.col("sqft_living") <= 0,
        "Superficie del terreno menor o igual a cero": F.col("sqft_lot") <= 0,
        "Habitaciones negativas": F.col("bedrooms") < 0,
        "Baños negativos": F.col("bathrooms") < 0
    }

    for description, condition in invalid_conditions.items():

        total = df.filter(
            F.coalesce(condition, F.lit(False))
        ).count()

        print(f"{description}: {total}")

    print("\nAuditoría finalizada.")


def transform_data(df):

    print("\n========== TRANSFORMACIÓN DE DATOS ==========")

    # 1. Convertir la fecha al formato DATE
    df = df.withColumn(
        "date",
        F.to_date(
            F.to_timestamp("date", "yyyyMMdd'T'HHmmss")
        )
    )

    # 2. Convertir superficie habitable de pies cuadrados a metros cuadrados
    df = df.withColumn(
        "living_area_m2",
        F.round(
            F.col("sqft_living") * 0.09290304,
            2
        )
    )

    # 3. Calcular el precio por metro cuadrado
    df = df.withColumn(
        "price_per_m2",
        F.when(
            F.col("living_area_m2") > 0,
            F.round(
                F.col("price") / F.col("living_area_m2"),
                2
            )
        ).otherwise(None)
    )

    # 4. Mostrar estructura actualizada
    print("\nTransformaciones realizadas correctamente.")

    print("\nEstructura actualizada:")
    df.printSchema()

    # 5. Mostrar resultados
    print("\nPrimeros 5 registros transformados:")

    df.select(
        "id",
        "date",
        "price",
        "sqft_living",
        "living_area_m2",
        "price_per_m2"
    ).show(5, truncate=False)

    # 6. Mostrar cantidad final de registros y columnas
    print(f"\nRegistros finales: {df.count()}")
    print(f"Columnas finales: {len(df.columns)}")

    print("\nTransformación finalizada.")

    return df
