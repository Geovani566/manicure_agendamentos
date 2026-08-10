def horario_para_minutos(horario):
    partes=horario.split(":")
    #12         :        00
    horas=int(partes[0])
    minutos=int(partes[1])

    total_minutos= horas * 60 + minutos

    return total_minutos

def gerar_horarios(inicio, fim, intervalo=30):
    lista_horarios = []

    horario_atual = horario_para_minutos(inicio)
    horario_final = horario_para_minutos(fim)
    
    while horario_atual <= horario_final:
        horas=horario_atual // 60
        minutos=horario_atual % 60

        horario=f'{horas:02d}:{minutos:02d}'
        lista_horarios.append(horario)

        horario_atual = horario_atual+intervalo
    return lista_horarios
       

if __name__ == "__main__":
    print(gerar_horarios("08:00", "18:00", 30))
