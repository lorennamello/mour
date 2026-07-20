# Banco de Perguntas — Fase 2 (Operadoras)
### Versão 2 — revisada para reduzir viés de aceitação

**O que mudou nesta versão:** a v1 tinha perguntas diretas do tipo "isso teria valor pra vocês?" ou que já presumiam a resposta (ex: perguntar o que "tornaria um contrato de 10 anos aceitável" presume que a pessoa consideraria 10 anos). Nesta versão, cada hipótese virou uma **sequência de perguntas menores**, quase todas ancoradas em comportamento e decisões reais já tomadas (não em opinião hipotética), que nunca mencionam a solução da Moura antes de a própria pessoa trazer o conceito à tona. O objetivo não é a operadora responder diretamente à hipótese — é a gente inferir, pela conversa, se ela é verdadeira ou não.

**Técnicas aplicadas em toda a revisão:**
- Perguntar sobre a **última decisão real** tomada (comportamento passado), não sobre preferência hipotética.
- Perguntar sobre **processo e critério** ("como vocês decidem", "quem participa"), não sobre opinião.
- Quando um trade-off é necessário, apresentar como **escolha de recurso escasso** ("se só pudessem fazer uma coisa...") ou pedir para a própria pessoa nomear o que importa, sem eu sugerir as opções.
- Nunca introduzir o conceito da solução da Moura (recompra, pagar por disponibilidade, telemetria isolada, cláusula de saída) dentro da pergunta — deixar esses conceitos emergirem na fala do entrevistado, e só then aprofundar.

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
*Aquecimento, sem hipótese isolada — mapeia como a operadora decide hoje.*

**A1.** Como funciona hoje a gestão de energia/backup dos seus sites — quem participa de cada etapa (especificação, compra, instalação, manutenção, monitoramento)?
*Objetivo:* mapear a estrutura de decisão real, sem induzir nenhuma resposta — é uma pergunta de fato, não de opinião.

**A2.** Me conta sobre a última vez que algo deu errado na energia de um site — o que aconteceu, como vocês ficaram sabendo, e como foi resolvido?
*Objetivo:* captura comportamento real (não hipotético) para depois cruzar organicamente com H2.1, H2.2 e H4.2, sem nomear essas hipóteses na pergunta.

**A3.** Quais são hoje os maiores problemas ou frustrações que vocês têm com a infraestrutura de energia dos sites?
*Objetivo:* pergunta aberta de controle — o que a pessoa cita espontaneamente, sem qualquer sugestão minha, é o sinal mais forte de prioridade real.

---

## Bloco B — Modelo financeiro e estrutura de contrato

### H1.1 — CAPEX é uma restrição real / OPEX é preferido
**B1.** Como funciona o processo orçamentário para investimento em infraestrutura de energia dos sites — de que linha de orçamento isso normalmente sai?
*Objetivo:* entender se CAPEX é hoje uma restrição sentida na prática, sem perguntar diretamente "CAPEX é um problema pra vocês?".

**B2.** Nos últimos dois anos, algum projeto de expansão ou modernização de rede foi adiado, reduzido ou repriorizado por causa de disponibilidade de orçamento? Pode me contar como foi esse processo?
*Objetivo:* busca um evento concreto e recente — evidência muito mais confiável do que uma resposta a "vocês têm restrição de CAPEX?".

**B3.** Quando vocês pensam em onde investir capital este ano, com quais outras áreas a energia dos sites compete por prioridade?
*Objetivo:* mede o peso relativo do tema sem sugerir que ele deveria ser prioritário.

### H1.6 — hard saving vs. TCO
**B4.** Pode me contar sobre a última vez que vocês compararam propostas de dois fornecedores diferentes para esse tipo de equipamento ou serviço? O que fez uma proposta ganhar da outra?
*Objetivo:* decisão real e recente, não princípio declarado — evita a resposta socialmente desejável de "nós olhamos o TCO completo".

**B5.** Quando essa comparação é feita, quais custos entram na conta além do preço do equipamento — manutenção, visitas técnicas, reposição por furto, outros?
*Objetivo:* testa concretamente se custos indiretos entram na decisão real, sem perguntar "vocês pensam em TCO?".

**B6.** Esses custos indiretos são calculados pela mesma área que aprova a compra do equipamento, ou ficam em orçamentos/áreas diferentes?
*Objetivo:* revela se a comparação "injusta" (aluguel completo vs. bateria seca) acontece por escolha ou por fragmentação estrutural entre áreas — informação valiosa mesmo que a H1.6 se confirme.

### H1.2 — pagar por disponibilidade (tolling/uptime)
**B7.** Como é medido hoje o desempenho de um fornecedor de energia ou backup — existe algum indicador que vocês acompanham?
*Objetivo:* descobre se já existe uma cultura de medir resultado (não só entrega), sem introduzir o conceito de "pagar por disponibilidade".

**B8.** Pensando nos contratos de fornecimento que vocês têm hoje, em quais deles o pagamento está de alguma forma atrelado a um resultado ou desempenho, e em quais está atrelado só à entrega do produto?
*Objetivo:* pergunta-ponte — se a pessoa já reconhece esse tipo de estrutura em outros contratos, o caminho para aceitar um modelo de disponibilidade fica mais claro (ou não), sem eu ter proposto nada ainda.

### H1.5 — flexibilidade / prazo
**B9.** Quais são hoje os prazos típicos dos contratos de fornecimento e serviço que vocês assinam para infraestrutura de rede, de forma geral?
*Objetivo:* estabelece a régua real de comparação antes de qualquer pergunta sobre prazos longos.

**B10.** Como vocês avaliam se o prazo de um contrato é um risco aceitável, quando comparam propostas de fornecedores diferentes?
*Objetivo:* processo de decisão, não opinião sobre "10 anos seria bom ou ruim" — deixa a pessoa trazer o próprio critério.

**B11.** Já aconteceu de vocês precisarem encerrar ou renegociar um contrato antes do prazo por mudança de necessidade (aumento ou redução de demanda em algum site)? O que aconteceu nesse processo?
*Objetivo:* evento real — se a resposta for "sim, e foi difícil", já sinaliza a barreira de flexibilidade sem eu ter perguntado sobre ela diretamente.

---

## Bloco C — Sites legados e transição de ativos

### H1.3 / H2.3 — legado e recompra de ativos
**C1.** O que geralmente acontece com um equipamento (bateria, gabinete) quando ele é substituído ou um site é desativado?
*Objetivo:* factual, sem viés — descobre se já existe canal próprio de revenda/sucateamento (acha crítico para avaliar se "recomprar o ativo" é percebido como valor novo ou redundante).

**C2.** Já aconteceu de vocês avaliarem trocar de fornecedor ou modelo de contratação num site onde o equipamento atual ainda estava dentro da vida útil? O que pesou nessa decisão?
*Objetivo:* evento real análogo à situação de "site legado" — deixa a barreira (ou não) emergir organicamente.

**C3.** Se vocês tivessem que decidir hoje entre continuar com um equipamento recém-adquirido ou migrar para um novo modelo de fornecimento mais vantajoso a longo prazo, o que pesaria mais nessa decisão?
*Objetivo:* única pergunta hipotética do bloco, usada só depois das duas anteriores já terem dado contexto — apresentada como tensão genérica, não como "a Moura recompraria seu ativo".

---

## Bloco D — Dependência, confiança e risco de fornecedor único

### H2.4 — medo de perder domínio da operação
**D1.** Vocês já tiveram alguma experiência — boa ou ruim — terceirizando uma parte crítica da operação para um único fornecedor? O que aprenderam com isso?
*Objetivo:* experiência real e específica, não medo hipotético — normalmente revela a origem real de qualquer receio, se existir.

**D2.** O que costuma pesar mais quando vocês avaliam se um fornecedor pode assumir uma responsabilidade crítica — histórico dele, tamanho/estrutura da empresa, cláusulas contratuais específicas, outra coisa?
*Objetivo:* pergunta aberta de critério, sem eu sugerir nenhuma opção como "correta".

**D3.** Existe algum tipo de cláusula ou estrutura que vocês consideram padrão hoje em contratos de fornecimento crítico de longo prazo — algo que vocês simplesmente não assinariam sem ter?
*Objetivo:* deixa conceitos como cláusula de saída, transição assistida, etc. emergirem na fala da própria pessoa, sem eu ter mencionado nenhum deles.

### H6.1 — credibilidade / histórico da relação
**D4.** Quando avaliam um fornecedor para um contrato novo e maior, o desempenho dele em contratos menores ou anteriores que já existem entra na decisão? Tem algum exemplo de quando isso pesou, positiva ou negativamente?
*Objetivo:* pergunta de princípio geral, sem mencionar a Moura — mede se a lógica "histórico contamina decisão" existe antes de perguntar sobre o caso específico.

**D5.** Como você descreveria o histórico da relação de vocês com a Moura até aqui?
*Objetivo:* pergunta aberta e neutra — não presume que há desgaste; deixa a pessoa trazer isso (ou não) com as próprias palavras.

**D6.** Existe algo nessa relação que, se pudesse ser diferente, você mudaria?
*Objetivo:* segue naturalmente da D5 só se algo relevante for mencionado — evita forçar a reconstrução de confiança como pauta se a pessoa não trouxe o tema.

---

## Bloco E — Segurança física vs. dados/plataforma vs. gestão total

### H2.1 vs. H4.2 — a hipótese divergente (segurança física vs. dados)
**E1.** Pensando nos últimos incidentes que vocês tiveram relacionados à energia dos sites (queda, furto, falha), o que teve mais impacto: não saber que algo tinha acontecido a tempo, ou o dano físico/perda do próprio equipamento?
*Objetivo:* ancorado em eventos reais recentes, pede para a própria pessoa comparar — não sugiro qual das duas é mais importante.

**E2.** Se vocês tivessem que priorizar entre melhorar a visibilidade sobre o que acontece nos sites ou reforçar a proteção física dos equipamentos, sem poder fazer as duas coisas ao mesmo tempo, o que teria prioridade?
*Objetivo:* forçar a escolha via cenário de recurso escasso (técnica que reduz a tendência de responder "as duas são importantes") — mede diretamente qual das duas hipóteses divergentes domina.

### H4.2 — dados inteligentes
**E3.** Que tipo de informação sobre os sites vocês gostariam de ter hoje, mas não têm acesso?
*Objetivo:* pergunta aberta, sem sugerir "telemetria" ou qualquer solução — o que a pessoa cita espontaneamente é o dado mais confiável.

**E4.** Quando vocês precisam saber algo específico sobre um site (ex: quanto tempo de autonomia resta, se houve alguma queda recente), como essa informação chega até vocês hoje, e quanto tempo leva?
*Objetivo:* mede a dor real de acesso à informação sem introduzir a ideia de monitoramento remoto.

**E5.** Como vocês decidem hoje se vale a pena contratar uma camada extra de análise ou relatório sobre algo que já é monitorado de forma básica?
*Objetivo:* testa disposição a pagar por inteligência de dados de forma indireta — pelo processo de decisão, não perguntando "vocês pagariam por isso?".

### H3.1 — plataforma vale mais que hardware
**E6.** Quando vocês avaliam diferentes marcas ou fornecedores de bateria/equipamento, o que entra na comparação além do preço?
*Objetivo:* pergunta aberta — se "gestão", "dados" ou "visibilidade" surgirem espontaneamente, é sinal forte; se não surgirem, também é um dado importante.

**E7.** Pensando nos fornecedores de energia que vocês já tiveram, o que diferenciava o melhor do pior — mais o produto em si, ou como ele era acompanhado depois de instalado?
*Objetivo:* comparação baseada em experiência real, não em preferência abstrata.

### H3.2 — gestão total de energia
**E8.** Hoje, quantos fornecedores diferentes estão envolvidos na energia de um site típico (bateria, retificador, climatização, gerador, monitoramento)?
*Objetivo:* factual, estabelece a linha de base antes de qualquer pergunta sobre consolidação.

**E9.** Como é a experiência de gerenciar esses fornecedores separadamente — o que funciona bem, o que gera mais atrito?
*Objetivo:* deixa a dor de fragmentação (ou a ausência dela) emergir organicamente, sem sugerir que "um fornecedor único" seria melhor.

---

## Bloco F — Regulatório e risco

### H1.4 — argumento regulatório
**F1.** Quais exigências regulatórias vocês monitoram hoje em relação à disponibilidade de rede?
*Objetivo:* mapeia o peso do tema regulatório de forma factual antes de qualquer pergunta de priorização.

**F2.** Já aconteceu de vocês serem penalizados, multados ou notificados por indisponibilidade de rede relacionada a energia? Como isso foi tratado internamente?
*Objetivo:* evento real, se existir — evidência muito mais forte do que perguntar "isso preocupa vocês?".

**F3.** Entre os fatores que pesam numa decisão de investimento em energia dos sites, como vocês descreveriam a importância relativa de custo, risco regulatório e risco operacional — sem que eu sugira uma ordem?
*Objetivo:* pede que a própria pessoa ranqueie os fatores, evitando que a "resposta certa" já esteja embutida na pergunta.

---

## Bloco G — Monetização e novos modelos

### H4.1 — monetização de capacidade ociosa (VPP)
**G1.** Existe algum uso hoje, ou em estudo, para a capacidade de energia instalada nos sites além do backup da própria rede?
*Objetivo:* pergunta aberta, sem introduzir o conceito de venda de energia — testa maturidade real do tema.

**G2.** Existe alguma área ou iniciativa hoje olhando para eficiência energética, energia renovável ou receita a partir de ativos físicos da empresa, de forma mais ampla?
*Objetivo:* mede se o assunto já está no radar institucional, sem perguntar diretamente sobre monetização de bateria.

---

## Bloco H — Sustentabilidade e ESG

### H5.1 — ESG como critério eliminatório
**H1.** Quais critérios de sustentabilidade, se algum, aparecem hoje nos editais ou processos de compra de vocês?
*Objetivo:* factual e aberto, sem sugerir que deveria haver critério nenhum.

**H2.** Nos últimos processos de contratação de fornecedores de infraestrutura, algum fornecedor foi desclassificado ou perdeu pontos por não atender a critérios ambientais? Pode me contar sobre isso?
*Objetivo:* evento real — testa se o critério é eliminatório na prática, não apenas em teoria/discurso.

---

## Bloco I — Ecossistema: torreiras e redes neutras

### H7.1 — delegação para torreiras/redes neutras
**I1.** Hoje, como funciona a relação de vocês com quem administra o espaço físico dos sites (torres, rooftops) — é o mesmo fornecedor que cuida da energia, ou são sempre entidades diferentes?
*Objetivo:* factual, mapeia a estrutura real do ecossistema para aquela operadora.

**I2.** Vocês já perceberam alguma vantagem ou desvantagem em ter fornecedores separados para espaço físico e para energia?
*Objetivo:* deixa a percepção sobre consolidação (a favor ou contra) emergir da experiência real, sem sugerir a resposta esperada.

**I3.** *(específica para a Ufinet)* No pacote de infraestrutura que vocês entregam a operadoras e provedores hoje, o que está incluso além do espaço físico e conectividade?
*Objetivo:* factual — descobre se energia já está ou poderia estar dentro do escopo que a Ufinet revende, sem perguntar diretamente "vocês comprariam energia da Moura para revender?".

**I4.** *(específica para a Ufinet)* Quem normalmente decide o fornecedor de energia de um site — vocês, ou o cliente final que usa a infraestrutura de vocês?
*Objetivo:* mapeia se a Ufinet tem, de fato, poder de decisão sobre esse ponto — pré-requisito para a hipótese fazer sentido nesse cliente específico.

---

## Bloco J — Fechamento / prospectivo

**J1.** Quando uma decisão desse porte (fornecedor de infraestrutura crítica, contrato de vários anos) é tomada aqui, quais áreas costumam estar envolvidas, do início ao fim?
*Objetivo:* mapeamento de stakeholders baseado em processo real, não hipotético.

**J2.** Pensando numa decisão parecida que vocês tomaram recentemente, quem precisou aprovar em cada etapa?
*Objetivo:* ancora a J1 num caso concreto — evita a resposta genérica/institucional ("normalmente é o comitê X") que nem sempre reflete o que acontece na prática.

**J3.** Tem algo sobre como vocês lidam com energia e infraestrutura crítica dos sites que a gente não perguntou, e que você acha importante a gente saber?
*Objetivo:* pergunta de fechamento aberta — captura qualquer hipótese não coberta e sinaliza respeito pelo tempo/conhecimento da pessoa.

---

## Notas de aplicação

- **Ufinet**: priorizar Blocos B, E, I (com ênfase em I3/I4) — perfil de rede neutra, não operadora de varejo. Reduzir peso dos Blocos C e D, que pressupõem sites de rádio-base próprios.
- **Algar**: aplicar o Bloco E integralmente, mesmo com a expectativa (não confirmada) de menor incidência de furto pelo perfil rooftop — não presumir a resposta antes de perguntar.
- **Claro**: aplicar D4-D6 com atenção — se a relação estiver mesmo desgastada, isso pode aparecer espontaneamente já na D4, antes mesmo de perguntar nominalmente sobre a Moura.
- **TIM**: sem ajuste especial necessário: o roteiro completo se aplica bem dado o perfil mais aberto já identificado internamente.

---

*Fontes: `Lista de hipóteses - Consolidadas.docx` (time Moura + MJV) e `Bench_Moura.pdf` (benchmarking de 9 empresas + ecossistema de telecom), cruzados com as 15 transcrições de entrevistas internas.*
