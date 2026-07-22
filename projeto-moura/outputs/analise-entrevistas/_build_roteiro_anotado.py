#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import html as h

# ---------- Objetivos gerais (topo da página) ----------
OBJETIVOS_GERAIS = [
    "Entender como a gestão de energia e infraestrutura crítica dos sites funciona hoje, na prática, antes de qualquer apresentação de solução.",
    "Validar, na voz da própria operadora, as dores operacionais que a Moura já percebe internamente sobre o setor — furto, falta de visibilidade, sites legados, ruído de alarmes.",
    "Testar se a liberação de capital (CAPEX) é, de fato, o motivador central para migrar da compra de equipamento para um modelo de serviço contratado.",
    "Entender como a operadora contrata e avalia fornecedores críticos hoje, e o que tornaria um contrato de serviço de longo prazo aceitável.",
    "Investigar se a operadora pagaria por acesso a dados e inteligência preditiva sobre os sites, independentemente do hardware físico.",
    "Avaliar o peso real do risco regulatório (Anatel) e dos critérios de sustentabilidade nas decisões de investimento em energia.",
    "Mapear a relação entre energia e espaço físico dos sites (torreiras/redes neutras), e se faz sentido consolidar os dois fornecedores.",
    "Entender a visão de futuro da própria operadora sobre a gestão de energia dos sites, e identificar quem mais precisa estar envolvido numa decisão desse porte.",
]

NOTE_TOP = (
    "Esta é uma versão anotada do roteiro final (“Opção 1”) que vocês fecharam. Fizemos três ajustes pontuais, sinalizados "
    "no chat: (1) corrigimos a numeração do último bloco, que aparecia como “Bloco 9” no corpo do texto mas “Bloco 8” no "
    "sumário; (2) posicionamos a pergunta sobre o histórico da relação com a Moura, que estava sem lugar definido, no Bloco 4; "
    "(3) reformulamos a pergunta sobre dimensionamento de baterias (Bloco 3), que a própria autora já tinha marcado como "
    "precisando de revisão por induzir a resposta. Três hipóteses do conjunto original de 17 não têm teste direto nesta versão "
    "(segurança física vs. dados, monetização de capacidade ociosa, terceirizar o fardo operacional como argumento isolado) — "
    "não foram adicionadas sem validação."
)

# ---------- Blocks ----------
# Each: (num, title, objective_short, [ (qnum, question, [subitems], rationale_html, tag) ])
# tag: None | 'hipotese' | 'dor'

BLOCKS = [
    (0, "Apresentação e Contexto", "Mapear o papel do entrevistado e o momento atual da operadora, para calibrar a leitura de todas as respostas seguintes.", [
        ("1", "Me conta um pouco do seu papel — o que você é responsável dentro da operadora e o que passa pela sua mão quando o assunto é infraestrutura de rede e energia dos sites?", [],
         "Não testa uma hipótese específica — é uma pergunta de mapeamento. Serve para entender o alcance real de decisão da pessoa (o que ela decide, o que ela só influencia, o que não passa por ela), o que ajuda a interpretar o peso de tudo que ela disser a seguir e a identificar quem mais precisa ser ouvido depois.", None),
        ("2", "Como você descreveria, em poucas palavras, o atual momento da sua operadora em relação à expansão de rede (ex: 5G) e modernização de infraestrutura?", [],
         "Também não testa uma hipótese isolada — é uma pergunta de calibração. Uma operadora em expansão acelerada tende a ter urgências e critérios de decisão diferentes de uma operadora em consolidação ou contenção de custos. A resposta ajuda a interpretar corretamente as respostas dos blocos seguintes, principalmente as do Bloco 5 (CAPEX/OPEX).", None),
    ]),
    (1, "Como a Operação de Energia Funciona Hoje", "Entender, de forma aberta, como a rotina de monitoramento e manutenção de energia funciona hoje, antes de explorar dores específicas.", [
        ("3", "Hoje, como funciona a rotina de monitoramento e manutenção dos sites de vocês?",
         ["Quem é o time responsável", "Como está estruturado (papéis)", "Quais atividades estão envolvidas", "O que ocupa mais o tempo no dia a dia"],
         "Pergunta de mapeamento factual, sem hipótese associada diretamente. O objetivo é entender como a operação de energia realmente funciona hoje — quem faz o quê — antes de perguntar sobre qualquer dor ou problema específico. Essa base é o que permite interpretar com precisão as respostas do Bloco 2.", None),
        ("4", "Como vocês têm visibilidade do que está acontecendo em cada site?",
         ["Como a informação chega até você", "O que você consegue monitorar em tempo real"],
         "Prepara o terreno para duas hipóteses aprofundadas mais à frente: a de que a operadora pagaria por dados e inteligência preditiva sobre os sites (Bloco 6), e a de que a plataforma de monitoramento vale mais que o hardware físico em si. Aqui, ainda em tom de mapeamento, buscamos entender o ponto de partida real: o que a operadora já enxerga hoje.", "hipotese"),
    ]),
    (2, "Dores e Gargalos Operacionais", "Validar, na voz da operadora, as dores operacionais e regulatórias que a Moura já percebe internamente sobre o setor — sem presumir que são verdadeiras.", [
        ("5", "Quais são os problemas que aparecem com mais frequência quando o assunto é energia dos sites?",
         ["Quais dão mais trabalho", "Quais geram mais custo para resolver"],
         "Pergunta de controle aberta: não sugerimos nenhum problema específico, deixamos a operadora nomear livremente. O que ela citar espontaneamente é o sinal mais confiável de qual dor pesa mais na prática — e serve para conferir se as dores que a Moura já mapeou internamente (furto, falta de visibilidade, sites legados) realmente batem com o que a operadora sente, ou se existe alguma dor que a Moura ainda não tinha identificado.", "dor"),
        ("6", "Quando um problema de energia acontece em algum site, como você fica sabendo?",
         ["Como acontece esse processo", "Média de quanto tempo leva (SLA) — da detecção até a resolução", "Como decidem quais alertas ou chamados são prioridade"],
         "Dor interna testada: a Moura já percebe, pelas entrevistas internas, que as operadoras costumam operar sob um volume alto de alarmes, com dificuldade real de saber quais merecem atenção imediata. Essa pergunta verifica se isso é real para essa operadora, e mede o tempo médio entre detectar e resolver — um dado que, se for longo, reforça o valor de uma camada de monitoramento mais inteligente.", "dor"),
        ("7", "Nesse processo de investigar o problema, já aconteceu de vocês…",
         ["Descobrirem só depois de já terem causado um grande impacto? Como foi?", "Realizarem “visitas improdutivas” — enviarem o técnico a campo e descobrir que o problema não era de energia ou que a solução era outra? Como foi?"],
         "Testa duas dores internas ao mesmo tempo: (1) a falta de monitoramento preditivo — a operadora só percebe o problema depois que ele já causou impacto; e (2) o custo de mandar um técnico a campo para descobrir, já no local, que o problema era outro (uma “visita improdutiva”). Ambas já mapeadas internamente como gargalos recorrentes do setor, mas que precisam ser confirmadas na voz do cliente.", "dor"),
        ("8-9", "Como o vandalismo e o furto de baterias impactam a operação de vocês hoje? Atualmente, como vocês ficam sabendo que um site foi vandalizado ou teve baterias furtadas?",
         ["Como acontece esse processo — da descoberta até a reposição", "Quanto tempo costuma levar (SLA)"],
         "O furto de baterias é, segundo a própria imersão interna da Moura, a maior dor do setor — mas isso precisa ser confirmado pela operadora, não presumido. A pergunta testa o real impacto operacional do furto hoje, e principalmente como a operadora fica sabendo que ele aconteceu: se é avisada automaticamente, se só percebe quando a energia cai, ou se descobre por terceiros. Essa resposta é a evidência mais direta de que existe (ou não) uma lacuna de visibilidade que uma solução de telemetria resolveria.", "dor"),
        ("10", "Além do furto, vocês conseguem saber com antecedência que uma bateria está se degradando, ou só descobrem quando ela já falhou?",
         ["Como acontece esse processo de monitoramento"],
         "Testa a hipótese de que uma plataforma de inteligência de dados vale mais do que o hardware físico em si — aqui, pelo ângulo específico de saber com antecedência que uma bateria está degradando, em vez de só descobrir quando ela já falhou. Se a resposta for “só descobrimos quando falha”, é evidência forte a favor dessa hipótese.", "hipotese"),
        ("11", "O que acontece quando um site fica sem energia por mais tempo do que o backup aguenta?",
         ["Quem é acionado", "Quais são os impactos operacionais", "Quais são os impactos regulatórios"],
         "Funciona como ponte para a pergunta seguinte, sobre o peso regulatório. Aqui buscamos entender, de forma factual, o que realmente acontece quando o pior cenário se concretiza, e que tipo de consequência (operacional e regulatória) isso gera na prática, antes de perguntar diretamente sobre a Anatel.", None),
        ("12", "Quais exigências regulatórias da Anatel vocês monitoram hoje em relação à disponibilidade de rede? Como isso é acompanhado internamente?",
         ["Já aconteceu de vocês serem penalizados, notificados, ou chegarem perto disso, por indisponibilidade de rede relacionada a energia? Como foi?", "Como isso pesa nas decisões de investimento em energia dos sites?", "Existe algum tipo de consequência contratual para o fornecedor responsável (multa, desconto, outra)?"],
         "Hipótese testada: o argumento regulatório — o risco de multa da Anatel por indisponibilidade — engaja mais na decisão do que o argumento puramente financeiro (custo do equipamento). Buscamos primeiro um evento real (já foram penalizados ou chegaram perto?) como evidência mais forte do que uma opinião hipotética, e só depois perguntamos diretamente sobre o peso disso nas decisões de investimento.", "hipotese"),
    ]),
    (3, "Infraestrutura Física e Legado dos Sites", "Mapear a composição do parque de sites e testar se uma oferta de recompra destravaria a modernização de sites legados.", [
        ("13", "De uma forma geral, como é composto hoje o parque de sites de vocês?",
         ["“Idade”", "Tipo de instalação (ex.: greenfield, rooftop)", "São “padronizados” ou não", "Proporção de antigos x recentes (infraestrutura de backup)"],
         "Pergunta factual de mapeamento. Serve para confirmar (ou não) a percepção interna da Moura de que uma parte relevante do parque das operadoras já é “legado” — infraestrutura mais antiga que precisaria ser atualizada — antes de entrar no tema de recompra e sites legados nas perguntas seguintes.", None),
        ("14", "Quando vocês dimensionam a quantidade de baterias necessária para um novo site, como esse cálculo costuma ser feito, e existe algum tipo de margem de segurança aplicada?",
         [],
         "<strong>Pergunta reformulada</strong> em relação ao rascunho original (“vocês acabam comprando bateria a mais por segurança, deixando capital ocioso?”), que a própria autora já tinha sinalizado como precisando de revisão por induzir a resposta. Hipótese testada: existe uma tendência de superdimensionamento de baterias “por segurança”, gerando capital parado sem necessidade — um ponto de ineficiência que um modelo com telemetria e dimensionamento sob demanda poderia resolver. A versão usada aqui pergunta pelo processo de forma neutra, deixando a margem de segurança — se existir — emergir da resposta, sem sugerir que ela é excessiva.", "hipotese"),
        ("15", "Falando sobre os “sites legados” (parque já instalado), como vocês lidam com a atualização desses sites?",
         ["Como vocês pensam o ciclo de vida de um equipamento como bateria ou gabinete depois de instalado", "Existe um tempo mínimo esperado de uso antes de considerar substituição", "Quando um equipamento é de fato substituído ou um site desativado, o que normalmente acontece com o que foi removido", "Como é a logística de gerenciar as trocas e o descarte dos equipamentos velhos"],
         "Hipótese testada: uma oferta de recompra (a Moura comprar o ativo que a operadora já tem instalado, para depois alugar o serviço de volta) seria o mecanismo que destravaria a adoção do serviço nos sites já equipados — hoje a maior barreira de escala, segundo a imersão interna. O item sobre descarte verifica se a operadora já tem um canal próprio de revenda ou reaproveitamento do equipamento removido — o que mudaria completamente o valor percebido de uma proposta de recompra.", "hipotese"),
        ("16", "Como funciona a relação de vocês com quem administra o espaço físico dos sites (Torreiras)?",
         ["É o mesmo fornecedor que cuida da energia", "São sempre entidades diferentes", "Como funciona esse aluguel", "Quais são as vantagens e desvantagens dessa relação"],
         "Hipótese testada: faria sentido, do ponto de vista da operadora, que o mesmo fornecedor cuidasse do espaço físico do site (torreira) e da energia — ou ela prefere manter esses dois papéis separados. É a hipótese de que a Moura poderia se posicionar em parceria com torreiras/redes neutras em vez de vender diretamente à operadora.", "hipotese"),
        ("17", "Vocês já perceberam alguma vantagem ou desvantagem em ter fornecedores separados para espaço físico e para energia?", [],
         "Aprofunda a mesma hipótese da pergunta anterior, agora pedindo diretamente por uma avaliação da experiência — vantagem ou desvantagem — de manter os dois papéis separados.", "hipotese"),
    ]),
    (4, "Relação com Fornecedores e Contratos de Longo Prazo", "Entender como a operadora contrata e avalia fornecedores críticos hoje, testando a disposição a modelos de contrato mais longos e baseados em resultado.", [
        ("18", "Como funciona hoje a contratação de fornecedores para a infraestrutura dos sites?",
         ["Tem um fornecedor principal por área ou vários dividindo a mesma entrega", "Os contratos tendem a ser curtos ou longos (de mais ou menos quanto tempo)"],
         "Pergunta de mapeamento factual, sem hipótese isolada — estabelece a régua de comparação (quantos fornecedores, que tipo de contrato) antes das perguntas mais específicas sobre CAPEX/OPEX no Bloco 5.", None),
        ("19", "Especificamente para energia e backup — bateria, retificador, gerador, monitoramento — quantos fornecedores diferentes estão envolvidos hoje?",
         ["O que funciona bem ao gerenciar esses fornecedores separadamente", "O que gera mais atrito"],
         "Hipótese testada: a operadora teria apetite por consolidar a gestão de toda a energia do site num único parceiro, em vez de lidar com vários fornecedores fragmentados. A resposta sobre o que gera mais atrito ao gerenciar separadamente é a evidência mais direta dessa hipótese.", "hipotese"),
        ("20", "Como é essa relação com os fornecedores de energia e equipamentos hoje?",
         ["O que você espera de um fornecedor", "O que costuma gerar insatisfação"],
         "Pergunta aberta que antecede, de propósito, a pergunta sobre o histórico com a Moura especificamente (posicionada logo a seguir). Deixar a operadora falar livremente sobre expectativas e frustrações com fornecedores em geral, antes de perguntar sobre a Moura por nome, evita que a resposta seguinte seja apenas uma reação defensiva ou socialmente esperada.", None),
        ("20a", "Como você descreveria o histórico da relação de vocês com a Moura até aqui?", [],
         "<strong>Pergunta reposicionada</strong> — no rascunho original estava sem lugar definido. Decidimos colocá-la aqui, logo após a operadora falar abertamente sobre fornecedores em geral. Hipótese testada: a experiência recente da operadora com a venda tradicional de bateria da Moura (não o serviço) pode estar prejudicando a disposição de negociar um contrato de serviço de longo prazo — especialmente relevante em relações mais desgastadas. É uma pergunta aberta e neutra: não presume que existe desgaste, deixa a operadora trazer isso com as próprias palavras.", "hipotese"),
        ("21", "Quando vocês precisam contratar ou renovar algo relacionado à infraestrutura de energia, como funciona esse processo?",
         ["Quem está envolvido na decisão", "O que pesa na hora de escolher um fornecedor", "Quais critérios costumam usar", "Além do preço do equipamento, quais custos entram na conta? (manutenção, visitas técnicas, reposição por furto, outros)"],
         "Hipótese testada: a comparação de propostas hoje é feita majoritariamente pelo preço do equipamento (“hard saving”), sem considerar custos indiretos como manutenção, visitas técnicas e reposição por furto — o que faz uma proposta de serviço completo parecer mais cara do que realmente é quando comparada de forma completa (TCO). O último item, sobre quais custos entram na conta, é o teste mais direto dessa hipótese.", "hipotese"),
        ("22", "Esses custos indiretos costumam estar no mesmo orçamento que aprova a compra do equipamento, ou ficam em áreas diferentes?", [],
         "Aprofunda a hipótese anterior, testando a causa estrutural: se a comparação incompleta entre comprar e contratar acontece por escolha consciente da operadora, ou porque diferentes áreas internas calculam esses custos separadamente e nunca são somados numa única conta.", "hipotese"),
        ("23", "Como vocês enxergam contratos de fornecimento mais longos (5, 8, 10 anos) nessa área?",
         ["Existe um posicionamento padrão ou depende do caso", "O que costuma ser indispensável para assinar um contrato de longo prazo em fornecimento crítico?"],
         "Hipótese testada: operadoras resistem a contratos engessados de longo prazo (o modelo de serviço da Moura costuma ser de 10 anos) e teriam mais disposição a assinar se determinadas condições estivessem garantidas. A pergunta não sugere quais seriam essas condições — deixa a operadora nomear o que seria indispensável, o que pode revelar mecanismos como cláusulas de saída sem que a Moura precise propô-los primeiro.", "hipotese"),
        ("24", "Em contratos que vocês têm hoje, existe algum caso em que o pagamento está atrelado a resultado ou nível de serviço — não só à entrega do produto?",
         ["Já negociaram algum tipo de garantia de desempenho com penalidade para o fornecedor?"],
         "Hipótese testada: a operadora estaria mais disposta a contratar um modelo em que paga pela garantia de que o site vai continuar funcionando (disponibilidade), e não pelo equipamento em si — um modelo de “tolling”. Verificamos se esse tipo de estrutura de pagamento por resultado já é praticada em outros contratos, o que indicaria que o conceito não é estranho à cultura de compra da operadora.", "hipotese"),
    ]),
    (5, "CAPEX, OPEX e Modelos de Serviço", "Testar se a liberação de capital (CAPEX) é, de fato, o motivador central para migrar da compra de equipamento para um modelo de serviço.", [
        ("25", "Como funciona a aprovação de investimento para energia e backup dos sites?",
         ["Já aconteceu de um projeto ser adiado ou reduzido de escopo por falta de orçamento? Como foi?"],
         "Testa a pré-condição da hipótese central deste bloco: para que a conversão de CAPEX em OPEX tenha valor real, o CAPEX precisa ser, de fato, um recurso escasso e disputado dentro da operadora. Um projeto real que foi adiado ou reduzido por falta de orçamento é a evidência mais concreta possível — muito mais forte do que uma resposta hipotética.", "hipotese"),
        ("26", "Como vocês pensam hoje sobre a decisão de comprar um ativo/equipamento versus contratar um serviço?",
         ["Quais vantagens e desvantagens vocês veem entre os dois modelos", "Existe alguma preferência clara ou depende do caso", "Já existe alguma área da infraestrutura de vocês que funciona em modelo de serviço contratado? Se sim, como foi a experiência e o que mudou na operação?"],
         "Hipótese central testada: a conversão de CAPEX para OPEX é o principal valor que levaria a operadora a preferir contratar um serviço de energia em vez de comprar o equipamento. O item sobre se já existe alguma área funcionando em modelo de serviço é o teste mais forte — um precedente real na própria operadora vale mais como evidência do que uma resposta sobre o que ela “acha” que prefere.", "hipotese"),
        ("27", "Em outras áreas da operação de vocês, já aconteceu de terceirizarem algo que antes era gerenciado internamente?",
         ["Se sim, o que motivou e como foi a experiência?"],
         "Testa a mesma hipótese de preferência por serviço, mas por um ângulo comportamental, fora do domínio de energia: se a operadora já demonstrou, na prática, disposição a terceirizar algo que antes gerenciava internamente, isso é evidência de que a lógica de servitização já é aceita pela cultura da empresa.", "hipotese"),
        ("28", "Como a empresa decide, de forma geral, o que manter sob controle direto e o que pode ser delegado a terceiros?",
         ["O que costuma pesar mais quando vocês avaliam se um fornecedor pode assumir uma responsabilidade crítica — histórico, estrutura da empresa, cláusulas contratuais, outra coisa?"],
         "Hipótese testada: existe um medo real de perder o domínio da operação ao terceirizar uma função crítica para um único fornecedor — um possível bloqueio cultural à servitização. Busca o princípio geral de decisão da empresa, ainda não aplicado a energia, para entender os critérios reais antes de qualquer aplicação específica.", "hipotese"),
        ("29", "E dentro do que envolve cuidar da energia dos sites…",
         ["Quais partes vocês fariam questão de manter internamente, mesmo que pudessem terceirizar, e por quê?"],
         "Aplica a mesma hipótese do medo de perder domínio especificamente ao caso de energia dos sites — pode revelar, de forma concreta, onde estaria a linha que a operadora não abriria mão de controlar, mesmo com uma proposta de serviço completo da Moura.", "hipotese"),
        ("30", "Se hoje vocês tivessem esse capital livre para outra finalidade, para onde ele provavelmente iria?", [],
         "Este é o teste mais direto do núcleo real da hipótese de CAPEX→OPEX: a conversão só tem valor estratégico de verdade se esse capital liberado tiver um destino mais valioso — como investir na expansão da própria rede (5G). Se a resposta for vaga ou não houver destino claro, o benefício seria apenas contábil, não estratégico, o que enfraquece essa hipótese como argumento de venda.", "hipotese"),
    ]),
    (6, "Telemetria e Inteligência de Dados", "Entender a maturidade analítica da operadora e testar a disposição a pagar por dados e inteligência sobre os sites.", [
        ("31", "De forma geral, como a empresa hoje usa dados e análises para tomar decisões operacionais? Existe uma cultura de dados ou ainda é algo em construção?", [],
         "Pergunta de mapeamento, sem hipótese isolada — mede a maturidade analítica geral da operadora antes de perguntar especificamente sobre dados de energia. Ajuda a calibrar até que ponto a operadora já está pronta para valorizar uma proposta baseada em inteligência de dados.", None),
        ("32", "O que vocês fazem quando precisam saber algo específico sobre um site?",
         ["Como essa informação chega até vocês hoje", "Quanto de esforço dá", "Quanto tempo leva", "O que poderia ser melhorado"],
         "Hipótese testada: existe uma dor real e mensurável de acesso à informação sobre os sites hoje — que poderia ser resolvida por uma camada de telemetria contínua. A pergunta não menciona monitoramento remoto ou qualquer solução; mede o esforço e o tempo reais que a operadora já gasta hoje, deixando a dor (ou a ausência dela) aparecer nos próprios números.", "hipotese"),
        ("33", "Quais tipos de informação sobre os sites vocês gostariam de ter hoje, mas não têm?",
         ["O que mudaria na tomada de decisão se você tivesse acesso a isso"],
         "Hipótese testada: a operadora pagaria por dados inteligentes e monitoramento contínuo sobre os sites. Pergunta aberta — não sugere “telemetria” como resposta, deixa a própria operadora nomear a informação que falta, o sinal mais confiável de uma necessidade real e não induzida.", "hipotese"),
        ("34", "Se existisse uma forma de ter acesso constante a esse tipo de informação, o que isso mudaria na forma como vocês tomam decisão sobre os sites?", [],
         "Teste final e indireto da mesma hipótese sobre dados: mede o valor percebido de ter acesso constante à informação, sem perguntar diretamente “vocês pagariam por isso?” — a resposta sobre o que mudaria na tomada de decisão é uma forma indireta e mais confiável de medir disposição a pagar.", "hipotese"),
    ]),
    (7, "Sustentabilidade", "Entender se critérios de sustentabilidade já são fator eliminatório na escolha de fornecedores, ou ainda um tema secundário.", [
        ("35", "Como critérios de sustentabilidade entram na avaliação de fornecedores?",
         ["É algo formal com peso definido, ou ainda é mais informal", "Já aconteceu de um fornecedor, em qualquer categoria, perder pontos ou ser desclassificado por não atender a algum critério ambiental ou social?"],
         "Hipótese testada: critérios de sustentabilidade e ESG já viraram um critério eliminatório (não apenas um diferencial) nos processos de compra de infraestrutura crítica. O item sobre um fornecedor já ter sido desclassificado busca um evento real como evidência — muito mais forte do que perguntar se o tema “é importante”.", "hipotese"),
        ("36", "Especificamente para equipamentos de energia/bateria, existe alguma exigência relacionada a descarte, reciclagem ou origem do material?",
         ["Essas exigências vêm de uma política local, ou de diretrizes globais da matriz/grupo?"],
         "Aprofunda a mesma hipótese especificamente para a categoria de energia e bateria — a mais relevante para a proposta da Moura (que já opera com logística reversa 100% reciclável). O item sobre política local ou global é informação estratégica: indica com quem a Moura precisaria argumentar para tornar esse critério um diferencial de peso.", "hipotese"),
    ]),
    (8, "Visão de Futuro", "Fechar a conversa entendendo prioridades e a visão de futuro da própria operadora, sem sugerir a proposta da Moura.", [
        ("37", "Se você pudesse resolver um problema da infraestrutura de energia hoje que tiraria um peso da sua operação, o que seria?", [],
         "Pergunta de fechamento generativa, sem hipótese específica associada — funciona como uma síntese de tudo que foi conversado. Deixar a operadora priorizar livremente, sem qualquer sugestão prévia da Moura, é o teste final e mais honesto de qual dor realmente pesa mais depois de toda a conversa.", None),
        ("38", "Como você enxerga a gestão de energia nos sites daqui a alguns anos?",
         ["O que você acha que vai mudar", "O que você gostaria que fosse diferente do que é hoje"],
         "Pergunta prospectiva aberta que pode revelar espontaneamente conceitos como monetização de dados, geração própria de energia ou modelos de serviço mais avançados — validando quais hipóteses de futuro já estão na cabeça da própria operadora, antes mesmo de a Moura apresentar qualquer proposta.", None),
    ]),
]

# ---------- Rendering ----------

def render_objetivos_gerais():
    return "".join(f"<li>{h.escape(o)}</li>" for o in OBJETIVOS_GERAIS)

def render_blocos_overview():
    out = []
    for num, title, obj, _q in BLOCKS:
        out.append(f'''<div class="bloco-card">
            <div class="bloco-number">Bloco {num}</div>
            <div class="bloco-name">{h.escape(title)}</div>
            <div class="bloco-desc">{h.escape(obj)}</div>
        </div>''')
    return "\n".join(out)

def render_subitems(items):
    if not items:
        return ""
    lis = "".join(f"<li>{h.escape(i)}</li>" for i in items)
    return f'<ul class="psub-list">{lis}</ul>'

def render_question(qnum, text, subitems, rationale, tag):
    tag_html = ""
    if tag == "hipotese":
        tag_html = '<span class="origem-tag origem-hipotese">Testa uma hipótese</span>'
    elif tag == "dor":
        tag_html = '<span class="origem-tag origem-dor">Valida dor interna</span>'
    return f'''<li class="pergunta-item">
        <span class="pnum">{h.escape(str(qnum))}.</span>
        <div class="pcontent">
            <div class="ptext">{h.escape(text)}{tag_html}</div>
            {render_subitems(subitems)}
            <div class="rationale"><span class="rationale-label">Por que essa pergunta:</span> {rationale}</div>
        </div>
    </li>'''

def render_roteiro():
    out = []
    for num, title, obj, questions in BLOCKS:
        qitems = "".join(render_question(qn, txt, sub, rat, tag) for qn, txt, sub, rat, tag in questions)
        out.append(f'''<div class="bloco" id="bloco-{num}">
            <div class="bloco-header">
                <span class="bloco-badge">Bloco {num}</span>
                <div>
                    <div class="bloco-header-title">{h.escape(title)}</div>
                    <div class="bloco-subtitle">{h.escape(obj)}</div>
                </div>
            </div>
            <ul class="perguntas-list">{qitems}</ul>
        </div>''')
    return "\n".join(out)

TEMPLATE = r'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Roteiro de Entrevista Anotado — Fase 2 (Operadoras) | MJV + Moura Energia</title>
    <style>
        @font-face{ font-family:'Space Grotesk'; font-style:normal; font-weight:400; font-display:swap; src:url(data:font/ttf;base64,{{SG400}}) format('truetype'); }
        @font-face{ font-family:'Space Grotesk'; font-style:normal; font-weight:500; font-display:swap; src:url(data:font/ttf;base64,{{SG500}}) format('truetype'); }
        @font-face{ font-family:'Space Grotesk'; font-style:normal; font-weight:600; font-display:swap; src:url(data:font/ttf;base64,{{SG600}}) format('truetype'); }
        @font-face{ font-family:'Space Grotesk'; font-style:normal; font-weight:700; font-display:swap; src:url(data:font/ttf;base64,{{SG700}}) format('truetype'); }
        @font-face{ font-family:'Archivo'; font-style:normal; font-weight:300; font-display:swap; src:url(data:font/ttf;base64,{{ARC300}}) format('truetype'); }
        @font-face{ font-family:'Archivo'; font-style:normal; font-weight:400; font-display:swap; src:url(data:font/ttf;base64,{{ARC400}}) format('truetype'); }
        @font-face{ font-family:'Archivo'; font-style:normal; font-weight:500; font-display:swap; src:url(data:font/ttf;base64,{{ARC500}}) format('truetype'); }
        @font-face{ font-family:'Archivo'; font-style:normal; font-weight:600; font-display:swap; src:url(data:font/ttf;base64,{{ARC600}}) format('truetype'); }
        @font-face{ font-family:'Archivo'; font-style:italic; font-weight:400; font-display:swap; src:url(data:font/ttf;base64,{{ARC400I}}) format('truetype'); }

        :root {
            --impulso: #6200BE;
            --insight: #4B238D;
            --estrutura: #2A005D;
            --enfase: #1CB78D;
            --aeris: #EEE7FD;
            --lumina: #F6F3FE;
            --dark: #1E2336;
            --branco: #FFFFFF;
            --bloco-bg: #F8F9FC;
        }
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Archivo', sans-serif; background: #F0F2F8; color: var(--dark); font-size: 14px; line-height: 1.6; }

        .page-header {
            background: var(--estrutura); color: white; padding: 36px 48px 28px;
            display: flex; justify-content: space-between; align-items: flex-end; flex-wrap: wrap; gap: 16px;
        }
        .page-header-left h1 { font-family: 'Space Grotesk', sans-serif; font-size: 22px; font-weight: 700; text-transform: uppercase; letter-spacing: -0.3px; margin-bottom: 6px; }
        .page-header-left p { font-size: 13px; opacity: 0.7; }
        .page-header-right { font-family: 'Space Grotesk', sans-serif; font-size: 12px; opacity: 0.6; text-align: right; }

        .tab-nav {
            display: flex; background: var(--branco); border-bottom: 1px solid rgba(0,0,0,0.08);
            padding: 0 48px; position: sticky; top: 0; z-index: 100; box-shadow: 0 2px 8px rgba(0,0,0,0.06);
            overflow-x: auto; flex-wrap: nowrap;
        }
        .tab-nav a {
            padding: 14px 18px; font-family: 'Space Grotesk', sans-serif; font-size: 11px; font-weight: 700;
            text-transform: uppercase; letter-spacing: 0.6px; color: #888; text-decoration: none; white-space: nowrap;
            border-bottom: 3px solid transparent;
        }
        .tab-nav a:hover { color: var(--impulso); border-bottom-color: var(--impulso); }

        .main { max-width: 960px; margin: 0 auto; padding: 36px 24px 80px; }

        .note-box-top {
            background: #fffbeb; border: 1px solid #fde68a; border-radius: 12px; padding: 18px 22px;
            margin-bottom: 24px; font-size: 13px; color: #78350f; line-height: 1.7;
        }
        .note-box-top strong { font-weight: 700; }

        .objetivos-box { background: var(--branco); border-radius: 12px; padding: 24px 28px; margin-bottom: 24px; border: 1px solid rgba(0,0,0,0.06); }
        .objetivos-title {
            font-family: 'Space Grotesk', sans-serif; font-size: 12px; font-weight: 700; text-transform: uppercase;
            letter-spacing: 1.2px; margin-bottom: 14px; padding-bottom: 10px; border-bottom: 2px solid var(--impulso); color: var(--impulso);
        }
        .obj-list { list-style: none; }
        .obj-list li { padding: 8px 0; font-size: 13.5px; line-height: 1.55; border-bottom: 1px solid rgba(0,0,0,0.05); padding-left: 20px; position: relative; }
        .obj-list li:last-child { border-bottom: none; }
        .obj-list li::before { content: '\2014'; position: absolute; left: 0; color: var(--impulso); font-size: 12px; }

        .blocos-overview { display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 10px; margin-bottom: 28px; }
        .bloco-card { background: var(--branco); border-radius: 10px; padding: 16px; border: 1px solid rgba(0,0,0,0.06); }
        .bloco-number { font-family: 'Space Grotesk', sans-serif; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.8px; margin-bottom: 6px; color: var(--impulso); }
        .bloco-name { font-family: 'Space Grotesk', sans-serif; font-size: 12.5px; font-weight: 700; text-transform: uppercase; color: var(--estrutura); line-height: 1.3; margin-bottom: 4px; }
        .bloco-desc { font-size: 11px; color: #777; line-height: 1.4; }

        .roteiro-section { background: var(--branco); border-radius: 14px; padding: 28px 32px; margin-bottom: 20px; border: 1px solid rgba(0,0,0,0.06); }

        .bloco { margin-bottom: 34px; scroll-margin-top: 60px; }
        .bloco-header { display: flex; align-items: flex-start; gap: 12px; margin-bottom: 16px; padding-bottom: 12px; border-bottom: 1px solid rgba(0,0,0,0.08); }
        .bloco-badge {
            font-family: 'Space Grotesk', sans-serif; font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.8px;
            padding: 4px 12px; border-radius: 20px; white-space: nowrap; background: var(--aeris); color: var(--impulso); margin-top: 2px;
        }
        .bloco-header-title { font-family: 'Space Grotesk', sans-serif; font-size: 15px; font-weight: 700; text-transform: uppercase; color: var(--estrutura); margin-bottom: 3px; }
        .bloco-subtitle { font-size: 12.5px; color: #555; font-style: italic; line-height: 1.5; }

        .perguntas-list { list-style: none; }
        .pergunta-item { display: flex; gap: 14px; padding: 16px 0; border-bottom: 1px solid rgba(0,0,0,0.05); }
        .pergunta-item:last-child { border-bottom: none; }

        .pnum { font-family: 'Space Grotesk', sans-serif; font-size: 13px; font-weight: 700; min-width: 32px; padding-top: 1px; color: var(--impulso); }
        .pcontent { flex: 1; }
        .ptext { font-size: 14.5px; line-height: 1.55; color: var(--dark); font-weight: 500; }

        .psub-list { list-style: none; margin: 8px 0 0; }
        .psub-list li { font-size: 12.5px; color: #555; padding: 3px 0 3px 16px; position: relative; line-height: 1.45; }
        .psub-list li::before { content: '\2013'; position: absolute; left: 0; color: #aaa; }

        .rationale {
            font-size: 12.5px; color: #555; margin-top: 10px; line-height: 1.6; background: var(--bloco-bg);
            border-left: 3px solid var(--enfase); padding: 10px 14px; border-radius: 2px;
        }
        .rationale-label { font-family: 'Space Grotesk', sans-serif; font-weight: 700; text-transform: uppercase; font-size: 10px; letter-spacing: 0.5px; color: var(--enfase); display: block; margin-bottom: 4px; }

        .origem-tag {
            display: inline-block; font-size: 10px; font-family: 'Space Grotesk', sans-serif; font-weight: 700;
            text-transform: uppercase; letter-spacing: 0.5px; padding: 2px 8px; border-radius: 4px; margin-left: 8px; vertical-align: middle;
        }
        .origem-hipotese { background: #dbeafe; color: #0046C1; }
        .origem-dor { background: #fef3c7; color: #92400e; }

        footer { max-width: 960px; margin: 0 auto; padding: 8px 24px 60px; font-size: 11px; color: #888; }

        @media print {
            .tab-nav { display: none; }
            body { background: white; font-size: 12px; }
        }
        @media (max-width: 600px) {
            .main { padding: 20px 16px 60px; }
            .roteiro-section { padding: 20px 18px; }
        }
    </style>
</head>
<body>

<div class="page-header">
    <div class="page-header-left">
        <h1>Roteiro de Entrevista Anotado — Fase 2</h1>
        <p>MJV Technology & Innovation · Projeto Moura Energia | Energia como Serviço · Conversa com as Operadoras (Opção 1)</p>
    </div>
    <div class="page-header-right">
        SP-00028<br>9 blocos · 38 perguntas · hipóteses e dores sinalizadas
    </div>
</div>

<div class="tab-nav">
    <a href="#objetivos">Objetivos Gerais</a>
    <a href="#bloco-0">Bloco 0</a>
    <a href="#bloco-1">Bloco 1</a>
    <a href="#bloco-2">Bloco 2</a>
    <a href="#bloco-3">Bloco 3</a>
    <a href="#bloco-4">Bloco 4</a>
    <a href="#bloco-5">Bloco 5</a>
    <a href="#bloco-6">Bloco 6</a>
    <a href="#bloco-7">Bloco 7</a>
    <a href="#bloco-8">Bloco 8</a>
</div>

<div class="main">

    <div class="note-box-top">
        <strong>Nota sobre esta versão:</strong> __NOTE_TOP__
    </div>

    <div class="objetivos-box" id="objetivos">
        <div class="objetivos-title">Objetivos Gerais da Entrevista</div>
        <ul class="obj-list">__OBJETIVOS_GERAIS__</ul>
    </div>

    <div class="blocos-overview">__BLOCOS_OVERVIEW__</div>

    <div class="roteiro-section" id="roteiro">
        __ROTEIRO__
    </div>

</div>

<footer>
    Fontes: roteiro final definido pelo time (“Fase 2 — Conversa com as Operadoras: Hipóteses e Roteiro”, Opção 1), hipóteses consolidadas (<span style="font-family:'Space Grotesk',sans-serif">Lista de hipóteses - Consolidadas.docx</span>) e dores percebidas na imersão interna (documentos <span style="font-family:'Space Grotesk',sans-serif">00</span> a <span style="font-family:'Space Grotesk',sans-serif">17</span> do repositório).
</footer>

</body>
</html>
'''

out = (TEMPLATE
       .replace("__NOTE_TOP__", NOTE_TOP)
       .replace("__OBJETIVOS_GERAIS__", render_objetivos_gerais())
       .replace("__BLOCOS_OVERVIEW__", render_blocos_overview())
       .replace("__ROTEIRO__", render_roteiro())
       )

# add id anchors to bloco divs
import re
def add_ids(match):
    return match.group(0)

with open("roteiro-v3-template.html", "w", encoding="utf-8") as f:
    f.write(out)

print("wrote roteiro-v3-template.html, size:", len(out))
