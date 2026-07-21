# Roteiro de Entrevista — Fase 2 (Operadoras)
### Duração estimada: 50-70 min · ● essencial · ○ aprofundamento se houver tempo

**Como usar:** siga a ordem sugerida, mas deixe a conversa fluir — se o entrevistado já respondeu algo mais à frente, pule. As perguntas ● cobrem o mínimo necessário para testar cada hipótese/dor; as ○ aprofundam se o tempo e o interesse permitirem. A lógica completa de cada pergunta (por que ela existe, o que estamos tentando descobrir) está no documento `16-logica-perguntas-por-hipotese.md` — aqui vai só o essencial para conduzir a conversa.

---

## 0. Antes de começar (nota interna, não falar)
- Confirmar gravação/NDA e alinhamento sobre confidencialidade.
- Objetivo comunicado ao entrevistado: entender a visão dele sobre gestão de energia/infraestrutura crítica — **não é uma reunião de apresentação de solução**.
- Registrar cargo, área e tempo de casa da pessoa antes de começar.

## 1. Abertura (3-5 min)

*"Obrigado por reservar esse tempo. A ideia da nossa conversa é entender, pela sua experiência, como funciona hoje a gestão de energia e infraestrutura crítica dos sites de vocês — os desafios, as prioridades, como as decisões são tomadas. Não estamos aqui para apresentar uma solução hoje; queremos genuinamente entender o cenário de vocês primeiro. Tudo bem?"*

---

## 2. Bloco A — Contexto e Organização Atual (5-8 min)

● Como funciona hoje a gestão de energia/backup dos seus sites — quem participa de cada etapa (especificação, compra, instalação, manutenção, monitoramento)?
● Me conta sobre a última vez que algo deu errado na energia de um site — o que aconteceu, como vocês ficaram sabendo, e como foi resolvido?
○ Quais são hoje os maiores problemas ou frustrações que vocês têm com a infraestrutura de energia dos sites?

*Transição: "Você mencionou [retomar algo dito] — eu queria entender um pouco mais alguns desses pontos."*

---

## 3. Bloco B — Validação das Dores Operacionais Percebidas
*(dores identificadas na imersão interna da Moura — aqui testamos se elas se confirmam na voz do cliente, sem presumir)*

**Visibilidade e inventário dos ativos**
● Se eu pedisse para saber quantas baterias estão instaladas e funcionando corretamente num site específico agora, quanto tempo levaria para vocês responderem com confiança?
*Testa o "apagão de inventário" percebido internamente pela Moura, sem presumir que ele existe.*

**Furto e reposição**
● Quando uma bateria é furtada, qual é o processo desde a descoberta até a reposição funcionando de novo no site? Quanto tempo isso costuma levar?
*Valida (ou não) a burocracia de reposição de até 90 dias identificada internamente.*
○ Existe algum padrão nos furtos que vocês já notaram — horário, tipo de site, região?

**Ruído operacional / alarmes**
● Quantos alertas ou chamados relacionados a energia a equipe de vocês recebe, em média, por dia ou semana? Como vocês decidem quais merecem atenção imediata?
*Testa a sobrecarga de alarmes/falsos positivos sem mencionar os números que a Moura já tem internamente.*

**Monitoramento preditivo**
● Hoje, vocês conseguem saber com antecedência que uma bateria está degradando, ou só descobrem quando ela já falhou?
*Testa se o monitoramento do cliente é reativo (binário) ou já tem componente preditivo.*

**Espaço físico / torreiras**
○ O espaço físico disponível nos sites já foi um fator limitante em algum projeto? Como isso é resolvido hoje?

**Fragmentação interna**
○ Quando um problema de energia em um site chega a afetar o cliente final, quantas áreas diferentes da empresa costumam ser acionadas até ele ser resolvido?
*Valida a dor de departamentalização/conflito entre áreas, sem perguntar diretamente sobre conflito.*

**Sites legados**
● Do total de sites que vocês têm hoje, que proporção você diria que já tem infraestrutura de backup mais antiga ou desatualizada?
*Valida a percepção interna de que uma fatia grande do parque é "legado".*

---

## 4. Bloco C — Modelo Financeiro e Contratual (10 min)

**CAPEX como restrição (H1.1)**
● Como funciona o processo orçamentário para investimento em infraestrutura de energia dos sites?
● Se hoje vocês tivessem esse capital livre para outra finalidade, para onde ele provavelmente iria?
○ Quais vantagens e desvantagens vocês veem entre comprar esse tipo de equipamento e contratar um serviço que já inclua o equipamento?

**Hard saving vs. TCO (H1.6)**
● Pode me contar sobre a última vez que vocês compararam propostas de dois fornecedores de equipamento de energia/backup? O que fez uma ganhar da outra?
○ Esses custos indiretos (manutenção, furto, visitas técnicas) são calculados pela mesma área que aprova a compra do equipamento?

**Pagar por disponibilidade (H1.2)**
● Hoje, quando um site fica indisponível por falta de energia, existe algum tipo de consequência contratual para o fornecedor responsável?
○ Onde está o maior risco hoje — no equipamento em si, ou na garantia de que o site vai continuar funcionando independente do que aconteça com o equipamento?

**Flexibilidade de prazo (H1.5)**
● Já tiveram algum contrato de longo prazo que, com o tempo, deixou de fazer sentido pela mudança na necessidade real? O que aconteceu?
○ Vocês já usaram algum modelo de contrato em que a capacidade contratada pode subir ou descer conforme a necessidade muda, com qualquer fornecedor?

---

## 5. Bloco D — Sites Legados e Transição (5 min) — H1.3 / H2.3

● Como vocês pensam o ciclo de vida de um equipamento como bateria ou gabinete depois de instalado — existe um tempo mínimo esperado de uso antes de considerar substituição?
● Já aconteceu de vocês quererem trocar de fornecedor desse tipo de equipamento mesmo com o atual ainda funcionando bem? O que motivou, e o que fizeram com o que já estava instalado?
○ E quando um equipamento é de fato substituído ou um site desativado, o que normalmente acontece com o que foi removido?

---

## 6. Bloco E — Confiança e Dependência (5-8 min) — H2.4 / H6.1

● Vocês já tiveram alguma experiência — boa ou ruim — terceirizando uma parte crítica da operação para um único fornecedor? O que aprenderam?
● Quando avaliam um fornecedor para um contrato novo e maior, o desempenho dele em contratos menores ou anteriores que já existem entra na decisão?
● Como você descreveria o histórico da relação de vocês com a Moura até aqui?
○ Existe algo nessa relação que, se pudesse ser diferente, você mudaria?
○ Existe algum tipo de cláusula que vocês consideram padrão hoje em contratos de fornecimento crítico de longo prazo?

---

## 7. Bloco F — Prioridade: Físico vs. Dados vs. Gestão Total (8 min) — H2.1/H4.2, H3.1, H3.2

**Segurança física vs. dados (hipóteses divergentes internamente)**
● Pensando nos últimos incidentes relacionados à energia dos sites, o que aconteceu, e o que vocês só descobriram depois de já ter causado impacto?
● Se vocês tivessem que escolher entre investir em melhorar a visibilidade sobre os sites ou reforçar a proteção física dos equipamentos, sem poder fazer as duas coisas ao mesmo tempo, o que teria prioridade?

**Plataforma vs. hardware**
○ Pensando nos fornecedores de energia que vocês já tiveram, o que diferenciava o melhor do pior — mais o produto em si, ou como ele era acompanhado depois de instalado?

**Gestão total vs. pontual**
● Especificamente para a energia de um site (bateria, retificador, climatização, gerador, monitoramento), quantos fornecedores diferentes estão envolvidos hoje?
○ Como é a experiência de gerenciar esses fornecedores separadamente — o que funciona bem, o que gera mais atrito?

---

## 8. Bloco G — Regulatório, Monetização e ESG (5 min) — H1.4, H4.1, H5.1

● O risco de multa da Anatel por indisponibilidade de rede pesa nas decisões de investimento em energia dos sites?
○ Existe algum uso hoje, ou em estudo, para a capacidade de energia instalada nos sites além do backup da própria rede?
○ Quais critérios de sustentabilidade, se algum, aparecem hoje nos editais ou processos de compra de vocês?

---

## 9. Bloco H — Ecossistema: Torreiras e Redes Neutras (5 min) — H7.1

● Hoje, como funciona a relação de vocês com quem administra o espaço físico dos sites — é o mesmo fornecedor que cuida da energia, ou são sempre entidades diferentes?
○ Vocês já perceberam alguma vantagem ou desvantagem em ter fornecedores separados para espaço físico e para energia?

**Variante Ufinet** (perfil de rede neutra, não operadora de varejo):
● No pacote de infraestrutura que vocês entregam a operadoras/provedores hoje, o que está incluso além de espaço físico e conectividade?
● Quem, na prática, decide o fornecedor de energia de um site — a Ufinet ou o cliente final?

---

## 10. Fechamento (5 min)

● Quando uma decisão desse porte (fornecedor de infraestrutura crítica, contrato de vários anos) é tomada aqui, quais áreas costumam estar envolvidas, do início ao fim?
● Tem algo sobre como vocês lidam com energia e infraestrutura crítica dos sites que a gente não perguntou, e que você acha importante a gente saber?

*"Muito obrigado pelo tempo e pela abertura. Vamos consolidar o que conversamos com o time e, se fizer sentido, podemos voltar a falar em uma próxima etapa."*

---

## Notas de adaptação por cargo/operadora

- **Diretor(a) de Infraestrutura / Gerente de Engenharia** (ex: Fabiano-Claro, Gustavo Lima-TIM): priorizar Blocos A, F e H — visão técnica e de arquitetura de fornecedores.
- **Gerente de Compras** (ex: Alessandro-Claro, Tatiana Pinel-TIM): priorizar Blocos C, D e E — processo de decisão, TCO, histórico de fornecedor.
- **Gerente Regional / Operações** (ex: Rodrigo Feitoza-TIM, Luisa Prestes-TIM): priorizar Blocos B e F — dor operacional do dia a dia, ruído de alarmes, furto.
- **Ufinet (Cleber Camargo, Head de Operações):** reduzir peso dos Blocos D e E (pressupõem sites de rádio-base próprios); dar todo o tempo extra ao Bloco H com a variante específica.
- **Claro:** iniciar o Bloco E com atenção redobrada — se a relação estiver mesmo desgastada pelo repricing passado, isso deve aparecer espontaneamente antes de perguntar nominalmente sobre a Moura.
- **Algar:** sem contato definido ainda — ver sugestão de perfil (Diretor de Engenharia/Infraestrutura) no documento `15-banco-perguntas-fase2-por-hipotese.md`.

---

*Fontes: hipóteses consolidadas pelo time (`Lista de hipóteses - Consolidadas.docx`), benchmark de mercado (`Bench_Moura.pdf`), dores percebidas na imersão interna (documentos `00` a `15` desta pasta) e lógica de funil por hipótese (`16-logica-perguntas-por-hipotese.md`).*
