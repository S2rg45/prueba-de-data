from statistics_pragma import statistics_config


def get_data():
  config_conect = statistics_config.connection_database()
  with config_conect.cursor() as query:
    query.execute("""
                  INSERT INTO public.validation(
                  total_count, average_value, min_value, max_value)
                  select 	--te.execution_time,
                      --te.price,
                      count(price),
                      avg(price),
                      min(price),
                      max(price)
	                from public.test te
                  """)
    config_conect.commit()
    config_conect.close()
    # query.fetchall()
    
