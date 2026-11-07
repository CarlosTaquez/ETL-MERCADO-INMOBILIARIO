
from pyspark.sql import SparkSession

from etl.extract import extract_data
from etl.transform import audit_data, transform_data
from etl.load import load_data

spark = SparkSession.builder \
    .appName("MercadoInmobiliarioETL") \
    .master("local[*]") \
    .getOrCreate()

try:
    archivo = "data/raw/kc_house_data.csv"

    # 1. Extracción
    df = extract_data(spark, archivo)

    # 2. Auditoría
    audit_data(df)

    # 3. Transformación
    df_transformed = transform_data(df)

    # 4. Carga en PostgreSQL
    load_data(df_transformed)

    print("\n========== PROCESO ETL FINALIZADO ==========")
    print(f"Registros procesados: {df_transformed.count()}")
    print(f"Columnas transformadas: {len(df_transformed.columns)}")

finally:
    spark.stop()
