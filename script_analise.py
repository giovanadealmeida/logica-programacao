#!/bin/bash
#Este é um script para gerar um relatorio diario

#Data atual
data_atual=$(date + "%Y-%m-%d")

#Diretorio de saida para relatorios
output_dir="/home/usuario/relatorios"

#Gera o relatorio com dados de analise
python script_analise.py >"$output_dir/relatorio_$data_atual.txt"

echo "Relatorio diario gerado em: $output_dir/relatorio_$data_atual.txtY"
