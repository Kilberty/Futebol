
def sql_stat_brasileiro():
    sql_insert = """
        INSERT INTO STATS_Brasileiro(
            ID_Partida, Periodo, Temporada, Posse_Mandante, Posse_Visitante, ChutesTotal_Mandante,
            ChutesTotal_Visitante, ChutesAlvo_Mandante, ChutesAlvo_Visitante, ChutesFora_Mandante,
            ChutesFora_Visitante, ChutesBloqueados_Mandante, ChutesBloqueados_Visitante, Escanteios_Mandante,
            Escanteios_Visitante, Faltas_Mandante, Faltas_Visitante, Amarelo_Mandante, Amarelo_Visitante,
            Lateral_Mandante, Lateral_Visitante, TiroMeta_Mandante, TiroMeta_Visitante, GrandesChances_Mandante,
            GrandesChances_Visitante, GrandesChancesPerdidas_Mandante, GrandesChancesPerdidas_Visitante,
            ContraAtaque_Mandante, ContraAtaque_Visitante, ChutesContraAtaque_Mandante, ChutesContraAtaque_Visitante,
            ChutesArea_Mandante, ChutesArea_Visitante, ChutesForaArea_Mandante, ChutesForaArea_Visitante,
            DefesasGoleiro_Mandante, DefesasGoleiro_Visitante, Passes_Mandante, Passes_Visitante,
            PassesPrecisos_Mandante, PassesPrecisos_Visitante, Dribles_Mandante, Dribles_Visitante,
            PerdaPosse_Mandante, PerdaPosse_Visitante, DuelosGanhos_Mandante, DuelosGanhos_Visitante,
            DueloAereoVencido_Mandante, DueloAereoVencido_Visitante, Desarmes_Mandante, Desarmes_Visitante,
            Interceptacoes_Mandante, Interceptacoes_Visitante, Cortes_Mandante, Cortes_Visitante,
            Vermelho_Mandante, Vermelho_Visitante,BolaLonga_Mandante,BolaLonga_Visitante,Cruzamentos_Mandante,Cruzamentos_Visitante,
            Impedimento_Mandante, Impedimento_Visitante,TotalBL_Mandante,TotalBL_Visitante,CruzamentoTotal_Mandante,CruzamentoTotal_Visitante,
            DriblesTotal_Mandante, DriblesTotal_Visitante,GolContraAtaque_Mandante, GolContraAtaque_Visitante 
        ) VALUES (
            :ID_Partida, :Periodo,:Temporada,:Posse_Mandante, :Posse_Visitante, :ChutesTotal_Mandante,
            :ChutesTotal_Visitante, :ChutesAlvo_Mandante, :ChutesAlvo_Visitante, :ChutesFora_Mandante,
            :ChutesFora_Visitante, :ChutesBloqueados_Mandante, :ChutesBloqueados_Visitante, :Escanteios_Mandante,
            :Escanteios_Visitante, :Faltas_Mandante, :Faltas_Visitante, :Amarelo_Mandante, :Amarelo_Visitante,
            :Lateral_Mandante, :Lateral_Visitante, :TiroMeta_Mandante, :TiroMeta_Visitante, :GrandesChances_Mandante,
            :GrandesChances_Visitante, :GrandesChancesPerdidas_Mandante, :GrandesChancesPerdidas_Visitante,
            :ContraAtaque_Mandante, :ContraAtaque_Visitante, :ChutesContraAtaque_Mandante, :ChutesContraAtaque_Visitante,
            :ChutesArea_Mandante, :ChutesArea_Visitante, :ChutesForaArea_Mandante, :ChutesForaArea_Visitante,
            :DefesasGoleiro_Mandante, :DefesasGoleiro_Visitante, :Passes_Mandante, :Passes_Visitante,
            :PassesPrecisos_Mandante, :PassesPrecisos_Visitante, :Dribles_Mandante, :Dribles_Visitante,
            :PerdaPosse_Mandante, :PerdaPosse_Visitante, :DuelosGanhos_Mandante, :DuelosGanhos_Visitante,
            :DueloAereoVencido_Mandante, :DueloAereoVencido_Visitante, :Desarmes_Mandante, :Desarmes_Visitante,
            :Interceptacoes_Mandante, :Interceptacoes_Visitante, :Cortes_Mandante, :Cortes_Visitante,
            :Vermelho_Mandante, :Vermelho_Visitante,:BolaLonga_Mandante,:BolaLonga_Visitante,:Cruzamento_Mandante,:Cruzamento_Visitante,
            :Impedimento_Mandante,:Impedimento_Visitante,:BolaLongaTotal_Mandante,:BolaLongaTotal_Visitante,
            :CruzamentosTotal_Mandante,:CruzamentosTotal_Visitante, :DriblesTotal_Mandante, :DriblesTotal_Visitante,
            :GolContraAtaque_Mandante, :GolContraAtaque_Visitante 
        )
    """
    return sql_insert


def brasileiro_stat_insert(cursor, parametros):
    sql_insert = sql_stat_brasileiro()
    cursor.execute(sql_insert, parametros)




