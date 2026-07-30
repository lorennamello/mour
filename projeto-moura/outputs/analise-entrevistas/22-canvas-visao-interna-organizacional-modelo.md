# Modelo proposto: um terceiro canvas para a visão interna organizacional (complementar ao BMC)

*Este documento é uma etapa de **desenho do modelo**, não de análise de dados. Ainda não voltei às 15 entrevistas para preencher este canvas — isso é o próximo passo, depois que você validar ou ajustar a estrutura abaixo. O objetivo aqui é só responder: qual é a lógica, quais são os blocos, e como isso se encaixa (sem se sobrepor) ao BMC que já fizemos.*

---

## 1. O problema que este canvas resolve

O BMC (`20-bmc-as-is-moura-energia.md`) descreve a **lógica de negócio** do produto Energia como Serviço: o que ele entrega, para quem, como cobra, com que recursos e parceiros. Mas ao longo da imersão interna apareceram, repetidamente, achados que não cabem em nenhuma dessas 9 caixas — porque não são sobre a lógica do negócio, são sobre **a capacidade da organização de executar essa lógica de forma saudável e sustentável**. Hoje esses achados estão "avulsos" numa seção do BMC chamada "Desafios complementares" — 11 pontos sem estrutura própria, sem framework, sem lugar certo para crescer.

São coisas como: governança fragmentada entre times, turnover levando conhecimento junto, precificação feita em silos, premissas de risco desatualizadas, medo de mudança dentro do próprio cliente, hardware que "virou produção" sem nunca ter sido validado como produto maduro. Nenhum desses é "modelo de negócio errado" — são sintomas de **maturidade organizacional**, e é exatamente esse pedaço que este novo canvas precisa cobrir.

## 2. As duas referências que você trouxe, e como as usei

- **O worksheet do livro de BPM** (10 categorias: Contexto de Negócio, Contexto Cultural, Medição de Desempenho, Gargalos, Questões de Handoff, Regras de Negócio, Capacidades, Custos, Envolvimento Humano, Interações com Clientes) — essas categorias foram pensadas originalmente para diagnosticar um *processo*. Troquei "processo" por "produto" em todas as perguntas, como você pediu, porque aqui o objeto de análise é o produto Energia como Serviço, não um processo isolado.
- **A Cadeia de Valor de Porter** (o segundo print, com "faixas de apoio" cruzando o topo — Infraestrutura, RH, Tecnologia, Aquisições — e colunas de atividade primária embaixo, terminando numa seta de "Margin") — usei isso como referência **de formato**, não de conteúdo: a ideia de ter uma camada que atravessa tudo (no caso de Porter, o apoio organizacional; no nosso caso, a cultura) e um resultado visível à direita (no caso de Porter, a margem; no nosso caso, o custo da fricção interna).

## 3. Nome proposto

**Canvas de Prontidão Organizacional** (em inglês, se preferir manter o padrão do BMC: *Organizational Readiness Canvas*). A lógica do nome: o BMC descreve *o que* o negócio promete entregar; este canvas descreve *se a organização está pronta*, na prática, para sustentar essa entrega em escala — culturalmente, operacionalmente, tecnicamente. "Prontidão" (não "maturidade" ou "saúde") porque o objetivo final é responder uma pergunta de decisão: dado o que a imersão mostrou, a Moura está pronta para escalar este modelo, ou existem lacunas organizacionais que precisam ser fechadas primeiro? Duas alternativas, se preferir outro tom: **Canvas de Capacidade Organizacional** (mais neutro, descritivo) ou **Canvas de Maturidade Interna** (mais próximo da linguagem que você já usou na conversa).

## 4. Como ele se relaciona com o BMC (a fronteira, para não duplicar)

| | BMC | Canvas de Prontidão Organizacional |
|---|---|---|
| Pergunta que responde | O que o negócio entrega, para quem, como cobra? | A organização consegue sustentar essa entrega bem, hoje? |
| Lente | Lógica de negócio (estática) | Capacidade de execução (dinâmica, sobre gente e governança) |
| Exemplo de achado | "A mensalidade é ~R$2.000/site" | "A modelagem que gerou esse preço já está desatualizada e ninguém recalibrou" |
| Onde mora hoje | Os 9 blocos do BMC | A seção solta "Desafios complementares" do BMC — que este canvas substitui por uma estrutura própria |

Dois blocos deste novo canvas têm nome parecido com blocos do BMC — vale já deixar a diferença clara:
- **"Custos" (novo canvas) ≠ "Estrutura de Custos" (BMC).** No BMC, custo é o custo *do produto* (CAPEX de gabinete, frete, funding). Aqui, custo é o custo *da fricção organizacional* — retrabalho, atraso, turnover, decisão feita em silo. É dinheiro que nenhuma linha do orçamento do produto captura hoje, mas que existe.
- **"Interações com Clientes" (novo canvas) ≠ "Relacionamento com Clientes" (BMC).** No BMC, é a lógica da relação prometida ao cliente (contrato de 10 anos, ponto de contato dedicado). Aqui, é a mecânica interna por trás disso — quem dentro da Moura realmente ouve o cliente, se esse feedback chega a quem decide, se há redundância ou ruído nesse caminho.

## 5. A estrutura visual proposta

Peguei emprestado da Cadeia de Valor de Porter a ideia de **faixa + colunas + resultado**, adaptada:

```
┌──────────────────────────────────────────────────────────────────────────┐
│                         CONTEXTO CULTURAL  (faixa que atravessa tudo)     │
│         liderança · qualidade · aceitação/resistência · treinamento      │
└──────────────────────────────────────────────────────────────────────────┘
┌───────────────────────────┐
│ CONTEXTO DE NEGÓCIO        │   ← bloco-âncora (por que o produto existe,
│ DO PRODUTO                 │     ajuste estratégico, riscos, tecnologia)
└───────────────────────────┘
┌───────────┬───────────┬───────────┬───────────┬───────────┐   ┌─────────┐
│Governança │Capacidades│ Handoffs  │ Envolvi-  │ Medição   │   │ CUSTO   │
│e Regras   │           │e Gargalos │mento      │de Desem-  │ → │ DA      │
│de Negócio │           │           │Humano     │penho      │   │FRICÇÃO  │
└───────────┴───────────┴───────────┴───────────┴───────────┘   │ INTERNA │
┌──────────────────────────────────────────────────────────┐    └─────────┘
│              INTERAÇÕES COM CLIENTES (lente interna)      │
└──────────────────────────────────────────────────────────┘
```

- **A faixa do topo (Contexto Cultural)** não é uma caixa entre outras — ela atravessa e colore todas as demais, exatamente como as "camadas de cima" no seu print da Cadeia de Valor. Cultura não é um departamento, é o ambiente em que todos os outros blocos operam.
- **O bloco-âncora (Contexto de Negócio do Produto)** é o equivalente da Proposta de Valor no BMC: por que este produto existe e para onde ele deveria estar indo.
- **As cinco colunas centrais** são o "motor" operacional — onde moram a maior parte dos achados soltos que você já tem.
- **A saída à direita (Custo da Fricção Interna)** é o equivalente da seta "Margin" de Porter: o resultado visível e mensurável de todos os gaps anteriores — o que a organização está pagando, em dinheiro, tempo ou risco, por não ter essas seis frentes bem resolvidas.
- **A faixa da base (Interações com Clientes)** fica embaixo porque, na prática, é o ponto onde a fragilidade interna acaba aparecendo para fora — é o "teste de estresse" que revela se o resto do canvas está funcionando.

## 6. Os 9 blocos, com as perguntas-guia (processo → produto)

### Contexto Cultural
*Faixa superior, atravessa todos os blocos.*
- Quais lideranças são responsáveis pelo sucesso da entrega do **produto**? Quão comprometidas elas estão com mudanças nele?
- Como a excelência do **produto** é definida — e essa definição é compreendida da mesma forma em toda a organização?
- Os indivíduos afetados pelo **produto** entendem e aceitam o motivo das mudanças que ele exige? Existem incentivos que, sem querer, remam contra a cooperação?
- Como o treinamento sobre o **produto** é conduzido, e ele acompanha as mudanças que o produto vai exigindo?

### Contexto de Negócio do Produto
*Bloco-âncora.*
- Por que o **produto** existe? O que levou à sua criação — e essa razão original ainda é válida hoje?
- Onde o **produto** se encaixa na cadeia de valor da organização, e ele está alinhado aos objetivos estratégicos atuais?
- Quão bem o **produto** opera no ambiente de negócio atual — e quão bem ele se adaptaria se esse ambiente mudasse?
- Quais riscos (externos e internos) o **produto** enfrenta, e a organização consegue mitigá-los?
- Que sistemas/tecnologias sustentam o **produto** hoje, e quão sustentáveis eles são?

### Governança e Regras de Negócio
- As regras/decisões que governam o **produto** cobrem, de forma completa, os cenários que de fato acontecem na operação — ou há lacunas e contradições?
- As áreas ou processos que dependem uns dos outros para sustentar o **produto** são regidas por regras consistentes entre si?
- Existem aprovações, etapas ou restrições no **produto** que geram obstáculo sem necessidade real, e que poderiam ser eliminadas?
- Quando e por que as regras atuais do **produto** foram criadas — elas foram atualizadas desde então, ou continuam sendo aplicadas por inércia?

### Handoffs e Gargalos
- Quais são as transferências entre áreas mais prováveis de atrasar o **produto** (de uma equipe para outra, de uma etapa para a próxima)?
- Existe algum gargalo de informação ou de serviço no fluxo do **produto**? Esse gargalo nasce de uma transferência malfeita, ou de uma etapa que acontece rápido demais e gera retrabalho?
- Algum desses handoffs poderia ser eliminado sem perda? Onde os fluxos de informação do **produto** se juntam — e esse ponto de junção é preciso, ou é fonte de erro?

### Capacidades
*(Extrapolado por mim a partir do título da categoria — sinalize se quiser as perguntas originais do livro.)*
- Que competências a organização precisa ter, hoje, para sustentar o **produto** em escala — e quais dessas competências já existem de forma madura, versus quais ainda dependem de um MVP que "virou produção" sem nunca ter sido validado como industrial?
- A organização sabe, de forma explícita, quais dessas capacidades são essenciais e quais são acessórias? Há um plano deliberado para desenvolver as que faltam, ou isso acontece de forma reativa?
- Que capacidades hoje dependem de um parceiro externo (ex.: transferência tecnológica incompleta) em vez de estarem internalizadas?

### Envolvimento Humano
*(Extrapolado por mim a partir do título da categoria.)*
- Quanto do funcionamento do **produto** hoje depende de esforço manual ou de decisão individual de uma pessoa específica, em vez de processo documentado?
- O que acontece com o **produto** quando uma pessoa-chave sai da organização? Esse conhecimento está documentado, ou é perdido e precisa ser redescoberto (e re-errado) pela próxima pessoa?
- Existem pessoas cuja saída/entrada muda significativamente a qualidade ou o ritmo de entrega do **produto**?

### Medição de Desempenho
*(Extrapolado por mim a partir do título da categoria.)*
- Como o sucesso do **produto** é medido hoje, internamente — e essa medição é sobre qualidade real de entrega, ou só sobre volume/prazo?
- As premissas usadas para planejar o **produto** (financeiras, de risco, operacionais) são revisadas periodicamente contra o que de fato acontece — ou continuam sendo usadas mesmo desatualizadas?
- A excelência do **produto** é uma competência reconhecida e incentivada na estratégia da organização, ou é invisível nos incentivos de quem o executa?

### Custo da Fricção Interna
*Saída, à direita — equivalente à "Margin" de Porter.*
- Quanto custa, em tempo e dinheiro, o retrabalho gerado pelos gargalos e handoffs mapeados acima?
- Quanto custa o turnover e a perda de conhecimento (tempo de nova pessoa reaprendendo o que a anterior já sabia)?
- Quanto custa a decisão feita em silo, sem a colaboração entre áreas que existia antes (ex.: força-tarefa de precificação que se perdeu)?
- Esses custos aparecem em algum lugar do orçamento hoje, ou são absorvidos silenciosamente como "jeito que as coisas são"?

### Interações com Clientes (lente interna)
*Faixa inferior — onde a fragilidade interna aparece para fora.*
- Quem, dentro da organização, realmente ouve o cliente sobre o **produto** — e essa pessoa/área tem poder de decisão, ou só registra a informação?
- As sugestões e reclamações do cliente sobre o **produto** chegam a quem poderia agir sobre elas? Existe redundância ou ruído nesse caminho?
- A organização sabe, com dados (não impressão), se o cliente está satisfeito com o **produto** — e essas métricas de satisfação estão dentro do esperado?
- Existe dúvida interna sobre se a organização está falando com as pessoas certas dentro do cliente?

## 7. Prova de que o modelo funciona: os 11 "Desafios complementares" já têm casa

Para validar a estrutura antes de sair coletando dado novo, mapeei os 11 pontos que hoje estão soltos no BMC (seção "Desafios complementares") para os blocos deste canvas. Se cada um encontra um lugar claro, o modelo está fazendo o que deveria:

| # | Desafio (já levantado no BMC) | Bloco no novo canvas |
|---|---|---|
| 1 | Hardware "MVP que virou produção" | **Capacidades** |
| 2 | Governança fragmentada (ITEM/Engenharia/TI) | **Governança e Regras de Negócio** + **Handoffs e Gargalos** |
| 3 | Modelagem original subestimou o risco | **Medição de Desempenho** |
| 4 | Cultura departamentalizada, times competem | **Contexto Cultural** |
| 5 | Turnover e perda de conhecimento histórico | **Envolvimento Humano** |
| 6 | Proposta de valor pouco quantificada financeiramente | **Medição de Desempenho** |
| 7 | "Estamos falando com as pessoas certas?" | **Interações com Clientes** |
| 8 | Medo de perda de emprego dentro das operadoras | **Interações com Clientes** / **Contexto Cultural** |
| 9 | Legado é a maior oportunidade não capturada | **Contexto de Negócio do Produto** |
| 10 | Escopo deliberadamente limitado | **Contexto de Negócio do Produto** |
| 11 | Confusão institucional sobre quem detém o CAPEX | **Contexto de Negócio do Produto** / **Interações com Clientes** |

Todos os 11 encontraram bloco. Nenhum ficou de fora, e nenhum bloco ficou vazio — bom sinal de que a estrutura está no tamanho certo (nem grande demais a ponto de sobrar espaço morto, nem pequena a ponto de forçar tudo em uma caixa só).

## 8. O que eu preciso de você para seguir

1. **Validar (ou trocar) o nome** — "Canvas de Prontidão Organizacional" ou uma das duas alternativas, ou outro nome que você prefira.
2. **Confirmar os 9 blocos e a fronteira com o BMC** (seção 4) — especialmente se "Custos" e "Interações com Clientes" fazem sentido como blocos distintos dos equivalentes do BMC, ou se prefere outro nome para evitar qualquer confusão na apresentação.
3. **Decidir sobre as 5 categorias extrapoladas** (Capacidades, Envolvimento Humano, Medição de Desempenho, Custo da Fricção Interna, e a fusão de Gargalos dentro de Handoffs) — se quiser, me envie o restante do livro e eu recalibro essas perguntas pelas originais; senão, sigo com o que propus.
4. Depois disso, o próximo passo é exatamente o que você descreveu: eu volto às 15 transcrições da imersão interna, releio com esses 9 blocos como lente, e preencho o canvas com evidência e fonte — no mesmo padrão dos outros dois documentos.
