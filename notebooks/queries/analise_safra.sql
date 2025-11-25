
SELECT
    t1.mes_safra,
    t1.total_leads_criados,
    t1.leads_vendidos,
    -- Conversão da Safra em Venda
    CAST(t1.leads_vendidos AS REAL) / t1.total_leads_criados AS taxa_conversao_venda,
    -- Quantidade de Visitas Realizadas (Agregadas por Mês)
    COALESCE(t2.visitas_realizadas, 0) AS visitas_realizadas
FROM
    (
        -- Subquery 1 (t1): Métricas de Volume e Venda por Mês de Safra
        SELECT
            strftime('%Y-%m', data_criacao) AS mes_safra,
            COUNT(DISTINCT lead_id) AS total_leads_criados,
            COUNT(DISTINCT CASE WHEN data_venda IS NOT NULL THEN lead_id END) AS leads_vendidos
        FROM
            df_funil
        WHERE
            -- Filtro para o 2º semestre de 2024
            data_criacao >= '2024-07-01' AND data_criacao < '2025-01-01'
        GROUP BY 1
    ) AS t1
LEFT JOIN
    (
        -- Subquery 2 (t2): Visitas Únicas por Mês de Referência
        SELECT
            mes_referencia AS mes_safra,
            COUNT(DISTINCT id_visita) AS visitas_realizadas
        FROM
            visitas
        WHERE
            data_visita >= '2024-07-01' AND data_visita < '2025-01-01'
        GROUP BY 1
    ) AS t2 ON t1.mes_safra = t2.mes_safra

ORDER BY
    t1.mes_safra DESC;
