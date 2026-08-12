# 06 — Oportunidades e direcionamento
### Reconciliação das duas trilhas, arquitetura de oportunidades e próximos passos

Base: 15 entrevistas (5 externas + 10 internas, 7 lidas na íntegra), Diagnóstico Fase 2.2,
proposta MJV e documentos da pasta `oportunidades/`.
Regra aplicada: **a oportunidade nasce da entrevista**; o material externo entra como
estrutura, e seus dados só quando o racional das entrevistas já sustenta o ponto.

---

## 1. O problema a resolver antes da reunião

O material que vai à diretoria carrega **duas leituras que ainda não conversam**:

| | Diagnóstico Fase 2.2 | Motores de Receita (v3 / deck 13ago) |
|---|---|---|
| Conclusão | Faltam fundamentos antes da escala | "O produto não está errado. O empacotamento está" |
| Ritmo implícito | Recuar e revalidar | Começar em setembro, roadmap de 90 dias |
| Base | Entrevistas do projeto | Documentos internos + benchmark, sem participação nas entrevistas |

Se a sala receber as duas como estão, vai perguntar qual vale. Pior: vai escolher a mais
confortável. **A reconciliação precisa estar num slide, não subentendida.**

### A ponte — e ela é sustentada por evidência

> **Desagregar não é o oposto de fortalecer fundamentos. É o método para fortalecê-los.**

Um pacote único, vendido a um mercado que já o rejeitou quatro vezes, é uma aposta grande sobre
hipóteses não validadas. Três ofertas separadas são três apostas menores, cada uma testável
contra uma dor que as entrevistas já comprovaram, cada uma reduzindo uma incerteza diferente.

E há uma prova de que a Moura sabe fazer isso — **dentro de casa, no BES**:

> "No BES a gente já tem três produtos: backup de energia, a economia da energia [...] e um
> terceiro que a gente chama de qualidade de energia [...] A gente estava entregando isso de
> graça ao cliente, e agora estamos passando a cobrar."
> — Thiago, liderança de EaaS, 00:49:04 / 00:54:27

E o reconhecimento de que isso não foi feito em telecom:
> "**A gente realmente não conseguiu empacotar** [...] Sempre parto do pressuposto que não é
> por impossibilidade. É porque a gente não pensou o suficiente sobre isso." — Thiago, 00:56:50

→ Isso muda a natureza da recomendação. Deixa de ser uma tese trazida de fora e passa a ser
**um modelo que a Moura já opera com sucesso em outro produto e ainda não levou para telecom**.
Diante da diretoria, isso vale muito mais.

### Correção obrigatória de uma frase

A p.22 do 2.2 adota literalmente *"O produto não está errado, mas o empacotamento está."*
Isso **contradiz a p.15 do próprio deck** (monitoramento pouco confiável, dados pouco
acionáveis, hardware em maturação, instalação inconsistente) e é desmentido por fonte primária:

- 30–35% do parque com erro de instalação da fonte, o que impede a alarmística funcionar
  (Francisco/TI, 00:17:56)
- A plataforma não avisa vandalismo: *"acontece muitas vezes de eu saber pelo cliente [...] vou
  olhar a plataforma e não está dizendo nada"* (Consultor Vivo, 00:14:39)
- A autonomia contratada — o objeto do contrato — não é visível na plataforma (Consultor Vivo, 00:18:15)

**Formulação que a evidência sustenta:**
> *"A bateria não é o problema. O pacote é — e a camada de serviço que o sustenta ainda não
> está pronta."*

Mantém o insight, elimina a contradição, e não entrega à diretoria uma frase que qualquer
pessoa da operação pode derrubar na sala.

---

## 2. Três correções de leitura que a evidência impõe

Antes dos clusters, três pontos em que a evidência das entrevistas **diverge** do material da
pasta `oportunidades/`. Nenhum invalida a estrutura de três motores; todos mudam o conteúdo.

### 2.1 Rastreabilidade não é o mecanismo que o comprador quer

O relatório externo propõe marcação permanente com rastreabilidade em nível de célula como
mecanismo principal do motor antifurto. **O comprador diz o contrário, sem ambiguidade:**

> "eu vejo uma certa inutilidade, botar um GPS dentro dela [...] o GPS você vai saber pra onde
> ela foi. **Eu não sei se você recupera ela de fato** [...] Não adianta colocar lá se eu tenho
> uma quadrilha por trás disso." — compras estratégicas, Claro, 00:53:54 / 00:55:24

E sobre a solução atual da Moura:
> "A Moura fala: eu tenho um sistema anti-vandalismo. **Veja bem, porque é um sistema fraco,
> porque esse sistema já foi hackeado**" — compras estratégicas, Claro, 00:21:56

**O que o comprador de fato compra, hoje, de dois fornecedores:** desbloqueio remoto, porque
elimina uma visita a campo — *"Isso salva o OPEX para mim"* (00:27:43). O produto ideal, na
definição dele: *"bateria intercambiável de 100Ah ou 150Ah, e com um desbloqueio remoto [...]
até uma certa blindagem e desbloqueio remoto, já está bom"* (00:53:32).

→ **O vetor de valor não é recuperar o ativo. É não mandar gente ao site.** O mesmo mecanismo
aparece em todas as fontes: Ufinet internalizou um técnico que filtra acionamento e reduziu o
custo a 1/8 (50:36); a Claro correlaciona falha e tráfego para não despachar equipe (00:27:01).

### 2.2 A plataforma de telemetria é commodity — o valor está uma camada acima

O relatório trata "telemetria interoperável no parque legado" como motor de assinatura. As
entrevistas mostram que a camada de coleta já está resolvida e é **gratuita**:

> "a gente usa o sistema Zabbix [...] **praticamente todas as operadoras estão usando o
> Zabbix** [...] é uma plataforma aberta" + Grafana para visualização, configurados por time
> interno — José, Algar, 14:37 / 18:39
> "nós estamos desenvolvendo dentro de casa uma solução totalmente agnóstica" — Daniel Machado,
> Claro, 00:56:01
> "todas as FCCs têm SNMP [...] Delta, Iopec, Emerson, Schneider, Vertiv" — José, Algar, 20:34

**O que continua não resolvido, dito pelos próprios clientes:**
- Consolidação gerencial: falta "visão gerencial e estratégica consolidada de todos os prédios
  simultaneamente" (TIM, item 35)
- Fragmentação de software por fabricante: "eu tenho que ir a cada fabricante, pegar o software
  deles [...] no NOC eu vou ter três para fazer" (compras Claro, 00:31:52)
- **Alocação de investimento**: "usar inteligência artificial [...] para a gente pensar até no
  investimento, onde a gente deve investir mais bateria, onde a gente tem que investir menos"
  (Algar, 21:17) — e hoje isso é feito em Excel: "a gente faz muito ainda manual. Muito,
  muito" (22:58). A Claro está construindo o mesmo com ML (01:04:30).

→ **Não vender "monitoramento". Vender decisão de dimensionamento e despacho.** A Moura tem o
insumo que ninguém tem — histórico real de uso de bateria em 400+ sites, em ambientes e
temperaturas variados (Francisco, 00:20:42) — e não o usa nem para si:
> — "a gente entrega para eles um diagnóstico [...] você não precisa de 10 baterias, você
>   precisa de 5?" — "**Não, não fazemos isso. Sim, podemos fazer isso.**" — Espinoza, 00:23:45

### 2.3 Data center e ambiente controlado não são "onde a dor é maior" — são onde a conta fecha

O relatório posiciona o contrato de performance para data centers, no-break e POPs internos. A
evidência **confirma o alvo, mas por outra razão** — e a razão importa para o pitch:

> "Quando for os grandes data centers, de repente compensa [...] é um ambiente controlado [...]
> onde você **não tem manutenção, não tem furto** [...] climatizado, muito bem controlado a
> parte de temperatura. **Eu acho que o BP fecha**" — José, Algar, 29:48 / 30:34

E a explicação física, que ninguém mais deu:
> "a bateria, a vida útil dela de cair, é por temperatura [...] esses pontos que são muito
> greenfield, a oscilação vai de 10 graus na madrugada a 50 graus durante o dia [...] **o ciclo
> de troca que eles teriam que fazer de bateria era muito maior**" — 29:54

Mas atenção: na TIM, "nos prédios industriais a dor da falta de baterias é **menor** devido à
alta redundância" (item 31). Ou seja: **é onde a economia fecha, não onde o cliente sofre.**
O pitch nesses ambientes é econômico, não de dor.

E o cliente nomeou o produto:
> "um que eu entendo que possa ser vantajoso é **serviço as a service de No-Break**. No-Break é
> um equipamento que é muito caro. A cada sete anos você tem uma troca de capacitor [...] **Eu
> acho que o único que funciona como a service é o No-Break**" — José, Algar, 25:47 / 26:32

---

## 3. Arquitetura de oportunidades

Cinco clusters. Cada um posicionado na esteira, com a incerteza que reduz. **A ordem não é de
tamanho de mercado — é de quanto fundamento cada um destrava.**

---

### CLUSTER A — Consolidação de parque legado
**Posição na esteira:** valida Customer Segment + Job to be Done · **Maior maturidade de todas**

**Hipótese:** a operadora não quer alugar bateria; quer se livrar da gestão de milhares de
gabinetes velhos — e paga por isso quando a conta aparece numa linha de custo que ela já
reconhece.

**Evidência — é a única oportunidade com demanda ativa puxada pelo cliente:**
> "Esse novo projeto, eles querem que a Moura **assuma sites já existentes** [...] a ideia é a
> Moura comprar o legado e depois colocar como uma locação" — Driele, 00:15:23 / 00:16:10
> Origem: a Telefônica queria alugar só a bateria; a Moura não faz; o cliente respondeu *"se
> vocês não podem atender do jeito que a gente quer, ofereça pra gente algo que vá nos
> atender"* — 00:14:17

**O mecanismo financeiro — o mais forte da base inteira:**
> "você tem aí três gabinetes velhos, eu vou tirar esses três e colocar um novo [...] eu compro
> como sucata [...] **Você paga 10 metros quadrados e eu consigo reduzir para 6. Então você vai
> pagar 4 metros quadrados a menos** [...] Começa a fazer sentido do ponto de vista do bolso"
> — Espinoza, 00:10:59 / 00:11:29

Por que funciona: as towercos viraram "**inimigo número um**" e a cobrança é por m² de projeção
(Espinoza, 00:21:25). **Este é o único argumento em toda a base que ataca uma despesa recorrente
que o cliente já paga e já odeia** — não exige provar payback sobre a bateria.

**Convergências:** TIM não cobriu 100% dos sites de acesso em 8 anos e busca "modelos de
contratação mais flexíveis" (item 26); a Claro tem ~R$1 bi imobilizado em bateria e "quase
enxuga gelo" (00:25:57); 90% dos sites da Moura hoje são novos e o legado é reconhecido
internamente como "**o principal ponto**" (Daniel, 00:36:21).

**Maior incerteza a reduzir:** o custo real de assumir parque de terceiro, de idade e estado
desconhecidos — e a operação de troca com o site ativo ("você tem que ter gente lá desligando o
equipamento, instalando ao mesmo tempo. Super complexo", Espinoza, 00:11:29).

**O que precisa ser verdade:** que a economia de m² + consolidação supere o custo de aquisição
do legado e da migração. **Já há vistorias em campo em curso** (Driele, 00:14:52) — a
verificação está começando sozinha.

---

### CLUSTER B — Disponibilidade contratada (garantir o banho)
**Posição na esteira:** redefine a Proposta de Valor · **Destrava o Problem-Solution Fit**

**Hipótese:** o cliente não compra horas de autonomia; compra o site no ar. Remunerar por
disponibilidade alinha o que se vende ao que se decide.

**Evidência interna — a formulação já existe na casa:**
> "a gente na prática está **alugando a caixa d'água, a gente não está garantindo banho** [...]
> em algum momento o cliente vai dizer: **me garante um banho** [...] me garante disponibilidade
> de energia [...] Eu consigo visualizar com muita clareza hoje que só alugar a caixa d'água
> não será suficiente no longo prazo" — Thiago, 00:48:02 / 00:50:45

**Evidência do comprador:**
> "eu vou te contratar um período X de autonomia, não de capacidade de energia, 4 horas que
> seja. **Eu nunca sei se a falta de energia vai durar 30 minutos, 5, 10, 15 ou 20**"
> — Fabiano, Claro, 00:45:01

**Quatro operadoras, quatro réguas diferentes — a padronização em horas não sobrevive:**
| Fonte | Régua real | Determinante |
|---|---|---|
| Claro | 2h / 4h / 6h por site | frequência × duração de falta × tráfego (00:27:01) |
| TIM | discutiu 1h e 2h contra o padrão de 4h | importância do site (item 44) |
| Algar | 4h greenfield · **12h** prédio comercial | **acesso ao gerador** (12:17) |
| Ufinet | **8h+**, um POP com **72h** | distância e criticidade do cliente (24:09 / 23:00) |

**E a linguagem de compra por resultado já é o padrão da casa do cliente:**
> "A gente contrata serviço. **Eu não contrato HC** [...] Eu vou te cobrar o resultado [...]
> espero que você atenda em até 4 horas tantos% dos meus incidentes" — Fabiano, Claro, 00:38:16

**Maior incerteza:** a Moura consegue assumir SLA de disponibilidade com a capilaridade atual?
A evidência diz que ainda não — cobertura sem a região Norte, bases da RSM no litoral (Daniel,
00:32:41), e a Algar rejeitou justamente por isso: "ele teria que ter equipes muito
distribuídas [...] o custo dessas equipes não ficaria vantajoso" (28:49).

**O que precisa ser verdade:** que a disponibilidade seja mensurável e auditável pela
plataforma. **Hoje não é** — a autonomia entregue sequer aparece na tela (Consultor Vivo,
00:18:15). **Cluster B depende do Cluster C.**

---

### CLUSTER C — Inteligência de dimensionamento e despacho
**Posição na esteira:** habilitador · **Pré-requisito de B e de qualquer contrato de performance**

**Hipótese:** o dado que a Moura já coleta vale mais como decisão de investimento do que como
tela de monitoramento.

**Evidência de demanda, em três operadoras:**
> "usar inteligência artificial [...] cruzamentos [...] com o histórico [...] para a gente
> pensar até **no investimento, onde a gente deve investir mais bateria, onde menos**" — Algar, 21:17
> "a gente avalia qual é a frequência de falta de energia, qual a duração [...] correlacionar
> com dados de tráfego, para priorizar o investimento" — Claro, 00:27:01
> "a gente tem uma planta viva [...] ferramentas que analisam isso para dizer: tira daqui, põe
> lá [...] otimizar a planta" — Daniel Machado, Claro, 01:04:30

**O ativo que só a Moura tem:**
> "eu estou conseguindo fazer um **teste em grande escala com diferentes ambientes, diferentes
> temperaturas**" — Francisco/TI, 00:20:42

**E o que precisa ser consertado antes de vender qualquer coisa:**
- 30–35% do parque com erro de instalação da fonte (Francisco, 00:17:56)
- alertas com falso positivo e falso negativo (Consultor Vivo, 00:14:08)
- a operadora **não tem acesso à plataforma**, só recebe relatórios (Francisco, 00:18:30)

**Maior incerteza:** a Moura consegue tornar o dado confiável antes de tentar monetizá-lo? Sem
isso, o cluster não existe — e uma demonstração falha destrói a credibilidade dos outros dois.

> **Esta é a hipótese mais crítica do portfólio inteiro.** É a única cuja falha derruba B e C
> simultaneamente, e é interna — depende só da Moura.

---

### CLUSTER D — Redução de exposição (não proteção adicional)
**Posição na esteira:** ajuste de solução dentro do PSF · **Menor prioridade de investimento**

**Hipótese:** o mercado já decidiu barater o alvo. Vender mais proteção rema contra a corrente.

**Evidência:**
> "eu coloco essa bateria mais cara no campo, mas ela é roubada [...] **Se me roubarem, a
> empresa não vai gastar tanto para repor**" — compras Claro, 00:23:54 / 00:24:32
> "câmera não inibe mais [...] mesmo você filmando a cara dele, você não [tem o que fazer]"
> — Ufinet, 40:18
> "é uma **briga de gato e rato**" — compras Claro, 00:57:24
> Concorrência real: serralheiro a "100, 200 reais a hora" soldando uma placa — 00:58:02

**E a Moura já está indo nessa direção, sem ter nomeado:**
> "através de um redimensionamento de energia, está estudando **colocar menos bateria no
> gabinete** [...] para diminuir essa atratividade do nosso gabinete" — Consultor Vivo, 00:12:09

**O erro de premissa, quantificado:**
> "cerca de **7% dos gabinetes** foram vandalizados [...] nosso modelo de negócio foi baseado
> em **2%** [...] a gente está 5% acima" — Consultor Vivo, 00:11:36 / 00:12:30
Cruza com 5–7% de incidência declarados pela Claro (00:34:44): **a premissa de 2% estava fora
da realidade do mercado desde o início.** Não foi azar de execução — foi erro de modelagem.

**Consequência para a precificação — a formulação mais precisa da base:**
> "o furto é uma coisa que **não está na mão dele, está na minha mão**. Então é um risco que ele
> está assumindo e que está na minha mão" — José, Algar, 28:49

→ Precificar integralmente um risco cuja mitigação depende do cliente sempre resultará em prêmio
maior que o custo do cliente gerindo sozinho. **A saída não é precificar melhor: é
compartilhar** — risco como linha explícita, com faixas por ambiente, e não diluído na
mensalidade.

**Maior incerteza:** existe disposição a pagar por redução de exposição como item separado, ou
isso é apenas engenharia de produto que a Moura precisa fazer para proteger a própria margem?
**A evidência atual sugere a segunda.**

---

### CLUSTER E — Agenda energética ampliada
**Posição na esteira:** exploração · **Horizonte mais longo, maior incerteza**

**Hipótese:** backup é uma fatia de uma necessidade energética que está crescendo mais rápido.

**Evidência convergente das três pontas:**
> "os sites vão ter que ser cada vez mais autônomos [...] energia solar e BESS [...] **você não
> vai precisar nem de gerador** [...] ele mesmo vai se auto sustentar" — José, Algar, 47:36
> "eu posso ir desligando coisas aos poucos [...] **transformar uma hora de backup em 4 horas**"
> — Fabiano, Claro, 00:52:25 (teste planejado no laboratório CRT)
> Ufinet já instala painéis solares em POPs de alto consumo — 08:53
> "a malha de energia no Brasil **não está preparada** para esses grandes data centers" — Algar, 43:44
> Dissipação: de 1.500 W/rack para **60 kW/rack** com IA — Algar, 45:05

**E dentro da Moura o ativo já existe:** o BES tem três produtos (backup, economia, qualidade)
e o VPP com captação solar por ERB estava mapeado como fase 2 desde 2022 (Francisco, 00:05:50).
> "vejo uma oportunidade nos sites de telecom para a gente também entregar economia de energia"
> — Thiago, 00:50:11

**Maior incerteza:** regulatória. O próprio Thiago aponta que o ONS já desliga plantas solares
por excesso de geração (00:51:57).

**Recomendação:** não é motor de receita para 2026. É a razão pela qual **não se deve estreitar
a identidade do negócio a "aluguel de bateria"** — e deve aparecer no deck como horizonte, com
uma frase, não como frente de investimento.

---

## 4. Sequenciamento — o que a evidência recomenda

| Horizonte | Foco | Por quê |
|---|---|---|
| **Agora** | **C — confiabilidade do dado** | Interno, sob controle total da Moura, e pré-requisito de B. Sem isso nenhuma promessa de disponibilidade é auditável. |
| **Agora** | **A — legado Telefônica** | Demanda ativa puxada pelo cliente, vistorias em curso, e o único argumento financeiro que ataca custo já reconhecido (m² de towerco). |
| **Próximo** | **B — disponibilidade contratada** | Depende de C. Exige também resposta à capilaridade — a razão declarada da recusa da Algar. |
| **Próximo** | **D — redução de exposição** | Tratar primeiro como correção de margem interna; só depois avaliar como oferta. |
| **Horizonte** | **E — agenda energética** | Sinaliza direção; não consome caixa em 2026. |

**A urgência é real e tem data:** o contrato Telefônica prevê instalação em 3 anos; hoje há 415
sites de 1.911 (Daniel, 00:13:17), e ele mesmo avalia que o prazo precisará de aditivo
(00:25:59). Quando a implantação terminar, cessa a receita de instalação e resta a mensalidade
de ~R$ 2.000/site/mês (00:27:35). **A curva seguinte de receita precisa começar antes disso.**

---

## 5. Correção de rota comercial — o achado mais acionável da base

Thiago suspeita que fala com o interlocutor errado:
> "eu tenho dúvidas se a gente está fazendo interlocução com **as pessoas certas** [...] a
> área que a gente lida é um pouco dessa área de operações" — 00:26:16

**A resposta está em outra entrevista interna:**
> "é o **time de planejamento** que puxa a verba [...] **Não é compras. Compras só quer saber do
> leilão do preço**" — Driele, 00:17:56
Ciclo: planejamento levanta idade dos sites → pede a verba ("a gente precisa de 45 milhões") →
recebe aprovação → passa a compras já com fornecedores preferenciais — 00:19:03 / 00:20:08

E do lado do comprador, a confirmação de que preço é o último critério:
> "antes de entrar no preço, tem que verificar tudo que é jurídico [...] **é muito mais jurídico
> ou operacional do que de preço**" — compras Claro, 00:47:35

→ **A Moura entra na conversa no momento em que a verba já foi definida e o jogo já é preço.**
Nenhuma melhoria de proposta de valor compensa entrar tarde. Este é um ajuste sem custo, com
efeito imediato — e merece slide próprio.

**Barreiras de execução, com fonte:**
- SLA interno inexistente: "O que impacta é a demora da Moura na resposta"; "a gente não tem um
  padrão, um fluxo, um SLA formalizado internamente"; "o alinhamento do alinhamento"; "**Isso é
  algo normal. Não deveria, mas acaba sendo algo normal dentro da Moura**" — Driele, 00:25:30 a 00:26:33
- Um diretor da Vivo pediu ajuda em nov/2025 e "**até hoje a gente não respondeu**" — Espinoza, 00:15:07
- Round-trip técnico: comercial não responde, dispara para engenharia, espera, devolve sem
  entender — "Esse tempo, se eu tivesse lá, eu já estava com o outro" — Espinoza, 00:20:31
- Governança de pipeline perdida: o checkpoint quinzenal acabou; "**nós vamos fechar com a
  Claro? Não sei. Se ninguém falou nada, não vai**" — Daniel, 00:12:25

---

## 6. Insumos para a sessão de nova proposta de valor + BMC

**O que precisa estar decidido antes da sessão:**
1. Qual segmento é o cliente prioritário — a evidência aponta para **operadora grande com
   parque legado**, mas o deck ainda registra "diferentes interpretações sobre quem é o cliente
   prioritário" (p.10)
2. Qual métrica a oferta vende: horas de autonomia ou disponibilidade
3. Se o risco de furto vira linha explícita e compartilhada

**Já disponível como insumo, e que dispensa novo levantamento:**
- Mensalidade média: ~R$ 2.000/site/mês · CAPEX por gabinete: ~R$ 100 mil (Daniel)
- Incidência real de vandalismo: 7% no parque Moura vs. 2% da premissa; 5–7% declarado pela
  Claro; ~R$ 100 mil já acima do cap proporcional
- Critérios financeiros do comprador: payback ≤ 3 anos com IPC (TIM); break-even calculado de
  1a8m a 2,5 anos (Claro)
- Ganho comprovado: ~1 ponto percentual de disponibilidade em 6 meses de trial (Daniel)
- Réguas de autonomia por contexto (tabela do Cluster B)

**Materiais a levar prontos para o grupo atacar:** BMC as-is da p.14 e VPC por perfil de
operadora, ambos pré-preenchidos, para a sessão **editar** em vez de construir do zero.

---

## 7. LACUNAS E NÃO VERIFICÁVEIS

### 7.1 Entrevistas não lidas na íntegra
Aline (Imersão), Andrea (Imersão), Josi (Expansão de Serviços) e Gustavo. As três primeiras são
centrais para precificação e para a visão de produto — **Andrea é apontada por Daniel e por
Francisco como a orquestradora do modelo e responsável pela modelagem financeira**. Conclusões
sobre governança de precificação devem ser tratadas como preliminares até essa leitura.
*Nota operacional:* o arquivo do Gustavo tem espaço no nome (`Gustavo -transcript.txt`) e falhou
em acesso direto; exige aspas no caminho.

### 7.2 Dependências de arquivos ausentes do acervo
Continuam **não verificáveis** neste diretório, e todas as afirmações que dependem delas devem
ser marcadas como tal:
- deck da Fase 1 (parque de ~115 mil sites, towercos, Mordor Intelligence)
- Report de Fechamento do Trial TIM, jan/2024 (os 237 alertas / 4 visitas)
- Projeto Básico de Locação da Telefônica (1.911 sites, contrato de 10 anos)
- BAAS Brasil, Moura as a Service, MaaS Telecom Telefônica
- 2 entrevistas internas adicionais (o relatório externo cita 12; o acervo tem 10)

**Parcialmente resolvido:** o resultado do trial TIM tem confirmação independente por fonte
interna — ~1 ponto percentual de ganho de disponibilidade em 6 meses (Daniel, 00:38:18) — e a
TIM confirma sucesso técnico com reprovação no CFO (item 27/28). O número específico de
237 alertas / 4 visitas permanece não verificável.

### 7.3 Divergências registradas, não resolvidas
- **Anatel:** a engenharia da Claro afirma que "não [há] multa, mas existe um indicador da
  Anatel que chama RQAL", cuja quebra libera o cliente da fidelização (00:31:50). A área de
  compras da mesma operadora menciona exigência de 4h "pela Anatel" (00:36:30). A Ufinet diz
  não estar sujeita (41:47). **O material comercial da Moura afirma que há multa.** Recomendação:
  corrigir o material antes da próxima proposta; **avaliar com cuidado se isso vai ao palco** —
  é achado relevante, mas expõe erro em material em uso.
- **"80% a 90% dos furtos são de oportunidade"**: fonte única (José/Algar, 10:34), declarada
  como leitura qualitativa. Não usar como dado ao lado de números medidos.

### 7.4 Restrição de confidencialidade
Thiago pede explicitamente, ao falar de mudança de estrutura e pessoas (00:28:42): *"por favor,
não coloque isso no relatório nem nada"*. **Esse trecho não foi usado e não deve ser.** O ponto
adjacente sobre maturidade do time comercial foi dito sem ressalva e está utilizado — sem
nomear pessoas nem antecipar mudanças organizacionais.
