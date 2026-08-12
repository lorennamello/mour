# 02 — Auditoria de conteúdo
### A síntese cobre os achados das entrevistas?

**Veredito curto:** a síntese está **correta no que afirma** — não encontrei nenhuma afirmação
do deck contrariada pelas entrevistas. O problema é outro: **o deck é mais fraco do que a
evidência permite.** Achados fortes, quantificados e ditos em primeira pessoa aparecem no deck
como generalidades de consultoria. Há também duas afirmações que vão além do que a base sustenta
e uma perna inteira do diagnóstico que não foi entregue.

---

## 1. Matriz de cobertura

| # | Achado nas entrevistas | Status no 2.2 | Ação |
|---|---|---|---|
| 1 | O contrato Telefônica foi originado pelo cliente, não vendido | **Subdimensionado** — dito em prosa na p.14, sem a força do verbatim | Elevar |
| 2 | Quatro avaliações independentes, quatro rejeições, mesma razão econômica | **Ausente** como quadro | Criar |
| 3 | A amortização de 2-3 anos sobre ativo de 10-12 anos inviabiliza o modelo | **Ausente** | Criar — é a explicação estrutural |
| 4 | Furto real 7% vs. premissa 2%; cap contratual estourado | **Subdimensionado** — "custos superaram as premissas" | Quantificar |
| 5 | O risco de furto é controlado pelo cliente, não pelo fornecedor | **Parcial** — p.19 diz que encarece, não diz por quê | Aprofundar |
| 6 | Quatro réguas de autonomia distintas (2h a 72h) | **Subdimensionado** — afirmado sem prova | Tabelar |
| 7 | A métrica certa é disponibilidade — dito internamente ("caixa d'água") | **Presente** (p.20), sem o verbatim | Elevar |
| 8 | Telefônica pediu que a Moura assuma sites legados; vistorias em curso | **Ausente** | Criar — é a única demanda ativa |
| 9 | Consolidação de gabinetes reduz m² pagos à towerco | **Ausente** | Criar — melhor argumento financeiro da base |
| 10 | Quem tem a verba é planejamento, não compras | **Ausente** | Criar |
| 11 | Jurídico pesa mais que preço (insolvência, lista homologada) | **Ausente** | Incluir |
| 12 | Zabbix/Grafana e desenvolvimento interno como alternativa gratuita | **Subdimensionado** — "telemetria própria" na p.12 | Nomear |
| 13 | 30-35% do parque com erro de instalação | **Subdimensionado** — "instalação pouco padronizada" | Quantificar |
| 14 | A plataforma não avisa vandalismo; a operação sabe pelo cliente | **Ausente** | Incluir — prova a p.15 |
| 15 | A autonomia contratada não é visível na plataforma | **Ausente** | Incluir |
| 16 | A operadora não tem acesso à plataforma, só a relatórios | **Ausente** | Incluir |
| 17 | O modelo já é multi-produto no BES (backup, economia, qualidade) | **Ausente** | Criar — legitima a p.22 |
| 18 | Precedente 2018: Moura fora da RFQ de lítio, entrou 3 anos depois | **Ausente** | Criar — argumento de urgência |
| 19 | Towercos recusaram por contágio no custo de capital | **Ausente** | Incluir |
| 20 | SLA interno inexistente; demora de resposta afeta o cliente | **Parcial** — bullets genéricos na p.16 | Ancorar |
| 21 | Dimensionamento por site: cliente quer, Moura tem o dado e não faz | **Ausente** | Incluir |
| 22 | Data center / no-break: onde o cliente diz que a conta fecha | **Ausente** | Incluir |
| 23 | Vida útil da bateria cai por oscilação térmica em greenfield | **Ausente** | Incluir — fundamenta a segmentação |
| 24 | Projeto Telefônica é rentável hoje; o risco é variância | **Contradito em tom** pela p.14 | Corrigir |

**Resumo:** de 24 achados relevantes, **11 estão ausentes**, 8 subdimensionados, 4 presentes, 1
com tom contraditório.

---

## 2. Achados fortes que o deck não aproveita

### 2.1 A explicação contábil de por que o EaaS não fecha
O deck afirma repetidamente que "o TCO precisa fechar" e "o retorno é difícil de comprovar", mas
nunca explica **por que** estruturalmente não fecha. O comprador explicou:
> "se eu tenho um ativo que dura 10, 12 anos, já começa que quem investe traz essa amortização
> para 2 3 anos, aí ele coloca serviço em cima, **não tem como ficar mais em conta**" (Claro, 00:50:01)

Sem isso, a barreira parece negociável. Com isso, fica claro que exige mudança de desenho —
que é exatamente o que o deck vai propor na p.22.

### 2.2 O cliente já obtém o benefício de OPEX sem contratar EaaS
> "eu já tenho isso diluído durante o tempo. Então, é como se eu tivesse um aluguel. **Eu não
> vejo vantagem de agregar alguém nisso que não me deu algo diferente**" (Ufinet, 32:11)

Um dos dois pilares da proposta de valor atual — liberar CAPEX — é replicável por condição
comercial de compra. **Isso derruba metade do pitch e não está no deck.**

### 2.3 As towercos recusaram pelo mesmo motivo que ameaça a Moura
> "Ganha esse negócio de torre quem tem o custo de capital mais barato [...] a gente viu que há
> um risco na linha de custo, que a gente não tem como garantir essa estabilidade [...] o meu
> investidor fala: a tua empresa tá mais arriscada" (Thiago, 00:19:21)

E, do financeiro da Moura: *"A receita é fixa, mas o custo pode ser muito variável"* (00:22:45).
**O canal natural recusou pela razão exata que hoje pressiona a margem da Moura.** É o achado
mais elegante da base e não aparece.

### 2.4 A oportunidade do legado, com demanda declarada
Ver `06`, Cluster A. É a única frente com pedido explícito do cliente e vistorias em campo — e
está fora do deck.

### 2.5 O precedente do lítio
> "A Moura, nosso maior fornecedor, não participou, porque ela não tinha bateria de lítio [...]
> Ela entrou três anos depois" (Espinoza, 00:16:20)

O deck argumenta que "o mercado amadureceu mais rápido do que a Moura consolidou seu modelo"
(título da versão anterior). Existe um precedente interno que prova o padrão. Não usá-lo é
desperdiçar o argumento mais persuasivo disponível para urgência.

---

## 3. Afirmações que a evidência não sustenta — ou sustenta mais fraco que o tom

### 3.1 "O produto não está errado, mas o empacotamento está" (p.22) — **CORRIGIR**
Contradiz a p.15 do próprio deck e é desmentida por três fontes primárias (erro de instalação em
30-35%, alertas não confiáveis, autonomia invisível). Ver `06`, seção 1.

### 3.2 "Expectativa crescente por monitoramento inteligente com IA e manutenção preditiva" (p.18) — **REESCREVER**
Das cinco fontes externas:
- **Algar** pede predição — mas para alocar CAPEX, não para manutenção (21:17)
- **Claro** desenvolve ML própria, e o requisito declarado para terceiros é **interoperabilidade
  e custo** (00:57:22)
- **TIM** aponta interoperabilidade via SNMP como requisito contratual (item 39)
- **Ufinet**, perguntado sobre que dado lhe falta: *"Nesse ponto, não"* (39:36)
- **Compras Claro**: a dor é ter três softwares diferentes no NOC (00:31:52)

**Uma fonte pede predição; quatro pedem interoperabilidade e consolidação.** O deck está
recomendando liderar por um atributo que a maioria não pediu — e isso propagaria para a
estratégia de produto.

### 3.3 "Custos [...] colocam pressão sobre a rentabilidade do modelo" (p.14) — **AJUSTAR O TOM**
O financeiro afirma: *"O projeto tem se mostrado rentável, quando a gente olha a DRE dele"*
(00:27:35). O problema é variância, não prejuízo. Manter como está expõe o deck a uma correção
pública do próprio financeiro na reunião.

### 3.4 "A concorrência em servitização completa ainda é limitada" (p.12) — **INCLUIR A RESSALVA**
Verdadeiro, mas incompleto. A base mostra por que é limitada: **um concorrente quebrou**
(C-Towers, Daniel 00:41:08) e as towercos recusaram por contágio de custo de capital. Escassez
de concorrentes aqui é sinal de dificuldade estrutural, não de oceano azul livre.

---

## 4. Divergências entre a visão interna e a do mercado

Este é o cruzamento mais produtivo do material e o deck só explora parte dele.

| Tema | Moura acredita | O mercado diz | Consequência |
|---|---|---|---|
| **Monitoramento** | "principal atrativo [...] eles não têm nem perto dessa granularidade" (Daniel, 00:20:37) | Zabbix/Grafana em todas as operadoras; Claro desenvolve solução agnóstica; requisito é interoperabilidade | Vender granularidade não diferencia; vender **decisão de investimento** sim |
| **Antifurto** | "grande estandarte sobre a redução de furto" (Francisco, 00:07:07) | "sistema fraco, já foi hackeado"; "câmera não inibe mais"; concorre com serralheiro | Deixa de ser diferencial; vira requisito de margem |
| **Assumir o risco de furto** | pilar da proposta de valor (Thiago, 00:39:58) | "é um risco que ele está assumindo e que está na minha mão" (Algar) | Precificar tudo encarece; compartilhar é o caminho |
| **Liberar CAPEX** | pilar principal (Thiago e Daniel) | Ufinet já dilui via condição de pagamento; Claro chama de troca de investimento por despesa | O argumento existe, mas não é suficiente sozinho |
| **Escopo do pacote** | "nossa solução é uma solução completa" (Driele, 00:14:17) | Ufinet quer **mais** escopo (espaço + manutenção); Telefônica queria **menos** (só bateria) | Prova que o pacote fixo não serve — a favor da p.22 |
| **Qualidade premium** | barreira de entrada e diferencial (Daniel, 00:40:05) | "os produtos hoje estão muito nivelados em qualidade" (Algar, 37:08); mercado escolhe média qualidade barata | Qualidade não vence a venda; serviço sim |
| **Furto como dor a resolver** | dor crítica do cliente | "não se estresse, eu vivo isso 5 vezes por dia" (Vivo, via Consultor) | Dor real, mas já gerida — baixa disposição a pagar prêmio |

→ **Cinco das sete linhas mostram a Moura apostando em atributos que o mercado não compra.**
Este quadro, sozinho, sustenta a conclusão de maturidade melhor do que qualquer framework.

---

## 5. Qualidade da base — o que limita as conclusões

**Assimetria de fontes externas:** três das cinco têm transcrição literal completa (Claro
engenharia, Claro compras, Ufinet, Algar — quatro, na verdade). **A TIM tem apenas anotações de
IA, sem transcrição** — todo achado da TIM é paráfrase e não permite verbatim. Isso importa
porque a TIM é a operadora com trial concluído.

**Cobertura interna:** 7 de 10 entrevistas lidas na íntegra. Não lidas: Aline, Andrea, Josi,
Gustavo. **Andrea é apontada por duas fontes como responsável pela modelagem financeira e pela
orquestração do produto** — conclusões sobre governança de precificação são preliminares.

**Nenhuma entrevista com a Vivo/Telefônica como cliente.** O único contrato em operação não tem
voz do comprador no acervo. Toda a leitura sobre por que a Telefônica comprou vem de fontes
internas e de um profissional de compras da Claro que passou pela Vivo. **É a lacuna mais
relevante da base de evidências** — e vale registrar como recomendação de próxima etapa.
