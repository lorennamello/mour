# Canvas de Prontidão Organizacional — Moura Energia (preenchido)

*Este documento substitui, com dado real, o modelo em branco proposto em `22-canvas-visao-interna-organizacional-modelo.md`. Cada um dos 9 blocos traz **Como é hoje (AS IS)** e **O que está faltando** — no mesmo espírito do exemplo que você deu: se o comercial não tem conhecimento técnico (AS IS), o que falta é treinamento (GAP). As citações são o mais literais possível, extraídas diretamente das transcrições brutas da imersão interna (não das versões já sintetizadas), com arquivo e falante indicados.*

---

## Atualização do modelo: material completo do livro

O documento completo que você enviou tem **11 categorias**, não 10 — a foto original não mostrava duas delas: **Variação** e **Controle de Processo**. Para manter o canvas do mesmo tamanho do BMC (9 blocos) e evitar fragmentar demais, consolidei:
- **Variação** → dentro de **Capacidades** (ambas tratam de dimensionamento/consistência: o quanto o produto varia de execução e se isso é tolerável).
- **Controle de Processo** → dentro de **Governança e Regras de Negócio** (ambas tratam de regras, aprovações e quem responde pelo quê).

As perguntas-guia de cada bloco abaixo já são as **originais completas** do material (não mais a versão extrapolada por mim na primeira proposta).

---

## Nota metodológica sobre a evidência

Duas coisas específicas **não têm citação literal** nas transcrições brutas, mesmo aparecendo em sínteses anteriores (inclusive minhas, no BMC):
1. O termo "força-tarefa" (usado no BMC para descrever perda de estrutura de precificação) — a evidência bruta mais próxima é indireta (ver bloco Governança).
2. Qualquer custo de fricção interna **quantificado em reais** — os entrevistados descrevem o problema (retrabalho, atraso, piora de retorno) qualitativamente, nunca em R$.

Marquei os dois pontos como **interpretação**, não como citação direta, nos blocos correspondentes.

---

## 1. Contexto Cultural
*Faixa que atravessa todos os blocos — perguntas: liderança, qualidade, aceitação, treinamento.*

**Como é hoje (AS IS):**
- A própria organização reconhece que ainda está **departamentalizada**: o time de TI tem 4-5 pessoas dedicadas ao produto, mas falta alguém de Engenharia ou do ITEM dedicado da mesma forma — *"deveria ter alguém de engenharia ou alguém, assim como do ITEM (...) teve, na minha visão, uma deficiência no handover de algumas questões."* (Francisco, TI)
- A liderança está comprometida, mas o ritmo de adaptação interna não acompanha o ritmo do mercado — *"a mora está cercada de gente competente (...) mas a gente está entrando num negócio que se move muito rápido (...) o mercado não espera, ele atropela."* (José Espinosa)
- Já existe reconhecimento interno de que a estrutura atual precisa mudar: uma reorganização estava sendo desenhada para colocar alguém com **"lógica mais mercadológica"** cuidando do produto — *"a gente, nas próximas semanas, inclusive, deve fazer uma mudança de estrutura (...) para que a gente tenha uma pessoa (...) de treinamento da equipe comercial, de escutar, de ser a dona do produto."* (Thiago)

**O que está faltando:**
- Um "dono" de produto com viés de mercado (escuta, treinamento comercial), não só de modelagem financeira — o próprio Thiago já nomeia essa lacuna (ver também bloco Medição de Desempenho).
- Handover formal e documentado entre ITEM (concepção) e Engenharia (operação/melhoria contínua) — hoje depende de boa vontade, não de processo.
- *Nota: a leitura de "força-tarefa perdida" (usada no BMC) não tem citação literal correspondente — é uma inferência a partir do relato sobre perda de estrutura de precificação (ver bloco Governança), não um fato citado diretamente.*

---

## 2. Contexto de Negócio do Produto
*Bloco-âncora — perguntas: por que o produto existe, mudança/riscos, tecnologia, estratégia e metas.*

**Como é hoje (AS IS):**
- A razão de ser do produto é clara e validada: resolver a dor de CAPEX e de disponibilidade da operadora, terceirizando a gestão de energia — *"veio esse novo modelo de energia como serviço para facilitar, para curar uma dor deles, que é a dor de CAPEX (...) Deixa que da bateria, da energia, cuido eu."* (Karina)
- O risco de furto é estrutural ao próprio negócio, não um efeito colateral: *"a bateria tem valor no mercado negro (...) se a bateria é furtada, quando cai a energia (...) cai a rede de todo mundo."* (Andrea)
- O risco de funding já pressiona a viabilidade: *"a gente não vem conseguindo atribuir a mesma taxa de juros de captação que André conseguiu no passado (...) isso já piora também meu aluguel."* (Time Financeiro)
- Escopo do produto é claro e verticalizado: gabinete + fonte + monitoramento remoto + garantia de disponibilidade por 10 anos (Karina).

**O que está faltando:**
- Um modelo de captação de capital mais estável (hoje sujeito a pioras de taxa que encarecem o próprio produto).
- Um mecanismo estrutural de mitigação de furto, além da provisão financeira — hoje o risco é absorvido no preço, não reduzido na causa.

---

## 3. Governança e Regras de Negócio
*Inclui Controle de Processo — perguntas: completude e adequação das regras, aprovações desnecessárias, controles existentes.*

**Como é hoje (AS IS):**
- O fluxo de decisão comercial funciona por **orquestração informal de pessoas**, não por regra ou SLA formal: *"a gente literalmente funciona como esse elo que une todas as áreas, suportando com informações (...) para fazer com que o processo se consolide."* (Maria Cecília, Financeiro)
- Não existe papel formal designado de interface entre Engenharia e Comercial: *"Existe alguém designado para esse atendimento comercial, essa visão técnica no comercial? Não (...) alguém realmente só para essa função, não."* (Yasmin, Engenharia)
- A precificação depende de uma capacidade que se perdeu com a saída de uma pessoa específica: *"como ela [Andrea] não tem esse braço financeiro dentro da área dela desde que a André saiu, eu estou apanhando ela nesse último ano."* (Time Financeiro) — esta é a evidência mais próxima da leitura de "força-tarefa perdida" citada no BMC, mas de forma indireta.
- O SLA existe formalmente no contrato com o cliente, mas não é cumprido internamente como planejado: *"o tempo de resposta, os SLA de atendimento nosso, os reais não estão iguais ao planejado."* (Consultor de Projetos/Vivo)
- Aprovação de precificação é lenta, com muitas idas e vindas: *"foram muitas idas e vindas para a gente ir montando uma solução personalizada (...) o que talvez frustre um pouco o comercial (...) a gente demora para dar resposta para o cliente."* (Time Financeiro)

**O que está faltando:**
- SLA interno formal entre Engenharia, Comercial e Financeiro (hoje só existe SLA formal olhando para fora, para o cliente).
- Papel dedicado de interface comercial-técnica, em vez de "follow-up" informal.
- Reposição da capacidade de modelagem financeira/precificação perdida com a saída de pessoas-chave.

---

## 4. Capacidades
*Inclui Variação/Dimensionamento — perguntas: o processo/produto pode ser dimensionado para cima? Qual é o custo quando ocioso? Que dependências existem?*

**Como é hoje (AS IS):**
- O hardware de monitoramento é, nas palavras do próprio time de TI, um **"MVP que virou produção"**: nasceu pequeno (15 sites) e cresceu para mais de 400 sites sem nunca ter sido redesenhado como produto industrial maduro — só agora está recebendo um "upgrade" tardio. *"No início foi um MVP que acabou (...) entramos em produção com algumas melhorias (...) agora a gente está dando um upgrade nesse ecossistema para conseguir sustentar o crescimento."* (Francisco, TI)
- Falhas de instalação em campo foram documentadas visualmente pelo próprio ITEM — fio errado, porta errada, energia sequer ligada: *"um compilado de todos os erros que foram encontrados em campo (...) usaram um fio que não podia (...) instalaram, mas nem ligaram a energia."* (Francisco, citando Vanessa/ITEM)
- Falhas de configuração de fábrica geram retrabalho em campo, porque nem todos os testes são feitos antes do envio: *"a gente não faz todos os testes em fábrica (...) alguns problemas em campo já poderiam (...) ter sido diagnosticado em fábrica."* (Yasmin, Engenharia)
- A capacidade de campo (RSM) não cobre todo o território por decisão deliberada, não por incapacidade pontual: *"a gente não vai para o norte, tá? É um acordo que a gente fez."* (Andrea)

**O que está faltando:**
- Versão industrial madura da plataforma (já em andamento, mas tardia frente ao volume atual de sites).
- Bateria completa de testes em fábrica antes do envio a campo.
- Modelo de parceiro terceirizado/quarteirizado para cobrir geografias fora do alcance do RSM — sugestão já dada pelo próprio Consultor de Projetos: *"eles podem terceirizar (...) uma quarteirização de parceiros que estão melhor distribuídos geograficamente."*

---

## 5. Handoffs e Gargalos

**Como é hoje (AS IS):**
- O handover entre ITEM (concepção) e Engenharia (operação) é deficiente — mesma evidência do bloco Capacidades, aqui com foco no atraso que gera: *"teve, na minha visão, uma deficiência no handover de algumas questões."* (Francisco, TI)
- O repasse entre Comercial e Engenharia é sustentado por "follow-up" informal, sem função dedicada — mesma citação de Yasmin do bloco Governança.
- O maior gargalo do ciclo de precificação, segundo o próprio time financeiro, é o tempo de resposta da Engenharia: *"a maior dificuldade que a gente tem é o tempo de resposta (...) de engenharia, determinar qual produto, até a gente chegar no preço."* (Time Financeiro)
- Dados não confiáveis geram retrabalho e atraso direto: *"essa não confiabilidade dos dados gera retrabalho (...) gera retardo."* (Consultor de Projetos/Vivo)
- Pedidos e processos já se perderam por troca de pessoas, sem sistema de handover: *"teve problemas nossos, de fato, dessas trocas de pessoas, onde a gente perdeu processos (...) perdeu o pedido (...) a gente não internalizou."* (Karina)

**O que está faltando:**
- Processo formal de handover entre áreas — hoje depende de "força de vontade" e follow-up manual, não de rotina definida.
- SLA de tempo de resposta entre Engenharia e Comercial/Financeiro.
- Checklist ou sistema de transição para quando uma pessoa sai, cobrindo pedidos e processos em andamento.

---

## 6. Envolvimento Humano

**Como é hoje (AS IS):**
- Turnover comercial de **100% em um ano**, confirmado duas vezes na mesma fala: *"a gente teve, com a saída da antiga gerente, que a gente teve um turnover de 100% da equipe. 100%."* (Karina)
- A perda de conhecimento histórico força um trabalho manual de reconstrução: *"a gente está resgatando e-mails, a gente está resgatando pedidos, a gente está resgatando, sério, nesse nível."* (Karina)
- A rotatividade também atinge a operação: *"está acontecendo uma rotatividade muito grande (...) desde que eu cheguei tem dois anos, não existe mais o time inicial."* (José Espinosa)
- Parte do trabalho de monitoramento ainda depende de garimpo manual de dados que não chegam prontos: *"eu tenho informação que eu não tenho (...) vomitada na minha frente."* (Consultor de Projetos/Vivo)

**O que está faltando:**
- Documentação/repositório de conhecimento histórico compartilhado — sugerido explicitamente pelo próprio time financeiro: *"se todo mundo que estivesse envolvido no projeto hoje soubesse do histórico (...) eles acabam colocando [premissas antigas] para todos os projetos porque não sabem qual foi a raiz."* (Time Financeiro)
- Processo formal de onboarding/handover quando uma pessoa-chave sai.
- Estruturação/automação dos dados para reduzir a dependência de garimpo manual.

---

## 7. Medição de Desempenho

**Como é hoje (AS IS):**
- As premissas financeiras já se mostraram menos conservadoras do que a realidade em pelo menos uma dimensão relevante: o time reconhece que o risco percebido está maior do que o imaginado no início — *"a gente vem entendendo que talvez o risco esteja um pouquinho maior do que o que a gente imaginava no início."* (Time Financeiro)
- O papel do PO (dono do produto) é descrito, por um dos entrevistados mais seniores, como excessivamente financeiro: *"a estrutura que a gente tem para cuidar deste produto (...) está lá representada por Andréa como (...) Product Owner, infelizmente também está com uma visão muito interna, muito com um viés financeiro do negócio."* (Thiago)
- Propostas comerciais já "morreram" silenciosamente, sem que o time seguinte soubesse que existiam: *"a gente vendeu, apresentou uma proposta no passado que morreu (...) com toda essa troca do time, o time nem entendia que eles eram os executivos da Morenergia."* (Karina)

**O que está faltando:**
- Recalibração periódica e explícita das premissas financeiras contra o dado real (hoje o ajuste parece acontecer de forma reativa, não como rotina).
- Redesenho do papel do PO para incluir escuta de mercado, treinamento comercial e materiais promocionais — não só modelagem financeira. O próprio Thiago já descreve o que falta: *"plugada com uma modelagem financeira do negócio, mas sem uma abordagem mais mercadológica, sem uma abordagem de treinar a equipe comercial, de escutar."*
- Processo de acompanhamento de propostas em aberto, para que não se percam silenciosamente na troca de pessoas.

---

## 8. Custo da Fricção Interna
*Saída do canvas — equivalente à "Margin" na Cadeia de Valor de Porter.*

**Como é hoje (AS IS) — sempre qualitativo, nunca quantificado em R$:**
- Retrabalho por dados não confiáveis (Consultor de Projetos/Vivo).
- Retrabalho de campo por falha de configuração de fábrica não testada previamente (Yasmin).
- Custo de captação pior, pressionando diretamente o preço final do aluguel (Time Financeiro).
- Esforço de "resgate" manual de e-mails e pedidos perdidos por turnover (Karina).

**O que está faltando:**
- **Medição do próprio custo da fricção.** Este é o achado mais importante do bloco: em nenhuma das 15 entrevistas alguém quantificou, em reais, o custo de retrabalho, turnover ou captação — todos descrevem o problema qualitativamente ("gera retrabalho", "isso já piora meu aluguel"), mas ninguém tem o número. Isso significa que a organização está pagando um custo real e recorrente que **não aparece em nenhuma linha de orçamento hoje** — o que, por si só, dificulta priorizar a correção desses problemas frente a outras prioridades que têm número.

---

## 9. Interações com Clientes (lente interna)
*Diferente do "Relacionamento com Clientes" do BMC — aqui é a mecânica interna por trás da relação, não a lógica prometida ao cliente.*

**Como é hoje (AS IS):**
- Existe uma dúvida explícita e recorrente — repetida por dois entrevistados diferentes, em momentos diferentes — sobre se a Moura fala com as pessoas certas dentro do cliente: *"eu tenho dúvidas se a gente está fazendo interlocução com as pessoas certas (...) porque eu não sei se tem ali algum receio por parte deles de perder protagonismo também."* (Thiago) e *"não sabemos se estamos falando com as pessoas certas."* (Gustavo Moura)
- Quem de fato fala com o cliente hoje está fragmentado entre pelo menos três frentes — comercial, uma área de apoio chamada "Contratos" (Josi) e a operação (José Espinosa) — sem um dono único: *"o acompanhamento é feito aqui na área comercial (...) temos uma área de apoio que chama Contratos (...) a Josi (...) vai fazer toda a programação da fábrica para que consiga atender a operação (...) que é o José Espinosa."* (Aline Souza)
- A "escuta ativa" do cliente aparece como algo a se desenvolver, não como processo já existente: *"talvez valesse a pena a gente aprofundar um pouco mais até ter uma escuta mais ativa dele nesse sentido."* (Maria Cecília, Financeiro)

**O que está faltando:**
- Mapeamento formal de quem são "as pessoas certas" dentro de cada operadora — a dúvida está identificada há tempo, mas ainda não foi respondida.
- Canal estruturado de escuta/feedback do cliente — busquei especificamente por evidência de um canal formal (ouvidoria, pesquisa de satisfação, processo de coleta de sugestão) e não encontrei menção a nenhum nas 15 entrevistas. Isso não prova que não existe, mas indica que, se existe, não é algo presente na cabeça de quem foi entrevistado.
- Um dono único e claro da relação com o cliente — hoje ela está fragmentada entre comercial, contratos e operação, cada um com um pedaço.

---

## Síntese — o padrão que se repete nos 9 blocos

Um único fio conecta praticamente todos os "O que está faltando" acima: **a Moura tem pessoas competentes fazendo o trabalho de um processo que ainda não existe.** Onde deveria haver handover documentado, há follow-up informal. Onde deveria haver SLA interno, há orquestração pessoal. Onde deveria haver conhecimento compartilhado, há resgate manual de e-mail. Onde deveria haver medição de custo de fricção, há apenas relato qualitativo. Isso não é uma crítica a nenhuma pessoa específica — pelo contrário, boa parte da evidência mostra pessoas comprometidas compensando, no esforço individual, a ausência de estrutura. Mas é exatamente esse padrão — **estrutura que não acompanhou o crescimento** — que este canvas foi desenhado para tornar visível.

---

## Metodologia e fontes

- **Evidência primária**: 15 transcrições brutas da imersão interna (`entrevistas-internas/*.txt`), levantadas especificamente para este canvas a partir dos 9 blocos definidos em `22-canvas-visao-interna-organizacional-modelo.md`.
- **Cruzamento**: síntese executiva por tema (`13-visao-executiva-por-tema.md`) e "Desafios complementares" do BMC (`20-bmc-as-is-moura-energia.md`) usados para orientar onde procurar evidência bruta, não como fonte primária de citação.
- **Transparência sobre limitação**: dois pontos (o termo "força-tarefa" e qualquer custo quantificado em R$ de fricção interna) não têm citação literal nas transcrições — marcados como interpretação em vez de evidência direta nos blocos correspondentes.
