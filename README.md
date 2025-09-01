Esse código é um simulador de alerta baseado em EWMA (Exponential Weighted Moving Average), voltado para sistemas de detecção de anomalias como em um SIEM (Security Information and Event Management).
Objetivo do Script
Monitorar uma série de taxas de logs por minuto (por exemplo, número de eventos de segurança registrados a cada minuto) e gerar alertas sempre que a taxa atual exceder 3× a média exponencial ponderada anterior (EWMA).
Feito em aula 
