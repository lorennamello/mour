# Análise Temática — Francisco (Diretor de TI)

**Contexto da entrevista:** diretor de TI do grupo Moura, envolvido desde a concepção do projeto em 2022 (aproximação com AWS).

---

## 1. Proposta de valor — o que entrega e para quem

**Fato:** ele descreve o valor sob a ótica do que a plataforma deveria entregar: "recursos básicos, alarmística [...] a capacidade preditiva de saber quando o site está sendo furtado [...] agir proativamente [...] fornecer informações para a própria operadora [...] Não temos a obrigação de passá-las, mas no nosso ponto de vista é um diferencial para o negócio."
**Fato — valor para a própria Moura (não só para o cliente):** os dados coletados ajudam a entender ciclos de bateria, dimensionar capacidade corretamente, identificar falhas de qualidade — "para a Moura, para a fábrica" isso é "extremamente positivo".
**Fato — visão de futuro do valor:** "o futuro [...] é a gente conseguir vender aquilo que é intangível [...] os dados [...] têm algum valor. O que a gente não descobriu ainda [...] é como interpretar esses [dados]. Como eu transformo o dado em informação." Cita analogia com Amazon/Magazine Luiza (migração de varejo para tecnologia).

**Interpretação:** Francisco enxerga o valor do produto em duas camadas temporais distintas: hoje é operacional/defensivo (evitar furto, cumprir SLA); no futuro, é a monetização de dados como produto em si — ele é o único entrevistado que articula essa segunda camada como tese central de sua visão.

---

## 2. Desafios internos por área

### Tecnologia (a área dele)
**Fato — causa raiz dos problemas de alarmística:** não é primariamente conectividade, mas **erro de instalação de hardware/firmware em campo**: "quando a gente vai investigando [...] a gente vê que não é telecomunicação puramente [...] existe uma questão ainda fundamental [...] que é a parte de como foi feita a instalação do hardware e do firmware."
**Fato — magnitude do problema:** estimativa de ~70-80 sites com fonte mal instalada, "arredondando aí uns 30, 35%" (dos sites auditados na época).
**Fato — falha de handover entre áreas:** "teve, na minha visão, uma deficiência no handover de algumas questões [...] tem a deficiência do fato dessa galera não estar [sob] a gestão de priorização de André[a]." — aponta necessidade de a PO orquestrar melhor engenharia, ITEM e TI.
**Fato — plataforma ainda em fase de maturação:** "essa versão final estável nunca chegou, em termos de hardware [...] no patamar industrial" — o "Connect" ainda roda numa Raspberry Pi não industrializada.
**Fato — dependência de terceiro para controle de acesso (cadeado):** "hoje a gente tem terceirizado e é muito sensível [...] eu dependo do terceiro estar totalmente funcional [...] ainda é uma fragilidade do ecossistema."
**Fato — segurança da informação com fornecedores chineses:** "tem me preocupado muito, tirado meu sono [...] alguns componentes chineses que a gente tem usado [...] Eu não tenho estabelecido um padrão de segurança da informação [...] a gente não tem [...] um monitoramento contínuo, 24 por 7."

### Produto/Operação (via a lente dele)
**Fato:** só ~30 mil dos sites totais do mercado têm bateria de fato instalada nas operadoras em geral (dado repetido por outros, mas ele reforça a leitura estratégica: TI é o "agente para mudar a forma como a empresa trabalha").
**Fato:** reorganização recente da TI em 4 Business Units (BUs) para focar em produto, não só projeto — processo que "devemos concluir esse ano" (na época da entrevista).

### Financeiro
**Fato — tensão estrutural CAPEX x OPEX:** "para telecom, o FII é muito pequeno mensal [...] é muito grande[,] o CAPEX inicial. O contrato também é muito grande, são [prazos] muito longos, mas o FII mensal não comporta a solução [de segurança robusta 24x7]. A gente tem que ser criativo."

### Comercial
Não é foco direto — ele comenta apenas de forma lateral sobre a necessidade de "trabalhar essa troca de valores" com operadoras (ex.: parceria de conectividade/satélite com a TIM/V8) como possível moeda de troca comercial futura.

---

## 3. Áreas internas — como ele percebe outras áreas

**Fato — sobre o ITEM:** "o ITEM entregou essa POC [...] hoje a gente faz P&D e suporte do produto. A Moura[,] ela conseguiu absorver em parte o software, mas ela usa ainda por trás a base de dados que a gente suporta" — reconhece que o hardware de telecom (diferente do BES) ainda não foi transferido tecnologicamente para dentro da Moura, criando dependência contínua do ITEM.
**Fato — sobre a governança do produto (Andrea/PO):** reforça que a gestão de priorização do time disciplinar (TI + engenharia + ITEM) deveria estar com Andrea — "é o que a gente vem, entre aspas, costurando" (sugerindo que essa costura ainda não é fluida).
**Fato — sobre a relação TI ↔ Moura Energia:** "a Moura Energia [...] acaba alocando micro[times] nas outras empresas da Moura para servir a ela [...] o pagamento para a gente vem de forma indireta [...] é como se a gente fosse um terceirizado" — mesmo estando "sob o mesmo guarda-chuva", a relação funcional é quase de prestação de serviço interno, com todas as fricções que isso pode gerar.

---

## 4. Modelo comercial

Não é a área dele; contribui apenas com uma leitura de possível "moeda de troca" com operadoras (parcerias de conectividade), mas não descreve processo comercial.

---

## 5. Visão sobre os clientes

**Fato — leitura estratégica do movimento das operadoras (via conversa recente com a V8/TIM):** "o plano do cara é o seguinte [...] Enquanto telecomunicação, eu não tenho como me sustentar a operação [...] Eu preciso partir para [...] fazer tecnologia [...] É tanto que a Claro se juntou com a HITS, a [TIM] comprou a V8 e a Vivo está patinando ainda nesse meio de campo."
**Fato — projeto concreto citado (Anel Verde, SP):** operadoras avançando para "soluções compostas" de infraestrutura + tecnologia (ex.: visão computacional substituindo cabines de pedágio) — ele lê isso como uma tendência estrutural de as operadoras precisarem de parceiros de infraestrutura física (como a Moura) para viabilizar esses projetos, já que elas não têm o ativo físico (bateria) necessário.

**Interpretação:** ele antecipa que as operadoras vão precisar cada vez mais de parceiros como a Moura à medida que migram para "tecnologia" além do core de telecom — isso posicionaria a Moura não como fornecedora de energia, mas como parte de um ecossistema de infraestrutura mais amplo.

---

## 6. Barreiras de expansão

**Fato — 3 motivos para o crescimento não ser mais acelerado hoje** (ele enumera explicitamente): (1) falta de confiabilidade 100% do ecossistema; (2) CAPEX alto de gabinete/instalação exigindo eficiência para começar a amortizar; (3) falta de disciplina/padrões de instalação e checagem — "a gente ainda não aprendeu a trabalhar de forma disciplinar."
**Fato:** ritmo de expansão também depende do cliente — "ela [Vivo] direciona [...] tem esse lote aqui disponível" — mesmo com capacidade ociosa (~200 sites liberados), o gargalo real, segundo ele, "seria menos" essa liberação e mais os 3 fatores internos citados.

---

## 7. Ecossistema e mercado

**Fato — referências internacionais dele:** EUA (qualidade, especialmente Califórnia — clima parecido com o Brasil), China (velocidade mas qualidade inferior — "a China deixa de ser uma inspiração nessa perspectiva de qualidade"), Israel (cybersecurity, "indiscutível o nível que eles estão"), Palo Alto e Fortinet (segurança), Oracle (processamento de dados a médio prazo).
**Fato — benchmark nacional:** WEG — "eles são muito mais ousados [...] o risco é muito mais alto [...] a gente aqui na Amor sempre vai ser um passo de cada vez."
**Fato — visão crítica sobre dependência da China:** "eles copiam tudo [...] eu só não acredito que eles invadiram ainda o Brasil e colonizaram porque a gente tem as barreiras tarifárias [...] se não fosse isso, eu não sei o que seria da indústria nacional" — mesmo assim, a Moura acabou de assinar contrato com fornecedor chinês (K-12) para nova linha na metalúrgica, ilustrando a tensão entre discurso e prática.

---

## 8. Visão de futuro

**Fato — dois eixos de evolução da plataforma:**
1. **Dados** — infraestrutura de hardware/software para suportar crescimento, armazenar e processar mais dados, "transformar isso em informação".
2. **Ampliar a receita além do FII mensal** — usar a capacidade física instalada (sites) para outras finalidades: carregamento veicular ("eletroposto"), sensores adicionais (meteorologia, temperatura), replicar o modelo para outros setores (bancos, home base).
**Fato — conceito de "chassi único":** unificar telecom + BES + HomeBES numa mesma base/infraestrutura de dados para ganhar densidade de informação e permitir cruzamentos inusitados (ele cita, de forma quase lúdica, cruzar dados de uma bicicleta elétrica da Moura com dados de energia da estação rádio-base — "não tem nada a ver, mas tem tudo a ver").
**Fato — roadmap H1/H2/H3 mencionado (dele e de outro participante presente):** H2 é aproximadamente o horizonte do VPP (fotovoltaico + BES); H3 seria hidrogênio — mas ele reconhece não ter visibilidade dessa fronteira aplicada especificamente a telecom: "Para o produto específico [...] eu não consigo ter essa visibilidade ainda."
**Fato — recomendação de discurso para o cliente:** migrar o argumento de custo puro para argumento de **nível de serviço regulatório** (tempo de reestabelecimento após furto, penalidade Anatel evitada) como gatilho mais forte de decisão do que economia direta.

---

## 9. Hipóteses para validação (Fase 2 — com operadoras)

| O que o time interno acredita (opinião de Francisco) | Hipótese estruturada para testar com o mercado |
|---|---|
| Raiz dos problemas de confiabilidade da plataforma é erro de instalação, não conectividade — mas o cliente pode não perceber essa distinção. | O cliente pode estar atribuindo instabilidade/falta de confiança **à tecnologia da Moura como um todo**, quando a causa concreta é erro de instalação em sites específicos — testar diretamente com a operadora se casos pontuais de falha já pesaram na decisão de não expandir o contrato, e se isolar a causa (instalação vs. produto) muda a percepção. |
| Operadoras estão migrando para "soluções compostas" (tecnologia + infraestrutura), citando TIM/V8 e Claro/HITS. | As operadoras podem estar abertas a uma parceria de infraestrutura mais ampla (não só energia) com a Moura, desde que a oferta inclua também **conectividade** (satélite, link dedicado) — testar apetite por esse tipo de parceria estratégica ampliada com a área de tecnologia/inovação das operadoras, não apenas com engenharia de energia. |
| Argumento de custo puro é fraco; nível de serviço regulatório (Anatel) seria um gatilho mais forte. | Essa é uma hipótese ainda não testada por ninguém internamente — vale confirmar diretamente com compliance/regulatório das operadoras se o risco de multa Anatel realmente pesa na decisão de contratar energia como serviço, ou se, na prática, as multas são raras/pouco relevantes no orçamento delas. |

## 10. Pessoas-chave para falar dentro do cliente (operadora)

**Já conversados, segundo ele:**
- Contato recente com a **V8** (empresa de tecnologia comprada pela TIM) — não é uma conversa tradicional com "cliente operadora", mas sim com uma aquisição de tecnologia da TIM; ele usa essa conversa para entender a tendência estratégica do grupo TIM, não para negociar o contrato de energia.

**Não conversados / lacuna identificada:**
- Não nomeia contatos específicos em Vivo, TIM ou Claro — seu foco é mais de tendência de mercado do que de relacionamento.
- Sugere (sem nomear) que o interlocutor-chave para o futuro poderia ser a área de **tecnologia/inovação** das operadoras (dado o movimento delas para "soluções compostas"), e não a engenharia de infraestrutura tradicional — recomendação a explorar na Fase 2.
