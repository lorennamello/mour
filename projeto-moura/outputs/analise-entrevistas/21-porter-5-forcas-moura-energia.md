# As 5 Forças de Porter — Moura Energia (Energia como Serviço)

*Modelagem construída a partir de três blocos de fontes: (1) a imersão interna — 15 transcrições internas já consolidadas nos documentos anteriores; (2) a imersão externa — as entrevistas completas com **Fabiano** (Diretoria de Infraestrutura de Missão Crítica, Claro) e **Vinícius/Luiz** (Engenharia de Infraestrutura, TIM); (3) a análise de mercado — o relatório "Diagnóstico Fase 1" (benchmark interno de ~20 concorrentes) e o relatório "Mercado de ISPs e Operadoras Regionais no Brasil" (dimensionamento de mercado, matriz competitiva, radar de players de BESS). Escopo: o produto **Energia como Serviço** da Moura, o mesmo recorte usado no BMC AS IS.*

*Este documento tem duas partes: a análise em si (com citação de fonte em cada bloco) e, ao final de cada força, uma caixa **"Como eu preenchi este quadrante"** explicando o raciocínio — para que você entenda a lógica por trás da ferramenta e consiga apresentá-la com autonomia.*

---

## O que são as 5 Forças de Porter (antes de entrar na análise)

Diferente do BMC — que descreve **como o seu próprio negócio funciona hoje** (por dentro) — as 5 Forças de Porter descrevem **o quão atrativo e defensável é o mercado em que esse negócio compete** (por fora). É uma ferramenta de 1979, de Michael Porter, e a pergunta que ela responde é: *"Neste mercado, quem tem o poder — eu, meus fornecedores, meus clientes, meus concorrentes diretos, ou alternativas que nem são meus concorrentes diretos?"*

Ela não substitui uma SWOT, mas cobre um pedaço que a SWOT não estrutura bem: a SWOT lista forças/fraquezas/oportunidades/ameaças de forma solta; Porter obriga você a decompor a "ameaça" em cinco fontes de pressão específicas e a avaliar cada uma isoladamente, com evidência. O resultado prático: você sai de "o mercado é difícil" para "o mercado é difícil especificamente porque o comprador tem poder de barganha alto — e é isso que eu preciso neutralizar primeiro, não o resto."

As cinco forças, na disposição clássica (a mesma do seu template):

| Posição no canvas | Força | Pergunta que ela responde |
|---|---|---|
| Topo | **Ameaça de novos entrantes** | É fácil para alguém novo entrar nesse mercado e roubar a minha fatia? |
| Esquerda | **Poder de negociação dos fornecedores** | Meus fornecedores (de insumos, componentes, capital) podem apertar minha margem? |
| Centro | **Rivalidade entre concorrentes** | Quão acirrada é a briga com quem já está no mercado hoje? |
| Direita | **Poder de barganha dos compradores** | Meus clientes têm força para ditar preço e condições? |
| Base | **Ameaça de produtos/serviços substitutos** | Existe uma forma totalmente diferente de resolver o mesmo problema do cliente? |

Quanto mais forte cada uma dessas cinco forças, menos atrativo (mais disputado, com menos margem de manobra) é o mercado. O objetivo final da análise não é só classificar cada força — é identificar **qual delas é a que mais aperta a Moura hoje**, porque é ali que a estratégia precisa agir primeiro.

---

## 1. Poder de barganha dos compradores — **ALTO** (nas 3 grandes operadoras) / **BAIXO** (nos ISPs regionais)

**O que essa força pergunta:** o cliente consegue empurrar preço para baixo, exigir mais por menos, ou trocar de fornecedor sem custo? Isso depende de coisas como: quantos compradores existem (poucos e grandes = mais poder), quão sensível ele é a preço, se ele tem capacidade técnica de fazer sozinho o que você oferece, e se trocar de fornecedor é fácil para ele.

**O que veio das fontes:**

- **A TIM rodou dois pilotos completos de Energia como Serviço com a Moura** (e em paralelo, no mesmo teste, com a Unicoba) — resultado tecnicamente positivo em ambos: aumento de disponibilidade, melhora no tempo de resposta, monitoramento remoto funcionando. Mesmo assim, **os dois projetos foram travados pelo CFO por não fecharem o payback dentro do teto de 3 anos exigido pela área financeira**. Na fala literal de Vinícius: *"só tem benefícios, mas não fecha a conta."* Isso não é um "não" técnico — é um "não" de poder de compra: o cliente pode dizer não a um produto que ele mesmo reconhece que funciona.
- **A Claro avaliou o mesmo modelo com quatro fornecedores em paralelo** (Moura, ZTE, Unicoba, SE Power) mais as torreiras/sharing companies, e chegou à mesma conclusão pelo mesmo motivo: Fabiano elogia explicitamente a qualidade do produto Moura ("visitei a fábrica, eles têm produtos de qualidade, vai funcionar, vai ser uma maravilha") mas recusa o negócio puramente por TCO — o break-even de 2 a 2,5 anos não foi "tentador" para a Claro mesmo no melhor cenário. A frase que resume o poder do comprador aqui: *"eu não vou comprar um negócio que se eu investisse eu teria um retorno."* Ele decide, o fornecedor se adapta.
- **Contratação por resultado, não por insumo**: a Claro contrata seus prestadores de campo "por serviço", com SLA e penalidade — não por headcount ou por equipamento. Isso desloca o risco operacional para quem fornece, um sinal clássico de comprador com poder.
- **O comprador grande tem capacidade técnica de prescindir do fornecedor**: a Claro desenvolveu internamente (com o time do Daniel) uma solução própria, agnóstica de fabricante, de hardware e software para monitoramento de energia — especificamente para não depender de nenhum fornecedor único. Isso é uma ameaça direta ao valor que a Moura tentaria vender como diferencial (a plataforma de monitoramento).
- **Interoperabilidade elimina lock-in técnico**: a TIM hoje consegue misturar bateria Moura, Narada, Unicoba e Huawei na mesma fonte, via protocolo padrão (SNMP) — o que antes era uma barreira técnica ("bateria só fala com a fonte do mesmo fabricante") virou commodity. Trocar de fornecedor deixou de ter custo técnico.
- **Contraponto — no segmento de ISPs regionais o poder de compra é o oposto**: o relatório de mercado mostra 11.853 ISPs pulverizados, nenhum deles com escala para fazer engenharia financeira própria, 89% dizendo que o CAPEX de energia é uma barreira real, e 78% de interesse declarado em modelo de assinatura — desde que o valor mensal seja previsível. É um comprador fragmentado, sem musculatura de CFO para travar um payback de 3 anos como a TIM fez.

**Perguntas-guia respondidas:**

- **O cliente consegue trocar facilmente de fornecedor?** Sim — hoje mais do que nunca. A interoperabilidade via SNMP deixa a TIM misturar bateria de fabricantes diferentes na mesma fonte, e tanto a TIM quanto a Claro cotaram/testaram vários fornecedores lado a lado no mesmo processo de decisão. Não existe lock-in técnico prendendo o cliente.
- **O custo de troca é baixo?** Sim, para as grandes operadoras — o único atrito que aparece nas entrevistas é interno (processo de homologação/compra), não técnico. Nos ISPs regionais o custo de troca também é baixo, mas por outro motivo: eles ainda não têm um fornecedor de EaaS consolidado para trocar — o problema deles é falta de capital para entrar, não dificuldade de sair.
- **O preço pesa muito na decisão?** Foi o único fator que decidiu os dois casos documentados. Nem TIM nem Claro contestaram a qualidade técnica do produto Moura — os dois pilotos caíram exclusivamente porque o payback/TCO não fechou dentro do teto financeiro interno.
- **O cliente consegue pressionar por melhores condições?** Sim, com força máxima: cotar 4 fornecedores em paralelo (Claro) e rodar 2 pilotos com fornecedores concorrentes ao mesmo tempo (TIM) é pressão de preço institucionalizada. E ainda têm uma carta extra — desenvolver alternativa própria (a plataforma agnóstica de monitoramento da Claro) —, que reduz a dependência de qualquer fornecedor único a praticamente zero.

**Leitura estratégica:** o comprador que a Moura tentou vender primeiro (as 3 grandes operadoras) é exatamente o comprador com mais poder de barganha do mercado inteiro — concentrado, sofisticado, com disciplina financeira rígida e capacidade de construir alternativa própria. O comprador com menos poder (ISPs regionais) é o que o relatório de mercado recomenda como prioridade de entrada. Essa é provavelmente a tensão mais importante da análise inteira.

> **Como eu preenchi este quadrante:** parti das duas transcrições da imersão externa (Claro e TIM) porque elas são evidência direta e recente de comportamento de compra real — não hipótese. Nos dois casos, o padrão se repete de forma quase idêntica (piloto tecnicamente bem-sucedido, rejeitado no financeiro), o que dá confiança de que não é um caso isolado, é como grandes operadoras decidem. Depois cruzei com o dado quantitativo do relatório de mercado (seção 13, que o próprio relatório marca como estimativa/hipótese a validar, não pesquisa primária) para mostrar o contraste com o segmento de ISPs, e com a seção 15 do mesmo relatório, que já recomenda esse pivô.

---

## 2. Rivalidade entre concorrentes — **ALTA**

**O que essa força pergunta:** quantos concorrentes diretos existem, quão parecidas são as ofertas, e a briga é por preço (destrutiva) ou por diferenciação (saudável)?

**O que veio das fontes:**

- O **Diagnóstico Fase 1** mapeou e comparou ~20 empresas em 4 arquétipos que competem pelo mesmo espaço da Moura:
  - **Especialistas em bateria** (concorrência mais direta): EnerSys, Polarium, UCB Power. A **UCB Power é o concorrente mais próximo e mais perigoso** — já anunciou entrada em Battery as a Service, adquiriu a carteira de clientes e a patente antifurto da EP Telecom em 2024, e tem investimento relevante entrando. Risco classificado como **"alto"** no próprio relatório interno da Moura.
  - **Especialistas em operação de energia**: Aggreko, IPT PowerTech, Hybrico — este último o mais parecido conceitualmente com a proposta da Moura (EaaS sustentável, nascido de uma dor real de operadora — o primeiro contrato da Hybrico foi com a Tigo Honduras).
  - **Especialistas em infraestrutura de telecom**: Camusat/Aktivco (modelo ESCO, mais de 6.600 sites sob contrato na África), Vertiv.
  - **Gestão inteligente da energia**: Huawei Digital Power — plataforma full-stack (SmartSite/CloudLi) com IA, já com early moves em Virtual Power Plant.
  - Outros brasileiros no radar: **Delta Brasil** (médio risco), **Nilko** (médio — domina o gabinete/cabine outdoor, um adjacente perigoso se decidir empacotar gabinete + bateria), **Grupo Alpha** (médio-baixo, mas já presente no site fazendo instalação e manutenção).
- No relatório de **Mercado de ISPs**, a matriz competitiva específica desse segmento traz mais seis frentes: TS Shara/NHS/Intelbras (nobreaks, modelo CAPEX puro), locação de geradores a diesel (Aggreko, Engie, locais), distribuidoras de energia (Equatorial, Enel, CPFL), integradores de energia solar regionais, Huawei/Vertiv/Schneider (BESS enterprise, caro demais para ISP pequeno) e — o mais relevante do ponto de vista de rivalidade crescente — **startups nacionais de EaaS (Voltz, Nuvem Energia)**, classificadas no próprio relatório como **"alta (emergente)"**, o maior risco de médio prazo justamente por já estarem construindo modelo de assinatura para o mesmo público de PMEs que a Moura quer atacar.
- **Nas próprias entrevistas de imersão externa, a rivalidade aparece nominalmente**: a TIM testou Moura *e* Unicoba lado a lado, no mesmo piloto, nos mesmos critérios; a Claro cotou Moura, ZTE, Unicoba e SE Power ao mesmo tempo. Isso confirma em campo o que o benchmark já apontava: a Moura nunca está sozinha na mesa de decisão.
- **Matriz de posicionamento (produto × serviço) do Diagnóstico Fase 1** mostra Huawei, Polarium, EnerSys, Vertiv e UCB Power já mais avançados em "serviço/digitalização" do que a Moura hoje — um sinal de que parte da concorrência já correu na frente na dimensão que mais importa para o EaaS (não é fabricar bateria, é orquestrar o serviço).

**Perguntas-guia respondidas:**

- **Quem são os principais concorrentes?** No arquétipo de bateria: UCB Power, EnerSys, Polarium. No de operação de energia: Aggreko, IPT PowerTech, Hybrico. No de infraestrutura de telecom: Camusat/Aktivco, Vertiv. Em gestão inteligente: Huawei Digital Power. No radar nacional: Delta Brasil, Nilko, Grupo Alpha. No segmento de ISPs, mais seis frentes: TS Shara/NHS/Intelbras, locadoras de geradores a diesel, distribuidoras de energia, integradores solares regionais, BESS enterprise (Huawei/Vertiv/Schneider) e as startups Voltz e Nuvem Energia.
- **Como eles competem?** Cada arquétipo compete numa dimensão diferente: os especialistas em bateria competem por presença de mercado e movimento estratégico (a UCB Power comprando carteira e patente da EP Telecom); os especialistas em operação competem por modelo de contrato e SLA (Camusat com ESCO, mais de 6.600 sites); os de gestão inteligente competem por plataforma e IA (Huawei com SmartSite/CloudLi já mirando Virtual Power Plant); as startups de EaaS competem por foco e velocidade num nicho (PMEs via assinatura).
- **Eles competem por preço, qualidade, inovação ou atendimento?** As quatro dimensões ao mesmo tempo, cada arquétipo puxando uma: preço (fabricantes chineses de célula, TS Shara/NHS no CAPEX puro), qualidade (elogiada nas duas entrevistas — hoje é piso, não diferencial, porque todo mundo bate essa barra), inovação (Huawei e UCB Power à frente da Moura em serviço/digitalização, segundo a própria matriz de posicionamento do Diagnóstico), atendimento (Camusat vendendo por SLA em vez de equipamento).
- **O mercado é muito disputado?** Sim — ~20 concorrentes mapeados no benchmark interno mais outras seis frentes no relatório de ISPs, e nos dois casos reais documentados a Moura nunca esteve sozinha na mesa: a Claro cotou 4 fornecedores, a TIM testou 2 em paralelo no mesmo piloto.
- **O crescimento é lento ou rápido?** Rápido — 78% de interesse declarado em modelo de assinatura no segmento de ISPs, startups de EaaS já classificadas como "risco alto/emergente" no relatório, e towercos/redes neutras entrando lateralmente com movimento recente (últimos 1-2 anos).

**Leitura estratégica:** não existe hoje um concorrente único e óbvio — existe uma rivalidade **fragmentada em várias frentes simultâneas**, o que também significa que nenhum concorrente sozinho "fechou" o mercado ainda. A janela está aberta, mas se fechando: os players mais avançados (Polarium, Huawei, EnerSys) e os mais ágeis (startups de EaaS) estão se movendo mais rápido do que a Moura na dimensão de serviço.

> **Como eu preenchi este quadrante:** essa força foi a mais fácil de sustentar com dado direto, porque tanto o Diagnóstico Fase 1 quanto o relatório de Mercado de ISPs já trazem matrizes competitivas prontas (a "régua de capacidades" e a "matriz de posicionamento produto×serviço" de um lado; a "matriz de atributos" e o "radar de players de BESS" do outro). Meu trabalho foi cruzar as duas listas (elas se sobrepõem parcialmente — Huawei, Vertiv e Aggreko aparecem nas duas) e confirmar com evidência de campo (Claro e TIM citando concorrentes específicos por nome) que essas listas não são teóricas — são concorrentes reais na mesa de decisão.

---

## 3. Poder de negociação dos fornecedores — **MÉDIO-ALTO**

**O que essa força pergunta:** os fornecedores da Moura (de componentes, matéria-prima, capital) conseguem impor preço, prazo ou condição — ou a Moura tem alternativas fáceis?

**O que veio das fontes:**

- **Concentração de fornecedor de gabinete**: o Diagnóstico Fase 1 identifica que existe **apenas um fornecedor homologado no Brasil** para fabricar a estrutura metálica dos gabinetes usados pela Moura Energia — uma concentração extrema, próxima de monopólio, num insumo crítico do produto.
- **Pressão dos fabricantes asiáticos de célula de lítio**: entrada maciça de baterias de lítio chinesas muito baratas, citada tanto no Diagnóstico quanto confirmada nas próprias entrevistas externas — Fabiano (Claro) menciona um fornecedor chinês "maluco" cujo preço reduzia o break-even do modelo CAPEX de bateria de ~10 anos para 2,5 anos, um preço "que ele nunca tinha visto". Isso tem duas leituras: para a Moura como *fabricante*, esses players pressionam o custo de célula para baixo (o que ajuda, se a Moura compra célula) mas também entram como concorrentes de preço agressivo (o que machuca); do lado de fornecimento, a dependência de célula asiática é um ponto de exposição.
- **Dependência de fornecedor externo para antifurto/segurança**: a trava de proteção patrimonial (cadeado bluetooth) depende de um fornecedor externo (Promon), com componentes chineses sem auditoria — risco de cibersegurança adicional apontado no próprio diagnóstico interno.
- **Sensibilidade ao custo de capital ("funding")**: como o modelo de aluguel exige capital de giro imobilizado por anos, o Diagnóstico aponta que a viabilidade do negócio "explode" quando a taxa de captação sobe — ou seja, os provedores de capital (bancos, linhas como o BNB) também funcionam como um fornecedor crítico, e caro, do modelo.

**Perguntas-guia respondidas:**

- **Existem muitos ou poucos fornecedores?** Depende do insumo, e é uma resposta polarizada: só **1 fornecedor homologado** para o gabinete metálico (extremo de "poucos"); **muitos** fornecedores de célula de lítio (mercado chinês pulverizado e agressivo); **poucos e caros** provedores de capital adequados ao perfil de longo prazo do modelo de aluguel.
- **Quais são eles?** O fornecedor de estrutura metálica de gabinete (não nomeado no Diagnóstico), os fabricantes de célula de lítio chineses, a Promon (trava de proteção patrimonial via bluetooth) e os bancos/linhas de crédito como o BNB.
- **Eles oferecem algo difícil de substituir?** O de gabinete sim — monopólio de fato, sem homologação alternativa no país. A célula não — é abundante e a tendência é de preço caindo, não subindo. O capital sim, é estruturalmente necessário para sustentar um modelo que imobiliza caixa por anos.
- **É fácil trocar de fornecedor?** Não para o gabinete (não há para onde trocar). Sim para célula (excesso de oferta). Não para capital (poucas linhas adequadas a esse perfil de risco/prazo).
- **Eles conseguem aumentar preços ou impor condições?** O fornecedor de gabinete sim, por ausência de alternativa. O de capital também — o próprio Diagnóstico diz que a viabilidade do modelo "explode" quando a taxa de captação sobe. Os de célula não — a tendência de mercado é de commoditização e preço em queda.

**Leitura estratégica:** o maior risco aqui não é o custo da célula em si (isso tende a cair estruturalmente, como mostra o próprio mercado), é a **concentração** — um único fornecedor de gabinete e a dependência de capital de terceiros são dois pontos de estrangulamento que a Moura não controla e que, se apertarem, travam a escala do modelo independentemente de quão bem ele venda.

> **Como eu preenchi este quadrante:** esta foi a força com menos evidência direta nas entrevistas externas (Claro e TIM falam pouco sobre os fornecedores *da Moura* — falam do lado deles, como compradores). Por isso me apoiei quase inteiramente no Diagnóstico Fase 1, que tem uma seção específica ("Ecossistema e Mercado") tratando exatamente da cadeia de suprimentos da Moura. É uma força que merece validação futura com uma conversa direta com o time de Compras/Operações da Moura — o material que temos hoje é bom, mas mais estreito que os das outras quatro forças.

---

## 4. Ameaça de novos entrantes — **ALTA**

**O que essa força pergunta:** é fácil para um player novo (ou um player de outro setor) entrar nesse mercado específico e roubar espaço rapidamente?

**O que veio das fontes:**

- O relatório de Mercado de ISPs identifica explicitamente **"startups nacionais de EaaS (Voltz, Nuvem Energia e similares)"** como o **maior risco competitivo de médio prazo** — não porque sejam grandes, mas porque estão "construindo modelos de assinatura para PMEs" exatamente no segmento onde a Moura ainda não tem presença consolidada, e podem se mover mais rápido por serem menores e mais focadas.
- **Barreira tecnológica caindo**: como visto na força de Rivalidade, a interoperabilidade entre baterias de fabricantes diferentes (confirmada pela TIM) significa que a diferenciação técnica não é mais uma barreira de entrada forte — qualquer fabricante de bateria homologado consegue, hoje, plugar em uma rede de operadora sem desenvolvimento proprietário.
- **As torreiras (towercos) são um entrante "de fora" plausível**: American Tower (~22.800 sites), Highline (~13.500), SBA (~11.828), Sitios LatAm (~11.300) já controlam 63,68% das torres do país e já hospedam múltiplas operadoras no mesmo site — o passo natural seguinte é embutir energia como parte do pacote de locação de infraestrutura, o que as torna concorrentes "de trás para frente" sem nunca terem vendido bateria antes. O relatório interno já da nota "3 estrelas" de escalabilidade para BaaS a esse grupo.
- **Redes neutras também têm o caminho aberto**: a V.tal e a Fibrasil já anunciam estações de energia com autonomia de 4h+ como parte da oferta de colocation — um movimento de entrada lateral, não de um concorrente de bateria, mas de um dono de infraestrutura que decide verticalizar energia.
- **Baixa barreira de capital para o "entrante pequeno"**: no segmento de ISPs regionais, qualquer integrador solar local já vende BESS + solar num modelo CAPEX simples — a barreira real não é tecnológica, é apenas não ter ainda um modelo de assinatura estruturado, algo replicável.

**Perguntas-guia respondidas:**

- **É caro entrar nesse mercado?** Assimétrico. Caro para quem entra do zero, fabricando bateria e financiando o capital de giro que o modelo de assinatura exige. Barato para quem já tem um ativo adjacente pronto: a towerco que já tem a torre, o integrador solar que já vende BESS+solar, a rede neutra que já tem o site de colocation — para eles, energia é só mais um item empacotado numa oferta que já existe.
- **O que está envolvido?** Capital de giro para sustentar o modelo de assinatura, homologação técnica do equipamento e — cada vez menos — desenvolvimento proprietário de software, já que a interoperabilidade (confirmada pela TIM) tornou isso menos necessário.
- **Existe necessidade de tecnologia, certificações ou marca forte?** Tecnologia sim, mas commoditizando rápido (baterias de fabricantes diferentes já interoperam via protocolo padrão). Certificação existe, mas não é proibitiva — Claro e TIM testaram 4 e 2 fornecedores homologados diferentes sem dificuldade nenhuma. Marca forte não pesou em nenhuma das duas decisões documentadas: as duas operadoras decidiram 100% por número de TCO, não por reputação de marca.
- **É difícil conquistar clientes?** Menos do que se esperaria. Como a decisão do comprador é movida quase inteiramente por matemática de payback, um entrante com melhor engenharia financeira consegue entrar na mesa de decisão rapidamente — não depende de relacionamento de longo prazo construído, como mostra o fato de a Claro ter aberto cotação simultânea para 4 fornecedores.
- **As barreiras são altas ou baixas?** Mistas, e é exatamente essa mistura que classifica a força como alta: altas em capital/funding para quem entra do zero, baixas em tecnologia e em conquista de cliente. Como três tipos diferentes de entrante conseguem contornar a barreira que for mais alta para eles, a soma das três frentes resulta em ameaça alta.

**Leitura estratégica:** a ameaça de novo entrante é alta porque vem de três direções diferentes ao mesmo tempo — startups puramente de EaaS (de baixo para cima), towercos e redes neutras (de lado, verticalizando a própria infraestrutura) e fabricantes globais commoditizados entrando por preço (de cima para baixo). Nenhuma dessas três é hipotética: todas já têm movimento real documentado.

> **Como eu preenchi este quadrante:** cruzei três sinais do relatório de Mercado de ISPs que, isolados, pareciam pontos soltos, mas juntos formam um padrão claro de entrada por múltiplas direções: a tabela de "Players Nacionais de BESS para Telecom" (que classifica Voltz/Nuvem Energia como ameaça "alta/emergente"), a tabela de torreiras com a coluna "Escalabilidade para BaaS", e o parágrafo sobre redes neutras (V.tal, Fibrasil). Também usei o próprio comportamento técnico relatado pela TIM (baterias de fabricantes diferentes já conversam entre si) como evidência de que a barreira tecnológica, que segurava novos entrantes no passado, está caindo.

---

## 5. Ameaça de produtos/serviços substitutos — **MÉDIA-ALTA**

**O que essa força pergunta:** existe uma forma completamente diferente de resolver o mesmo problema do cliente — não um concorrente que vende a mesma coisa, mas uma alternativa que faz o problema desaparecer de outro jeito?

**O que veio das fontes:**

- **O substituto mais forte não é um produto — é o próprio cliente gerenciando a energia internamente.** Tanto a Claro quanto a TIM, hoje, fazem a gestão de energia com equipe e processo próprios (equipes terceirizadas geridas internamente, softwares desenvolvidos in-house). Esse é o "concorrente invisível" citado também no relatório de Mercado de ISPs — a inércia operacional, "sempre foi assim", é o padrão dominante hoje, não a exceção.
- **Gerador a diesel** continua sendo a solução-padrão em sites remotos e nos ISPs regionais — 72% dos que usam diesel gostariam de substituí-lo mas não têm capital para o CAPEX de BESS, segundo o relatório de mercado. É um substituto fraco tecnicamente (caro, poluente, manutenção complexa) mas ainda dominante por inércia e por não exigir compromisso de longo prazo com um único fornecedor.
- **Redução de demanda em vez de aumento de capacidade — um substituto conceitual novo**: Fabiano (Claro) descreve uma ideia que ele já testa internamente — em vez de comprar mais bateria para aguentar mais tempo sem energia, a rede pode se autolimitar (desligar 5G e manter só 4G, por exemplo) para esticar a autonomia da bateria que já existe. Isso ataca o problema por engenharia de software, não por mais hardware — um caminho que nenhum fornecedor de energia (Moura inclusa) resolve.
- **Compra + manutenção própria (modelo tradicional) segue vencendo a conta financeira** nos dois casos documentados (Claro e TIM): em ambos, o modelo de propriedade teve break-even mais curto que o modelo de aluguel. Isso é, na prática, o cliente escolhendo o substituto "óbvio" (comprar e manter) em vez do produto novo (alugar como serviço) — mesmo reconhecendo os benefícios operacionais do segundo.
- **Consolidação via M&A como substituto indireto**: grupos como Vero, Unifique e Brisanet compram ISPs menores e, ao padronizar a infraestrutura adquirida, podem optar por internalizar a gestão de energia em escala própria em vez de contratar um EaaS externo — outra forma do comprador resolver o problema sem o produto da Moura.

**Perguntas-guia respondidas:**

- **Existe outra maneira de atender essa necessidade?** Sim, quatro identificadas nas fontes: gestão própria (equipe e software internos), gerador a diesel, redesenho da demanda de energia via software (a rede se autolimita em vez de crescer a bateria) e internalização via M&A (grupos que compram ISPs menores padronizam e passam a gerenciar energia em escala própria).
- **Quais são as maneiras?** As quatro listadas acima — nenhuma delas é um fornecedor concorrente vendendo o mesmo tipo de produto; todas resolvem o problema de energia sem passar por um contrato de EaaS.
- **O cliente já utiliza alternativas?** Sim, nos dois casos documentados: tanto a Claro quanto a TIM hoje gerenciam energia com equipe e processo próprios, e foi exatamente para essa alternativa que voltaram depois de rejeitar o piloto de EaaS da Moura.
- **Essas alternativas são mais baratas, rápidas ou convenientes?** A gestão própria venceu no cálculo financeiro das próprias operadoras — foi mais barata no horizonte de payback que elas usam para decidir, senão o piloto não teria sido recusado. O diesel não é mais barato no longo prazo, mas é mais rápido e simples de manter porque já está instalado e não exige compromisso contratual novo. O redesenho de demanda via software é o mais barato de todos, porque não exige nenhum hardware novo — resolve o problema por engenharia, não por investimento.
- **Quão fácil é a substituição?** Muito fácil — é a opção padrão, não exige nenhuma mudança de comportamento do cliente, é literalmente "continuar fazendo como já é feito hoje". É essa facilidade, mais do que qualquer característica técnica das alternativas, que faz essa força pesar tanto.

**Leitura estratégica:** o adversário mais difícil de vencer aqui não tem marca, não tem preço de tabela e não aparece em nenhuma RFP — é a decisão de continuar fazendo como sempre foi feito. É uma ameaça mais silenciosa que a rivalidade direta, mas, pelas duas entrevistas externas, é a que efetivamente barrou a Moura duas vezes até agora.

> **Como eu preenchi este quadrante:** esta foi a força que exigiu mais interpretação, porque "substituto" é o conceito mais fácil de confundir com "concorrente direto" dentro do framework. O critério que usei para separar foi: um concorrente vende a mesma coisa de outro jeito (ex.: UCB Power vendendo BaaS é rivalidade); um substituto resolve o mesmo problema sem ser esse tipo de produto (gestão própria, diesel, ou redesenhar a demanda de energia via software são exemplos). A evidência mais forte veio de novo das entrevistas externas — nos dois casos, quando a operadora rejeitou o EaaS, ela não migrou para um concorrente da Moura, voltou para o modelo de propriedade/gestão própria. Isso é a assinatura clássica de uma força de substituição forte, não de rivalidade.

---

## Síntese — onde a pressão está concentrada

| Força | Intensidade | Em uma frase |
|---|---|---|
| Poder de barganha dos compradores | 🔴 Alto (grandes operadoras) / 🟢 Baixo (ISPs regionais) | O mesmo produto encontra dois mercados opostos dentro do setor de telecom. |
| Rivalidade entre concorrentes | 🔴 Alto | Nenhum concorrente fechou o mercado ainda, mas vários estão avançando mais rápido em "serviço" do que a Moura. |
| Ameaça de novos entrantes | 🔴 Alto | Entra gente por três portas ao mesmo tempo: startups de EaaS, towercos/redes neutras, e fabricantes globais baratos. |
| Poder de negociação dos fornecedores | 🟡 Médio-alto | Concentração perigosa em um insumo (gabinete) e em capital, mas commodities (célula) tendem a ficar mais baratas. |
| Ameaça de substitutos | 🟡 Média-alta | O adversário mais forte hoje não é um concorrente — é o cliente decidindo continuar fazendo sozinho. |

**A leitura mais importante para apresentar:** as duas forças mais altas (poder do comprador grande e rivalidade) **já se manifestaram na prática**, nas duas tentativas reais registradas nas entrevistas externas — não são projeções teóricas. Isso muda o tom da apresentação: você não está dizendo "o mercado pode ser difícil", está dizendo "o mercado já mostrou, duas vezes, exatamente como e por que é difícil — e temos os dois casos documentados para provar."

---

## Como apresentar isso (guia rápido)

1. **Comece pela pergunta central de Porter, não pelas cinco caixas**: "o quão atrativo é esse mercado, e onde está a maior pressão contra a gente?" — as pessoas entendem a lógica antes de ver o detalhe.
2. **Use os dois casos reais (Claro e TIM) como prova, não como anexo.** É a parte mais forte da análise porque não é opinião nem benchmark de terceiro — é comportamento de compra documentado, duas vezes, com o mesmo padrão.
3. **Não apresente as cinco forças como "iguais em importância".** A síntese acima já aponta qual força pesa mais — comece por ela (poder do comprador) e conecte as outras a ela: é porque o comprador grande tem tanto poder que a rivalidade fica mais acirrada (todo mundo compete pelo mesmo cliente exigente) e que os substitutos ganham força (o comprador prefere voltar ao que já conhece a arriscar em um modelo novo).
4. **Feche com a mesma pergunta que fecha o BMC**: dado esse mapa de forças, qual segmento de cliente (ISPs regionais vs. grandes operadoras) e qual proposta de valor (o quê precisa mudar no TCO/payback) fazem esse modelo fazer sentido primeiro?

---

## Metodologia e fontes

- **Imersão externa**: transcrições completas de Fabiano (Diretoria de Infraestrutura de Missão Crítica, Claro) e Vinícius/Luiz (Engenharia de Infraestrutura, TIM) — arquivos `imersao-externa/transcricao-claro-fabiano.md` e `imersao-externa/transcricao-tim-vinicius.md`.
- **Diagnóstico interno**: `analise-de-mercado/Diagnostico_Fase1_Moura_MJV.pdf` (60 páginas) — 12 entrevistas internas + benchmark de ~20 concorrentes, seções "Ecossistema e Mercado", "Régua de capacidades" e "Deep dives" por concorrente.
- **Pesquisa de mercado**: `analise-de-mercado/Mercado_ISPs_Operadoras_Regionais_Brasil.pdf` (78 páginas) — dimensionamento do mercado de ISPs, matriz competitiva, radar de players de BESS, matriz de risco. *Nota importante: a seção 13 desse relatório ("Percepções do Mercado") é explicitamente marcada pela própria MJV como síntese ilustrativa baseada em fontes secundárias, não pesquisa primária — tratei os números dessa seção como hipótese de mercado, não como dado de campo, e sinalizei isso no texto acima.*
- **Visão de projeto**: `analise-de-mercado/Moura_Project_Management.pdf` — objetivos e fases do projeto (contexto, não conteúdo analítico direto).
- Documentos anteriores da imersão interna (`00` a `20`) para cruzamento de contexto (contrato Vivo, episódio TIM do lado interno, hipóteses de PMF).
