# Roteiro de Entrevista — Fase 2 (Operadoras)
### Versão 2 — fluxo exploratório, sem bloco isolado de "dores"
### Duração estimada: 50-70 min · ● essencial · ○ aprofundamento se houver tempo

**O que mudou nesta versão:** a v1 tinha um bloco só para validar as dores operacionais, separado dos blocos de hipótese, e vários blocos entravam direto na pergunta pontual sem abrir com contexto — o que deixava a conversa parecendo um interrogatório. Agora cada bloco é organizado por **tema real de conversa** (fornecedores/contratação, operação do dia a dia, infraestrutura física, dependência de fornecedor, prioridades, regulatório, ecossistema) e sempre abre com uma pergunta ampla de contexto antes de estreitar para hipótese ou dor específica. As perguntas de dor interna ficam dentro do bloco a que pertencem, não isoladas.

**Como usar:** siga a ordem sugerida, mas deixe a conversa fluir — se o entrevistado já respondeu algo mais à frente, pule. As perguntas ● cobrem o mínimo necessário; as ○ aprofundam se o tempo permitir. A lógica completa de cada pergunta está no documento `16-logica-perguntas-por-hipotese.md`.

---

## 0. Antes de começar (nota interna, não falar)
- Confirmar gravação/NDA e alinhamento sobre confidencialidade.
- Objetivo comunicado ao entrevistado: entender a visão dele sobre gestão de energia/infraestrutura crítica — **não é uma reunião de apresentação de solução**.
- Registrar cargo, área e tempo de casa da pessoa antes de começar.

## 1. Abertura (3-5 min)

*"Obrigado por reservar esse tempo. A ideia da nossa conversa é entender, pela sua experiência, como funciona hoje a gestão de energia e infraestrutura crítica dos sites de vocês — os desafios, as prioridades, como as decisões são tomadas. Não estamos aqui para apresentar uma solução hoje; queremos genuinamente entender o cenário de vocês primeiro. Tudo bem?"*

---

## 2. Bloco 1 — Panorama Geral (5-8 min)
*Abertura ampla, sem hipótese isolada — entender o cenário antes de entrar em qualquer tema específico.*

● Como funciona hoje a gestão de energia/backup dos seus sites — quem participa de cada etapa (especificação, compra, instalação, manutenção, monitoramento)?
● Me conta sobre a última vez que algo deu errado na energia de um site — o que aconteceu, como vocês ficaram sabendo, e como foi resolvido?
○ Quais são hoje os maiores problemas ou frustrações que vocês têm com a infraestrutura de energia dos sites?

*Transição: "Você mencionou [retomar algo dito] — eu queria entender um pouco mais alguns desses pontos."*

---

## 3. Bloco 2 — Fornecedores e Modelo de Contratação (10 min)
*Abre entendendo como a contratação funciona hoje, antes de perguntar sobre orçamento, comparação de propostas e prazos.*

● Como funciona, de forma geral, a contratação de empresas fornecedoras de infraestrutura para vocês — como costuma ser esse processo, do início ao fim?
● E especificamente para energia/backup dos sites, como isso funciona hoje — vocês têm um fornecedor principal ou vários, contratos curtos ou longos?

**CAPEX como restrição (H1.1)**
● Como funciona o processo orçamentário quando um projeto desses precisa de investimento?
● Se hoje vocês tivessem esse capital livre para outra finalidade, para onde ele provavelmente iria?

**Hard saving vs. TCO (H1.6)**
● Pode me contar sobre a última vez que vocês compararam propostas de dois fornecedores de equipamento de energia/backup? O que fez uma ganhar da outra?

**Pagar por disponibilidade (H1.2)**
● Hoje, quando um site fica indisponível por falta de energia, existe algum tipo de consequência contratual para o fornecedor responsável?

**Flexibilidade de prazo (H1.5)**
○ Já tiveram algum contrato de longo prazo que, com o tempo, deixou de fazer sentido pela mudança na necessidade real? O que aconteceu?

---

## 4. Bloco 3 — Operação do Dia a Dia: Monitoramento, Alarmes e Furto (10-12 min)
*Abre entendendo a rotina de acompanhamento dos sites, antes de perguntar sobre volume de alarmes, inventário e furto.*

● No dia a dia, como funciona o acompanhamento dos sites — quem monitora, com que frequência, o que é rotina e o que costuma ser exceção?
● Quantos alertas ou chamados relacionados a energia a equipe de vocês recebe, em média, por dia ou semana? Como vocês decidem quais merecem atenção imediata?
● Se eu pedisse para saber quantas baterias estão instaladas e funcionando corretamente num site específico agora, quanto tempo levaria para vocês responderem com confiança?
● Hoje, vocês conseguem saber com antecedência que uma bateria está degradando, ou só descobrem quando ela já falhou?
● Quando uma bateria é furtada, qual é o processo desde a descoberta até a reposição funcionando de novo no site? Quanto tempo isso costuma levar?
○ Existe algum padrão nos furtos que vocês já notaram — horário, tipo de site, região?

---

## 5. Bloco 4 — Infraestrutura Física e Legado dos Sites (8 min)
*Abre com o panorama do parque de sites, antes de perguntar sobre espaço físico e substituição de equipamentos.*

● Como é composto hoje o parque de sites de vocês — é bem heterogêneo em idade e tipo de instalação, ou razoavelmente padronizado?
● Que proporção você diria que já tem infraestrutura de backup mais antiga ou desatualizada?
○ O espaço físico disponível nos sites já foi um fator limitante em algum projeto? Como isso é resolvido hoje?
● Como vocês pensam o ciclo de vida de um equipamento como bateria ou gabinete depois de instalado — existe um tempo mínimo esperado de uso antes de considerar substituição?
● Já aconteceu de vocês quererem trocar de fornecedor desse tipo de equipamento mesmo com o atual ainda funcionando bem? O que motivou, e o que fizeram com o que já estava instalado?
○ E quando um equipamento é de fato substituído ou um site desativado, o que normalmente acontece com o que foi removido?

---

## 6. Bloco 5 — Fornecedores Críticos: Confiança e Dependência (8 min)
*Abre mapeando quantos fornecedores críticos existem hoje, antes de perguntar sobre terceirizar e sobre a relação com a Moura.*

● Hoje, quantos fornecedores diferentes vocês têm envolvidos na parte crítica da operação de energia, e como essas relações costumam ser estruturadas — contratos curtos, parcerias de longo prazo, uma mistura dos dois?
○ Quando um problema de energia em um site chega a afetar o cliente final, quantas áreas diferentes da empresa costumam ser acionadas até ele ser resolvido?
● De forma geral, como a empresa decide o que manter sob controle direto e o que pode ser delegado a terceiros, quando se trata de funções críticas?
● Vocês já tiveram alguma experiência — boa ou ruim — terceirizando uma parte crítica da operação para um único fornecedor? O que aprenderam?
● Quando avaliam um fornecedor para um contrato novo e maior, o desempenho dele em contratos menores ou anteriores que já existem entra na decisão?
● Como você descreveria o histórico da relação de vocês com a Moura até aqui?

---

## 7. Bloco 6 — Prioridades: O Que Mais Preocupa na Energia dos Sites (8 min)
*Retoma os incidentes já mencionados no Bloco 1 para entender o que mais pesa: visibilidade, proteção física ou fragmentação de fornecedores.*

● Entre os problemas de energia que vocês têm hoje, quais vocês diriam que geram mais trabalho ou custo para resolver, depois que acontecem?
● Pensando nos últimos incidentes relacionados à energia dos sites, o que aconteceu, e o que vocês só descobriram depois de já ter causado impacto?
● Se vocês tivessem que escolher entre investir em melhorar a visibilidade sobre os sites ou reforçar a proteção física dos equipamentos, sem poder fazer as duas coisas ao mesmo tempo, o que teria prioridade?
○ Pensando nos fornecedores de energia que vocês já tiveram, o que diferenciava o melhor do pior — mais o produto em si, ou como ele era acompanhado depois de instalado?
● Especificamente para a energia de um site (bateria, retificador, climatização, gerador, monitoramento), quantos fornecedores diferentes estão envolvidos hoje?

---

## 8. Bloco 7 — Regulatório, Monetização e Sustentabilidade (5 min)
*Abre com o que já é monitorado hoje em termos regulatórios, antes de perguntar sobre peso na decisão, monetização e ESG.*

● Quais exigências regulatórias vocês monitoram hoje em relação à disponibilidade de rede?
● Isso pesa nas decisões de investimento em energia dos sites? Já aconteceu de vocês serem penalizados ou notificados por indisponibilidade?
○ Existe algum uso hoje, ou em estudo, para a capacidade de energia instalada nos sites além do backup da própria rede?
○ Quais critérios de sustentabilidade, se algum, aparecem hoje nos editais ou processos de compra de vocês?

---

## 9. Bloco 8 — Ecossistema: Espaço Físico e Energia (5 min)

● Hoje, como funciona a relação de vocês com quem administra o espaço físico dos sites — é o mesmo fornecedor que cuida da energia, ou são sempre entidades diferentes?
○ Vocês já perceberam alguma vantagem ou desvantagem em ter fornecedores separados para espaço físico e para energia?

**Variante Ufinet** (perfil de rede neutra, não operadora de varejo):
● Como vocês descreveriam o portfólio de serviços que a Ufinet oferece hoje para operadoras/provedores — além de conectividade e espaço físico, o que mais costuma estar incluso?
● A energia dos sites hoje entra de alguma forma no que vocês oferecem, ou é sempre responsabilidade do cliente final?
● Quem, na prática, decide o fornecedor de energia de um site — a Ufinet ou o cliente final?

---

## 10. Bloco 9 — Fechamento (5 min)

● Quando uma decisão desse porte (fornecedor de infraestrutura crítica, contrato de vários anos) é tomada aqui, quais áreas costumam estar envolvidas, do início ao fim?
● Tem algo sobre como vocês lidam com energia e infraestrutura crítica dos sites que a gente não perguntou, e que você acha importante a gente saber?

*"Muito obrigado pelo tempo e pela abertura. Vamos consolidar o que conversamos com o time e, se fizer sentido, podemos voltar a falar em uma próxima etapa."*

---

## Notas de adaptação por cargo/operadora

- **Diretor(a) de Infraestrutura / Gerente de Engenharia** (ex: Fabiano-Claro, Gustavo Lima-TIM): priorizar Blocos 1, 6 e 8 — visão técnica e de arquitetura de fornecedores.
- **Gerente de Compras** (ex: Alessandro-Claro, Tatiana Pinel-TIM): priorizar Blocos 2, 4 e 5 — processo de decisão, TCO, histórico de fornecedor.
- **Gerente Regional / Operações** (ex: Rodrigo Feitoza-TIM, Luisa Prestes-TIM): priorizar Blocos 3 e 6 — dor operacional do dia a dia, ruído de alarmes, furto.
- **Ufinet (Cleber Camargo, Head de Operações):** reduzir peso dos Blocos 4 e 5 (pressupõem sites de rádio-base próprios); dar todo o tempo extra ao Bloco 8 com a variante específica.
- **Claro:** conduzir o Bloco 5 com atenção redobrada — se a relação estiver mesmo desgastada pelo repricing passado, isso deve aparecer espontaneamente antes de perguntar nominalmente sobre a Moura.
- **Algar:** sem contato definido ainda — ver sugestão de perfil (Diretor de Engenharia/Infraestrutura) no documento `15-banco-perguntas-fase2-por-hipotese.md`.

---

*Fontes: hipóteses consolidadas pelo time (`Lista de hipóteses - Consolidadas.docx`), benchmark de mercado (`Bench_Moura.pdf`), dores percebidas na imersão interna (documentos `00` a `15` desta pasta) e lógica de funil por hipótese (`16-logica-perguntas-por-hipotese.md`).*
