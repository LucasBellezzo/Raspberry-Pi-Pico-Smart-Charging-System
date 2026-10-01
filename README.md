Controle Inteligente de Sessão de Recarga

Protótipo educacional em MicroPython para Raspberry Pi Pico, desenvolvido para a Sprint 3 do desafio GoodWe, inspirado no conceito do GoodWe Smart Energy Controller. O sistema simula o gerenciamento inteligente de uma sessão de recarga de veículo elétrico com base no balanço entre geração e consumo de energia.

📋 Descrição

O protótipo calcula a energia disponível a partir da diferença entre a potência gerada e o consumo da residência, determinando automaticamente o estado da sessão de recarga. O resultado é sinalizado por três LEDs (verde, amarelo e vermelho) e detalhado via Monitor Serial.

Fórmula utilizada:

Energia disponível = Geração - Consumo
⚡ Estados da Recarga
Estado	Condição	LED	Status
Energia suficiente	energia > 1000 W	🟢 Verde	RECARGA AUTORIZADA
Energia limitada	0 < energia ≤ 1000 W	🟡 Amarelo	RECARGA REDUZIDA
Energia insuficiente	energia ≤ 0 W	🔴 Vermelho	RECARGA BLOQUEADA
🔌 Hardware / Ligações
Componente	Pino no Pico
LED Verde	GP3
LED Amarelo	GP2
LED Vermelho	GP1

O circuito pode ser montado fisicamente ou simulado no Wokwi.

🖥️ Como executar
Abra o projeto no simulador Wokwi usando o PiPico
Copie o arquivo main.py via upload direto no Wokwi
Execute o script — o programa roda automaticamente três cenários de teste e imprime os resultados no Monitor Serial
🧪 Cenários de teste incluídos
python
controlar_recarga(4500, 2500)  # Energia suficiente  -> LED verde
controlar_recarga(1800, 1500)  # Energia limitada     -> LED amarelo
controlar_recarga(1000, 1800)  # Energia insuficiente -> LED vermelho

Cada chamada acende o LED correspondente por 2 segundos e imprime no terminal:

==============================
      CONTROLADOR DE RECARGA
==============================
Gerador  : 4500 W
Consumo  : 2500 W
Energia  : 2000 W
Status   : RECARGA AUTORIZADA
==============================


Demonstração da energia disponível em diferentes bases numéricas (exemplo com 2000 W):

Base	Valor
Decimal	2000
Binário	11111010000
Hexadecimal	0x7D0

