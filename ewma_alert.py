"""
SIEM EWMA Alert Simulation (compatible com Python 3.8+)

Este script demonstra a lógica de alerta local baseada em EWMA:
- Calcula a EWMA (α = 0.3) de uma série de taxas de logs por minuto.
- Dispara um alerta sempre que a taxa ultrapassa 3× a EWMA anterior.
"""

from typing import List

# --- Parâmetros configuráveis ---
alpha: float = 0.3           # peso dado ao valor mais recente
baseline_rate: float = 5.0   # valor inicial de EWMA (pode ser a média histórica)
alert_factor: float = 3.0    # múltiplo de EWMA para disparar alerta

# --- Estado global ---
ewma_prev: float = baseline_rate

def update_ewma(rate: float) -> float:
    """
    Atualiza a EWMA com a nova taxa e retorna o valor atualizado.
    Usa a variável global `ewma_prev` como EWMA anterior.
    """
    global ewma_prev
    ewma = alpha * rate + (1 - alpha) * ewma_prev
    ewma_prev = ewma
    return ewma

def check_alert(rate: float, prev_ewma: float) -> bool:
    """
    Retorna True se a taxa atual `rate` ultrapassar `alert_factor` × EWMA anterior.
    """
    return rate > alert_factor * prev_ewma

def simulate(rates: List[float]) -> None:
    """
    Simula o processamento de uma lista de taxas de logs por minuto,
    imprimindo EWMA e sinalizando alertas.
    """
    print(f"{'Minuto':>6} | {'Rate':>4} | {'EWMA_prev':>9} | {'EWMA':>7} | Alerta")
    print("-" * 50)

    global ewma_prev
    ewma_prev = baseline_rate  # reinicia EWMA

    for minute, rate in enumerate(rates, start=1):
        prev = ewma_prev            # guarda o valor anterior
        ewma = update_ewma(rate)    # calcula e atualiza EWMA global
        alert = check_alert(rate, prev)
        alert_msg = "🔔 ALERTA" if alert else ""
        print(f"{minute:6d} | {rate:4.0f} | {prev:9.2f} | {ewma:7.2f} | {alert_msg}")

if __name__ == "__main__":
    # Exemplo de taxas de logs por minuto (você pode trocar por dados reais)
    sample_rates: List[float] = [5, 6, 5, 7, 6, 5, 8, 20, 6, 5, 4, 3]
    simulate(sample_rates)


