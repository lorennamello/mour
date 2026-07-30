# Desafios Internos — Moura Energia, organizados em 7 blocos (bottom-up)

*Diferente do `25-canvas-prontidao-organizacional-minucioso.md` (que partiu de uma estrutura pré-definida de um livro de BPM), este documento foi construído de baixo para cima: primeiro levantamos ~40 desafios distintos direto da imersão interna e da planilha `Moura_Telecom_Phase_1__Interviews`, depois agrupamos em 7 blocos que emergiram dos próprios dados — não de um framework externo. Cada bloco só existe porque resolve um tipo de problema que exige um tipo de intervenção diferente dos outros blocos (ver critério de corte abaixo).*

**Fontes:** 15 transcrições brutas da imersão interna (`entrevistas-internas/*.txt`) e a planilha `Moura_Telecom_Phase_1__Interviews_4.xlsx` (abas Desafios, Áreas internas, Áreas internas Conflitos, Resumo 5 pontos, Clientes). Excluído deliberadamente todo conteúdo de mercado/comportamento do cliente (abas Barreiras de Expansão, Ecossistema e mercado, Hipóteses) — o foco aqui é só a visão interna.

---

## 1. Produto & Tecnologia
*O artefato físico/digital em si — maturidade, confiabilidade, design — independente de quem opera.*

**Como é hoje:**
- O hardware de monitoramento (Connect Plus) nasceu como POC/MVP (placa Raspberry, modems comerciais) e foi escalado para produção antes de virar produto industrial maduro. *"Isso não era produto. Isso ainda era experimental (...) A POC acabou virando produto muito rápido e ela setou um CAPEX enxuto. A gente de P&D tava tentando amadurecer o produto enquanto ele já tava sendo instalado."* — **Vanessa, P&D/ITEMM** (planilha, aba Desafios). Confirmado por **Francisco, TI**: *"É o MVP que virou produção (...) essa versão final estável nunca chegou, em termos de hardware."*
- O dispositivo IoT não é plug-and-play, o que já é, em si, um problema de design (distinto do erro humano de instalação, tratado no bloco 2). *"O pessoal em campo tem muita dificuldade de fazer a instalação correta. Então, ainda não é plug and play."* — **Yasmin, Engenharia** (planilha, aba Desafios).
- A detecção de furto pela própria plataforma não é confiável — o cliente às vezes descobre antes da Moura. *"Geralmente vão lá, acerram a parte do cadeado (...) a gente só sabe quando o cliente vai lá."* — **Yasmin** (planilha, aba Desafios). Confirmado por **Consultor de Projetos**: *"acontece muitas vezes de eu saber pelo cliente (...) Aí vou olhar a plataforma e não está dizendo nada."* (`0708_Entrevista_Consultor_de_Projetos_da_Moura_Energia_Operacao_Vivo.txt`)
- A trava/cadeado de segurança física é um componente terceirizado (Promon), fora do controle direto da Moura, e a infraestrutura usa componentes chineses sem padrão de segurança da informação auditado — risco de cibersegurança sem plano de contingência. — **Francisco, TI** (planilha, aba Desafios): *"se sistema desse terceiro for hackeado, a Moura perde imediatamente o acesso físico a todas as baterias ou pode sofrer vazamento de dados críticos (...) sem ter nenhum plano de contingência ou redundância."*
- Consumo de dados 4G ficou muito acima do premissado, elevando o OPEX. *"Hoje em dia, a gente consome bem mais do que o esperado e isso impactou em custo. A gente teve que aumentar nossos planos de dados."* — **Yasmin**, `Yasmin_Engenharia.txt`.
- Cada instalação é, na prática, um projeto customizado — não existe produto padronizado "de prateleira" que se repita entre clientes. *"Para cada companhia, vai ser uma solução diferente (...) muito customizável para cada cliente."* — **Driele**, `Driele_Expansao_do_modelo_de_servitizacao_em_telecom.txt`.

**O que falta:**
- Versão industrial madura, testada de ponta a ponta (o próprio upgrade "2.0" já em andamento, mas tardio frente ao volume atual).
- Um design mais plug-and-play, que reduza a dependência de perícia do instalador.
- Confiabilidade real do sistema de detecção automática de furto.
- Auditoria de segurança da informação e plano de contingência para o componente terceirizado.
- Recalibração de premissas de consumo de dados antes de assinar novos contratos.
- Um produto mais padronizado, com menos customização obrigatória por cliente.

---

## 2. Operação de Campo & Processos
*Como o trabalho físico é executado e coordenado dia a dia — logística, handoffs técnicos, capacidade geográfica.*

**Como é hoje:**
- O RSM (braço de campo) não é um fornecedor terceirizado local — é um CNPJ regional do próprio grupo Moura, o que torna a mobilização para zonas distantes lenta por definição estrutural, não por falha pontual. — **Tarcísio, Operações** (planilha, aba Áreas internas Conflitos): *"Como a RSM é um CNPJ regional do grupo e não um fornecedor local terceirizado, a Moura Energia sofre para atuar em zonas longínquas."*
- O SLA de atendimento presencial de 4h é logisticamente impossível em estados grandes. *"Num cenário ótimo, que nunca acontece (...) O cara levaria (...) sete horas para chegar lá, mas se o SLA é de quatro horas (...) os SLA de atendimento nosso, os reais não estão iguais ao planejado."* — **Tarcísio** (planilha, aba Desafios). A Moura decidiu deliberadamente não atender a região Norte: *"a gente não vai para o norte, tá? É um acordo que a gente fez."* — **Andrea**, `Imersao_Andrea.txt`.
- Descompasso entre a Fábrica (planejamento mensal engessado) e a Operação (demanda semanal dinâmica) já gerou risco de falta de gabinete em campo ou capital travado em estoque excessivo. — **Josiele, Fábrica** (planilha, aba Desafios).
- A Engenharia da Moura não tem nenhuma pessoa de software na equipe — fica "totalmente refém" do ITEMM para corrigir falha de software em campo. — **Yasmin** (planilha, aba Áreas internas Conflitos): *"hoje a gente não tem, por exemplo, uma pessoa de software na nossa equipe."*
- O handover de concepção (ITEMM/P&D) para operação (Engenharia) nunca se completou. *"O ITEMM, teoricamente, é aquela galera que entra, faz a concepção e entrega para a engenharia (...) Mas hoje ainda não está desse jeito. Teve, na minha visão, uma deficiência no handover."* — **Francisco, TI**, `Moura_Francisco_TI.txt` (confirmado na planilha).
- Falhas de processo na instalação (não checar sinal da região, conectar cabo errado, não ligar o equipamento) geram alarme falso e acionam a engenharia para problemas que não são de software. — **Vanessa** (planilha, aba Desafios): *"o cara instala, ele conecta um cabo errado, usa um material errado. O site entra na situação de manutenção muito rápido."*
- Gargalo de compras/abastecimento no início já atrasou implantações por falta de estoque. — **Daniel Garcia** (planilha, aba Áreas internas Conflitos): *"a gente poderia estar instalando mais site se tivesse essa estrutura (...) melhor estruturada."*
- Informação de campo não chega pronta — exige garimpo manual para virar informação útil. *"A informação não está dada, ela precisa ser minerada, eu preciso fazer um trabalho arqueológico."* — **Consultor de Projetos** (citado na planilha, aba Desafios, e na transcrição bruta).

**O que falta:**
- Normativas de instalação formalizadas e repassadas do ITEMM para o RSM.
- Modelo de parceiro local complementar (quarteirização) para regiões fora do alcance direto do RSM.
- Alinhamento de cadência entre planejamento de fábrica e demanda real da operação.
- Capacidade própria de software dentro da Engenharia, não dependente do ITEMM.
- Handover formal e documentado da concepção para a operação.
- Estrutura de compras dimensionada para o ritmo de expansão.
- Processo/ferramenta que já entregue dado interpretado, não bruto.

---

## 3. Pessoas & Cultura Organizacional
*O indivíduo e o clima — retenção, conhecimento tácito, valores, o que a empresa reconhece como "bom trabalho".*

**Como é hoje:**
- Turnover confirmado em **100%** da equipe comercial — desta vez com citação literal e direta. *"A gente teve um turnover de 100% da equipe."* — **Karina Fagundes, Gerente Comercial** (planilha, aba Desafios). *(Esta citação está na planilha Fase 1; nas 15 transcrições brutas revisadas anteriormente, só encontramos termos qualitativos como "giro importante" e "rotatividade muito grande" — a planilha resolve a lacuna que tínhamos sinalizado antes.)*
- A troca completa da equipe comercial gerou perda de histórico. *"A equipe inteira de DCBE [comercial] (...) trocou inteira. Então todos os analistas saíram (...) ficou um pouco sem histórico."* — **Daniel Garcia** (planilha, aba Áreas internas Conflitos).
- Conhecimento crítico do negócio concentrado em poucas pessoas. *"Fica, de certa forma, esse conhecimento está muito comigo."* — **Thiago Mello**, `Thiago_Energia_como_Servico_em_Telecom_TIM_Claro_Vivo_Evolucao_de_Produto_e_Estrategia_Comercial.txt`.
- Rotatividade também na operação — "não existe mais o time inicial" em 2 anos. — **José Espinosa**, `Jose_Espinoza.txt`.
- Cultura de qualidade hoje é conformidade ("fazer o que foi pedido"), não inovação — reconhecida como insuficiente pelo próprio time de operação. *"a gente é treinado assim para seguir o escrito (...) A gente tem que dar uma chacoalhada aqui e ter uma jornada de inovação."* — **José Espinosa**, mesma transcrição.
- **Sem evidência** de sistema formal de feedback/avaliação/desenvolvimento individual em nenhuma das 15 entrevistas ou na planilha.

**O que falta:**
- Retenção de pessoas e/ou processo que preserve conhecimento independente de quem está no cargo.
- Documentação/repositório de conhecimento compartilhado (sugerido pelo próprio time financeiro em outro contexto).
- Sistema formal de feedback e desenvolvimento de pessoas — hoje inexistente.
- Evolução cultural de "seguir o que foi pedido" para uma postura que também valorize inovação.

---

## 4. Colaboração entre Áreas & Estrutura Organizacional
*Como diferentes funções — não indivíduos — se conectam: papéis, SLA interno, decisão compartilhada, desenho de time.*

**Como é hoje:**
- Não existe SLA interno formalizado entre áreas. *"A gente não tem um padrão, um fluxo, um SLA formalizado internamente. A gente não tem esse tipo de padrão. Infelizmente."* — **Driele**, `Driele_Expansao_do_modelo_de_servitizacao_em_telecom.txt`. Confirmado na planilha (aba Áreas internas Conflitos): *"não existe um fluxo formal ou 'SLA de resposta interno' definido."*
- Não existe papel formalmente dedicado à interface Comercial-Engenharia. *"Existe alguém designado para esse atendimento comercial (...)? Não (...) alguém realmente só para essa função, não."* — **Yasmin**, `Yasmin_Engenharia.txt`.
- **Confirmado literalmente**: existia uma "Força-Tarefa" formal — as áreas recebiam um "Target" (preço-alvo do cliente) e se reuniam numa sala para espremer custos até a conta fechar. Isso não existe mais; hoje o trabalho é feito em silos, alongando os prazos. — **Time do Financeiro** (planilha, aba Desafios): *"Falta o engajamento entre os times — Antes existia uma 'Força-Tarefa' onde as áreas recebiam um 'Target' (...) e se uniam numa sala para espremer os custos até a conta fechar. Hoje, o trabalho é feito em silos."*
- O papel de PO (dono do produto) sofre para priorizar ações justamente por causa da estrutura departamentalizada — não é (só) um problema do indivíduo, é consequência do desenho organizacional. — **Francisco** (planilha, aba Áreas internas Conflitos): *"A PO sofre para priorizar as ações porque a estrutura é departamentalizada."*
- O time não é exclusivo — comercial e compras atendem Telecom, subestações e bancos ao mesmo tempo, "apagando incêndios" da venda avulsa de bateria. — **Karina** (planilha, aba Áreas internas Conflitos): *"a mesma equipe da Moura base (CMO) tentando operar dois modelos de negócios completamente diferentes e concorrentes ao mesmo tempo."*
- O mapeamento de quem é responsável por cada decisão/frente existe, mas só na memória de uma pessoa (Andrea), não documentado formalmente. — **Andrea**, `Andrea_Pontos_para_explorar_com_os_stakeholders.txt`.
- Falta fluidez no compartilhamento do que o comercial está negociando com os clientes; a operação roda desconectada das prospecções iniciais do comercial. — **Daniel Garcia** (planilha, aba Áreas internas Conflitos).

**O que falta:**
- SLA interno formalizado entre áreas.
- Papel formal dedicado à interface comercial-técnica.
- Retomada da Força-Tarefa (ou mecanismo equivalente) de precificação conjunta orientada a meta.
- Time exclusivo e dedicado ao produto, não compartilhado com a operação tradicional.
- Mapeamento de donos de decisão documentado, não só na memória de uma pessoa.
- Canal/rotina de compartilhamento de pipeline comercial com as demais áreas.

---

## 5. Capacidade Comercial
*A habilidade específica de vender — discurso, material, postura, foco em quem abordar.*

**Como é hoje:**
- O time não consegue tangibilizar financeiramente o valor do serviço. *"a gente gagueja pra um lado, gagueja pro outro (...) não sai do canto."* — **Thiago Mello**, planilha aba Desafios.
- Falta material institucional/apresentação robusta de TCO. *"a gente nunca teve também uma apresentação robusta (...) hoje, basicamente, a gente não consegue explicar, basicamente, financeiramente, é bem difícil."* — **Aline Souza** (planilha, aba Desafios).
- Falta especialista dedicado em marketing de produto B2B complexo. *"Não são boas (...) eu não tenho um especialista nisso no time."* — **Josiele** (planilha, aba Desafios).
- Abordagem inicial a stakeholders errados — o comercial ofereceu o serviço à área de Operações, que boicotou por medo de perder o emprego. — **Aline Souza** (planilha, aba Desafios): *"a gente percebeu que essa galera não estava afim (...) isso vai fazer perder meu emprego, porque vocês vão fazer gestão."*
- Postura reativa, não proativa, é reconhecida como problema pela própria organização: *"a MOURA sempre foi procurada e provocada pelos parceiros (...) sempre foi reativa, e hoje ela precisa ser proativa."* — nota sobre a fala de **Thiago Mello** (planilha, aba Modelo Comercial). Confirmado por **José Espinosa**: *"a gente não está fazendo isso (...) sem pensar nas alternativas. Então o produto, não tem inovação (...) a gente entrega o que eles pediram."*
- Sem acompanhamento formal de propostas comerciais — elas "somem" sem que ninguém perceba. *"A gente vendeu, apresentou uma proposta no passado que morreu."* — **Karina**, `Karina_Comercial.txt`. *"Um diretor não pode pedir uma ajuda da Amora em novembro de 2025, até hoje a gente não respondeu."* — **José Espinosa**, `Jose_Espinoza.txt`.

**O que falta:**
- Treinamento técnico estruturado e contínuo para o comercial.
- Material/apresentação de nível C-level com argumentação de TCO robusta.
- Expertise dedicada de marketing B2B complexo.
- Critério interno definido de para quem vender (mapa de stakeholder), não descoberto por tentativa e erro.
- Mudança de postura de reativa para proativa — reconhecida como necessária, ainda não incorporada.
- Processo formal de acompanhamento de propostas em aberto.

---

## 6. Financeiro, Risco & Custo
*Dinheiro — estrutura de capital, premissas de risco, custo de ineficiência.*

**Como é hoje:**
- O modelo é intensivo em capital e depende de uma única linha de crédito subsidiada (BNB). *"Você pega uma taxa cara com Itaú, o produto explode."* — **Daniel Garcia** (planilha, aba Desafios). Escalar exige aportes do porte do já feito (R$60 milhões) em curto espaço de tempo. — **Gustavo Moura** (planilha, aba Desafios).
- Premissas financeiras ficam desatualizadas e só são recalibradas de forma reativa — o frete foi modelado com média nacional sem diferenciação regional. *"a gente não distinguiu [o frete] por região (...) Foi mais um frete médio."* — **André**, `Time_Financeiro_Andre_Carol_Maria_Cecilia.txt`.
- Taxas de captação pioraram, aumentando a percepção de risco e o valor final do aluguel. — **Time do Financeiro** (planilha, aba Desafios): *"a gente não vem conseguindo atribuir a mesma taxa de juros de captação que André conseguiu no passado."*
- Custos de fricção interna já foram citados em valores concretos por pessoas diferentes, mas nunca consolidados num único lugar: ~R$10 mil de frete em alguns locais (**Andrea/Daniel Garcia**), de ~R$1 mil para R$5 mil/mês de dados por calibração errada do IoT (**Andrea**), ~R$100 mil de estouro do cap contratual de furto (**Daniel Garcia**).

**O que falta:**
- Diversificação de fontes de capital barato, hoje concentrada numa única linha.
- Rotina institucionalizada de recalibração periódica de premissas financeiras.
- Modelagem de frete diferenciada por região/rota.
- Consolidação dos três valores de fricção já citados isoladamente, num único lugar visível para quem decide.
- Plano de capital que sustente crescimento rápido sem depender de aporte pontual do acionista a cada salto de escala.

---

## 7. Relação com o Cliente
*Não "estamos falando com as pessoas certas" — mas o quanto a Moura realmente conhece a rotina/operação do cliente, e se personaliza ou trata todos igual.*

**Como é hoje:**
- O conhecimento profundo do cliente existe onde uma pessoa carrega esse conhecimento pessoalmente — não como prática organizacional. José Espinosa, que trabalhou 20+ anos dentro da própria estrutura que hoje atende como cliente (Vivo), descreve isso como método pessoal, não institucional: *"Eu conheço essa rotina dele. Porque eu estive lá mais de 20 anos da minha vida (...) Se puder, tiver uma sala lá, ficar lá dentro, entender essa rotina, respirar essas necessidades do cliente, tomar um cafezinho todos os dias (...) para sentir essa dor do cliente."* — **José Espinosa**, `Jose_Espinoza.txt`.
- O próprio entrevistado reconhece que, fora esse conhecimento pessoal, a postura da empresa é passiva por desconhecimento, e que isso já custou oportunidade: *"a gente, até por desconhecimento, eu sinto uma participação muito passiva (...) estou enxergando um monte de oportunidades que a gente está perdendo, que as coisas vão passando."* — **José Espinosa**, mesma transcrição.
- Perfis diferenciados por operadora já existem no radar comercial — Vivo eficiente/investidora, TIM aberta mas incomodada com ruído operacional, Claro conservadora e magoada por repricing passado (**Karina**, planilha aba Clientes) — mas, segundo a síntese do documento `13-visao-executiva-por-tema.md` (tema 5), a abordagem comercial usada hoje é praticamente a mesma para as três, apesar de reconhecidamente exigirem discursos diferentes.

**O que falta:**
- Institucionalizar o conhecimento sobre a rotina/operação do cliente — hoje existe só onde uma pessoa específica (por biografia pessoal) o carrega.
- Um processo real de imersão/proximidade com a rotina do cliente — hoje é aspiração de uma pessoa, não prática da empresa.
- Personalização de fato na abordagem por operadora, traduzindo o perfil que a Moura já sabe descrever em tratamento comercial diferente na prática.

---

## Critério usado para separar os blocos

Um bloco só existe separado dos outros se **o tipo de intervenção para resolver o problema for diferente**:
- **Produto & Tecnologia** se resolve reprojetando o artefato.
- **Operação de Campo** se resolve com logística, normativa e processo de execução.
- **Pessoas & Cultura** se resolve com liderança, retenção e valores — sobre como as pessoas se comportam.
- **Colaboração entre Áreas** se resolve com desenho organizacional, papéis e SLA — sobre como o sistema está desenhado, não sobre indivíduos.
- **Capacidade Comercial** se resolve com treinamento, material e mudança de método de venda.
- **Financeiro, Risco & Custo** se resolve com estrutura de capital e disciplina de modelagem.
- **Relação com o Cliente** se resolve aproximando a organização (não só um indivíduo) da rotina real de quem compra.

Casos de fronteira que exigiram decisão deliberada (documentados para você poder contestar se discordar):
- *IoT não ser plug-and-play* → Produto (falha de design), separado de *erro do técnico ao instalar* → Operação (falha de execução) — mesmo fenômeno observável (30-35% de erro), duas causas e dois remédios diferentes.
- *Gargalo de compras* → Operação (processo de abastecimento), não Financeiro, porque a causa citada é eficiência de processo, não modelagem de capital.
- *Cada instalação ser um projeto customizado* → Produto (falta de padronização de solução), não Comercial, porque a raiz é o desenho da oferta, não a habilidade de vender.
