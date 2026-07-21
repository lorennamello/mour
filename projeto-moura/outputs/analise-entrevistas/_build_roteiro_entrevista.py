#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import html

def esc(s):
    return s

# ---------- Shared question bank ----------
# Each block: (num, title, subtitle, [ (text, objective, tag) ])
# tag: None | ('hipotese', 'H1.1') | ('dor', None)

BLOCKS = [
    (1, "Contexto e Organização Atual", "Mapear como a operadora decide hoje, sem induzir resposta", [
        ("Como funciona hoje a gestão de energia/backup dos seus sites — quem participa de cada etapa (especificação, compra, instalação, manutenção, monitoramento)?",
         "Mapear a estrutura de decisão real, sem induzir nenhuma resposta.", None),
        ("Me conta sobre a última vez que algo deu errado na energia de um site — o que aconteceu, como vocês ficaram sabendo, e como foi resolvido?",
         "Captura comportamento real, útil para cruzar depois com as dores do Bloco 2.", None),
        ("Quais são hoje os maiores problemas ou frustrações que vocês têm com a infraestrutura de energia dos sites?",
         "Pergunta de controle aberta — o que surge espontaneamente é o sinal mais forte de prioridade real.", None),
    ]),
    (2, "Validação das Dores Operacionais Percebidas", "Dores identificadas na imersão interna da Moura — testadas aqui sem presumir que são verdadeiras", [
        ("Se eu pedisse para saber quantas baterias estão instaladas e funcionando corretamente num site específico agora, quanto tempo levaria para vocês responderem com confiança?",
         "Testa o “apagão de inventário” percebido internamente, sem presumir que ele existe.", ("dor", None)),
        ("Quando uma bateria é furtada, qual é o processo desde a descoberta até a reposição funcionando de novo no site? Quanto tempo isso costuma levar?",
         "Valida (ou não) a burocracia de reposição de até 90 dias identificada internamente.", ("dor", None)),
        ("Quantos alertas ou chamados relacionados a energia a equipe de vocês recebe, em média, por dia ou semana? Como vocês decidem quais merecem atenção imediata?",
         "Testa a sobrecarga de alarmes/falsos positivos sem citar os números que a Moura já tem internamente.", ("dor", None)),
        ("Hoje, vocês conseguem saber com antecedência que uma bateria está degradando, ou só descobrem quando ela já falhou?",
         "Testa se o monitoramento do cliente é reativo (binário) ou já tem componente preditivo.", ("dor", None)),
        ("O espaço físico disponível nos sites já foi um fator limitante em algum projeto? Como isso é resolvido hoje?",
         "Valida a dor de m² cobrado pelas torreiras, percebida internamente.", ("dor", None)),
        ("Quando um problema de energia em um site chega a afetar o cliente final, quantas áreas diferentes da empresa costumam ser acionadas até ele ser resolvido?",
         "Valida a dor de departamentalização/conflito entre áreas, sem perguntar diretamente sobre conflito.", ("dor", None)),
        ("Do total de sites que vocês têm hoje, que proporção você diria que já tem infraestrutura de backup mais antiga ou desatualizada?",
         "Valida a percepção interna de que uma fatia grande do parque é “legado”.", ("dor", None)),
    ]),
    (3, "Modelo Financeiro e Contratual", "Testa CAPEX/OPEX, hard saving, disponibilidade e flexibilidade de prazo", [
        ("Como funciona o processo orçamentário para investimento em infraestrutura de energia dos sites?",
         "Estabelece se CAPEX é, de fato, um recurso escasso e disputado na empresa como um todo.", ("hipotese", "H1.1")),
        ("Se hoje vocês tivessem esse capital livre para outra finalidade, para onde ele provavelmente iria?",
         "Testa o motor real da hipótese: CAPEX→OPEX só tem valor se libera capital para algo mais valioso.", ("hipotese", "H1.1")),
        ("Pode me contar sobre a última vez que vocês compararam propostas de dois fornecedores de equipamento de energia/backup? O que fez uma proposta ganhar da outra?",
         "Decisão real e recente — evita a resposta de princípio que pode não refletir a prática.", ("hipotese", "H1.6")),
        ("Hoje, quando um site fica indisponível por falta de energia, existe algum tipo de consequência contratual para o fornecedor responsável (multa, desconto, outra)?",
         "Descobre se já existe cultura de responsabilização por resultado especificamente em energia.", ("hipotese", "H1.2")),
        ("Já tiveram algum contrato de longo prazo que, com o tempo, deixou de fazer sentido pela mudança na necessidade real? O que aconteceu?",
         "Evento real de desalinhamento entre contrato e necessidade — sinal direto da barreira de prazo engessado.", ("hipotese", "H1.5")),
    ]),
    (4, "Sites Legados e Transição de Ativos", "Testa se a recompra (buy-and-lease-back) destravaria o parque já instalado", [
        ("Como vocês pensam o ciclo de vida de um equipamento como bateria ou gabinete depois de instalado — existe um tempo mínimo esperado de uso antes de considerar substituição?",
         "Testa a pré-condição da barreira: se não existe lógica de “aproveitar o que já paguei”, a barreira provavelmente não se sustenta.", ("hipotese", "H1.3")),
        ("Já aconteceu de vocês quererem trocar de fornecedor desse tipo de equipamento mesmo com o atual ainda funcionando bem? O que motivou, e o que fizeram com o que já estava instalado?",
         "Pede um caso real em que a tensão “equipamento ainda bom vs. trocar de fornecedor” já aconteceu.", ("hipotese", "H2.3")),
        ("E quando um equipamento é de fato substituído ou um site desativado, o que normalmente acontece com o que foi removido?",
         "Testa se já existe canal próprio de revenda/sucata — o que mudaria a proposta de recompra.", ("hipotese", "H1.3")),
    ]),
    (5, "Confiança e Dependência de Fornecedor Único", "Testa o medo de perder domínio da operação e o peso do histórico de relação", [
        ("Vocês já tiveram alguma experiência — boa ou ruim — terceirizando uma parte crítica da operação para um único fornecedor? O que aprenderam com isso?",
         "Experiência real e específica — normalmente revela a origem real de qualquer receio.", ("hipotese", "H2.4")),
        ("Quando avaliam um fornecedor para um contrato novo e maior, o desempenho dele em contratos menores ou anteriores que já existem entra na decisão?",
         "Princípio geral, sem mencionar a Moura — mede se a lógica “histórico contamina decisão” existe.", ("hipotese", "H6.1")),
        ("Como você descreveria o histórico da relação de vocês com a Moura até aqui?",
         "Pergunta aberta e neutra — não presume desgaste, deixa a pessoa trazer isso com as próprias palavras.", ("hipotese", "H6.1")),
    ]),
    (6, "Físico vs. Dados/Plataforma vs. Gestão Total", "Testa qual das duas hipóteses divergentes domina, e o apetite por consolidação de fornecedores", [
        ("Pensando nos últimos incidentes relacionados à energia dos sites, o que aconteceu, e o que vocês só descobriram depois de já ter causado impacto?",
         "Evento real recente — a resposta espontânea sobre “o que só descobrimos depois” já sinaliza onde está a maior dor.", ("hipotese", "H2.1 / H4.2")),
        ("Se vocês tivessem que escolher entre investir em melhorar a visibilidade sobre os sites ou reforçar a proteção física dos equipamentos, sem poder fazer as duas coisas ao mesmo tempo, o que teria prioridade?",
         "Cenário de recurso escasso — reduz a tendência de responder “as duas são importantes”.", ("hipotese", "H2.1 / H4.2")),
        ("Pensando nos fornecedores de energia que vocês já tiveram, o que diferenciava o melhor do pior — mais o produto em si, ou como ele era acompanhado depois de instalado?",
         "Comparação baseada em experiência real, testa se a plataforma vale mais que o hardware.", ("hipotese", "H3.1")),
        ("Especificamente para a energia de um site — bateria, retificador, climatização, gerador, monitoramento — quantos fornecedores diferentes estão envolvidos hoje?",
         "Estabelece a linha de base real antes de qualquer pergunta sobre consolidação de fornecedores.", ("hipotese", "H3.2")),
    ]),
    (7, "Regulatório, Monetização e ESG", "Testa o peso do argumento Anatel, o apetite por monetização de energia e critérios de sustentabilidade", [
        ("O risco de multa da Anatel por indisponibilidade de rede pesa nas decisões de investimento em energia dos sites?",
         "Mede se compliance regulatório já é um critério ativo de decisão.", ("hipotese", "H1.4")),
        ("Existe algum uso hoje, ou em estudo, para a capacidade de energia instalada nos sites além do backup da própria rede?",
         "Testa a maturidade da operadora para pensar em monetização de capacidade ociosa (VPP).", ("hipotese", "H4.1")),
        ("Quais critérios de sustentabilidade, se algum, aparecem hoje nos editais ou processos de compra de vocês?",
         "Testa se ESG já é critério eliminatório ou ainda é diferencial opcional.", ("hipotese", "H5.1")),
    ]),
    (8, "Ecossistema: Torreiras e Redes Neutras", "Testa se faz sentido consolidar energia e espaço físico no mesmo fornecedor", [
        ("Hoje, como funciona a relação de vocês com quem administra o espaço físico dos sites — é o mesmo fornecedor que cuida da energia, ou são sempre entidades diferentes?",
         "Factual, mapeia a estrutura real do ecossistema para essa operadora.", ("hipotese", "H7.1")),
        ("Vocês já perceberam alguma vantagem ou desvantagem em ter fornecedores separados para espaço físico e para energia?",
         "Deixa a percepção sobre consolidação emergir da experiência real.", ("hipotese", "H7.1")),
    ]),
    (9, "Fechamento", "Mapeamento de stakeholders e espaço aberto para o que não foi perguntado", [
        ("Quando uma decisão desse porte (fornecedor de infraestrutura crítica, contrato de vários anos) é tomada aqui, quais áreas costumam estar envolvidas, do início ao fim?",
         "Mapeamento de stakeholders baseado em processo real, não hipotético.", None),
        ("Tem algo sobre como vocês lidam com energia e infraestrutura crítica dos sites que a gente não perguntou, e que você acha importante a gente saber?",
         "Pergunta de fechamento aberta — captura qualquer hipótese não coberta.", None),
    ]),
]

UFINET_BLOCK8 = (8, "Ecossistema: o Papel da Própria Ufinet", "Testa a Hipótese do Ecossistema pelo ângulo invertido — a Ufinet como possível compradora do serviço da Moura", [
    ("Como vocês descreveriam o portfólio de serviços que a Ufinet oferece hoje para operadoras/provedores — além de conectividade e espaço físico, o que mais costuma estar incluso?",
     "Mapeia o escopo atual do portfólio, sem sugerir a inclusão de energia.", ("hipotese", "H7.1")),
    ("Existe algum serviço que a Ufinet já agregou ao portfólio ao longo do tempo, que não fazia parte da oferta original? O que motivou essa expansão?",
     "Testa se o modelo de “pacote crescente” já é praticado, evidência de apetite por agregar novos serviços.", ("hipotese", "H7.1")),
    ("A energia dos sites hoje entra de alguma forma no que vocês oferecem, ou é sempre responsabilidade do cliente final?",
     "Descobre se energia já está ou poderia estar dentro do escopo que a Ufinet revende.", ("hipotese", "H7.1")),
    ("Quem, na prática, decide o fornecedor de energia de um site — a Ufinet ou o cliente final que usa a infraestrutura de vocês?",
     "Mapeia se a Ufinet tem, de fato, poder de decisão sobre esse ponto — pré-requisito para a hipótese fazer sentido.", ("hipotese", "H7.1")),
])

# ---------- Per-operator metadata ----------
OPERATORS = [
    {
        "key": "claro",
        "avatar": "CL",
        "name": "Claro",
        "role": "Fabiano (Dir. Infraestrutura) · Alessandro (Ger. Compras) · Rafael (Ger. Infraestrutura)",
        "tags": ["Presencial/Remoto", "Big Three", "Relação a Reparar", "Cultura Patrimonialista"],
        "color": "claro",
        "objetivos": [
            "Entender, pela voz de quem decide, como funciona hoje a gestão de energia e backup dos sites da Claro — antes de qualquer apresentação da solução da Moura.",
            "Avaliar com cuidado o histórico da relação comercial com a Moura (venda tradicional de bateria e o episódio de repricing) e o quanto isso pesa hoje na disposição de negociar um contrato de serviço de longo prazo.",
            "Testar se a decisão de Compras é dominada por “hard saving” (preço da bateria) ou se já existe espaço para uma conversa de TCO e disponibilidade.",
            "Validar as dores internas já mapeadas pela Moura sobre a Claro — cultura mais conservadora, viés patrimonialista ligado à matriz global, menor abertura a modelos de aluguel.",
            "Mapear, além dos três contatos já definidos, quem mais precisaria estar convencido para um contrato desse porte avançar.",
        ],
        "note": "A Claro é a relação mais sensível das quatro operadoras. A imersão interna revelou um episódio de repricing malconduzido que quase custou o orçamento anual do cliente — os decisores guardam mágoa disso, segundo relato interno da Moura. Priorizar o Bloco 5 (Confiança e Dependência) com atenção redobrada: se o desgaste aparecer espontaneamente na fala do entrevistado, reconhecer antes de avançar para os blocos de proposta de valor.",
        "block_notes": {5: "Prioridade alta para esta operadora — ver nota acima sobre o histórico de repricing."},
        "block_override": {},
    },
    {
        "key": "tim",
        "avatar": "TIM",
        "name": "TIM",
        "role": "Gustavo Lima (Ger. Engenharia) · Tatiana Pinel (Ger. Compras) · Rodrigo Feitoza (Regional RJ) · Luisa Prestes (Ger. Operações)",
        "tags": ["4 Interlocutores", "Contato Quente", "Aberta à Inovação", "Centro de Pesquisa Próprio"],
        "color": "tim",
        "objetivos": [
            "Aproveitar os quatro ângulos diferentes que essas entrevistas oferecem — engenharia, compras, regional e operações — para entender onde a decisão realmente se forma dentro da TIM.",
            "Testar a percepção interna de que a TIM não tem uma dor aguda de CAPEX, mas se incomoda com o “kikiki” operacional e valoriza inovação (tem centro de pesquisa próprio).",
            "Aprofundar o relacionamento já existente — um gerente regional se ofereceu espontaneamente, numa conversa anterior, para ajudar a levar o case até o Board.",
            "Testar como a competição interna entre regionais e a matriz (headquarters) afeta a decisão — já mapeada como uma dinâmica real na imersão interna.",
            "Entender o apetite da TIM por temas mais avançados (monetização, dados, ESG), dado o perfil mais aberto à inovação já identificado.",
        ],
        "note": "A TIM já tem um contato “quente”: um gerente regional se ofereceu espontaneamente, numa conversa anterior, para ajudar a levar o case para o Board (diretoria italiana). Vale usar esta entrevista para consolidar esse apoio e entender os próximos passos para a apresentação ao Board — sem perder o objetivo de validar as hipóteses com rigor.",
        "block_notes": {7: "A TIM tende a responder bem aqui, dado o perfil mais aberto à inovação já identificado."},
        "block_override": {},
    },
    {
        "key": "algar",
        "avatar": "AL",
        "name": "Algar",
        "role": "Contato ainda a definir — sugestão: Diretor(a) de Engenharia/Infraestrutura",
        "tags": ["Perfil Regional", "Rooftop Predominante", "Contato a Confirmar"],
        "color": "algar",
        "objetivos": [
            "Mapear, antes de tudo, quem é de fato o interlocutor mais estratégico dentro da Algar — a sugestão de perfil (Engenharia/Infraestrutura) precisa ser validada ou ajustada com o time comercial da Moura.",
            "Entender como funciona a gestão de energia numa operadora regional com infraestrutura própria histórica — provavelmente diferente do padrão das grandes (Vivo/TIM/Claro).",
            "Testar, sem presumir, se a dor de furto/segurança física é tão relevante para a Algar quanto para as demais — a imersão interna sugere que boa parte dos sites da Algar é rooftop (mais seguro), o que pode enfraquecer esse argumento especificamente aqui.",
            "Investigar o histórico de uma proposta já enviada pela Moura à Algar sem retorno, mencionado internamente, e o que pode ter travado esse processo.",
        ],
        "note": "A Algar é a única das quatro operadoras sem um contato definido até o momento — a sugestão, com base no perfil da empresa, é o cargo de Diretor(a) de Engenharia/Infraestrutura como ponto de entrada mais estratégico, mas vale confirmar com o time comercial da Moura se já existe algum relacionamento prévio. A imersão interna já registra o envio de uma proposta à Algar no passado, sem retorno — vale investigar o que aconteceu com esse processo.",
        "block_notes": {6: "Não presumir baixa relevância de furto pelo perfil rooftop — perguntar mesmo assim."},
        "block_override": {},
    },
    {
        "key": "ufinet",
        "avatar": "UF",
        "name": "Ufinet",
        "role": "Cleber Camargo (Head de Operações)",
        "tags": ["Rede Neutra", "Perfil Diferente", "Testa Hipótese Invertida"],
        "color": "ufinet",
        "objetivos": [
            "Reconhecer, antes de tudo, que a Ufinet não é uma operadora de varejo como as outras três — é uma infraestrutura atacadista/rede neutra, mais parecida com players como V.tal e Fibrasil.",
            "Testar a Hipótese do Ecossistema (H7.1) pelo ângulo invertido: a Ufinet pode ser compradora do serviço da Moura para embutir no que ela mesma revende a operadoras e provedores.",
            "Entender o portfólio de infraestrutura que a Ufinet já entrega hoje, e se/como a energia dos sites entra (ou poderia entrar) nesse pacote.",
            "Reduzir o peso de blocos que pressupõem sites de rádio-base próprios (Sites Legados e Confiança/Dependência como operadora final) e dar mais espaço ao bloco de Ecossistema.",
        ],
        "note": "A Ufinet tem um perfil estrutural diferente das outras três operadoras — mais próximo de uma Rede Neutra/infraestrutura atacadista do que de uma operadora de varejo com sites de rádio-base próprios. Os Blocos 4 (Sites Legados) e 5 (Confiança e Dependência) devem ser tratados com peso reduzido; o Bloco 8 (Ecossistema) é o mais estratégico desta conversa e usa perguntas específicas, testando se a própria Ufinet seria compradora do serviço da Moura.",
        "block_notes": {4: "Peso reduzido — pressupõe sites de rádio-base próprios, que não é o perfil da Ufinet.",
                        5: "Peso reduzido pelo mesmo motivo do Bloco 4."},
        "block_override": {8: UFINET_BLOCK8},
    },
]

COLOR_MAP = {
    "claro":  ("#0046C1", "#dbeafe"),
    "tim":    ("#6200BE", "#EEE7FD"),
    "algar":  ("#0F8F6E", "#d7f5ec"),
    "ufinet": ("#C1650B", "#fde9d0"),
}

def render_person_tags(tags):
    return "".join(f'<span class="person-tag">{html.escape(t)}</span>' for t in tags)

def render_objetivos(objs):
    return "".join(f"<li>{html.escape(o)}</li>" for o in objs)

def render_blocos_overview(color):
    out = []
    for num, title, subtitle, _q in BLOCKS:
        out.append(f'''<div class="bloco-card">
            <div class="bloco-number {color}">Bloco {num}</div>
            <div class="bloco-name">{html.escape(title)}</div>
            <div class="bloco-desc">{html.escape(subtitle)}</div>
        </div>''')
    return "\n".join(out)

def render_question(idx, text, obj, tag, color):
    tag_html = ""
    if tag:
        kind, code = tag
        if kind == "hipotese":
            tag_html = f'<span class="origem-tag origem-hipotese">Hipótese {html.escape(code)}</span>'
        elif kind == "dor":
            tag_html = '<span class="origem-tag origem-dor">Dor Interna</span>'
    return f'''<li class="pergunta-item">
        <span class="pnum {color}">{idx}.</span>
        <div class="pcontent">
            <div class="ptext">{html.escape(text)}{tag_html}</div>
            <div class="psub">{html.escape(obj)}</div>
        </div>
    </li>'''

def render_roteiro(op):
    color = op["color"]
    blocks = list(BLOCKS)
    for num, block in op["block_override"].items():
        for i, (n, *_rest) in enumerate(blocks):
            if n == num:
                blocks[i] = block
    counter = 1
    out = []
    for num, title, subtitle, questions in blocks:
        extra_note = op["block_notes"].get(num)
        subtitle_html = html.escape(subtitle)
        if extra_note:
            subtitle_html += f' <strong>&mdash; {html.escape(extra_note)}</strong>'
        qitems = []
        for text, obj, tag in questions:
            qitems.append(render_question(counter, text, obj, tag, color))
            counter += 1
        out.append(f'''<div class="bloco">
            <div class="bloco-header">
                <span class="bloco-badge {color}">Bloco {num}</span>
                <div>
                    <div class="bloco-header-title">{html.escape(title)}</div>
                    <div class="bloco-subtitle">{subtitle_html}</div>
                </div>
            </div>
            <ul class="perguntas-list">
                {''.join(qitems)}
            </ul>
        </div>''')
    return "\n".join(out)

def render_operator_section(op, active=False):
    color = op["color"]
    active_cls = " active" if active else ""
    return f'''
<div class="person-section{active_cls}" id="section-{op['key']}">

    <div class="person-header {color}">
        <div class="person-avatar">{html.escape(op['avatar'])}</div>
        <div class="person-info">
            <div class="person-name">{html.escape(op['name'])}</div>
            <div class="person-role">{html.escape(op['role'])}</div>
            <div class="person-tags">{render_person_tags(op['tags'])}</div>
        </div>
    </div>

    <div class="objetivos-box">
        <div class="objetivos-title {color}">Objetivos da Entrevista</div>
        <ul class="obj-list">{render_objetivos(op['objetivos'])}</ul>
        <div class="note-box"><strong>Nota:</strong> {html.escape(op['note'])}</div>
    </div>

    <div class="blocos-overview">{render_blocos_overview(color)}</div>

    <div class="roteiro-section">
        <div class="intro-box {color}">
            <div class="intro-label">Abertura — fala sugerida</div>
            <div class="intro-text">"Obrigado por reservar esse tempo. A ideia da nossa conversa é entender, pela sua experiência, como funciona hoje a gestão de energia e infraestrutura crítica dos sites de vocês — os desafios, as prioridades, como as decisões são tomadas. Não estamos aqui para apresentar uma solução hoje; queremos genuinamente entender o cenário de vocês primeiro. Tudo bem?"</div>
        </div>
        {render_roteiro(op)}
    </div>

</div>'''

def render_tab_nav():
    out = []
    for i, op in enumerate(OPERATORS):
        cls = f"active-{op['color']}" if i == 0 else ""
        out.append(f'<button class="tab-btn {cls}" data-color="{op["color"]}" onclick="showOperator(\'{op["key"]}\', this)">{html.escape(op["name"])}</button>')
    return "\n".join(out)

def render_legend():
    return '''<div style="display:flex; gap:16px; flex-wrap:wrap; margin: 24px 0 8px; font-size:12px; color:#666;">
        <span><span class="origem-tag origem-hipotese">Hipótese</span> Pergunta que testa uma das 17 hipóteses consolidadas pelo time</span>
        <span><span class="origem-tag origem-dor">Dor Interna</span> Pergunta que valida uma dor percebida pela Moura na imersão interna (Fase 1)</span>
    </div>'''

sections_html = "\n".join(render_operator_section(op, active=(i == 0)) for i, op in enumerate(OPERATORS))

color_vars = "\n".join(
    f"            --{k}: {v[0]}; --{k}-light: {v[1]};" for k, v in COLOR_MAP.items()
)

tab_btn_css = "\n".join(
    f"        .tab-btn.active-{k} {{ color: var(--{k}); border-bottom-color: var(--{k}); }}" for k in COLOR_MAP
)
header_bg_css = "\n".join(
    f"        .person-header.{k} {{ background: var(--{k}); color: white; }}" for k in COLOR_MAP
)
title_border_css = "\n".join(
    f"        .objetivos-title.{k} {{ color: var(--{k}); border-color: var(--{k}); }}" for k in COLOR_MAP
)
badge_css = "\n".join(
    f"        .bloco-badge.{k} {{ background: var(--{k}-light); color: var(--{k}); }}" for k in COLOR_MAP
)
pnum_css = "\n".join(
    f"        .pnum.{k} {{ color: var(--{k}); }}" for k in COLOR_MAP
)
bloco_number_css = "\n".join(
    f"        .bloco-number.{k} {{ color: var(--{k}); }}" for k in COLOR_MAP
)
intro_box_css = "\n".join(
    f"        .intro-box.{k} {{ border-left-color: var(--{k}); }}" for k in COLOR_MAP
)

TEMPLATE = r'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Roteiro de Entrevista — Fase 2 (Operadoras) | MJV + Moura Energia</title>
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
__COLOR_VARS__
        }

        * { margin: 0; padding: 0; box-sizing: border-box; }

        body {
            font-family: 'Archivo', sans-serif;
            background: #F0F2F8;
            color: var(--dark);
            font-size: 14px;
            line-height: 1.6;
        }

        .page-header {
            background: var(--estrutura);
            color: white;
            padding: 36px 48px 28px;
            display: flex;
            justify-content: space-between;
            align-items: flex-end;
            flex-wrap: wrap;
            gap: 16px;
        }
        .page-header-left h1 {
            font-family: 'Space Grotesk', sans-serif;
            font-size: 22px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: -0.3px;
            margin-bottom: 6px;
        }
        .page-header-left p { font-size: 13px; opacity: 0.7; }
        .page-header-right {
            font-family: 'Space Grotesk', sans-serif;
            font-size: 12px;
            opacity: 0.6;
            text-align: right;
        }

        .tab-nav {
            display: flex;
            background: var(--branco);
            border-bottom: 1px solid rgba(0,0,0,0.08);
            padding: 0 48px;
            position: sticky;
            top: 0;
            z-index: 100;
            box-shadow: 0 2px 8px rgba(0,0,0,0.06);
            flex-wrap: wrap;
        }
        .tab-btn {
            padding: 16px 24px;
            font-family: 'Space Grotesk', sans-serif;
            font-size: 12px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.8px;
            border: none;
            background: none;
            cursor: pointer;
            border-bottom: 3px solid transparent;
            color: #888;
            transition: all 0.2s;
        }
        .tab-btn:hover { color: var(--dark); }
__TAB_BTN_CSS__

        .main { max-width: 960px; margin: 0 auto; padding: 36px 24px 80px; }

        .person-section { display: none; }
        .person-section.active { display: block; }

        .person-header {
            border-radius: 14px;
            padding: 28px 32px;
            margin-bottom: 28px;
            display: flex;
            gap: 24px;
            align-items: flex-start;
            flex-wrap: wrap;
        }
__HEADER_BG_CSS__

        .person-avatar {
            width: 56px; height: 56px;
            border-radius: 50%;
            display: flex; align-items: center; justify-content: center;
            font-family: 'Space Grotesk', sans-serif;
            font-size: 16px; font-weight: 700;
            background: rgba(255,255,255,0.2);
            flex-shrink: 0;
        }
        .person-info { flex: 1; min-width: 240px; }
        .person-name { font-family: 'Space Grotesk', sans-serif; font-size: 22px; font-weight: 700; margin-bottom: 4px; }
        .person-role { font-size: 13px; opacity: 0.9; margin-bottom: 12px; }
        .person-tags { display: flex; gap: 8px; flex-wrap: wrap; }
        .person-tag {
            background: rgba(255,255,255,0.18);
            border: 1px solid rgba(255,255,255,0.3);
            border-radius: 20px;
            padding: 3px 12px;
            font-size: 11px;
            font-family: 'Space Grotesk', sans-serif;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        .objetivos-box {
            background: var(--branco);
            border-radius: 12px;
            padding: 24px 28px;
            margin-bottom: 24px;
            border: 1px solid rgba(0,0,0,0.06);
        }
        .objetivos-title {
            font-family: 'Space Grotesk', sans-serif;
            font-size: 12px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 1.2px;
            margin-bottom: 14px;
            padding-bottom: 10px;
            border-bottom: 2px solid;
        }
__TITLE_BORDER_CSS__

        .obj-list { list-style: none; }
        .obj-list li {
            padding: 7px 0;
            font-size: 13.5px;
            line-height: 1.5;
            border-bottom: 1px solid rgba(0,0,0,0.05);
            padding-left: 18px;
            position: relative;
        }
        .obj-list li:last-child { border-bottom: none; }
        .obj-list li::before { content: '\2014'; position: absolute; left: 0; color: #bbb; font-size: 12px; }

        .blocos-overview {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 10px;
            margin-bottom: 28px;
        }
        .bloco-card {
            background: var(--branco);
            border-radius: 10px;
            padding: 16px;
            border: 1px solid rgba(0,0,0,0.06);
            text-align: center;
        }
        .bloco-number {
            font-family: 'Space Grotesk', sans-serif;
            font-size: 11px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.8px;
            margin-bottom: 6px;
        }
__BLOCO_NUMBER_CSS__
        .bloco-name {
            font-family: 'Space Grotesk', sans-serif;
            font-size: 12px;
            font-weight: 700;
            text-transform: uppercase;
            color: var(--estrutura);
            line-height: 1.3;
        }
        .bloco-desc { font-size: 11px; color: #888; margin-top: 4px; line-height: 1.4; }

        .roteiro-section {
            background: var(--branco);
            border-radius: 14px;
            padding: 28px 32px;
            margin-bottom: 20px;
            border: 1px solid rgba(0,0,0,0.06);
        }

        .intro-box {
            background: var(--bloco-bg);
            border-radius: 10px;
            padding: 20px 24px;
            margin-bottom: 24px;
            border-left: 4px solid #ddd;
        }
__INTRO_BOX_CSS__

        .intro-label {
            font-family: 'Space Grotesk', sans-serif;
            font-size: 10px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 1.2px;
            margin-bottom: 8px;
            color: #888;
        }
        .intro-text { font-size: 13.5px; line-height: 1.7; color: var(--dark); font-style: italic; }

        .bloco { margin-bottom: 28px; }
        .bloco-header {
            display: flex;
            align-items: center;
            gap: 12px;
            margin-bottom: 16px;
            padding-bottom: 10px;
            border-bottom: 1px solid rgba(0,0,0,0.08);
        }
        .bloco-badge {
            font-family: 'Space Grotesk', sans-serif;
            font-size: 10px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.8px;
            padding: 4px 12px;
            border-radius: 20px;
            white-space: nowrap;
        }
__BADGE_CSS__

        .bloco-header-title {
            font-family: 'Space Grotesk', sans-serif;
            font-size: 14px;
            font-weight: 700;
            text-transform: uppercase;
            color: var(--estrutura);
        }
        .bloco-subtitle { font-size: 12px; color: #777; margin-top: 2px; }

        .perguntas-list { list-style: none; }
        .pergunta-item { display: flex; gap: 14px; padding: 12px 0; border-bottom: 1px solid rgba(0,0,0,0.05); }
        .pergunta-item:last-child { border-bottom: none; }

        .pnum { font-family: 'Space Grotesk', sans-serif; font-size: 13px; font-weight: 700; min-width: 28px; padding-top: 1px; }
__PNUM_CSS__

        .pcontent { flex: 1; }
        .ptext { font-size: 14px; line-height: 1.55; color: var(--dark); font-weight: 500; }
        .ptext strong { font-weight: 700; }
        .psub { font-size: 12px; color: #666; margin-top: 6px; line-height: 1.5; font-style: italic; }

        .origem-tag {
            display: inline-block;
            font-size: 10px;
            font-family: 'Space Grotesk', sans-serif;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            padding: 2px 8px;
            border-radius: 4px;
            margin-left: 8px;
            vertical-align: middle;
        }
        .origem-hipotese { background: #dbeafe; color: #0046C1; }
        .origem-dor { background: #fef3c7; color: #92400e; }

        .note-box {
            background: #fffbeb;
            border: 1px solid #fde68a;
            border-radius: 10px;
            padding: 14px 18px;
            margin-top: 20px;
            font-size: 12.5px;
            color: #78350f;
            line-height: 1.6;
        }
        .note-box strong { font-weight: 700; }

        @media print {
            .tab-nav { display: none; }
            .person-section { display: block !important; page-break-after: always; }
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
        <h1>Roteiro de Entrevista — Fase 2</h1>
        <p>MJV Technology & Innovation · Projeto Moura Energia | Energia como Serviço · Entrevistas com as Operadoras</p>
    </div>
    <div class="page-header-right">
        SP-00028<br>4 operadoras · 17 hipóteses · dores da imersão interna
    </div>
</div>

<div class="tab-nav">
__TAB_NAV__
</div>

<div class="main">
__SECTIONS__
__LEGEND__
</div>

<script>
function showOperator(key, btn) {
    document.querySelectorAll('.person-section').forEach(s => s.classList.remove('active'));
    document.querySelectorAll('.tab-btn').forEach(b => {
        b.className = b.className.replace(/active-\S+/g, '').trim();
    });
    document.getElementById('section-' + key).classList.add('active');
    btn.classList.add('active-' + btn.getAttribute('data-color'));
}
</script>

</body>
</html>
'''

out = (TEMPLATE
       .replace("__COLOR_VARS__", color_vars)
       .replace("__TAB_BTN_CSS__", tab_btn_css)
       .replace("__HEADER_BG_CSS__", header_bg_css)
       .replace("__TITLE_BORDER_CSS__", title_border_css)
       .replace("__BLOCO_NUMBER_CSS__", bloco_number_css)
       .replace("__BADGE_CSS__", badge_css)
       .replace("__PNUM_CSS__", pnum_css)
       .replace("__INTRO_BOX_CSS__", intro_box_css)
       .replace("__TAB_NAV__", render_tab_nav())
       .replace("__SECTIONS__", sections_html)
       .replace("__LEGEND__", render_legend())
       )

with open("roteiro-template.html", "w", encoding="utf-8") as f:
    f.write(out)

print("wrote roteiro-template.html, size:", len(out))
