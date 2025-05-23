total_segundos=1000000

segundos_minuto = 60
segundos_hora = 60 * segundos_minuto
segundos_dia = 24 * segundos_hora
segundos_semana = 7 * segundos_dia

semanas = total_segundos // segundos_semana
resto = total_segundos % segundos_semana

dias = resto // segundos_dia
resto = resto % segundos_dia

horas = resto // segundos_hora
resto = resto % segundos_hora

minutos = resto // segundos_minuto
segundos = resto % segundos_minuto

print(f"{total_segundos} segundos = {semanas} semanas {dias} días {horas} horas {minutos} minutos {segundos} segundos")
