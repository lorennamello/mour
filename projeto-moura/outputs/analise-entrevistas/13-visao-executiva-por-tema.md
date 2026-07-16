# Energia como Serviço (Telecom) — Visão Executiva por Tema
### Síntese da Fase 1 (Imersão Interna) para leitura de diretoria

**Fonte:** 12 entrevistas internas (Comercial, Engenharia, Operações, Financeiro, TI, P&D/ITEMM, Fábrica, Acionista) + planilha de compilação temática, cruzadas e validadas linha a linha contra as transcrições originais.
**O que este documento NÃO é:** não é uma repetição das entrevistas pessoa a pessoa (isso já existe nos documentos individuais `01-12`). Aqui, cada tema aparece **uma única vez**, com a conclusão consolidada — não a soma das falas.

---

## Resumo em uma tela

1. **A proposta de valor é sólida e validada na prática (Vivo), mas ainda não é repetível.** Existe um único playbook comprovado — o resto é construído do zero a cada operadora.
2. **A empresa está tentando vender um serviço premium em cima de uma base que ainda não é estável** — hardware "MVP que virou produção", instalação em campo com falha de até 30-35%, e um time comercial que passou por 100% de turnover.
3. **O maior travamento não é preço, é confiança e política interna do cliente.** Operações teme perder o próprio emprego; Compras compara aluguel completo com CAPEX seco; e o histórico recente de falhas na venda tradicional de baterias contamina a credibilidade da proposta de serviço.
4. **Sites legados (parque instalado) são a barreira estrutural nº 1 para escalar** — 90% do sucesso atual está restrito a sites novos.
5. **Cada operadora exige uma abordagem diferente.** Vivo já comprou a ideia; TIM está aberta mas precisa de um argumento de inovação/Board; Claro carrega mágoa de um repricing malconduzido e viés cultural de "ser dona do ativo".
6. **A ameaça de mercado mais concreta é a comoditização**: operadoras tentando comprar só o "aluguel de bateria seca", sem a camada de gestão/inteligência que é o verdadeiro diferencial da Moura.
7. **A Fase 2 (entrevistas com as operadoras) precisa checar, nomeadamente, 5 hipóteses centrais** — listadas no tema 10.

---

## 1. Proposta de Valor

**Conclusão central:** o valor entregue não é "uma bateria alugada" — é a transferência de um problema operacional crônico (gestão de um ativo físico crítico e dependência de infraestrutura roubável) para quem sabe fazer isso em escala, com previsibilidade orçamentária.

- O valor se sustenta em três pilares que se repetem em todas as áreas: **(1)** alívio de CAPEX / liberação de capital para o core business (5G); **(2)** delegação de uma "dor de cabeça" que as operadoras hoje gerenciam mal (elas não sabem, de fato, o que têm instalado em cada site); **(3)** verticalização da Moura (fabrica a bateria, é dona da plataforma, executa o serviço) — nenhum concorrente (torreiras, fabricantes chineses) entrega esse pacote completo.
- Vivo é o único cliente com o modelo maduro; TIM e Claro seguem em prospecção; há radar para adjacências (Aloha e ISPs menores, bancos, data centers, call centers).
- **Tensão a resolver:** o discurso comercial vende "foco no core business" como benefício, mas o próprio time reconhece que os clientes avaliam a proposta pelo "hard saving" (custo direto da bateria) e não pelo custo de oportunidade do capital liberado — ou seja, a Moura está tentando vender um argumento que o comprador típico ainda não usa para decidir.

---

## 2. Desafios Internos

**Conclusão central:** quase todo problema relatado, em qualquer área, converge para uma mesma causa-raiz — **a operação amadureceu mais devagar do que a ambição comercial**.

- **Produto físico:** o equipamento de monitoramento (Connect Plus) nasceu como MVP/prova de conceito em uma placa Raspberry Pi e foi para produção sem virar um produto industrial maduro — gera instabilidade constante de dados.
- **Instalação em campo:** falha de padronização (30-35% dos sites com erro de instalação) "cega" a plataforma e força visitas técnicas reativas em vez de manutenção preditiva.
- **Plataforma/dados:** informação pouco confiável (falsos positivos, dados "não vomitados" que exigem trabalho manual de garimpo) mina a proposta de valor baseada em monitoramento inteligente.
- **Comercial:** turnover de 100% da equipe em um ano apagou o histórico de relacionamento e de processo — o time atual está, em boa parte, "resgatando e-mails e pedidos perdidos" em vez de vender.
- **Financeiro/OPEX:** frete variável por região, provisão de furto ainda em calibração, e piora nas taxas de captação (funding) tornam a precificação mais cara hoje do que no contrato original com a Vivo.
- **Interno/cultura:** descompasso de ritmo entre Fábrica (planejamento mensal) e Operação (demanda semanal), e falha de handover entre ITEMM (P&D) e Engenharia, que deixou a Engenharia sem autonomia de software.

---

## 3. Áreas Internas — Papéis e Conflitos

**Conclusão central:** o organograma real é mais frágil do que a proposta de valor pressupõe — **não existe, hoje, uma "Moura Energia" com time dedicado**; comercial, compras e parte da engenharia são compartilhados com a operação tradicional de baterias (CMO), competindo pela atenção das mesmas pessoas.

- Padrão de conflito que se repete: **falhas de repasse (handover) entre áreas**, não falta de capacidade individual — ITEMM não repassou o produto maduro para a Engenharia operar; a Engenharia demora a responder o Comercial; a RSM executa sem receber diretrizes claras do ITEMM.
- Não existe SLA interno formal entre áreas — o fluxo depende de follow-up manual e de "força de vontade", o que os próprios entrevistados citam como fonte direta de atraso comercial (ver tema 5).
- Crítica pontual e relevante: o papel do PO (Product Owner) hoje é visto como excessivamente financeiro/voltado para dentro, com um vácuo no papel de "promover e escutar o mercado" — ou seja, ninguém está dedicado a fazer o produto evoluir com base no que o mercado pede.

---

## 4. Modelo Comercial

**Conclusão central:** a Moura tem **um único playbook comprovado e automatizado (Vivo)** e **nenhum playbook repetível para qualquer outro cliente** — cada nova proposta é construída do zero.

- Com a Vivo, o processo é hoje quase mecânico: o cliente envia a demanda pela própria plataforma dele, a engenharia calcula automaticamente a solução técnica, e o pedido segue. Esse nível de automação e confiança não existe com nenhum outro cliente.
- A venda tradicional (bateria avulsa) segue via LPU/BID — preço travado, sem obrigação de volume — e o relacionamento pessoal pesa mais do que o contrato formal.
- O modelo de serviço, na verdade, **não foi "vendido" para a Vivo — foi "comprado" por ela**: a operadora já tinha o projeto desenhado e orçamento aprovado; a Moura entrou no timing certo.
- Sintoma de alerta sistêmico: para outras operadoras, a proposta enviada frequentemente **"congela"** — sem contraproposta, sem negociação. Isso não é um problema de preço, é um sinal de que o modelo ainda não tem aderência ou confiança suficiente para gerar diálogo.

---

## 5. Visão sobre os Clientes

**Conclusão central:** **Vivo, TIM e Claro não são a mesma "operadora" com nomes diferentes** — exigem discursos de venda e pontos de entrada completamente distintos, mas a Moura hoje usa uma abordagem única para todos.

- **Vivo:** organizada, inovadora, foi quem puxou o modelo; já resolveu seu problema de CAPEX com a Moura.
- **TIM:** aberta à inovação (tem centro de pesquisa), sem dor aguda de CAPEX, mas incomodada com o ruído operacional do dia a dia ("kikiki"); já existe um aliado interno em nível de gerência regional disposto a levar o assunto ao Board.
- **Claro:** a mais conservadora ("sempre fiz assim"), viés cultural/global de ser dona do ativo (CAPEX), e carrega mágoa concreta de um repricing malconduzido pela Moura no passado, que quase custou o orçamento anual do cliente.
- Traço comum às três: são **organizações departamentalizadas que competem internamente**, com maturidade financeira baixa para comparar OPEX total contra CAPEX aparente — o que explica por que a venda "trava" independentemente do preço.

---

## 6. Barreiras de Expansão

**Conclusão central:** a barreira nº 1 não é tecnológica nem comercial — é estrutural: **90% do sucesso atual está limitado a sites novos**; o parque já instalado (legado) das operadoras é onde o modelo ainda não tem uma resposta pronta.

- **Internas:** intensidade de CAPEX necessária para escalar, dependência de um único fornecedor homologado de gabinete, e um modelo logístico (RSM) que não escala economicamente para regiões distantes (ex: Norte).
- **Do lado do cliente:** sites legados (cliente já comprou o ativo recentemente e não aceita pagar de novo por ele embutido no aluguel); risco de boicote interno pela área de Operações, que teme perder o próprio posto; viés cultural patrimonialista em operadoras como a Claro.
- **De mercado:** entrada de baterias de lítio chinesas mais baratas, pressionando o discurso de "hard saving"; e o próprio furto/vandalismo, que corrói a margem e a confiança no retorno do modelo.
- **Caminho já identificado para destravar sites legados:** operação financeira de *buy-and-lease-back* (a Moura recompra o ativo do cliente para depois alugar o serviço de volta) — citada por múltiplas áreas como pré-condição, não como opção.

---

## 7. Ecossistema e Mercado

**Conclusão central:** existe uma janela de mercado real, **criada porque dois outros players estruturais recusam parte do problema** — e a Moura é hoje a única peça que junta as duas partes que faltam.

- **Torreiras (TowerCos):** funcionam como empresas de real estate — vivem de receita previsível (aluguel de m²) e se recusam terminantemente a assumir o risco operacional de energia (furto, manutenção, OPEX variável), pois isso encareceria o custo de capital do próprio negócio delas.
- **Fabricantes chineses:** pressionam o preço do hardware para baixo e ainda não enfrentam a exigência plena de homologação Anatel para lítio — uma janela regulatória que deve se fechar, tornando essa vantagem de preço temporária.
- **Posicionamento da Moura:** o único player verticalizado (fabrica + monitora + presta o serviço) — o que a concorrência, seja torreira ou fabricante puro, não consegue replicar sozinha.
- **Leitura estratégica:** essa janela de oportunidade existe *por causa* das recusas estruturais de terceiros, não porque a Moura resolveu um problema que ninguém mais poderia resolver — vale monitorar sinais de que Torreiras ou fabricantes possam mudar de postura.

---

## 8. Visão de Futuro

**Conclusão central:** o roadmap se divide claramente em três horizontes, e a maturidade cai muito do primeiro para o terceiro — **o presente é sobre estabilizar e repetir; o futuro distante é sobre virar uma empresa de dados/energia, não de aluguel de bateria**.

- **Curto prazo (estabilizar o atual):** consertar a execução (qualidade de instalação, materiais comerciais de nível C-level, apresentações estruturadas para o Board de TIM e Claro).
- **Médio prazo (novas frentes já mapeadas):** destravar sites legados via buy-and-lease-back; expandir para bancos, ISPs regionais (Aloha, Brisanet, Vero), tração (empilhadeiras) com modelo de cobrança variável.
- **Longo prazo (disrupção):** deixar de "alugar a caixa d'água" (a bateria) para "garantir o banho" (a energia em si, via geração própria/solar híbrida) e monetizar dados/inteligência como um novo produto — inclusive fora de telecom (Home BES, indústrias que comprariam inteligência de qualidade de energia).
- **Leitura para a diretoria:** os dois primeiros horizontes dependem de resolver os temas 2, 3 e 6 (execução, organização interna, sites legados). O terceiro horizonte só faz sentido depois que os dois primeiros estiverem sob controle.

---

## 9. Hipóteses para Validar na Fase 2

**Conclusão central:** as ~15 hipóteses levantadas na Fase 1 convergem em **5 apostas centrais** que devem orientar as entrevistas com as operadoras:

| # | Hipótese central | O que a Fase 2 precisa confirmar ou refutar |
|---|---|---|
| 1 | A adoção trava mais por **política interna do cliente** (medo de demissão em Operações, disputa de protagonismo) do que por preço ou TCO | Perguntar diretamente a Operações e Engenharia do cliente sobre percepção de risco ao próprio cargo |
| 2 | O **histórico recente de falhas na venda tradicional de baterias** (atraso, faturamento, repricing) contamina a confiança para fechar um contrato de 10 anos de serviço | Testar se decisores associam espontaneamente os dois temas ao falar de "Moura" |
| 3 | **Sites legados** só destravam com uma estrutura financeira de recompra (buy-and-lease-back) — não com melhor discurso comercial | Validar se esse é de fato o único obstáculo ou se há resistência adicional |
| 4 | Existe demanda represada por **dados granulares** (telemetria contínua) que hoje ninguém precificou como produto à parte | Sondar disposição a pagar por relatórios/insights além do "aluguel básico" |
| 5 | Operadoras estão tentando **desmembrar a oferta** (comprar só o hardware/aluguel seco, sem a camada de gestão) — risco de comoditização do diferencial da Moura | Confirmar se isso é intenção deliberada de Compras ou um mal-entendido de escopo |

---

## 10. Pessoas-Chave por Operadora (Stakeholders)

**Conclusão central:** o padrão que se repete em todas as áreas é o mesmo — **a proposta só avança se entrar pelo topo (Board/C-level) e descer**, porque nenhum departamento isolado tem interesse ou mandato para aprovar sozinho. Ao mesmo tempo, é preciso ouvir a ponta (Operações/Engenharia/Regional) para entender a resistência real.

- **Perfis a entrevistar em cada operadora:** Alta Gestão/Board (decisão final e narrativa de TCO), Operações e Engenharia (onde mora o medo/boicote), Compras (dono do processo de BID/LPU), e um gerente Regional importante (visão de quem sente o problema na prática).
- **Vivo:** relação já madura — usar para entender o que funcionou e o que ainda incomoda no dia a dia operacional.
- **TIM:** já existe um aliado espontâneo em nível de gerência regional que pediu para ajudar a levar o modelo ao Board (contato "quente" para acelerar a Fase 2).
- **Claro:** relação mais sensível — antes de qualquer pitch novo, é preciso reconhecer e endereçar o desgaste do episódio de repricing; entrar direto no tema de valor sem isso pode reforçar a desconfiança.

---

## O que isso significa para a Fase 2

A Fase 1 confirma que a Moura tem uma proposta de valor validada, mas **não replicável ainda** — o modelo funciona porque foi construído artesanalmente para (e com) a Vivo. A Fase 2 não deve apenas testar "se as operadoras querem o serviço" — a resposta a isso já está sinalizada como positiva pelas próprias barreiras internas descritas (elas *querem* se livrar do problema). O ponto crítico a validar é **quem, dentro de cada operadora, tem o poder de dizer sim e o que precisa ver para confiar** — e essa resposta muda por operadora, o que reforça a necessidade de um roteiro de entrevista diferenciado para Vivo, TIM e Claro, e não um roteiro único.

---

*Documento gerado a partir da planilha `Moura_Telecom_Phase_1__Interviews.xlsx` (12 abas), cruzada e validada contra as 15 transcrições de entrevistas internas. Para o detalhamento granular por entrevistado, ver os documentos `01` a `12` nesta mesma pasta.*
