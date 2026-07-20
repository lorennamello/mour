# Banco de Perguntas — Fase 2 (Operadoras)
### Cobertura das hipóteses consolidadas, organizado por bloco temático de entrevista

**Como usar este documento:** esta é a primeira camada — um banco de perguntas que cobre todas as hipóteses consolidadas pelo time, organizado pela lógica de uma conversa real (não pela ordem do documento de hipóteses). Cada pergunta traz o objetivo e o(s) código(s) de hipótese que ela testa. A próxima etapa é adaptar isso a um roteiro específico por pessoa/cargo (Claro, TIM, Algar, Ufinet).

**Referência de códigos** (a partir de `Lista de hipóteses - Consolidadas`):

| Código | Hipótese |
|---|---|
| H1.1 | CAPEX→OPEX é o valor central da servitização (+ ISPs como "fit perfeito") |
| H1.2 | Modelo "Tolling"/Uptime — paga pela garantia de disponibilidade, não pelo aluguel do ativo |
| H1.3 | Buy-and-lease-back é o "tiro certo" para o legado |
| H1.4 | Argumento regulatório (Anatel) engaja mais que o financeiro |
| H1.5 | Flexibilidade/escala sob demanda — operadoras rejeitam contratos engessados de 10-15 anos |
| H1.6 | Hard saving / comparação "injusta" bateria vs. serviço completo |
| H2.1 | Segurança física da bateria pesa mais que software/telemetria |
| H2.2 | Terceirizar o "fardo operacional" é o argumento-chave |
| H2.3 | Ativos legados recém-comprados travam a aceitação |
| H2.4 | Medo de perder domínio da operação / bloqueio cultural |
| H3.1 | Plataforma/IA vale mais que o hardware físico |
| H3.2 | Operadoras querem gestão total de energia (não só backup) |
| H4.1 | Monetização de capacidade ociosa (Virtual Power Plant) |
| H4.2 | Pagariam por dados inteligentes / monitoramento contínuo |
| H5.1 | ESG/logística reversa virou critério eliminatório, não diferencial |
| H6.1 | Perda de credibilidade (falhas na venda tradicional de bateria) contamina o novo modelo |
| H7.1 | Hipótese da delegação para Torreiras/Redes Neutras |

---

## Bloco A — Contexto e maturidade atual
*Aquecimento, sem hipótese isolada — mapeia como a operadora realmente decide hoje, para calibrar as perguntas seguintes e informar quem entrevistar na próxima fase.*

**A1.** Como funciona hoje a gestão de energia/backup dos seus sites — quem é responsável internamente por cada etapa (especificação, compra, instalação, manutenção, monitoramento)?
*Objetivo:* mapear a estrutura de decisão real, insumo direto para o roteiro de multi-threading da próxima fase.

**A2.** Quais são hoje os maiores problemas ou frustrações que vocês têm com a infraestrutura de energia dos sites — técnicos, financeiros ou operacionais?
*Objetivo:* descoberta aberta, sem induzir resposta — serve de controle para comparar com as dores já mapeadas internamente. Pode validar organicamente H1.1, H1.6, H2.1 ou H2.2 antes de qualquer pergunta direcionada.

---

## Bloco B — Modelo financeiro e estrutura de contrato

**B1.** Quando vocês avaliam uma proposta desse tipo de infraestrutura, o que pesa mais: o valor de aquisição do equipamento, o custo total ao longo do contrato, ou outro critério?
*Objetivo:* testar se a lente é mesmo "hard saving" ou se já existe raciocínio de TCO. **[H1.6]**

**B2.** Hoje, quando um site fica indisponível por falta de energia, isso gera penalidade ou custo direto para vocês (contratual, regulatório, operacional)?
*Objetivo:* mede se o risco de indisponibilidade é sentido como custo real — pré-requisito para o modelo de tolling. **[H1.2, H1.4]**

**B3.** Se existisse um modelo em que vocês pagassem pela garantia de disponibilidade do site — e não pelo equipamento em si — isso mudaria a forma como avaliam esse tipo de contrato?
*Objetivo:* testa diretamente o modelo de tolling/uptime como proposta concreta. **[H1.2]** *Cruzamento: a reação aqui também mede a força residual de H1.6.*

**B4.** Qual prazo de contrato vocês considerariam confortável para esse tipo de serviço — e o que tornaria um prazo mais longo (8-10 anos) aceitável?
*Objetivo:* testa a barreira do prazo engessado e recolhe, sem induzir, o que destravaria prazos longos. **[H1.5]** *Cruzamento: liga direto com D1 (domínio/dependência).*

**B5.** Vocês têm hoje algum contrato com escala flexível — capacidade que sobe ou desce conforme a demanda real do site? Como isso funciona com outros fornecedores?
*Objetivo:* entende se a flexibilidade modular (referência Aggreko) já é padrão esperado de mercado ou é uma barreira específica do setor de energia. **[H1.5]**

---

## Bloco C — Sites legados e transição de ativos

**C1.** Para os sites onde vocês já têm baterias e gabinetes recém-instalados, como pensariam a transição para um modelo de serviço? Comprar esse ativo de vocês, dar um desconto proporcional, ou outra abordagem?
*Objetivo:* testa H1.3/H2.3 de forma aberta — deixa o cliente propor o mecanismo, sem assumir que buy-and-lease-back é a resposta certa. **[H1.3, H2.3]**

**C2.** Hoje, quando vocês trocam ou descomissionam baterias/gabinetes, o que acontece com esse material — revendem, sucateiam, devolvem ao fornecedor?
*Objetivo:* pergunta gerada a partir de um achado interno (a Telefônica já vende sucata por conta própria) — descobre se a operadora já tem canal próprio de monetização do ativo usado, o que muda inteiramente a proposta de recompra. **[H1.3]**

---

## Bloco D — Dependência, confiança e risco de fornecedor único

**D1.** O que precisaria estar garantido num contrato de 10 anos para vocês se sentirem confortáveis em terceirizar toda a operação de energia de um site?
*Objetivo:* testa o medo de perder domínio de forma aberta, sem sugerir a resposta (cláusula de saída, transparência, etc.). **[H2.4]** *Cruzamento: liga com B4.*

**D2.** Vocês avaliariam um fornecedor de energia com base no histórico dele em outros contratos que já têm com vocês, ou tratam como decisões completamente separadas?
*Objetivo:* testa se a relação comercial tradicional contamina a decisão sobre o serviço, sem mencionar a Moura nominalmente primeiro (evita resposta socialmente desejável). **[H6.1]**

**D3.** *(Reservada para operadoras com relação histórica a reparar, como a Claro)* Pensando na relação de vocês com a Moura hoje, o que precisaria acontecer para que a confiança em um contrato de longo prazo fosse maior?
*Objetivo:* pergunta direta, nomeando a Moura — só depois de D2 já ter medido o princípio geral. **[H6.1]**

---

## Bloco E — Prioridade real: segurança física vs. dados/plataforma vs. gestão total

**E1.** Quando pensam no que mais gera prejuízo ou dor de cabeça na energia dos sites, o que pesa mais: não saber o que está acontecendo em tempo real, ou os equipamentos serem fisicamente vulneráveis a furto/vandalismo?
*Objetivo:* teste comparativo direto entre as duas hipóteses internamente divergentes. **[H2.1 vs. H4.2]**

**E2.** Se um fornecedor oferecesse só a parte de monitoramento e inteligência de dados, sem mexer no hardware físico que vocês já têm, isso teria valor?
*Objetivo:* testa a variante "telemetria pura", isolada de qualquer alteração física. **[H4.2]**

**E3.** Vocês prefeririam contratar separadamente cada parte da energia do site (bateria, retificador, ar-condicionado, gerador, monitoramento) com fornecedores especializados, ou um único parceiro que cuide de tudo?
*Objetivo:* testa diretamente o apetite por escopo ampliado (gestão total) vs. BaaS pontual. **[H3.2]** *Cruzamento: também informa H7.1 se a resposta apontar preferência por consolidar via torreira/rede neutra.*

**E4.** O que pesa mais na hora de avaliar um fornecedor de bateria: a marca/durabilidade física do produto, ou a qualidade da plataforma de dados e gestão por trás dele?
*Objetivo:* testa diretamente se a plataforma vale mais que o hardware. **[H3.1]**

---

## Bloco F — Regulatório e risco

**F1.** O risco de multa da Anatel por indisponibilidade de rede pesa nas decisões de investimento em energia dos sites? Como isso é tratado internamente — é conversa de Compras, Jurídico, Regulatório?
*Objetivo:* testa o argumento regulatório e mapeia um possível stakeholder novo (área Regulatório) não presente na lista original de entrevistados. **[H1.4]**

---

## Bloco G — Monetização e novos modelos

**G1.** Vocês já pensaram nos sites de telecom como ativos de energia — algo que poderia gerar receita extra vendendo energia de volta para a rede elétrica local?
*Objetivo:* testa o apetite por VPP/monetização de capacidade ociosa — tema mais especulativo, útil para calibrar a maturidade da operadora no assunto. **[H4.1]**

**G2.** Existe hoje algum tipo de relatório ou dado sobre a operação dos sites que vocês pagariam para ter, mas que nenhum fornecedor oferece?
*Objetivo:* reforça H4.2 pelo ângulo do que falta, não do que existe — descobre necessidades ainda não mapeadas. **[H4.2]**

---

## Bloco H — Sustentabilidade e ESG

**H1.** Existe algum requisito de sustentabilidade (ESG, energia renovável, logística reversa) que hoje é obrigatório em editais/BIDs de vocês, ou ainda é um diferencial opcional?
*Objetivo:* testa diretamente se é critério eliminatório ou acessório — pergunta factual, fácil de responder com precisão. **[H5.1]**

---

## Bloco I — Ecossistema: torreiras e redes neutras

**I1.** Como vocês veem a relação entre a gestão da energia do site e a gestão do espaço físico (torre/rooftop)? Faz sentido que esses dois fornecedores sejam a mesma empresa, ou preferem mantê-los separados?
*Objetivo:* testa a hipótese de delegação para torreiras de forma aberta. **[H7.1]**

**I2.** *(Específica para a Ufinet, dado seu perfil de infraestrutura/rede neutra, mais próximo de players como V.tal e Fibrasil do que de uma operadora de varejo)* Hoje, quando vocês oferecem infraestrutura para operadoras/provedores, a energia do site já faz parte do pacote entregue, ou é sempre responsabilidade do cliente final?
*Objetivo:* testa se a Ufinet seria compradora do serviço da Moura para embutir no que revende adiante — o ângulo invertido da mesma hipótese. **[H7.1]**

---

## Bloco J — Fechamento / prospectivo

**J1.** Se a Moura oferecesse esse tipo de serviço para vocês, quem mais, dentro da empresa, precisaria estar convencido para esse contrato avançar?
*Objetivo:* mapeamento de stakeholders para orientar a estratégia de multi-threading da próxima fase — não testa uma hipótese específica desta lista, mas dá continuidade direta ao trabalho da rodada anterior sobre "vender para o stakeholder errado".

---

## Notas de aplicação

- **Ufinet** tem perfil estrutural diferente de Claro/TIM/Algar — mais próximo de uma Rede Neutra do que de uma operadora de varejo. Priorizar os Blocos B, E, I (com ênfase em I2) e reduzir o peso dos blocos C e D, que pressupõem sites de rádio-base próprios como os das outras três.
- **Algar**: dado o perfil predominantemente rooftop/seguro (menos furto), o Bloco E tende a confirmar a plataforma/dados (H3.1/H4.2) como argumento mais forte que segurança física (H2.1) — vale testar mesmo assim, para não presumir.
- **Claro**: priorizar D2/D3 (credibilidade) antes de qualquer pergunta de proposta de valor nova — o desgaste do repricing passado pode enviesar todas as respostas seguintes se não for endereçado primeiro.
- **TIM**: já existe um contato interno "quente" (gerente regional que se ofereceu para ajudar) — Bloco F (regulatório) e G (monetização) tendem a ressoar bem, dado o perfil mais aberto a inovação identificado internamente.

---

*Fontes: `Lista de hipóteses - Consolidadas.docx` (time Moura + MJV) e `Bench_Moura.pdf` (benchmarking de 9 empresas + ecossistema de telecom), cruzados com as 15 transcrições de entrevistas internas.*
