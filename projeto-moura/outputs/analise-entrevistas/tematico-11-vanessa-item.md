# Análise Temática — Vanessa (ITEM — P&D)

**Contexto:** coordenadora do time de P&D digital (hardware/software/firmware) e qualidade/homologação no ITEM, desde dez/2024. Duas conversas: uma breve institucional (Overview Moura + ITEM) e uma longa e técnica (Sobre o produto + serviço), onde ela conta a história completa do produto Telecom desde a origem.

---

## 1. Proposta de valor — o que entrega e para quem

**Fato — valor original identificado pelo ITEM (o "insight" fundador do negócio):** "as operadoras hoje têm muita dificuldade [...] têm furto, [...] não conseguem fazer o monitoramento [...] a saúde dessa bateria para trocar tempo antes dela não conseguir dar carga e recair na multa. Então, por quê? Ao invés de só vender a bateria, a gente não vende o serviço."
**Fato — valor concreto entregue (quando perguntada diretamente o que gerou valor na POC):** "Da telemetria ser feita por nós e não mais pela operadora. A responsabilidade e a garantia de que uma vez que eu estou vendo isso aqui, eu conseguiria avisar do problema [...] A questão da manutenção também é bem importante [...] a gente ficando com o serviço, a gente é que vai lá resolver pra ela."
**Fato — o que a operadora já tinha antes, e o diferencial real do que a Moura entrega:** a fonte já manda dados para a nuvem própria da operadora (telemetria nativa, obrigatória para cumprir Anatel); "a questão é, o que o nosso dá e o que o nosso a longo prazo [...] tem potencial de dar, cobre isso que as operadoras têm [e adiciona] mais informação e mais gatilhos e deveria prover mais segurança e confiabilidade do que só o espelhamento que eles têm."

**Interpretação:** Vanessa é a única entrevistada que consegue articular com precisão técnica *o que exatamente* a Moura entrega a mais do que a própria fonte/operadora já teria nativamente — um dado essencial para qualquer discurso de valor mais rigoroso, mas que não aparece de forma tão clara nas falas do time comercial.

---

## 2. Desafios internos por área

### Tecnologia/Produto (a área dela)
**Fato — a POC "virou produto rápido demais":** "Isso não era produto. Isso ainda era experimental [...] a gente sabia que tinham fragilidades [...] a ideia era o seguinte, vamos começar por esse, aí depois a gente vai tirar esse cara, vai colocar uma placa mais integrada [...] a solução ia evoluir gradativamente" — mas essa evolução gradual não aconteceu no ritmo planejado, pois "começou a corrida com outro tempo. A gente de P&D tava tentando amadurecer o produto enquanto ele já tava sendo instalado."
**Fato — consumo de dados excessivo:** modem comercial atual consome "da forma mais grosseira possível [...] tem gabinete consumindo mais de 2 gigas"; teste controlado do ITEM mostrou que a versão planejada consumiria ~15MB em 5 dias vs. ~300MB do modem atual — diferença de OPEX relevante ainda não capturada.
**Fato — segurança física limitada:** "hoje a gente tem um cabeado [cadeado], que é da Promon [...] mas ele é só um cadeado [...] No máximo ele avisa assim, arrombou" — o módulo de segurança mais robusto planejado (sensores de temperatura/vibração, trava reforçada) nunca foi desenvolvido.
**Fato — divisão de responsabilidade "confusa"/não resolvida:** ITEM ainda dá suporte de **hardware** para telecom (ao contrário do BES, já totalmente transferido) — "o time não é grande e ele se divide, a gente perde e suporta [...] pode gerar um certo gargalo."
**Fato — falta de contato direto com o cliente final:** "a gente já teve muito próximo [...] depois desse contato ficou assim, ó, vocês não têm mais acesso ao cliente final. Vocês têm que sempre pedir a engenharia pra intermediar" — mudança de política interna que limitou o fluxo de feedback direto do campo para o P&D.

### Processo/Instalação (não é a área dela, mas ela identifica com precisão)
**Fato — causa raiz de muitos problemas de campo:** "ainda hoje acontece [...] muitas falhas de processo, falhas de qualidade [...] verificar se o lugar tem ou não conexão. Na hora que o cara instala, ele conecta um cabo errado, usa um material errado."
**Fato — exemplo concreto relatado por ela:** visita a um site onde "não tava ligado na energia. Aí a bateria descarregou completamente e o site morreu [...] são coisas que a gente foi identificando que [...] é uma falha de processo."
**Fato — atribuição incorreta de causa:** "toda vez que gera uma dúvida, ah, é o Conect e falhou. Aí a gente é chamada e quando chega, não é o Conect [...] a gente não teve um período pra aprender com deixar em campo [...] a gente só vai aprender realmente quando der erro."

### Comercial
Não é a área dela — comenta apenas que a plataforma foi validada com requisitos vindos da própria Moura Energia, mas sem aprofundar no processo comercial em si.

### Financeiro
**Fato — tensão CAPEX x OPEX estrutural:** "o CAPEX, a POC acabou virando produto muito rápido e ela setou um CAPEX enxuto ali. Só que a ideia era que a solução robusta[,] ela diminuísse o OPEX, que hoje é muito grande [...] a questão da evolução da maturidade do produto passa por um equilíbrio entre essas duas coisas."

---

## 3. Áreas internas — como ela percebe outras áreas

**Fato — sobre a Moura Energia/engenharia de novos negócios:** "o nosso cliente de fato é engenharia de novos negócios, que é a engenharia que cuida [...] que tem como cliente a Moura Energia, então é como se a gente fosse um terceirizado [...] Mas como a gente está todo mundo sobre o guarda-chuva da Moura, essa relação fica meio cruzada."
**Fato — sobre a governança/priorização de decisões de produto:** decisões sobre evoluir hardware (ex.: depender ou não de fornecedor chinês para embarcar a solução) envolvem "uma decisão estratégica [...] Eu quero delegar ou não? [...] a gente vai oferecer opções pra Andréia. Ela vai escolher qual opção que quer."
**Fato — sobre a TI da Moura:** confirma que a TI "fez um espelhamento dessa nossa plataforma com outra identidade visual" (a plataforma MEX) a partir de requisitos vindos da Moura Energia — sem contato direto do ITEM com essa demanda ("a gente não teve esse contato direto").
**Fato — pessoas-chave apontadas por ela para aprofundamento futuro:** João Machado (engenheiro técnico, desde a fundação — "ele vai saber" as causas raiz de falência de outras empresas do setor, riscos e gargalos) e Marcos Malveira (gerente do ITEM, visão de negócio/estratégia, "desenhou junto com o Thiago Melo a solução técnica").

---

## 4. Modelo comercial

Não é foco dela, mas contribui um dado relevante ao histórico comercial:
**Fato:** a POC/dispositivo criado pelo ITEM foi testado primeiro no site da **TIM** (não Telefônica) — "Fizemos isso aqui com a Tim, no site da Tim [...] Amor Energia, ela nasceu do item [...] o berço, de fato, foi aqui."
**Fato:** quando a POC "deu certo", a decisão de vender veio de fora do ITEM: "aí disseram, vamos vender [...] Mas quem viu o valor foi o cliente?" — ela confirma que sim, foi a reação positiva do cliente (TIM) que acelerou a decisão comercial, antes de o produto estar tecnicamente maduro.

---

## 5. Visão sobre os clientes

**Fato — o que a plataforma ajuda a responder para quem opera (ex.: Espinosa):** saúde/estado dos sites, melhor momento de manutenção, se a autonomia contratual está garantida, alertas de degradação/furto indireto, análise geográfica cruzada com dados climáticos.
**Fato — o que a operadora já recebe de forma nativa (antes mesmo do Moura Energia):** telemetria própria da fonte, usada para cumprir a Anatel — "tem uma parte do gabinete que, por exemplo, a Tinha Viva, elas acessam livremente [...] Porque eles têm o sistema duplicado do nosso [...] Eles são obrigados a ter esse espelhamento."

**Interpretação:** essa fala é um dado crítico para o report — ela deixa claro que a informação básica de telemetria **já existe** de forma nativa na operadora antes mesmo de contratar a Moura; a decisão de compra do cliente não pode se apoiar apenas em "ter monitoramento", e sim na qualidade/confiabilidade/proatividade adicional que a Moura promete entregar — algo ainda não plenamente maduro segundo a própria Vanessa.

---

## 6. Barreiras de expansão

**Fato — risco de escalabilidade ligado à maturidade do produto, não ao mercado:** "pra gente, o único risco da escalabilidade hoje é pela maturidade do produto. E aí é uma questão estratégica [...] Se a gente vai continuar como tá e fazer só o básico [...] Ou se a gente vai fazer o roadmap que foi pensado."
**Fato — histórico do setor como alerta:** "várias empresas [que tentaram] entrar nesse setor faliram [...] o sistema de monitoramento que hoje as operadoras têm[,] ele não consegue sanar esses gargalos [...] o custo do OPEX fica muito alto [...] o contrato é muito longo [...] você só vai gastando dinheiro para manter o sistema e ele começa a não trazer retorno."

**Interpretação:** ela é a única entrevistada que articula, de forma quase causal, por que outras empresas do setor fracassaram — e conecta isso diretamente ao risco que a própria Moura corre se não amadurecer o produto na velocidade necessária, antes de escalar mais.

---

## 7. Ecossistema e mercado

**Fato — sobre o ITEM como instituição:** ICT (instituição de ciência e tecnologia) registrada no Ministério de Ciência e Tecnologia, sob o guarda-chuva Moura, sediada em Belo Jardim (com extensão em Recife); atua em P&D, fomento e inovação para toda a empresa, incluindo parcerias externas com outras ICTs e empresas do setor energético.
**Fato:** já desenvolveram versões do sistema para aplicação bancária e data center, além de um projeto até 2027/2028 unindo telecom e BES no conceito de VPP (virtual power plant).

---

## 8. Visão de futuro

**Fato — roadmap técnico em curso:** projeto para "amadurecer a solução e propor uma nova arquitetura" saindo do modelo atual (baseado em Raspberry Pi/dongle 4G comercial) para algo mais robusto — com o desafio de gerir a transição entre parque "legado" (com a solução antiga) e novos sites (arquitetura nova).
**Fato — dependência de decisão de fornecedor chinês:** evoluir a fonte para embarcar mais funcionalidades depende de o fornecedor aceitar, cobrar um preço absorvível e da Moura decidir se quer manter a propriedade intelectual internamente ou delegar ao fornecedor.
**Fato — "chassi único" (convergência com a visão de Francisco/TI):** ideia de concentrar telecom + BES + futuro HomeBES numa mesma base de dados, pois "eu vou estar na casa de CPFs e CNPJs de pequeno porte [...] imagine a quantidade de informação."
**Fato — encerramento da entrevista:** "o único risco da escalabilidade hoje é pela maturidade do produto [...] se isso realmente é um diferencial do mercado ou não [...] para que realmente a solução, no longo prazo, se diferencie de qualquer outra. E ganhe naquela relação de CAPEX e OPEX."

---

## 9. Hipóteses para validação (Fase 2 — com operadoras)

| O que o time interno acredita (opinião de Vanessa) | Hipótese estruturada para testar com o mercado |
|---|---|
| O risco de escalabilidade é a maturidade do produto (não o mercado) — alarmes falsos, falta de módulo de segurança robusto. | O ceticismo comercial de TIM/Claro pode já estar ligado a **casos concretos de falha técnica que a operadora vivenciou** (não apenas a uma objeção financeira genérica) — testar diretamente com engenharia dessas operadoras se episódios específicos de instabilidade/alarme falso influenciaram a decisão de não avançar. |
| A operadora já tem telemetria nativa da fonte (para cumprir Anatel) antes mesmo de contratar a Moura. | O argumento comercial "nós damos monitoramento" pode não ser suficientemente diferenciado aos olhos do cliente técnico, já que ele já tem uma telemetria própria — testar diretamente com a engenharia da operadora **o que especificamente falta** no sistema nativo dela hoje, para calibrar se o discurso de venda está batendo nessa lacuna real ou reforçando algo que o cliente já julga ter. |
| Outras empresas do setor faliram porque o sistema de monitoramento não conseguia sanar os gargalos (furto, multa Anatel, degradação de ativo) e o OPEX fugiu de controle. | As operadoras podem carregar **memória de fracassos anteriores** de fornecedores de servitização de energia, gerando ceticismo estrutural sobre a viabilidade do modelo como um todo — testar se esse histórico é mencionado espontaneamente pelas operadoras e quais garantias (financeiras, contratuais, técnicas) mitigariam esse ceticismo. |

## 10. Pessoas-chave para falar dentro do cliente (operadora)

**Já conversados:** nenhum contato direto com cliente final (operadora) é relatado por ela.

**Fato explícito sobre a ausência de acesso:** "a gente já teve muito próximo [...] depois desse contato ficou assim, ó, vocês não têm mais acesso ao cliente final. Vocês têm que sempre pedir a engenharia pra intermediar [...] a gente começou de fato a só ter contato com a engenharia [da Moura]."

**Interpretação:** essa é, em si, uma informação relevante para a Fase 2 — o ITEM (fonte primária do conhecimento técnico mais profundo do produto) está estruturalmente isolado do cliente final por uma política interna da própria Moura, o que significa que qualquer hipótese técnica levantada por ela (ex.: o que falta no sistema nativo da fonte) nunca foi testada diretamente com quem usaria essa informação do lado da operadora.

**Contatos internos recomendados por ela para aprofundar antes da Fase 2** (não são contatos do cliente, mas fontes internas-chave): **João Machado** (engenheiro técnico, desde a fundação — sabe causas raiz de falência de outras empresas do setor e riscos/gargalos) e **Marcos Malveira** (gerente do ITEM, visão de negócio/estratégia, desenhou a solução técnica com Thiago Mello).
