
def extract_data(spark, file_path):
    """
    Extrae los datos originales del dataset inmobiliario.
    """

    print("\n========== EXTRACCIÓN DE DATOS ==========")

    df = spark.read.csv(
        file_path,
        header=True,
        inferSchema=True,
        encoding="UTF-8"
    )

    print("\nDataset extraído correctamente.")
    print(f"Cantidad de registros: {df.count()}")
    print(f"Cantidad de columnas: {len(df.columns)}")

    print("\nColumnas del dataset:")
    print(df.columns)

    print("\nEstructura de los datos:")
    df.printSchema()

    print("\nPrimeros 5 registros:")
    df.show(5, truncate=False)

    return df
